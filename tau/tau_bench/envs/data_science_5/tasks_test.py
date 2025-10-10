from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="v5",
        user_id="ds_ops_001",
        instruction=(
            "Handle the delivery of the April-2025 temperature anomaly record with QC validation. Final outcome: series 'temp_anom_2025-04' contains three values; [('2025-04-05T00:00:00Z', 1.2), ('2025-04-15T00:00:00Z', -0.3), ('2025-04-27T00:00:00Z', 0.6)] and QC report 'QC_TEMP_ANOM_2025-04' (pdf) is generated."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "temp_anom_2025-04", "items": [
                {"timestamp": "2025-04-05T00:00:00Z", "value": 1.2},
                {"timestamp": "2025-04-15T00:00:00Z", "value": -0.3},
                {"timestamp": "2025-04-27T00:00:00Z", "value": 0.6}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "temp_anom_2025-04"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04"}),

            Action(name="AppendAuditEvent", kwargs={"event_type": "series_qc_recorded",
                                                      "details": {"series": "temp_anom_2025-04",
                                                                  "qc_label": "QC_TEMP_ANOM_2025-04"}}),
            Action(name="ReadAuditEvents", kwargs={"event_type": "series_qc_recorded"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_002",
        instruction=(
            "Coordinate the production of the June-2025 salinity anomaly with QC. Final result: series 'sal_anom_2025-06' includes two entries; [('2025-06-12T00:00:00Z', 0.5), ('2025-06-22T00:00:00Z', -0.1)] and is accessible; QC record 'QC_SAL_ANOM_2025-06' (pdf) is stored and available."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "sal_anom_2025-06", "items": [
                {"timestamp": "2025-06-12T00:00:00Z", "value": 0.5},
                {"timestamp": "2025-06-22T00:00:00Z", "value": -0.1}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "sal_anom_2025-06"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_SAL_ANOM_2025-06"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_SAL_ANOM_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-06.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_SAL_ANOM_2025-06"}),

            Action(name="AppendAuditEvent", kwargs={"event_type": "series_qc_recorded",
                                                      "details": {"series": "sal_anom_2025-06",
                                                                  "qc_label": "QC_SAL_ANOM_2025-06"}}),
            Action(name="ReadAuditEvents", kwargs={"event_type": "series_qc_recorded"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_003",
        instruction=(
            "Handle the assembly of the May-2025 rainfall anomaly dataset with QC. End state: series 'rain_anom_2025-05' contains three values; [('2025-05-05T00:00:00Z', 12.0), ('2025-05-15T00:00:00Z', -3.2), ('2025-05-25T00:00:00Z', 4.7)] and is retrievable; QC artifact 'QC_RAIN_ANOM_2025-05' (pdf) is available."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "rain_anom_2025-05", "items": [
                {"timestamp": "2025-05-05T00:00:00Z", "value": 12.0},
                {"timestamp": "2025-05-15T00:00:00Z", "value": -3.2},
                {"timestamp": "2025-05-25T00:00:00Z", "value": 4.7}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "rain_anom_2025-05"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_RAIN_ANOM_2025-05"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_RAIN_ANOM_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_RAIN_ANOM_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_RAIN_ANOM_2025-05"}),

            Action(name="AppendAuditEvent", kwargs={"event_type": "series_qc_recorded",
                                                      "details": {"series": "rain_anom_2025-05",
                                                                  "qc_label": "QC_RAIN_ANOM_2025-05"}}),
            Action(name="ReadAuditEvents", kwargs={"event_type": "series_qc_recorded"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_004",
        instruction=(
            "Coordinate the onboarding of the LSTM flood model (v2.0) with its configuration and a validation score. End state: model 'LSTM_Flood_v2' (type=rnn, framework=tensorflow, version=2.0, status=staged) is stored and readable; profile 'seq_default' records hidden_units=128, dropout=0.3, layers=3; validation Accuracy=0.902 is logged."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "LSTM_Flood_v2", "model_type": "rnn", "framework": "tensorflow",
                           "version": "2.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "LSTM_Flood_v2"}),

            Action(name="UpsertModelProfile",
                   kwargs={"model_name": "LSTM_Flood_v2", "config_name": "seq_default",
                           "params": {"hidden_units": 128, "dropout": 0.3, "layers": 3}}),
            Action(name="ReadModelProfiles", kwargs={"model_name": "LSTM_Flood_v2"}),

            Action(name="LogModelMetric",
                   kwargs={"model_name": "LSTM_Flood_v2", "metric_name": "Accuracy",
                           "value": 0.902, "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "LSTM_Flood_v2"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_005",
        instruction=(
            "Handle the registration of the Transformer climate model (v3.1) by including its configuration and a validation loss. Final outcome: the model 'Transformer_Climate_v3' (type=transformer, framework=pytorch, version=3.1, status=staged) is stored and can be accessed; the profile 'attention_default' captures heads=8, d_model=256, layers=6; validation Loss=0.145 is documented."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "Transformer_Climate_v3", "model_type": "transformer", "framework": "pytorch",
                           "version": "3.1", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "Transformer_Climate_v3"}),

            Action(name="UpsertModelProfile",
                   kwargs={"model_name": "Transformer_Climate_v3", "config_name": "attention_default",
                           "params": {"heads": 8, "d_model": 256, "layers": 6}}),
            Action(name="ReadModelProfiles", kwargs={"model_name": "Transformer_Climate_v3"}),

            Action(name="LogModelMetric",
                   kwargs={"model_name": "Transformer_Climate_v3", "metric_name": "Loss",
                           "value": 0.145, "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "Transformer_Climate_v3"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_006",
        instruction=(
            "Coordinate the configuration of a backfill cutoff for January 2026, initiate a lightweight readiness probe series, and file QC for operations. Final outcome: project settings reflect backfill_cutoff '2026-01-10T08:00:00Z'; the probe series 'backfill_probe_2026-01' includes 1 timestamps and is available; the audit event 'BACKFILL_READY' with note 'Early January backfill cutoff configured successfully.' is present; the QC report 'QC_CONFIG_BACKFILL_2026-01' (pdf) is filed and linked to an internal ops artifact."
        ),
        actions=[
            Action(name="PatchProjectSettings", kwargs={"updates": {"backfill_cutoff": "2026-01-10T08:00:00Z"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "backfill_cutoff"}),
            Action(name="WriteProcessedSeries", kwargs={"series_name": "backfill_probe_2026-01", "items": [
                {"timestamp": "2026-01-10T08:00:00Z", "value": 1}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "backfill_probe_2026-01"}),
            Action(name="AppendAuditEvent", kwargs={
                "event_type": "BACKFILL_READY",
                "message": "Early January backfill cutoff configured successfully."
            }),
            Action(name="ReadAuditEvents", kwargs={"event_type": "BACKFILL_READY"}),
            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2026-01"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_CONFIG_BACKFILL_2026-01",
                "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2026-01.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2026-01"}),
            Action(name="RecordStakeholderArtifact", kwargs={
                "output_label": "Backfill Cutoff Jan 2026",
                "audience": "internal_ops",
                "artifact_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2026-01.pdf"
            }),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Backfill Cutoff Jan 2026"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_007",
        instruction=(
            "Handle the registration of 'GradientBoosting_Wind_v3' and log an October-2025 validation batch with QC. End state: model 'GradientBoosting_Wind_v3' (type 'gradient_boosting', framework 'sklearn', version '3.0', status 'staged') is stored; validation lot 'VAL_WD_2025-10' includes 1 entries; validation MAE 0.95 is logged; QC report 'QC_WD_VAL_2025-10' (png) is recorded and readable."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "GradientBoosting_Wind_v3", "model_type": "gradient_boosting",
                           "framework": "sklearn", "version": "3.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "GradientBoosting_Wind_v3"}),
            Action(name="WritePredictionLot",
                   kwargs={"batch_name": "VAL_WD_2025-10", "model_name": "GradientBoosting_Wind_v3", "items": [
                       {"timestamp": "2025-10-10T12:00:00Z", "prediction": 15.3}
                   ]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_WD_2025-10"}),
            Action(name="LogModelMetric",
                   kwargs={"model_name": "GradientBoosting_Wind_v3", "metric_name": "MAE", "value": 0.95,
                           "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "GradientBoosting_Wind_v3"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_WD_VAL_2025-10",
                                                    "figure_path": "https://storage.example.com/reports/QC_WD_VAL_2025-10.png",
                                                    "artifact_type": "png"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_WD_VAL_2025-10"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_008",
        instruction=(
            "Coordinate the registration of 'GradientBoosting_Wind_v3' and log an October-2025 validation batch with QC. End state: model 'GradientBoosting_Wind_v3' (type 'gradient_boosting', framework 'sklearn', version '3.0', status 'staged') is stored; validation lot 'VAL_WD_2025-10' includes 2 entries; validation MAE 0.95 is logged; QC report 'QC_WD_VAL_2025-10' (png) is recorded and readable."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "GradientBoosting_Wind_v3", "model_type": "gradient_boosting",
                           "framework": "sklearn", "version": "3.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "GradientBoosting_Wind_v3"}),
            Action(name="WritePredictionLot",
                   kwargs={"batch_name": "VAL_WD_2025-10", "model_name": "GradientBoosting_Wind_v3", "items": [
                       {"timestamp": "2025-10-10T12:00:00Z", "prediction": 15.3}
                   ]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_WD_2025-10"}),
            Action(name="LogModelMetric",
                   kwargs={"model_name": "GradientBoosting_Wind_v3", "metric_name": "MAE", "value": 0.95,
                           "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "GradientBoosting_Wind_v3"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_WD_VAL_2025-10",
                                                    "figure_path": "https://storage.example.com/reports/QC_WD_VAL_2025-10.png",
                                                    "artifact_type": "png"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_WD_VAL_2025-10"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_009",
        instruction=(
            "Facilitate the onboarding of 'XGBoost_Rainfall_v1' while logging a validation set for July-2025. Final state: the model 'XGBoost_Rainfall_v1' (type 'xgboost', framework 'xgboost', version '1.0', status 'staged') is registered and accessible; the validation batch 'VAL_RAIN_2025-07' contains a single record ('2025-07-15T00:00:00Z', 124.3) which is accessible; an R² value of 0.93 is noted for the validation set and viewable; the QC report 'QC_RAIN_VAL_2025-07' (pdf) is archived and recoverable."
        ),
        actions=[
            # Model asset (create → validate)
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "XGBoost_Rainfall_v1", "model_type": "xgboost",
                           "framework": "xgboost", "version": "1.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "XGBoost_Rainfall_v1"}),

            # Forecasts (create → confirm)
            Action(name="WritePredictionLot",
                   kwargs={"batch_name": "VAL_RAIN_2025-07", "model_name": "XGBoost_Rainfall_v1", "items": [
                       {"timestamp": "2025-07-15T00:00:00Z", "prediction": 124.3}
                   ]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_RAIN_2025-07"}),

            # Metric (create → validate)
            Action(name="LogModelMetric",
                   kwargs={"model_name": "XGBoost_Rainfall_v1", "metric_name": "R2", "value": 0.93,
                           "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "XGBoost_Rainfall_v1"}),

            # QC report (verify → validate)
            Action(name="RecordQcReport",
                   kwargs={"figure_label": "QC_RAIN_VAL_2025-07",
                           "figure_path": "https://storage.example.com/reports/QC_RAIN_VAL_2025-07.pdf",
                           "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_RAIN_VAL_2025-07"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_010",
        instruction=(
            "Coordinate the registration of 'storm_features_v2' (v2.0), activate it, and document QC along with an activation audit. Final state: the feature bundle can be accessed; the file '/features/storm_features_v2.parquet' is present and retrievable; the configuration 'active_feature_set' is 'storm_features_v2'; the QC PDF 'QC_STORM_FEATURES_2025-06' is documented and accessible; an audit record 'FEATURE_SET_ACTIVATED' with the note 'storm_features_v2 set active.' is documented."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={
                "feature_set_name": "storm_features_v2",
                "version": "2.0",
                "columns": ["surge_height", "wind_speed", "precipitation"]
            }),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "storm_features_v2"}),

            Action(name="RegisterFileEntry", kwargs={
                "path": "/features/storm_features_v2.parquet",
                "mime_type": "application/parquet"
            }),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/storm_features_v2.parquet"}),

            Action(name="PatchProjectSettings", kwargs={"updates": {"active_feature_set": "storm_features_v2"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "active_feature_set"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_STORM_FEATURES_2025-06"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_STORM_FEATURES_2025-06",
                "figure_path": "https://storage.example.com/reports/QC_STORM_FEATURES_2025-06.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_STORM_FEATURES_2025-06"}),
            Action(name="AppendAuditEvent", kwargs={
                "event_type": "FEATURE_SET_ACTIVATED",
                "message": "storm_features_v2 set active."
            }),
            Action(name="ReadAuditEvents", kwargs={"event_type": "FEATURE_SET_ACTIVATED"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_011",
        instruction=(
            "Complete the process to finalize 'harbor_arrival_metrics_v2' (v2.0) and make it live in configuration. Desired outcome: feature_set 'harbor_arrival_metrics_v2' with fields ['arrival_count','dwell_time_mean','dwell_time_median'] is documented and accessible; file '/features/harbor_arrival_metrics_v2.parquet' is present and accessible; project setting 'active_feature_set' is set to 'harbor_arrival_metrics_v2'; QC PDF labeled 'QC_HARBOR_ARRIVAL_2025-03' is available and accessible."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={
                "feature_set_name": "harbor_arrival_metrics_v2",
                "version": "2.0",
                "columns": ["arrival_count", "dwell_time_mean", "dwell_time_median"]
            }),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "harbor_arrival_metrics_v2"}),

            Action(name="RegisterFileEntry", kwargs={
                "path": "/features/harbor_arrival_metrics_v2.parquet",
                "mime_type": "application/parquet"
            }),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/harbor_arrival_metrics_v2.parquet"}),

            Action(name="PatchProjectSettings",
                   kwargs={"updates": {"active_feature_set": "harbor_arrival_metrics_v2"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "active_feature_set"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_HARBOR_ARRIVAL_2025-03"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_HARBOR_ARRIVAL_2025-03",
                "figure_path": "https://storage.example.com/reports/QC_HARBOR_ARRIVAL_2025-03.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_HARBOR_ARRIVAL_2025-03"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_012",
        instruction=(
            "Produce a harbor ice-thickness series for May-2025 including QC and a deliverable. Desired outcome: series 'ice_thickness_2025-05' contains three points [('2025-05-01T00:00:00Z', 0.25), ('2025-05-08T00:00:00Z', 0.30), ('2025-05-15T00:00:00Z', 0.28)] and is accessible; QC figure 'QC_ICE_THICKNESS_2025-05' is available (artifact_type 'pdf') and accessible; stakeholder output 'Harbor Ice Thickness May 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf' and can be accessed."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "ice_thickness_2025-05", "items": [
                {"timestamp": "2025-05-01T00:00:00Z", "value": 0.25},
                {"timestamp": "2025-05-08T00:00:00Z", "value": 0.30},
                {"timestamp": "2025-05-15T00:00:00Z", "value": 0.28}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "ice_thickness_2025-05"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_ICE_THICKNESS_2025-05"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_ICE_THICKNESS_2025-05",
                "figure_path": "https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_ICE_THICKNESS_2025-05"}),

            Action(name="RecordStakeholderArtifact", kwargs={
                "output_label": "Harbor Ice Thickness May 2025",
                "audience": "internal",
                "artifact_path": "https://storage.example.com/reports/QC_ICE_THICKNESS_2025-05.pdf"
            }),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Harbor Ice Thickness May 2025"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_013",
        instruction=(
            "Conclude a May-2025 storm-surge feature bundle and enable it in config. End state: feature_set 'storm_surge_v2' (version '2.0') with fields ['max_surge','mean_surge'] is stored and retrievable; file '/features/storm_surge_v2.parquet' exists and is retrievable; project setting 'active_feature_set' equals 'storm_surge_v2'; QC figure 'QC_STORM_SURGE_2025-05' exists (artifact_type 'pdf') and is retrievable."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "storm_surge_v2", "version": "2.0",
                                                           "columns": ["max_surge", "mean_surge"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "storm_surge_v2"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/storm_surge_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/storm_surge_v2.parquet"}),

            Action(name="PatchProjectSettings", kwargs={"updates": {"active_feature_set": "storm_surge_v2"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "active_feature_set"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_STORM_SURGE_2025-05"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_STORM_SURGE_2025-05",
                "figure_path": "https://storage.example.com/reports/QC_STORM_SURGE_2025-05.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_STORM_SURGE_2025-05"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_014",
        instruction=(
            "Deploy a March-2025 rainfall-runoff anomaly series with a QC record and deliverable. End state: processed series 'rainfall_runoff_anom_2025-03' holds three points [('2025-03-05T00:00:00Z', 12.4), ('2025-03-12T00:00:00Z', 9.8), ('2025-03-19T00:00:00Z', 15.2)] and is retrievable; a QC PDF exists for label 'QC_RR_ANOM_2025-03' and is retrievable; stakeholder output 'Rainfall-Runoff Anomaly Mar 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf' and is retrievable."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "rainfall_runoff_anom_2025-03", "items": [
                {"timestamp": "2025-03-05T00:00:00Z", "value": 12.4},
                {"timestamp": "2025-03-12T00:00:00Z", "value": 9.8},
                {"timestamp": "2025-03-19T00:00:00Z", "value": 15.2}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "rainfall_runoff_anom_2025-03"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_RR_ANOM_2025-03"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_RR_ANOM_2025-03",
                "figure_path": "https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_RR_ANOM_2025-03"}),

            Action(name="RecordStakeholderArtifact", kwargs={
                "output_label": "Rainfall-Runoff Anomaly Mar 2025",
                "audience": "internal",
                "artifact_path": "https://storage.example.com/reports/QC_RR_ANOM_2025-03.pdf"
            }),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Rainfall-Runoff Anomaly Mar 2025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_015",
        instruction=(
            "Handle the staging of 'CNN_FloodExtent_v1' with a validation entry dated July-2025. End state: the model 'CNN_FloodExtent_v1' (type=cnn, framework=tensorflow, version=1.0, status=staged) is to be persisted and retrievable; the validation batch 'VAL_FE_2025-07' includes one row ('2025-07-12T15:00:00Z', 0.88); ensure that validation MAE=0.09 is logged; make sure the QC artifact 'QC_FE_VAL_2025-07' (png) is stored and accessible."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "CNN_FloodExtent_v1", "model_type": "cnn", "framework": "tensorflow",
                           "version": "1.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "CNN_FloodExtent_v1"}),

            Action(name="WritePredictionLot",
                   kwargs={"batch_name": "VAL_FE_2025-07", "model_name": "CNN_FloodExtent_v1",
                           "items": [{"timestamp": "2025-07-12T15:00:00Z", "prediction": 0.88}]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_FE_2025-07"}),

            Action(name="LogModelMetric",
                   kwargs={"model_name": "CNN_FloodExtent_v1", "metric_name": "MAE", "value": 0.09,
                           "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "CNN_FloodExtent_v1"}),

            Action(name="RecordQcReport", kwargs={"figure_label": "QC_FE_VAL_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_FE_VAL_2025-07.png",
                                                    "artifact_type": "png"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_FE_VAL_2025-07"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_016",
        instruction=(
            "Coordinate the staging of 'GRU_Rainfall_v1' using June-2025 validation information. End state: ensure the model 'GRU_Rainfall_v1' (type=gru, framework=pytorch, version=1.0, status=staged) is available; the batch 'VAL_RF_2025-06' should include one entry ('2025-06-15T09:00:00Z', 15.3); record validation RMSE=1.2; make certain the QC artifact 'QC_RF_VAL_2025-06' (pdf) is recorded and retrievable."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "GRU_Rainfall_v1", "model_type": "gru", "framework": "pytorch",
                           "version": "1.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "GRU_Rainfall_v1"}),

            Action(name="WritePredictionLot", kwargs={"batch_name": "VAL_RF_2025-06", "model_name": "GRU_Rainfall_v1",
                                                        "items": [{"timestamp": "2025-06-15T09:00:00Z",
                                                                   "prediction": 15.3}]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_RF_2025-06"}),

            Action(name="LogModelMetric",
                   kwargs={"model_name": "GRU_Rainfall_v1", "metric_name": "RMSE", "value": 1.2,
                           "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "GRU_Rainfall_v1"}),

            Action(name="RecordQcReport", kwargs={"figure_label": "QC_RF_VAL_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_RF_VAL_2025-06.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_RF_VAL_2025-06"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_017",
        instruction=(
            "Handle the registration of 'RF_Temperature_v3' and capture a validation run for May-2025. Final state: model 'RF_Temperature_v3' (type 'random_forest', framework 'sklearn', version '3.1', status 'staged') is stored; validation lot 'VAL_TEMP_2025-05' contains one record ('2025-05-05T00:00:00Z', 18.7) and is readable; R² value 0.91 is logged under validation split; QC report 'QC_TEMP_VAL_2025-05' is saved as pdf and retrievable."
        ),
        actions=[
            Action(name="StoreModelArtifact", kwargs={
                "model_name": "RF_Temperature_v3",
                "model_type": "random_forest",
                "framework": "sklearn",
                "version": "3.1",
                "status": "staged"
            }),
            Action(name="FetchModelRecord", kwargs={"model_name": "RF_Temperature_v3"}),

            Action(name="WritePredictionLot", kwargs={
                "batch_name": "VAL_TEMP_2025-05",
                "model_name": "RF_Temperature_v3",
                "items": [{"timestamp": "2025-05-05T00:00:00Z", "prediction": 18.7}]
            }),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_TEMP_2025-05"}),

            Action(name="LogModelMetric", kwargs={
                "model_name": "RF_Temperature_v3",
                "metric_name": "R2",
                "value": 0.91,
                "dataset_split": "validation"
            }),
            Action(name="ReadModelMetrics", kwargs={"model_name": "RF_Temperature_v3"}),

            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_TEMP_VAL_2025-05",
                "figure_path": "https://storage.example.com/reports/QC_TEMP_VAL_2025-05.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_TEMP_VAL_2025-05"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_018",
        instruction=(
            "Coordinate the configuration of 'Prophet_TideCycle_v1' with the validation details for May-2025. End state: model 'Prophet_TideCycle_v1' (type=prophet, framework=prophet, version=1.0, status=staged) is inserted; batch 'VAL_TC_2025-05' has one row ('2025-05-20T06:00:00Z', 2.44); MAPE=4.5 is logged; QC file 'QC_TC_VAL_2025-05' (pdf) exists."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "Prophet_TideCycle_v1", "model_type": "prophet", "framework": "prophet",
                           "version": "1.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "Prophet_TideCycle_v1"}),

            Action(name="WritePredictionLot",
                   kwargs={"batch_name": "VAL_TC_2025-05", "model_name": "Prophet_TideCycle_v1",
                           "items": [{"timestamp": "2025-05-20T06:00:00Z", "prediction": 2.44}]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_TC_2025-05"}),

            Action(name="LogModelMetric",
                   kwargs={"model_name": "Prophet_TideCycle_v1", "metric_name": "MAPE", "value": 4.5,
                           "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "Prophet_TideCycle_v1"}),

            Action(name="RecordQcReport", kwargs={"figure_label": "QC_TC_VAL_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_TC_VAL_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_TC_VAL_2025-05"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_019",
        instruction=(
            "Handle deployment of 'XGB_WindDamage_v1' with validation results from February-2025. End state: model 'XGB_WindDamage_v1' (type=xgboost, framework=xgboost, version=1.6, status=staged) is registered; batch 'VAL_WD_2025-02' includes one row ('2025-02-14T18:00:00Z', 12.8); validation MAE=1.7 is stored; QC document 'QC_WD_VAL_2025-02' (pdf) exists and is retrievable."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "XGB_WindDamage_v1", "model_type": "xgboost", "framework": "xgboost",
                           "version": "1.6", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "XGB_WindDamage_v1"}),

            Action(name="WritePredictionLot",
                   kwargs={"batch_name": "VAL_WD_2025-02", "model_name": "XGB_WindDamage_v1",
                           "items": [{"timestamp": "2025-02-14T18:00:00Z", "prediction": 12.8}]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_WD_2025-02"}),

            Action(name="LogModelMetric",
                   kwargs={"model_name": "XGB_WindDamage_v1", "metric_name": "MAE", "value": 1.7,
                           "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "XGB_WindDamage_v1"}),

            Action(name="RecordQcReport", kwargs={"figure_label": "QC_WD_VAL_2025-02",
                                                    "figure_path": "https://storage.example.com/reports/QC_WD_VAL_2025-02.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_WD_VAL_2025-02"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_020",
        instruction=(
            "Coordinate the registration of 'LSTM_FloodRisk_v2' with validation entry from April-2025. End state: model 'LSTM_FloodRisk_v2' (type=lstm, framework=tensorflow, version=2.0, status=staged) is accessible; validation batch 'VAL_FR_2025-04' contains one row ('2025-04-05T12:00:00Z', 0.76); validation RMSE=0.32 is logged; QC artifact 'QC_FR_VAL_2025-04' (png) is stored."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "LSTM_FloodRisk_v2", "model_type": "lstm", "framework": "tensorflow",
                           "version": "2.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "LSTM_FloodRisk_v2"}),

            Action(name="WritePredictionLot",
                   kwargs={"batch_name": "VAL_FR_2025-04", "model_name": "LSTM_FloodRisk_v2",
                           "items": [{"timestamp": "2025-04-05T12:00:00Z", "prediction": 0.76}]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_FR_2025-04"}),

            Action(name="LogModelMetric",
                   kwargs={"model_name": "LSTM_FloodRisk_v2", "metric_name": "RMSE", "value": 0.32,
                           "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "LSTM_FloodRisk_v2"}),

            Action(name="RecordQcReport", kwargs={"figure_label": "QC_FR_VAL_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_FR_VAL_2025-04.png",
                                                    "artifact_type": "png"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_FR_VAL_2025-04"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_021",
        instruction=(
            "Handle the processing of December-2024 salinity anomalies with QC and draft an internal report. Finalize with: series 'sal_anom_2024-12' comprising four values; ensure QC file 'QC_SAL_ANOM_2024-12' (pdf) is available; the internal stakeholder output 'Salinity Anomaly Dec 2024' should reference the QC artifact."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "sal_anom_2024-12", "items": [
                {"timestamp": "2024-12-03T00:00:00Z", "value": 0.12},
                {"timestamp": "2024-12-10T00:00:00Z", "value": -0.04},
                {"timestamp": "2024-12-18T00:00:00Z", "value": 0.05},
                {"timestamp": "2024-12-27T00:00:00Z", "value": 0.09}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "sal_anom_2024-12"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_SAL_ANOM_2024-12"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_SAL_ANOM_2024-12",
                                                    "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2024-12.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_SAL_ANOM_2024-12"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Salinity Anomaly Dec 2024", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_SAL_ANOM_2024-12.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Salinity Anomaly Dec 2024"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_022",
        instruction=(
            "Coordinate the creation of the tidal harmonics dataset for January 2025, validate the QC output, and issue a summary for public consumption. Complete with: 'tidal_harm_2025-01' series processed with three entries, the archival of QC report 'QC_TIDAL_HARM_2025-01.pdf', and a stakeholder product titled 'Tidal Harmonics Jan 2025' for 'external' audience linking to the QC document."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "tidal_harm_2025-01", "items": [
                {"timestamp": "2025-01-05T00:00:00Z", "value": 1.21},
                {"timestamp": "2025-01-15T00:00:00Z", "value": 1.15},
                {"timestamp": "2025-01-25T00:00:00Z", "value": 1.18}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "tidal_harm_2025-01"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_TIDAL_HARM_2025-01"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_TIDAL_HARM_2025-01",
                "figure_path": "https://storage.example.com/reports/QC_TIDAL_HARM_2025-01.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_TIDAL_HARM_2025-01"}),

            Action(name="RecordStakeholderArtifact", kwargs={
                "output_label": "Tidal Harmonics Jan 2025",
                "audience": "external",
                "artifact_path": "https://storage.example.com/reports/QC_TIDAL_HARM_2025-01.pdf"
            }),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Tidal Harmonics Jan 2025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_023",
        instruction=(
            "Handle the computation of February-2025 surge residuals series, archive the results, and make sure to distribute the QC output. Final requirement: series 'surge_resid_2025-02' contains four values; QC document 'QC_SURGE_RESID_2025-02' (pdf) is available; stakeholder output 'Feb 2025 Surge Residual' cites the PDF."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "surge_resid_2025-02", "items": [
                {"timestamp": "2025-02-02T00:00:00Z", "value": -0.11},
                {"timestamp": "2025-02-10T00:00:00Z", "value": 0.07},
                {"timestamp": "2025-02-18T00:00:00Z", "value": 0.02},
                {"timestamp": "2025-02-26T00:00:00Z", "value": -0.05}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "surge_resid_2025-02"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_SURGE_RESID_2025-02"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_SURGE_RESID_2025-02",
                                                    "figure_path": "https://storage.example.com/reports/QC_SURGE_RESID_2025-02.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_SURGE_RESID_2025-02"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Feb 2025 Surge Residual", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_SURGE_RESID_2025-02.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Feb 2025 Surge Residual"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_024",
        instruction=(
            "Coordinate the publication of the June-2025 salinity index dataset with QC. Final condition: time series 'sal_index_2025-06' comprises three entries; [('2025-06-04T00:00:00Z', 33.1), ('2025-06-16T00:00:00Z', 34.2), ('2025-06-29T00:00:00Z', 32.8)] QC report 'QC_SAL_INDEX_2025-06' (pdf) is filed and accessible."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "sal_index_2025-06", "items": [
                {"timestamp": "2025-06-04T00:00:00Z", "value": 33.1},
                {"timestamp": "2025-06-16T00:00:00Z", "value": 34.2},
                {"timestamp": "2025-06-29T00:00:00Z", "value": 32.8}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "sal_index_2025-06"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_SAL_INDEX_2025-06"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_SAL_INDEX_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_SAL_INDEX_2025-06.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_SAL_INDEX_2025-06"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_025",
        instruction=(
            "Handle the assembly of the rainfall deviation set for May-2025 with a QC check. Final condition: series 'rain_dev_2025-05' includes three values; [('2025-05-03T00:00:00Z', -5.1), ('2025-05-12T00:00:00Z', 2.4), ('2025-05-25T00:00:00Z', -1.7)]; QC artifact 'QC_RAIN_DEV_2025-05' is available (pdf)."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "rain_dev_2025-05", "items": [
                {"timestamp": "2025-05-03T00:00:00Z", "value": -5.1},
                {"timestamp": "2025-05-12T00:00:00Z", "value": 2.4},
                {"timestamp": "2025-05-25T00:00:00Z", "value": -1.7}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "rain_dev_2025-05"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_RAIN_DEV_2025-05"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_RAIN_DEV_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_RAIN_DEV_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_RAIN_DEV_2025-05"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_026",
        instruction=(
            "Coordinate the validation of a 30-year NOAA tide gauge archive. Final condition: the processed series 'noaa_tide_qc_1990_2020' encompasses summary values [('mean_sea_level', 2.34), ('max_tide', 3.78)] and is accessible; a QC PDF labeled 'QC_NOAA_TIDE_1990_2020' is archived (artifact_type 'pdf') and retrievable; stakeholder artifact 'NOAA Tide QC 1990-2020' (audience 'internal') links to 'https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf' and is retrievable."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "noaa_tide_qc_1990_2020", "items": [
                {"timestamp": "mean_sea_level", "value": 2.34},
                {"timestamp": "max_tide", "value": 3.78}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "noaa_tide_qc_1990_2020"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_NOAA_TIDE_1990_2020"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_NOAA_TIDE_1990_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_NOAA_TIDE_1990_2020"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "NOAA Tide QC 1990-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_NOAA_TIDE_1990_2020.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "NOAA Tide QC 1990-2020"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_027",
        instruction=(
            "Handle the release of a March-2025 salinity anomaly dataset. End state: processed series 'salinity_anom_2025-03' contains three entries [('2025-03-07T00:00:00Z', 0.07), ('2025-03-14T00:00:00Z', -0.02), ('2025-03-21T00:00:00Z', 0.04)] and is accessible; a QC PDF for label 'QC_SAL_ANOM_2025-03' is logged (artifact_type 'pdf') and accessible; stakeholder artifact 'Salinity Anomaly Mar 2025' (audience 'internal') links to 'https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf' and is accessible."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "salinity_anom_2025-03", "items": [
                {"timestamp": "2025-03-07T00:00:00Z", "value": 0.07},
                {"timestamp": "2025-03-14T00:00:00Z", "value": -0.02},
                {"timestamp": "2025-03-21T00:00:00Z", "value": 0.04}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "salinity_anom_2025-03"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_SAL_ANOM_2025-03"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_SAL_ANOM_2025-03",
                                                    "figure_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_SAL_ANOM_2025-03"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Salinity Anomaly Mar 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_SAL_ANOM_2025-03.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Salinity Anomaly Mar 2025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_028",
        instruction=(
            "Coordinate the maintenance of the feature bundle 'harbor_ops_v2' and mark it active with QC. End state: feature_set 'harbor_ops_v2' (version '2.0') with fields ['arrival_count','dwell_time_median','departure_count'] is available and accessible; file '/features/harbor_ops_v2.parquet' exists and is accessible; project setting 'active_feature_set' is set to 'harbor_ops_v2' and accessible; QC PDF for label 'QC_HARBOR_OPS_2025-03' is logged (artifact_type 'pdf') and accessible."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "harbor_ops_v2", "version": "2.0",
                                                           "columns": ["arrival_count", "dwell_time_median",
                                                                       "departure_count"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "harbor_ops_v2"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/harbor_ops_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/harbor_ops_v2.parquet"}),

            Action(name="PatchProjectSettings", kwargs={"updates": {"active_feature_set": "harbor_ops_v2"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "active_feature_set"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_HARBOR_OPS_2025-03"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_HARBOR_OPS_2025-03",
                                                    "figure_path": "https://storage.example.com/reports/QC_HARBOR_OPS_2025-03.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_HARBOR_OPS_2025-03"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_029",
        instruction=(
            "Handle the release of the April-2025 temperature anomaly dataset with QC and prepare an internal report. End state: series 'temp_anom_2025-04' contains two entries; [('2025-04-10T00:00:00Z', 1.1), ('2025-04-25T00:00:00Z', -0.3)] and is accessible; QC document 'QC_TEMP_ANOM_2025-04' is available (pdf); stakeholder output 'Temp Anomaly Apr 2025' (audience=internal) is attached."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "temp_anom_2025-04", "items": [
                {"timestamp": "2025-04-10T00:00:00Z", "value": 1.1},
                {"timestamp": "2025-04-25T00:00:00Z", "value": -0.3}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "temp_anom_2025-04"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_TEMP_ANOM_2025-04"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Temp Anomaly Apr 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_TEMP_ANOM_2025-04.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Temp Anomaly Apr 2025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_030",
        instruction=(
            "Coordinate the generation of the June 2025 precipitation anomaly dataset, conduct QC checks, and secure the outcomes in the archive. End state: processed series 'precip_anom_2025-06' contains three values [('2025-06-01T00:00:00Z', -5.0), ('2025-06-15T00:00:00Z', 3.2), ('2025-06-29T00:00:00Z', -1.1)] and is retrievable; QC record 'QC_PRECIP_ANOM_2025-06' (pdf) is formed and ready for access."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "precip_anom_2025-06", "items": [
                {"timestamp": "2025-06-01T00:00:00Z", "value": -5.0},
                {"timestamp": "2025-06-15T00:00:00Z", "value": 3.2},
                {"timestamp": "2025-06-29T00:00:00Z", "value": -1.1}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "precip_anom_2025-06"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-06"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_PRECIP_ANOM_2025-06",
                "figure_path": "https://storage.example.com/reports/QC_PRECIP_ANOM_2025-06.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-06"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_031",
        instruction=(
            "Handle the collection of February 2025 river flow anomaly data, verify QC output, and store the outcomes. End state: the processed series 'flow_anom_2025-02' comprises three records [('2025-02-03T00:00:00Z', 120), ('2025-02-14T00:00:00Z', 110), ('2025-02-25T00:00:00Z', 130)] and can be retrieved; a QC report labeled 'QC_FLOW_ANOM_2025-02' (pdf) is generated and easily accessible."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "flow_anom_2025-02", "items": [
                {"timestamp": "2025-02-03T00:00:00Z", "value": 120},
                {"timestamp": "2025-02-14T00:00:00Z", "value": 110},
                {"timestamp": "2025-02-25T00:00:00Z", "value": 130}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "flow_anom_2025-02"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_FLOW_ANOM_2025-02"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_FLOW_ANOM_2025-02",
                "figure_path": "https://storage.example.com/reports/QC_FLOW_ANOM_2025-02.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_FLOW_ANOM_2025-02"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_032",
        instruction=(
            "Coordinate the preparation of feature collection 'precip_extremes_v1' (version '1.0') with columns ['daily_rainfall_max','monthly_rainfall_mean','extreme_event_count'] and ensure it is set as active. Final state: the feature set is queryable; the file '/features/precip_extremes_v1.parquet' exists and is valid; project option 'climate_features' is configured to 'precip_extremes_v1'; QC summary 'QC_PRECIP_2025-08' is recorded as a PDF."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "precip_extremes_v1", "version": "1.0",
                                                           "columns": ["daily_rainfall_max", "monthly_rainfall_mean",
                                                                       "extreme_event_count"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "precip_extremes_v1"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/precip_extremes_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/precip_extremes_v1.parquet"}),

            Action(name="PatchProjectSettings", kwargs={"updates": {"climate_features": "precip_extremes_v1"}}),
            Action(name="ReadProjectSettings", kwargs={}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_PRECIP_2025-08"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_PRECIP_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_PRECIP_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_PRECIP_2025-08"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_033",
        instruction=(
            "Handle QC for the merged satellite rainfall dataset spanning 2000–2020. Final condition: time series 'rainfall_sat_qc_2000_2020' contains [('avg_rainfall',114.6),('max_rainfall_day',312.0)] and is available; QC document 'QC_RAINFALL_SAT_2000_2020' is stored as a PDF; stakeholder output 'Rainfall QC 2000-2020' (audience external) connects to 'https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf'."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "rainfall_sat_qc_2000_2020", "items": [
                {"timestamp": "avg_rainfall", "value": 114.6},
                {"timestamp": "max_rainfall_day", "value": 312.0}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "rainfall_sat_qc_2000_2020"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_RAINFALL_SAT_2000_2020"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_RAINFALL_SAT_2000_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_RAINFALL_SAT_2000_2020"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Rainfall QC 2000-2020", "audience": "external",
                           "artifact_path": "https://storage.example.com/reports/QC_RAINFALL_SAT_2000_2020.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Rainfall QC 2000-2020"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_034",
        instruction=(
            "Coordinate validation of 25 years of atmospheric CO₂ records. Final condition: series 'co2_qc_1990_2015' includes [('avg_co2_ppm',402.5),('max_co2_ppm',419.1)] accessible; QC document 'QC_CO2_1990_2015' exists as a PDF; stakeholder product 'Global CO₂ QC 1990-2015' (external) links to 'https://storage.example.com/reports/QC_CO2_1990_2015.pdf'."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "co2_qc_1990_2015", "items": [
                {"timestamp": "avg_co2_ppm", "value": 402.5},
                {"timestamp": "max_co2_ppm", "value": 419.1}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "co2_qc_1990_2015"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CO2_1990_2015"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_CO2_1990_2015",
                                                    "figure_path": "https://storage.example.com/reports/QC_CO2_1990_2015.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CO2_1990_2015"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Global CO₂ QC 1990-2015", "audience": "external",
                           "artifact_path": "https://storage.example.com/reports/QC_CO2_1990_2015.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Global CO₂ QC 1990-2015"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_035",
        instruction=(
            "Handle river flow data verification for the Amazon (1980–2010). Final state: the series 'amazon_discharge_qc_1980_2010' includes [('avg_discharge',85000.0),('peak_discharge',120000.0)] and is accessible; the QC record 'QC_AMAZON_DISCHARGE_1980_2010' (pdf) is saved; stakeholder output 'Amazon River Discharge QC 1980-2010' (internal) links to 'https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf'."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "amazon_discharge_qc_1980_2010", "items": [
                {"timestamp": "avg_discharge", "value": 85000.0},
                {"timestamp": "peak_discharge", "value": 120000.0}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "amazon_discharge_qc_1980_2010"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_AMAZON_DISCHARGE_1980_2010"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_AMAZON_DISCHARGE_1980_2010",
                                                    "figure_path": "https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_AMAZON_DISCHARGE_1980_2010"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Amazon River Discharge QC 1980-2010", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_AMAZON_DISCHARGE_1980_2010.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Amazon River Discharge QC 1980-2010"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_036",
        instruction=(
            "Coordinate registration of 'ARIMA_Tide_v2' and conduct validation on the May 2025 batch with QC. Final state: the model 'ARIMA_Tide_v2' (type arima, framework statsmodels, version 2.0, status staged) is stored and accessible; the validation lot 'VAL_TIDE_2025-05' includes a single entry ('2025-05-09T00:00:00Z', 1.45); MAPE 7.8 is noted; the QC report 'QC_TIDE_VAL_2025-05' is available as PDF."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "ARIMA_Tide_v2", "model_type": "arima", "framework": "statsmodels",
                           "version": "2.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "ARIMA_Tide_v2"}),

            Action(name="WritePredictionLot", kwargs={"batch_name": "VAL_TIDE_2025-05", "model_name": "ARIMA_Tide_v2",
                                                        "items": [{"timestamp": "2025-05-09T00:00:00Z",
                                                                   "prediction": 1.45}]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_TIDE_2025-05"}),

            Action(name="LogModelMetric", kwargs={"model_name": "ARIMA_Tide_v2", "metric_name": "MAPE", "value": 7.8,
                                                    "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "ARIMA_Tide_v2"}),

            Action(name="RecordQcReport", kwargs={"figure_label": "QC_TIDE_VAL_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_TIDE_VAL_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_TIDE_VAL_2025-05"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_037",
        instruction=(
            "Handle the onboarding of 'GRU_Temperature_v1' with June 2025 validation and quality control. Store the model 'GRU_Temperature_v1' (type gru, framework pytorch, version 1.0, status staged); incorporate batch 'VAL_TEMP_2025-06' with a single record ('2025-06-18T12:00:00Z', 27.6); log MAE 0.3; ensure QC image 'QC_TEMP_VAL_2025-06' is available as PNG."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "GRU_Temperature_v1", "model_type": "gru", "framework": "pytorch",
                           "version": "1.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "GRU_Temperature_v1"}),

            Action(name="WritePredictionLot",
                   kwargs={"batch_name": "VAL_TEMP_2025-06", "model_name": "GRU_Temperature_v1",
                           "items": [{"timestamp": "2025-06-18T12:00:00Z", "prediction": 27.6}]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_TEMP_2025-06"}),

            Action(name="LogModelMetric",
                   kwargs={"model_name": "GRU_Temperature_v1", "metric_name": "MAE", "value": 0.3,
                           "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "GRU_Temperature_v1"}),

            Action(name="RecordQcReport", kwargs={"figure_label": "QC_TEMP_VAL_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_TEMP_VAL_2025-06.png",
                                                    "artifact_type": "png"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_TEMP_VAL_2025-06"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_038",
        instruction=(
            "Coordinate the staging of 'XGBoost_FloodRisk_v1' using the July 2025 validation dataset. Store model 'XGBoost_FloodRisk_v1' (type xgboost, framework xgboost, version 1.0, status staged); include lot 'VAL_FR_2025-07' with entry ('2025-07-20T00:00:00Z', 0.34); record RMSE 0.05; confirm QC PDF 'QC_FR_VAL_2025-07' exists."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "XGBoost_FloodRisk_v1", "model_type": "xgboost", "framework": "xgboost",
                           "version": "1.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "XGBoost_FloodRisk_v1"}),

            Action(name="WritePredictionLot",
                   kwargs={"batch_name": "VAL_FR_2025-07", "model_name": "XGBoost_FloodRisk_v1",
                           "items": [{"timestamp": "2025-07-20T00:00:00Z", "prediction": 0.34}]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_FR_2025-07"}),

            Action(name="LogModelMetric",
                   kwargs={"model_name": "XGBoost_FloodRisk_v1", "metric_name": "RMSE", "value": 0.05,
                           "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "XGBoost_FloodRisk_v1"}),

            Action(name="RecordQcReport", kwargs={"figure_label": "QC_FR_VAL_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_FR_VAL_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_FR_VAL_2025-07"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_039",
        instruction=(
            "Validate 'CNN_WaveHeight_v1' utilizing the Sept 2025 batch and QC. Final state: model stored (cnn, tensorflow, v1.0, staged); lot 'VAL_WH_2025-09' carries the entry ('2025-09-05T06:00:00Z', 1.72); MAE 0.12 logged; QC PNG 'QC_WH_VAL_2025-09' available."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "CNN_WaveHeight_v1", "model_type": "cnn", "framework": "tensorflow",
                           "version": "1.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "CNN_WaveHeight_v1"}),

            Action(name="WritePredictionLot",
                   kwargs={"batch_name": "VAL_WH_2025-09", "model_name": "CNN_WaveHeight_v1",
                           "items": [{"timestamp": "2025-09-05T06:00:00Z", "prediction": 1.72}]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_WH_2025-09"}),

            Action(name="LogModelMetric",
                   kwargs={"model_name": "CNN_WaveHeight_v1", "metric_name": "MAE", "value": 0.12,
                           "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "CNN_WaveHeight_v1"}),

            Action(name="RecordQcReport", kwargs={"figure_label": "QC_WH_VAL_2025-09",
                                                    "figure_path": "https://storage.example.com/reports/QC_WH_VAL_2025-09.png",
                                                    "artifact_type": "png"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_WH_VAL_2025-09"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_040",
        instruction=(
            "Stage 'LSTM_Rainfall_v2' using the Aug 2025 validation lot and QC. Model stored (lstm, pytorch, v2.0, staged); lot 'VAL_RF_2025-08' contains one entry ('2025-08-10T12:00:00Z', 22.5); RMSE 1.05 logged; QC PDF 'QC_RF_VAL_2025-08' exists."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "LSTM_Rainfall_v2", "model_type": "lstm", "framework": "pytorch",
                           "version": "2.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "LSTM_Rainfall_v2"}),

            Action(name="WritePredictionLot",
                   kwargs={"batch_name": "VAL_RF_2025-08", "model_name": "LSTM_Rainfall_v2",
                           "items": [{"timestamp": "2025-08-10T12:00:00Z", "prediction": 22.5}]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_RF_2025-08"}),

            Action(name="LogModelMetric",
                   kwargs={"model_name": "LSTM_Rainfall_v2", "metric_name": "RMSE", "value": 1.05,
                           "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "LSTM_Rainfall_v2"}),

            Action(name="RecordQcReport", kwargs={"figure_label": "QC_RF_VAL_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_RF_VAL_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_RF_VAL_2025-08"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_041",
        instruction=(
            "Handle the task of summarizing April-2025 sales ETL and inform finance. Final state: ETL job 'sales_rollup_2025-04' (task monthly_sales_aggregation) status finished, rows_processed=420; QC 'QC_SALES_2025-04' is available as PDF; audit event 'SALES_QC_DONE' along with message; 'April sales aggregation complete.' An email has been sent to finance-team@example.com with subject 'QC_SALES_2025-04', body 'Sales aggregation QC attached.' and attachment URL is sent."
        ),
        actions=[
            Action(name="LogEtlExecution",
                   kwargs={"run_name": "sales_rollup_2025-04", "task": "monthly_sales_aggregation",
                           "status": "finished", "rows_processed": 420}),
            Action(name="FetchEtlExecution", kwargs={"run_name": "sales_rollup_2025-04"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_SALES_2025-04"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_SALES_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_SALES_2025-04.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_SALES_2025-04"}),

            Action(name="AppendAuditEvent",
                   kwargs={"event_type": "SALES_QC_DONE", "message": "April sales aggregation complete."}),
            Action(name="ReadAuditEvents", kwargs={"event_type": "SALES_QC_DONE"}),

            Action(name="DispatchResultsMail",
                   kwargs={"to_address": "finance-team@example.com", "subject": "QC_SALES_2025-04",
                           "body_text": "Sales aggregation QC attached.",
                           "attachment": "https://storage.example.com/reports/QC_SALES_2025-04.pdf"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_042",
        instruction=(
            "Coordinate the compilation of Jan-2025 precipitation totals and distribute externally. Series 'precip_total_2025-01' includes 3 values; [('2025-01-05T00:00:00Z', 14.2), ('2025-01-18T00:00:00Z', 9.7), ('2025-01-30T00:00:00Z', 12.5)] and is retrievable; QC report 'QC_PRECIP_2025-01' exists; stakeholder report 'Jan 2025 Precipitation Summary' targets an external audience."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "precip_total_2025-01", "items": [
                {"timestamp": "2025-01-05T00:00:00Z", "value": 14.2},
                {"timestamp": "2025-01-18T00:00:00Z", "value": 9.7},
                {"timestamp": "2025-01-30T00:00:00Z", "value": 12.5}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "precip_total_2025-01"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_PRECIP_2025-01"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_PRECIP_2025-01",
                                                    "figure_path": "https://storage.example.com/reports/QC_PRECIP_2025-01.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_PRECIP_2025-01"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Jan 2025 Precipitation Summary", "audience": "external",
                           "artifact_path": "https://storage.example.com/reports/QC_PRECIP_2025-01.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Jan 2025 Precipitation Summary"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_043",
        instruction=(
            "Handle the preparation of April-2025 tidal maxima, ensure QC validation, and distribute a municipal summary. Result: series 'tide_max_2025-04' has 3 values [('2025-04-02T00:00:00Z',3.12),('2025-04-15T00:00:00Z',3.44),('2025-04-29T00:00:00Z',3.21)] retrievable; QC report 'QC_TIDE_MAX_2025-04' exists as PDF; stakeholder summary 'April 2025 Tide Max Report' (audience municipal) links to QC doc."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "tide_max_2025-04", "items": [
                {"timestamp": "2025-04-02T00:00:00Z", "value": 3.12},
                {"timestamp": "2025-04-15T00:00:00Z", "value": 3.44},
                {"timestamp": "2025-04-29T00:00:00Z", "value": 3.21}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "tide_max_2025-04"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_TIDE_MAX_2025-04"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_TIDE_MAX_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_TIDE_MAX_2025-04.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_TIDE_MAX_2025-04"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "April 2025 Tide Max Report", "audience": "municipal",
                           "artifact_path": "https://storage.example.com/reports/QC_TIDE_MAX_2025-04.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "April 2025 Tide Max Report"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_044",
        instruction=(
            "Coordinate the QC of the coastal wind dataset (1995–2015) and compile an internal summary. Result: processed set 'wind_qc_1995_2015' holds [('avg_wind',12.4),('max_wind_day',68.0)] retrievable; QC file 'QC_WIND_1995_2015' exists as PDF; stakeholder report 'Wind QC 1995-2015' (audience internal) references QC doc."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "wind_qc_1995_2015", "items": [
                {"timestamp": "avg_wind", "value": 12.4},
                {"timestamp": "max_wind_day", "value": 68.0}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "wind_qc_1995_2015"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_WIND_1995_2015"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_WIND_1995_2015",
                                                    "figure_path": "https://storage.example.com/reports/QC_WIND_1995_2015.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_WIND_1995_2015"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Wind QC 1995-2015", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_WIND_1995_2015.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Wind QC 1995-2015"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_045",
        instruction=(
            "Handle the configuration and validation of 'LSTM_StormSurge_v3' using July-2025 data. Result: model 'LSTM_StormSurge_v3' (type lstm, framework tensorflow, version 3.0, status staged) is saved and queryable; validation batch 'VAL_SS_2025-07' contains one row ('2025-07-15T03:00:00Z', 1.92); validation MAE=0.15 logged; QC record 'QC_SS_VAL_2025-07' stored as CSV."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "LSTM_StormSurge_v3", "model_type": "lstm", "framework": "tensorflow",
                           "version": "3.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "LSTM_StormSurge_v3"}),

            Action(name="WritePredictionLot",
                   kwargs={"batch_name": "VAL_SS_2025-07", "model_name": "LSTM_StormSurge_v3",
                           "items": [{"timestamp": "2025-07-15T03:00:00Z", "prediction": 1.92}]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_SS_2025-07"}),

            Action(name="LogModelMetric",
                   kwargs={"model_name": "LSTM_StormSurge_v3", "metric_name": "MAE", "value": 0.15,
                           "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "LSTM_StormSurge_v3"}),

            Action(name="RecordQcReport", kwargs={"figure_label": "QC_SS_VAL_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_SS_VAL_2025-07.csv",
                                                    "artifact_type": "csv"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_SS_VAL_2025-07"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_046",
        instruction=(
            "Coordinate the setup of 'ARIMA_Precip_v1' and log August-2025 validation. Result: model 'ARIMA_Precip_v1' (type arima, framework statsmodels, version 1.0, status staged) is recorded; validation batch 'VAL_PC_2025-08' contains ('2025-08-05T12:00:00Z', 5.7); R²=0.89 captured; QC file 'QC_PC_VAL_2025-08' saved as PDF."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "ARIMA_Precip_v1", "model_type": "arima", "framework": "statsmodels",
                           "version": "1.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "ARIMA_Precip_v1"}),

            Action(name="WritePredictionLot", kwargs={"batch_name": "VAL_PC_2025-08", "model_name": "ARIMA_Precip_v1",
                                                        "items": [
                                                            {"timestamp": "2025-08-05T12:00:00Z", "prediction": 5.7}]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_PC_2025-08"}),

            Action(name="LogModelMetric", kwargs={"model_name": "ARIMA_Precip_v1", "metric_name": "R2", "value": 0.89,
                                                    "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "ARIMA_Precip_v1"}),

            Action(name="RecordQcReport", kwargs={"figure_label": "QC_PC_VAL_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_PC_VAL_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_PC_VAL_2025-08"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_047",
        instruction=(
            "Handle the registration of 'RandomForest_Wind_v5' and document the validation for September-2025. Result: the model 'RandomForest_Wind_v5' (type random_forest, framework sklearn, version 5.0, status staged) is retained; validation batch 'VAL_WD_2025-09' contains ('2025-09-18T15:00:00Z', 12.6); RMSE=1.2 is stored; QC PNG 'QC_WD_VAL_2025-09' is documented and accessible."
        ),
        actions=[
            Action(name="StoreModelArtifact",
                   kwargs={"model_name": "RandomForest_Wind_v5", "model_type": "random_forest", "framework": "sklearn",
                           "version": "5.0", "status": "staged"}),
            Action(name="FetchModelRecord", kwargs={"model_name": "RandomForest_Wind_v5"}),

            Action(name="WritePredictionLot",
                   kwargs={"batch_name": "VAL_WD_2025-09", "model_name": "RandomForest_Wind_v5",
                           "items": [{"timestamp": "2025-09-18T15:00:00Z", "prediction": 12.6}]}),
            Action(name="ReadPredictionLots", kwargs={"batch_name": "VAL_WD_2025-09"}),

            Action(name="LogModelMetric",
                   kwargs={"model_name": "RandomForest_Wind_v5", "metric_name": "RMSE", "value": 1.2,
                           "dataset_split": "validation"}),
            Action(name="ReadModelMetrics", kwargs={"model_name": "RandomForest_Wind_v5"}),

            Action(name="RecordQcReport", kwargs={"figure_label": "QC_WD_VAL_2025-09",
                                                    "figure_path": "https://storage.example.com/reports/QC_WD_VAL_2025-09.png",
                                                    "artifact_type": "png"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_WD_VAL_2025-09"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_048",
        instruction=(
            "Coordinate the validation of a 25-year NOAA coastal wind record. Final state: the processed set 'noaa_wind_qc_1995_2020' maintains [('mean_wind_speed', 12.4), ('max_wind_speed', 29.8)]; QC report 'QC_NOAA_WIND_1995_2020' (pdf) is filed; stakeholder deliverable 'NOAA Wind QC 1995-2020' marked for internal distribution links to the QC file."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "noaa_wind_qc_1995_2020", "items": [
                {"timestamp": "mean_wind_speed", "value": 12.4},
                {"timestamp": "max_wind_speed", "value": 29.8}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "noaa_wind_qc_1995_2020"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_NOAA_WIND_1995_2020"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_NOAA_WIND_1995_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_NOAA_WIND_1995_2020"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "NOAA Wind QC 1995-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_NOAA_WIND_1995_2020.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "NOAA Wind QC 1995-2020"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_049",
        instruction=(
            "Handle Quality-checking of a 20-year NOAA river discharge record. Final outcome: processed series 'noaa_river_qc_2000_2020' captures [('mean_discharge', 350.6), ('max_discharge', 1120.3)]; QC artifact 'QC_NOAA_RIVER_2000_2020' is registered as pdf; stakeholder note 'NOAA River QC 2000-2020' (internal) links to the stored file."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "noaa_river_qc_2000_2020", "items": [
                {"timestamp": "mean_discharge", "value": 350.6},
                {"timestamp": "max_discharge", "value": 1120.3}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "noaa_river_qc_2000_2020"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_NOAA_RIVER_2000_2020"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_NOAA_RIVER_2000_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_NOAA_RIVER_2000_2020"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "NOAA River QC 2000-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_NOAA_RIVER_2000_2020.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "NOAA River QC 2000-2020"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_050",
        instruction=(
            "Coordinate QC on a 15-year NOAA rainfall dataset. Desired state: 'noaa_precip_qc_2005_2020' includes [('mean_precip', 102.7), ('max_precip_day', 210.5)]; QC report 'QC_NOAA_PRECIP_2005_2020' saved as pdf; summary 'NOAA Precip QC 2005-2020' (internal) published with link to the file."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "noaa_precip_qc_2005_2020", "items": [
                {"timestamp": "mean_precip", "value": 102.7},
                {"timestamp": "max_precip_day", "value": 210.5}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "noaa_precip_qc_2005_2020"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_NOAA_PRECIP_2005_2020"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_NOAA_PRECIP_2005_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_NOAA_PRECIP_2005_2020"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "NOAA Precip QC 2005-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_2005_2020.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "NOAA Precip QC 2005-2020"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_051",
        instruction=(
            "Handle the checking and registration of a decade NOAA salinity dataset. Final outcome: 'noaa_salinity_qc_2010_2020' has [('mean_salinity', 35.1), ('max_salinity', 36.7)]; QC doc 'QC_NOAA_SALINITY_2010_2020' stored as pdf; stakeholder record 'NOAA Salinity QC 2010-2020' (internal) links to the report."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "noaa_salinity_qc_2010_2020", "items": [
                {"timestamp": "mean_salinity", "value": 35.1},
                {"timestamp": "max_salinity", "value": 36.7}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "noaa_salinity_qc_2010_2020"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_NOAA_SALINITY_2010_2020"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_NOAA_SALINITY_2010_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_NOAA_SALINITY_2010_2020"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "NOAA Salinity QC 2010-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_NOAA_SALINITY_2010_2020.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "NOAA Salinity QC 2010-2020"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_052",
        instruction=(
            "Coordinate the auditing of a 12-year NOAA sea surface temperature series. Final state: 'noaa_sst_qc_2008_2020' reports [('mean_sst', 18.5), ('max_sst', 29.2)]; QC label 'QC_NOAA_SST_2008_2020' (pdf) stored; stakeholder entry 'NOAA SST QC 2008-2020' (internal) published with reference."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "noaa_sst_qc_2008_2020", "items": [
                {"timestamp": "mean_sst", "value": 18.5},
                {"timestamp": "max_sst", "value": 29.2}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "noaa_sst_qc_2008_2020"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_NOAA_SST_2008_2020"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_NOAA_SST_2008_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_NOAA_SST_2008_2020"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "NOAA SST QC 2008-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_NOAA_SST_2008_2020.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "NOAA SST QC 2008-2020"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_053",
        instruction=(
            "Coordinate the preparation of a logistic-regression wildfire risk dataset 'wildfire_risk_v1' for 2025-06. Final state: feature set 'wildfire_risk_v1' (version '1.0') with columns ['temperature','humidity','fire_risk'] is registered and accessible; feature file '/features/wildfire_risk_v1.parquet' is ensured to exist and be retrievable; a QC PDF is generated for label 'QC_WILDFIRE_RISK_2025-06' with the figure recorded (artifact_type 'pdf') and accessible; stakeholder output 'Wildfire Risk Jun 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf' and is accessible."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "wildfire_risk_v1", "version": "1.0",
                                                           "columns": ["temperature", "humidity", "fire_risk"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "wildfire_risk_v1"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/wildfire_risk_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/wildfire_risk_v1.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_WILDFIRE_RISK_2025-06"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_WILDFIRE_RISK_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_WILDFIRE_RISK_2025-06"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Wildfire Risk Jun 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_WILDFIRE_RISK_2025-06.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Wildfire Risk Jun 2025"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_054",
        instruction=(
            "Organize the publication of the flood prediction dataset 'flood_forecast_v2' for 2025-05. Final state: feature set 'flood_forecast_v2' (version '2.0') with columns ['rainfall','river_level','flood_probability'] is registered and accessible; feature file '/features/flood_forecast_v2.parquet' is ensured to exist and be retrievable; a QC PDF for 'QC_FLOOD_FORECAST_2025-05' is created and stored (artifact_type 'pdf'); stakeholder output 'Flood Forecast May 2025' (audience 'internal') references 'https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf' and is accessible."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "flood_forecast_v2", "version": "2.0",
                                                           "columns": ["rainfall", "river_level",
                                                                       "flood_probability"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "flood_forecast_v2"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/flood_forecast_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/flood_forecast_v2.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_FLOOD_FORECAST_2025-05"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_FLOOD_FORECAST_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_FLOOD_FORECAST_2025-05"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Flood Forecast May 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_FLOOD_FORECAST_2025-05.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Flood Forecast May 2025"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_055",
        instruction=(
            "Handle the air quality prediction dataset 'air_quality_index_v3' for 2025-07. End state: feature set 'air_quality_index_v3' (version '3.0') with columns ['PM2_5','PM10','AQI'] is registered and accessible; feature file '/features/air_quality_index_v3.parquet' is present and retrievable; a QC PDF for 'QC_AIR_QUALITY_2025-07' is created and documented (artifact_type 'pdf'); stakeholder output 'Air Quality Jul 2025' (audience 'internal') includes 'https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf' and is accessible."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "air_quality_index_v3", "version": "3.0",
                                                           "columns": ["PM2_5", "PM10", "AQI"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "air_quality_index_v3"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/air_quality_index_v3.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/air_quality_index_v3.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_AIR_QUALITY_2025-07"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_AIR_QUALITY_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_AIR_QUALITY_2025-07"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Air Quality Jul 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_AIR_QUALITY_2025-07.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Air Quality Jul 2025"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_056",
        instruction=(
            "Manage the release of the coastal erosion prediction dataset 'coastal_erosion_v2' for 2025-08. Final condition: feature set 'coastal_erosion_v2' (version '2.0') with columns ['wave_height','shoreline_change','erosion_risk'] is registered and accessible; feature file '/features/coastal_erosion_v2.parquet' is available and can be accessed; a QC PDF for 'QC_COASTAL_EROSION_2025-08' is generated and archived (artifact_type 'pdf'); stakeholder output 'Coastal Erosion Aug 2025' (audience 'internal') includes 'https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf' and is accessible."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "coastal_erosion_v2", "version": "2.0",
                                                           "columns": ["wave_height", "shoreline_change",
                                                                       "erosion_risk"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "coastal_erosion_v2"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/coastal_erosion_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/coastal_erosion_v2.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_COASTAL_EROSION_2025-08"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_COASTAL_EROSION_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_COASTAL_EROSION_2025-08"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Coastal Erosion Aug 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_COASTAL_EROSION_2025-08.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Coastal Erosion Aug 2025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_057",
        instruction=(
            "Develop a September-2025 sea-surface temperature anomaly dataset including QC. Final state: the processed series 'sst_anom_2025-09' contains three entries [('2025-09-03T00:00:00Z', 0.25), ('2025-09-15T00:00:00Z', -0.12), ('2025-09-28T00:00:00Z', 0.08)] and can be retrieved; a QC PDF under the label 'QC_SST_ANOM_2025-09' is documented and accessible."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "sst_anom_2025-09", "items": [
                {"timestamp": "2025-09-03T00:00:00Z", "value": 0.25},
                {"timestamp": "2025-09-15T00:00:00Z", "value": -0.12},
                {"timestamp": "2025-09-28T00:00:00Z", "value": 0.08}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "sst_anom_2025-09"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_SST_ANOM_2025-09"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_SST_ANOM_2025-09",
                                                    "figure_path": "https://storage.example.com/reports/QC_SST_ANOM_2025-09.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_SST_ANOM_2025-09"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_058",
        instruction=(
            "Construct an October-2025 chlorophyll anomaly dataset along with QC. Final state: processed series 'chl_anom_2025-10' includes [('2025-10-01T00:00:00Z', 1.15), ('2025-10-12T00:00:00Z', -0.95), ('2025-10-25T00:00:00Z', 0.60)] and can be retrieved; the QC file 'QC_CHL_ANOM_2025-10' is archived as a pdf and accessible."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "chl_anom_2025-10", "items": [
                {"timestamp": "2025-10-01T00:00:00Z", "value": 1.15},
                {"timestamp": "2025-10-12T00:00:00Z", "value": -0.95},
                {"timestamp": "2025-10-25T00:00:00Z", "value": 0.60}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "chl_anom_2025-10"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CHL_ANOM_2025-10"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_CHL_ANOM_2025-10",
                                                    "figure_path": "https://storage.example.com/reports/QC_CHL_ANOM_2025-10.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CHL_ANOM_2025-10"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_059",
        instruction=(
            "Handle logging of a November-2025 nitrate anomaly dataset with QC. Final state: the processed series 'no3_anom_2025-11' includes [('2025-11-05T00:00:00Z', 0.55), ('2025-11-16T00:00:00Z', -0.40), ('2025-11-29T00:00:00Z', 0.22)] and can be retrieved; the QC report 'QC_NO3_ANOM_2025-11' is saved as a pdf and is accessible."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "no3_anom_2025-11", "items": [
                {"timestamp": "2025-11-05T00:00:00Z", "value": 0.55},
                {"timestamp": "2025-11-16T00:00:00Z", "value": -0.40},
                {"timestamp": "2025-11-29T00:00:00Z", "value": 0.22}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "no3_anom_2025-11"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_NO3_ANOM_2025-11"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_NO3_ANOM_2025-11",
                                                    "figure_path": "https://storage.example.com/reports/QC_NO3_ANOM_2025-11.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_NO3_ANOM_2025-11"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_060",
        instruction=(
            "Coordinate registration of feature bundle 'port_departure_metrics_v1' version 1.1 and activate it. Final state: the feature bundle 'port_departure_metrics_v1' has columns ['departure_count','avg_wait_time','max_wait_time'] and is accessible; the feature file '/features/port_departure_metrics_v1.parquet' is present and readable; project settings indicate 'active_feature_set' = 'port_departure_metrics_v1'; the QC report 'QC_PORT_DEPARTURE_2025-03' is stored as a pdf and is accessible."
        ),
        actions=[
            Action(name="RegisterFeatureBundle",
                   kwargs={"feature_set_name": "port_departure_metrics_v1", "version": "1.1",
                           "columns": ["departure_count", "avg_wait_time", "max_wait_time"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "port_departure_metrics_v1"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/port_departure_metrics_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/port_departure_metrics_v1.parquet"}),

            Action(name="PatchProjectSettings",
                   kwargs={"updates": {"active_feature_set": "port_departure_metrics_v1"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "active_feature_set"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_PORT_DEPARTURE_2025-03"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_PORT_DEPARTURE_2025-03",
                                                    "figure_path": "https://storage.example.com/reports/QC_PORT_DEPARTURE_2025-03.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_PORT_DEPARTURE_2025-03"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_061",
        instruction=(
            "Handle the distribution of an April-2025 Puget Sound wave height dataset. Final state: the processed series 'wave_height_2025-04' contains three points [('2025-04-05T00:00:00Z', 1.2), ('2025-04-12T00:00:00Z', 0.8), ('2025-04-19T00:00:00Z', 1.5)] and can be accessed; a QC PDF titled 'QC_WAVE_HEIGHT_2025-04' is filed (artifact_type 'pdf') and accessible; the stakeholder artifact 'Wave Height Apr 2025' (audience 'internal') links to 'https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf' and is accessible."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "wave_height_2025-04", "items": [
                {"timestamp": "2025-04-05T00:00:00Z", "value": 1.2},
                {"timestamp": "2025-04-12T00:00:00Z", "value": 0.8},
                {"timestamp": "2025-04-19T00:00:00Z", "value": 1.5}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "wave_height_2025-04"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_WAVE_HEIGHT_2025-04"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_WAVE_HEIGHT_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_WAVE_HEIGHT_2025-04"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Wave Height Apr 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_WAVE_HEIGHT_2025-04.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Wave Height Apr 2025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_062",
        instruction=(
            "Coordinate the assembly of a logistic regression climate risk feature set 'climate_risk_v1' for Apr-2025. Final state: the feature set 'climate_risk_v1' (version '1.0') including fields ['temperature','rainfall','flood_risk'] is stored and accessible; the file '/features/climate_risk_v1.parquet' is available and accessible; a QC PDF labeled 'QC_CLIMATE_RISK_2025-04' is documented (artifact_type 'pdf') and accessible; the stakeholder artifact 'Climate Risk Apr 2025' (audience 'internal') refers to 'https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf' and is accessible."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "climate_risk_v1", "version": "1.0",
                                                           "columns": ["temperature", "rainfall", "flood_risk"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "climate_risk_v1"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/climate_risk_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/climate_risk_v1.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CLIMATE_RISK_2025-04"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_CLIMATE_RISK_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CLIMATE_RISK_2025-04"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Climate Risk Apr 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_CLIMATE_RISK_2025-04.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Climate Risk Apr 2025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_063",
        instruction=(
            "Handle surge-risk feature QC validation for April-2025. End state: feature bundle 'surge_risk_v2' (version 2.1) containing columns ['risk_index','exceedance_prob'] is registered and accessible; feature file '/features/surge_risk_v2.parquet' exists and is retrievable; QC report 'QC_SURGE_RISK_2025-04' is stored as a pdf and accessible; stakeholder artifact 'Surge Risk QC Apr 2025' (audience regulators) is published with a link to the pdf."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "surge_risk_v2", "version": "2.1",
                                                           "columns": ["risk_index", "exceedance_prob"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "surge_risk_v2"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/surge_risk_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/surge_risk_v2.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_SURGE_RISK_2025-04"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_SURGE_RISK_2025-04",
                                                    "figure_path": "https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_SURGE_RISK_2025-04"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Surge Risk QC Apr 2025", "audience": "regulators",
                           "artifact_path": "https://storage.example.com/reports/QC_SURGE_RISK_2025-04.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Surge Risk QC Apr 2025"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_064",
        instruction=(
            "Coordinate wave anomaly QC completion for May-2025. End state: feature bundle 'wave_anomaly_v1' (version 1.3) with columns ['hmean','hmax','stddev'] is registered and accessible; feature file '/features/wave_anomaly_v1.parquet' exists and can be accessed; QC report 'QC_WAVE_ANOMALY_2025-05' is archived as pdf; stakeholder artifact 'Wave Anomaly QC May 2025' (audience science_team) references the pdf and is accessible."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "wave_anomaly_v1", "version": "1.3",
                                                           "columns": ["hmean", "hmax", "stddev"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "wave_anomaly_v1"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/wave_anomaly_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/wave_anomaly_v1.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_WAVE_ANOMALY_2025-05"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_WAVE_ANOMALY_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_WAVE_ANOMALY_2025-05"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Wave Anomaly QC May 2025", "audience": "science_team",
                           "artifact_path": "https://storage.example.com/reports/QC_WAVE_ANOMALY_2025-05.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Wave Anomaly QC May 2025"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_065",
        instruction=(
            "Handle the task of validating the rainfall intensity QC for June-2025. Final status: the feature bundle 'rain_intensity_v3' (version 3.0) containing columns ['avg_rate','peak_rate','duration'] is saved and accessible; the feature file '/features/rain_intensity_v3.parquet' exists and can be retrieved; the QC report 'QC_RAIN_INTENSITY_2025-06' is archived in pdf format; the stakeholder artifact 'Rainfall Intensity QC Jun 2025' (audience external_partners) links to the pdf and is available."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "rain_intensity_v3", "version": "3.0",
                                                           "columns": ["avg_rate", "peak_rate", "duration"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "rain_intensity_v3"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/rain_intensity_v3.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/rain_intensity_v3.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_RAIN_INTENSITY_2025-06"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_RAIN_INTENSITY_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_RAIN_INTENSITY_2025-06"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Rainfall Intensity QC Jun 2025", "audience": "external_partners",
                           "artifact_path": "https://storage.example.com/reports/QC_RAIN_INTENSITY_2025-06.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Rainfall Intensity QC Jun 2025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_066",
        instruction=(
            "Coordinate the setup of the retrain window for April-2025 and ensure its confirmation. Final outcome: the project settings include retrain_window_start=2025-04-01T00:00:00Z and retrain_window_end=2025-04-30T23:59:59Z; the audit log entry 'MODEL_RETRAIN_WINDOW_SET' with the message 'April retrain window applied.' is logged and accessible; the QC report 'QC_CONFIG_RETRAIN_2025-04' is saved as a pdf and is accessible; an additional audit verification confirms the same event."
        ),
        actions=[
            Action(name="PatchProjectSettings", kwargs={"updates": {
                "retrain_window_start": "2025-04-01T00:00:00Z",
                "retrain_window_end": "2025-04-30T23:59:59Z"
            }}),
            Action(name="ReadProjectSettings", kwargs={"key": "retrain_window_start"}),
            Action(name="ReadProjectSettings", kwargs={"key": "retrain_window_end"}),

            Action(name="AppendAuditEvent", kwargs={
                "event_type": "MODEL_RETRAIN_WINDOW_SET",
                "message": "April retrain window applied."
            }),
            Action(name="ReadAuditEvents", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-04"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_CONFIG_RETRAIN_2025-04",
                "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-04.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-04"}),
            Action(name="ReadAuditEvents", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_067",
        instruction=(
            "Handle a validation checkpoint for February-2026 and verify readiness. End state: project settings contain validation_checkpoint '2026-02-14T14:00:00Z' and are accessible; audit event 'VALIDATION_CHECKPOINT_SET' with message 'Validation checkpoint created for mid-February.' is available and accessible; QC report 'QC_CONFIG_VALIDATION_2026-02' is saved as pdf and retrievable."
        ),
        actions=[
            Action(name="PatchProjectSettings",
                   kwargs={"updates": {"validation_checkpoint": "2026-02-14T14:00:00Z"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "validation_checkpoint"}),

            Action(name="AppendAuditEvent", kwargs={"event_type": "VALIDATION_CHECKPOINT_SET",
                                                      "message": "Validation checkpoint created for mid-February."}),
            Action(name="ReadAuditEvents", kwargs={"event_type": "VALIDATION_CHECKPOINT_SET"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CONFIG_VALIDATION_2026-02"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_CONFIG_VALIDATION_2026-02",
                                                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_VALIDATION_2026-02.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CONFIG_VALIDATION_2026-02"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_068",
        instruction=(
            "Coordinate the publication of the May-2025 precipitation anomaly series and include QC. End state: processed series 'precip_anom_2025-05' features three data points [('2025-05-02T00:00:00Z', -12.5), ('2025-05-18T00:00:00Z', 8.3), ('2025-05-29T00:00:00Z', 3.1)] and is accessible; QC PDF titled 'QC_PRECIP_ANOM_2025-05' is saved and accessible."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "precip_anom_2025-05", "items": [
                {"timestamp": "2025-05-02T00:00:00Z", "value": -12.5},
                {"timestamp": "2025-05-18T00:00:00Z", "value": 8.3},
                {"timestamp": "2025-05-29T00:00:00Z", "value": 3.1}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "precip_anom_2025-05"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-05"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_PRECIP_ANOM_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_PRECIP_ANOM_2025-05"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_069",
        instruction=(
            "Handle the publication of the June-2025 sea-level anomaly series ensuring QC validation. Final condition: processed series 'sea_lvl_anom_2025-06' comprises three entries [('2025-06-04T00:00:00Z', 0.12), ('2025-06-14T00:00:00Z', -0.05), ('2025-06-25T00:00:00Z', 0.22)] and is accessible; QC PDF titled 'QC_SEA_LVL_ANOM_2025-06' is archived and accessible."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "sea_lvl_anom_2025-06", "items": [
                {"timestamp": "2025-06-04T00:00:00Z", "value": 0.12},
                {"timestamp": "2025-06-14T00:00:00Z", "value": -0.05},
                {"timestamp": "2025-06-25T00:00:00Z", "value": 0.22}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "sea_lvl_anom_2025-06"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_SEA_LVL_ANOM_2025-06"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_SEA_LVL_ANOM_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_SEA_LVL_ANOM_2025-06.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_SEA_LVL_ANOM_2025-06"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_070",
        instruction=(
            "Coordinate the release of the July-2025 wind-speed anomaly series and append QC. Final condition: processed series 'windspd_anom_2025-07' comprises three entries [('2025-07-07T00:00:00Z', 2.5), ('2025-07-16T00:00:00Z', -1.8), ('2025-07-28T00:00:00Z', 0.9)] and is accessible; QC PDF titled 'QC_WINDSPD_ANOM_2025-07' is archived and accessible."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "windspd_anom_2025-07", "items": [
                {"timestamp": "2025-07-07T00:00:00Z", "value": 2.5},
                {"timestamp": "2025-07-16T00:00:00Z", "value": -1.8},
                {"timestamp": "2025-07-28T00:00:00Z", "value": 0.9}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "windspd_anom_2025-07"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_WINDSPD_ANOM_2025-07"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_WINDSPD_ANOM_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_WINDSPD_ANOM_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_WINDSPD_ANOM_2025-07"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_071",
        instruction=(
            "Handle the publication of the August-2025 humidity anomaly series with QC validation. End state: the processed series 'humid_anom_2025-08' features three points [('2025-08-03T00:00:00Z', 4.0), ('2025-08-14T00:00:00Z', -2.7), ('2025-08-26T00:00:00Z', 1.5)] and is accessible; QC PDF labeled 'QC_HUMID_ANOM_2025-08' is stored and accessible."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "humid_anom_2025-08", "items": [
                {"timestamp": "2025-08-03T00:00:00Z", "value": 4.0},
                {"timestamp": "2025-08-14T00:00:00Z", "value": -2.7},
                {"timestamp": "2025-08-26T00:00:00Z", "value": 1.5}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "humid_anom_2025-08"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_HUMID_ANOM_2025-08"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_HUMID_ANOM_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_HUMID_ANOM_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_HUMID_ANOM_2025-08"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_072",
        instruction=(
            "Manage the release of a July-2025 wave-height anomaly series with QC evidence. End state: the processed series 'wave_anom_2025-07' includes three points [('2025-07-07T00:00:00Z', 0.35), ('2025-07-18T00:00:00Z', -0.06), ('2025-07-29T00:00:00Z', 0.21)] and is available; a QC PDF labeled 'QC_WAVE_ANOM_2025-07' is available and retrievable."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "wave_anom_2025-07", "items": [
                {"timestamp": "2025-07-07T00:00:00Z", "value": 0.35},
                {"timestamp": "2025-07-18T00:00:00Z", "value": -0.06},
                {"timestamp": "2025-07-29T00:00:00Z", "value": 0.21}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "wave_anom_2025-07"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_WAVE_ANOM_2025-07"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_WAVE_ANOM_2025-07",
                "figure_path": "https://storage.example.com/reports/QC_WAVE_ANOM_2025-07.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_WAVE_ANOM_2025-07"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_073",
        instruction=(
            "Handle the publication of an August-2025 dissolved-oxygen anomaly series and ensure QC is attached. End state: the processed series 'do_anom_2025-08' contains three entries [('2025-08-02T00:00:00Z', 0.18), ('2025-08-14T00:00:00Z', -0.07), ('2025-08-27T00:00:00Z', 0.10)] and is accessible; a QC PDF labeled 'QC_DO_ANOM_2025-08' exists and can be retrieved."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "do_anom_2025-08", "items": [
                {"timestamp": "2025-08-02T00:00:00Z", "value": 0.18},
                {"timestamp": "2025-08-14T00:00:00Z", "value": -0.07},
                {"timestamp": "2025-08-27T00:00:00Z", "value": 0.10}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "do_anom_2025-08"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_DO_ANOM_2025-08"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_DO_ANOM_2025-08",
                "figure_path": "https://storage.example.com/reports/QC_DO_ANOM_2025-08.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_DO_ANOM_2025-08"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_074",
        instruction=(
            "Coordinate the onboarding of 'XGBoost_Rainfall_v1' (v1.0) along with its configuration, test score, and artifact. End state: the model 'XGBoost_Rainfall_v1' (type 'xgboost', framework 'xgboost', version '1.0', status 'staged') is stored; profile 'default' has max_depth=5, n_estimators=150, learning_rate=0.05; the test AUC=0.94 is noted; the artifact '/models/XGBoost_Rainfall_v1_v1.0.json' is documented and accessible."
        ),
        actions=[
            Action(name="StoreModelArtifact", kwargs={
                "model_name": "XGBoost_Rainfall_v1",
                "model_type": "xgboost",
                "framework": "xgboost",
                "version": "1.0",
                "status": "staged"
            }),
            Action(name="FetchModelRecord", kwargs={"model_name": "XGBoost_Rainfall_v1"}),

            Action(name="UpsertModelProfile", kwargs={
                "model_name": "XGBoost_Rainfall_v1",
                "profile_name": "default",
                "params": {"max_depth": 5, "n_estimators": 150, "learning_rate": 0.05}
            }),
            Action(name="ReadModelProfiles", kwargs={"model_name": "XGBoost_Rainfall_v1"}),

            Action(name="LogModelMetric", kwargs={
                "model_name": "XGBoost_Rainfall_v1",
                "metric_name": "AUC",
                "value": 0.94,
                "dataset_split": "test"
            }),
            Action(name="ReadModelMetrics", kwargs={"model_name": "XGBoost_Rainfall_v1"}),

            Action(name="RegisterFileEntry", kwargs={
                "path": "/models/XGBoost_Rainfall_v1_v1.0.json",
                "mime_type": "application/json"
            }),
            Action(name="RetrieveFileEntry", kwargs={"path": "/models/XGBoost_Rainfall_v1_v1.0.json"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_075",
        instruction=(
            "Handle the registration of a coastal flood dataset 'flood_risk_v5' for October-2025. Final result: feature bundle 'flood_risk_v5' (version '5.0') with columns ['flood_probability','storm_surge_height','risk_index'] is saved and retrievable; file '/features/flood_risk_v5.parquet' exists and is readable; QC PDF 'QC_FLOOD_RISK_2025-10' is generated; stakeholder artifact 'Flood Risk Oct 2025' (audience 'internal') links to the same pdf."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "flood_risk_v5", "version": "5.0",
                                                           "columns": ["flood_probability", "storm_surge_height",
                                                                       "risk_index"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "flood_risk_v5"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/flood_risk_v5.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/flood_risk_v5.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_FLOOD_RISK_2025-10"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_FLOOD_RISK_2025-10",
                                                    "figure_path": "https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_FLOOD_RISK_2025-10"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Flood Risk Oct 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_FLOOD_RISK_2025-10.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Flood Risk Oct 2025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_076",
        instruction=(
            "Coordinate the preparation of a tidal variation dataset 'tidal_variation_v3' for November-2025. Final outcome: bundle 'tidal_variation_v3' (version '3.0') with fields ['high_tide','low_tide','tidal_range'] is stored and accessible; file '/features/tidal_variation_v3.parquet' exists and is retrievable; QC report 'QC_TIDAL_VARIATION_2025-11' is archived; stakeholder output 'Tidal Variation Nov 2025' (audience 'internal') links to the report."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "tidal_variation_v3", "version": "3.0",
                                                           "columns": ["high_tide", "low_tide", "tidal_range"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "tidal_variation_v3"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/tidal_variation_v3.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/tidal_variation_v3.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_TIDAL_VARIATION_2025-11"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_TIDAL_VARIATION_2025-11",
                                                    "figure_path": "https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_TIDAL_VARIATION_2025-11"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Tidal Variation Nov 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_TIDAL_VARIATION_2025-11.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Tidal Variation Nov 2025"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_077",
        instruction=(
            "Confirm the validation of a 40-year NOAA precipitation archive. Desired outcome: processed series 'noaa_precip_qc_1980_2020' contains points [('annual_avg', 1023.4), ('max_annual', 1820.1), ('min_annual', 540.2)] and is available; QC document 'QC_NOAA_PRECIP_1980_2020' is filed; stakeholder note 'NOAA Precipitation QC 1980-2020' (audience 'internal') is linked to the pdf."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "noaa_precip_qc_1980_2020", "items": [
                {"timestamp": "annual_avg", "value": 1023.4},
                {"timestamp": "max_annual", "value": 1820.1},
                {"timestamp": "min_annual", "value": 540.2}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "noaa_precip_qc_1980_2020"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_NOAA_PRECIP_1980_2020"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_NOAA_PRECIP_1980_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_NOAA_PRECIP_1980_2020"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "NOAA Precipitation QC 1980-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_NOAA_PRECIP_1980_2020.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "NOAA Precipitation QC 1980-2020"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_078",
        instruction=(
            "Ensure QC of a 20-year USGS groundwater record. Target result: processed series 'usgs_groundwater_qc_2005_2025' includes summary [('mean_level', 15.7), ('lowest_level', 3.4), ('highest_level', 28.1)] and can be accessed; QC file 'QC_USGS_GW_2005_2025' is available as pdf; stakeholder entry 'USGS Groundwater QC 2005-2025' (audience 'internal') is linked to it."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "usgs_groundwater_qc_2005_2025", "items": [
                {"timestamp": "mean_level", "value": 15.7},
                {"timestamp": "lowest_level", "value": 3.4},
                {"timestamp": "highest_level", "value": 28.1}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "usgs_groundwater_qc_2005_2025"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_USGS_GW_2005_2025"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_USGS_GW_2005_2025",
                                                    "figure_path": "https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_USGS_GW_2005_2025"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "USGS Groundwater QC 2005-2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_USGS_GW_2005_2025.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "USGS Groundwater QC 2005-2025"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_079",
        instruction=(
            "Handle QC for a Landsat surface temperature dataset encompassing 1990–2020. Desired outcome: the processed series 'landsat_surf_temp_qc_1990_2020' comprises [('avg_temp', 22.3), ('max_temp_day', 38.7), ('min_temp_day', -4.2)] and remains readable; QC artifact 'QC_LANDSAT_TEMP_1990_2020' is preserved; stakeholder documentation 'Landsat Surface Temp QC 1990–2020' (audience 'internal') is linked to the report."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "landsat_surf_temp_qc_1990_2020", "items": [
                {"timestamp": "avg_temp", "value": 22.3},
                {"timestamp": "max_temp_day", "value": 38.7},
                {"timestamp": "min_temp_day", "value": -4.2}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "landsat_surf_temp_qc_1990_2020"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_LANDSAT_TEMP_1990_2020"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_LANDSAT_TEMP_1990_2020",
                                                    "figure_path": "https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_LANDSAT_TEMP_1990_2020"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Landsat Surface Temp QC 1990-2020", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_LANDSAT_TEMP_1990_2020.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Landsat Surface Temp QC 1990-2020"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_080",
        instruction=(
            "Coordinate QC for a TRMM rainfall archive covering the period from 1998–2018. Expected result: the processed series 'trmm_rainfall_qc_1998_2018' contains [('annual_avg', 105.7), ('max_daily_rain', 289.5), ('min_daily_rain', 0.0)] and is accessible; QC report 'QC_TRMM_RAINFALL_1998_2018' is available as a pdf; stakeholder note 'TRMM Rainfall QC 1998-2018' (audience 'external') connects to the stored pdf."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "trmm_rainfall_qc_1998_2018", "items": [
                {"timestamp": "annual_avg", "value": 105.7},
                {"timestamp": "max_daily_rain", "value": 289.5},
                {"timestamp": "min_daily_rain", "value": 0.0}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "trmm_rainfall_qc_1998_2018"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_TRMM_RAINFALL_1998_2018"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_TRMM_RAINFALL_1998_2018",
                                                    "figure_path": "https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_TRMM_RAINFALL_1998_2018"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "TRMM Rainfall QC 1998-2018", "audience": "external",
                           "artifact_path": "https://storage.example.com/reports/QC_TRMM_RAINFALL_1998_2018.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "TRMM Rainfall QC 1998-2018"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_081",
        instruction=(
            "Handle the preparation of a drought risk dataset 'drought_risk_v1' for September-2025. Desired outcome: bundle 'drought_risk_v1' (version '1.0') with fields ['soil_moisture','temperature','drought_index'] is stored and queryable; file '/features/drought_risk_v1.parquet' is available and retrievable; QC record 'QC_DROUGHT_RISK_2025-09' is archived as pdf; stakeholder artifact 'Drought Risk Sep 2025' (audience 'internal') links to 'https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf'."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "drought_risk_v1", "version": "1.0",
                                                           "columns": ["soil_moisture", "temperature",
                                                                       "drought_index"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "drought_risk_v1"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/drought_risk_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/drought_risk_v1.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_DROUGHT_RISK_2025-09"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_DROUGHT_RISK_2025-09",
                                                    "figure_path": "https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_DROUGHT_RISK_2025-09"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Drought Risk Sep 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_DROUGHT_RISK_2025-09.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Drought Risk Sep 2025"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_082",
        instruction=(
            "Coordinate the completion of sea surface temperature feature QC for June-2025. Desired outcome: bundle 'sst_features_v2' (version '2.1') with fields ['sst_mean','sst_max','sst_std'] is registered and accessible; file '/features/sst_features_v2.parquet' is available and retrievable; QC record 'QC_SST_FEATURES_2025-06' is stored; stakeholder artifact 'SST QC June 2025' (audience 'oceanography_team') links to 'https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf'."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "sst_features_v2", "version": "2.1",
                                                           "columns": ["sst_mean", "sst_max", "sst_std"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "sst_features_v2"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/sst_features_v2.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/sst_features_v2.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_SST_FEATURES_2025-06"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_SST_FEATURES_2025-06",
                                                    "figure_path": "https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_SST_FEATURES_2025-06"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "SST QC June 2025", "audience": "oceanography_team",
                           "artifact_path": "https://storage.example.com/reports/QC_SST_FEATURES_2025-06.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "SST QC June 2025"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_083",
        instruction=(
            "Ensure ocean current feature QC for July-2025 is concluded. Desired final state: bundle 'ocean_current_v1' (version '1.5') includes fields ['current_speed','current_dir','std_dev'] is saved and viewable; file '/features/ocean_current_v1.parquet' remains available and accessible; QC artifact 'QC_OCEAN_CURRENT_2025-07' is securely stored; stakeholder artifact 'Ocean Current QC July 2025' (for audience 'marine_team') points to 'https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf'."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "ocean_current_v1", "version": "1.5",
                                                           "columns": ["current_speed", "current_dir", "std_dev"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "ocean_current_v1"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/ocean_current_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/ocean_current_v1.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_OCEAN_CURRENT_2025-07"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_OCEAN_CURRENT_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_OCEAN_CURRENT_2025-07"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Ocean Current QC July 2025", "audience": "marine_team",
                           "artifact_path": "https://storage.example.com/reports/QC_OCEAN_CURRENT_2025-07.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Ocean Current QC July 2025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_084",
        instruction=(
            "Complete the ocean salinity feature QC for August-2025. The end status: bundle 'salinity_index_v1' (version '1.2') including fields ['salinity_mean','salinity_max','salinity_std'] is registered and available; file '/features/salinity_index_v1.parquet' is retrievable and accessible; QC record 'QC_SALINITY_INDEX_2025-08' is stored; stakeholder artifact 'Salinity Index QC Aug 2025' (designed for 'research_team') links to 'https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf'."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "salinity_index_v1", "version": "1.2",
                                                           "columns": ["salinity_mean", "salinity_max",
                                                                       "salinity_std"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "salinity_index_v1"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/salinity_index_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/salinity_index_v1.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_SALINITY_INDEX_2025-08"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_SALINITY_INDEX_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_SALINITY_INDEX_2025-08"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Salinity Index QC Aug 2025", "audience": "research_team",
                           "artifact_path": "https://storage.example.com/reports/QC_SALINITY_INDEX_2025-08.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Salinity Index QC Aug 2025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_085",
        instruction=(
            "You construct feature set 'coastal_flood_features_v1' (v1.0) with necessary columns ['water_level_max','wave_height_mean','precipitation_total'] and activate it. End state: feature set can be retrieved; feature file '/features/coastal_flood_features_v1.parquet' is available and accessible; project setting 'active_feature_set' is set to 'coastal_flood_features_v1'; QC PDF 'QC_COASTAL_FEATURES_2025-06' is saved and accessible."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={
                "feature_set_name": "coastal_flood_features_v1",
                "version": "1.0",
                "columns": ["water_level_max", "wave_height_mean", "precipitation_total"]
            }),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "coastal_flood_features_v1"}),

            Action(name="RegisterFileEntry", kwargs={
                "path": "/features/coastal_flood_features_v1.parquet",
                "mime_type": "application/parquet"
            }),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/coastal_flood_features_v1.parquet"}),

            Action(name="PatchProjectSettings",
                   kwargs={"updates": {"active_feature_set": "coastal_flood_features_v1"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "active_feature_set"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_COASTAL_FEATURES_2025-06"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_COASTAL_FEATURES_2025-06",
                "figure_path": "https://storage.example.com/reports/QC_COASTAL_FEATURES_2025-06.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_COASTAL_FEATURES_2025-06"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_086",
        instruction=(
            "Establish a May-2025 model retrain window and confirm it. End state: project settings show retrain_window_start '2025-05-01T00:00:00Z' and retrain_window_end '2025-05-31T23:59:59Z'; audit entry 'MODEL_RETRAIN_WINDOW_SET' with message 'May retrain window applied.' is verified twice; QC report 'QC_CONFIG_RETRAIN_2025-05' is stored as a PDF and checked."
        ),
        actions=[
            Action(name="PatchProjectSettings", kwargs={"updates": {
                "retrain_window_start": "2025-05-01T00:00:00Z",
                "retrain_window_end": "2025-05-31T23:59:59Z"
            }}),
            Action(name="ReadProjectSettings", kwargs={"key": "retrain_window_start"}),
            Action(name="ReadProjectSettings", kwargs={"key": "retrain_window_end"}),

            Action(name="AppendAuditEvent", kwargs={
                "event_type": "MODEL_RETRAIN_WINDOW_SET",
                "message": "May retrain window applied."
            }),
            Action(name="ReadAuditEvents", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-05"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_CONFIG_RETRAIN_2025-05",
                "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-05.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-05"}),
            Action(name="ReadAuditEvents", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_087",
        instruction=(
            "Handle setting up a retrain window for June 2025 and confirm its configuration. End state: settings should display retrain_window_start '2025-06-01T00:00:00Z' and retrain_window_end '2025-06-30T23:59:59Z'; audit event 'MODEL_RETRAIN_WINDOW_SET' with message 'June retrain window applied.' must be logged and verified twice; generate and provide a QC report 'QC_CONFIG_RETRAIN_2025-06' as a pdf."
        ),
        actions=[
            Action(name="PatchProjectSettings", kwargs={"updates": {
                "retrain_window_start": "2025-06-01T00:00:00Z",
                "retrain_window_end": "2025-06-30T23:59:59Z"
            }}),
            Action(name="ReadProjectSettings", kwargs={"key": "retrain_window_start"}),
            Action(name="ReadProjectSettings", kwargs={"key": "retrain_window_end"}),

            Action(name="AppendAuditEvent", kwargs={
                "event_type": "MODEL_RETRAIN_WINDOW_SET",
                "message": "June retrain window applied."
            }),
            Action(name="ReadAuditEvents", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-06"}),
            Action(name="RecordQcReport", kwargs={
                "figure_label": "QC_CONFIG_RETRAIN_2025-06",
                "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-06.pdf",
                "artifact_type": "pdf"
            }),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-06"}),
            Action(name="ReadAuditEvents", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_088",
        instruction=(
            "Coordinate the creation of a heatwave risk dataset 'heatwave_risk_v1' for the period 2025-08. End state: the dataset 'heatwave_risk_v1' (version '1.0') with columns ['temperature','humidity','heat_risk'] must be stored and accessible; ensure the feature file '/features/heatwave_risk_v1.parquet' is present and can be read; a QC PDF for the label 'QC_HEATWAVE_RISK_2025-08' with artifact_type 'pdf' should be available; the stakeholder output 'Heatwave Risk Aug 2025' (audience 'internal') needs to reference 'https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf' and be accessible."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "heatwave_risk_v1", "version": "1.0",
                                                           "columns": ["temperature", "humidity", "heat_risk"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "heatwave_risk_v1"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/heatwave_risk_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/heatwave_risk_v1.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_HEATWAVE_RISK_2025-08"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_HEATWAVE_RISK_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_HEATWAVE_RISK_2025-08"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Heatwave Risk Aug 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_HEATWAVE_RISK_2025-08.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Heatwave Risk Aug 2025"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_089",
        instruction=(
            "Handle the establishment of a December-2025 backfill cutoff and confirm readiness. End state: project config includes backfill_cutoff '2025-12-22T20:00:00Z' and is obtainable; audit log event 'BACKFILL_CUTOFF_APPLIED' with message 'Backfill cutoff applied for end-of-year runs.' is present and viewable; a QC PDF for label 'QC_CONFIG_BACKFILL_2025-12' with artifact_type 'pdf' is available."
        ),
        actions=[
            Action(name="PatchProjectSettings", kwargs={"updates": {"backfill_cutoff": "2025-12-22T20:00:00Z"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "backfill_cutoff"}),

            Action(name="AppendAuditEvent", kwargs={"event_type": "BACKFILL_CUTOFF_APPLIED",
                                                      "message": "Backfill cutoff applied for end-of-year runs."}),
            Action(name="ReadAuditEvents", kwargs={"event_type": "BACKFILL_CUTOFF_APPLIED"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-12"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-12",
                                                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-12.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-12"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v5",
        user_id="ds_ops_090",
        instruction=(
            "Coordinate the definition of a September-2025 backfill cutoff and verify readiness. End state: project config includes backfill_cutoff '2025-09-15T16:00:00Z' and can be read; audit log event 'BACKFILL_CUTOFF_CONFIRMED' with message 'September backfill cutoff completed successfully.' is present and recoverable; a QC PDF for label 'QC_CONFIG_BACKFILL_2025-09' with artifact_type 'pdf' is available."
        ),
        actions=[
            Action(name="PatchProjectSettings", kwargs={"updates": {"backfill_cutoff": "2025-09-15T16:00:00Z"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "backfill_cutoff"}),

            Action(name="AppendAuditEvent", kwargs={"event_type": "BACKFILL_CUTOFF_CONFIRMED",
                                                      "message": "September backfill cutoff completed successfully."}),
            Action(name="ReadAuditEvents", kwargs={"event_type": "BACKFILL_CUTOFF_CONFIRMED"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-09"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-09",
                                                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-09.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-09"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_091",
        instruction=(
            "Handle the publication of feature set 'cargo_throughput_summary_v3' version 3.0 and designate it as active. End state: feature_set 'cargo_throughput_summary_v3' with columns ['total_cargo','avg_loading_time','avg_unloading_time'] is recorded; feature file '/features/cargo_throughput_summary_v3.parquet' exists and is readable; project config 'active_feature_set' equals 'cargo_throughput_summary_v3'; a QC PDF exists for label 'QC_CARGO_THROUGHPUT_2025-03' and is readable."
        ),
        actions=[
            Action(name="RegisterFeatureBundle",
                   kwargs={"feature_set_name": "cargo_throughput_summary_v3", "version": "3.0",
                           "columns": ["total_cargo", "avg_loading_time", "avg_unloading_time"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "cargo_throughput_summary_v3"}),

            Action(name="RegisterFileEntry", kwargs={"path": "/features/cargo_throughput_summary_v3.parquet",
                                                       "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/cargo_throughput_summary_v3.parquet"}),

            Action(name="PatchProjectSettings",
                   kwargs={"updates": {"active_feature_set": "cargo_throughput_summary_v3"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "active_feature_set"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CARGO_THROUGHPUT_2025-03"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_CARGO_THROUGHPUT_2025-03",
                                                    "figure_path": "https://storage.example.com/reports/QC_CARGO_THROUGHPUT_2025-03.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CARGO_THROUGHPUT_2025-03"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_092",
        instruction=(
            "Coordinate the curation of feature set 'port_utilization_stats_v4' version 4.2 and set it to active. End state: feature_set 'port_utilization_stats_v4' with columns ['berth_occupancy','avg_turnaround_time','peak_traffic_hour'] is recorded; feature file '/features/port_utilization_stats_v4.parquet' exists and is readable; project config 'active_feature_set' equals 'port_utilization_stats_v4'; a QC PDF exists for label 'QC_PORT_UTILIZATION_2025-03' and is readable."
        ),
        actions=[
            Action(name="RegisterFeatureBundle",
                   kwargs={"feature_set_name": "port_utilization_stats_v4", "version": "4.2",
                           "columns": ["berth_occupancy", "avg_turnaround_time", "peak_traffic_hour"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "port_utilization_stats_v4"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/port_utilization_stats_v4.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/port_utilization_stats_v4.parquet"}),

            Action(name="PatchProjectSettings",
                   kwargs={"updates": {"active_feature_set": "port_utilization_stats_v4"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "active_feature_set"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_PORT_UTILIZATION_2025-03"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_PORT_UTILIZATION_2025-03",
                                                    "figure_path": "https://storage.example.com/reports/QC_PORT_UTILIZATION_2025-03.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_PORT_UTILIZATION_2025-03"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_093",
        instruction=(
            "Establish a July-2025 ingestion deadline and check system readiness. End state: ensure project settings include ingestion_deadline='2025-07-15T12:00:00Z' and can be retrieved; verify existence of audit log event 'INGESTION_DEADLINE_SET' with message 'Deadline established for mid-July ingestion.'; ensure a QC report labeled 'QC_CONFIG_INGESTION_2025-07' (pdf) is registered and accessible."
        ),
        actions=[
            Action(name="PatchProjectSettings", kwargs={"updates": {"ingestion_deadline": "2025-07-15T12:00:00Z"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "ingestion_deadline"}),

            Action(name="AppendAuditEvent", kwargs={"event_type": "INGESTION_DEADLINE_SET",
                                                      "message": "Deadline established for mid-July ingestion."}),
            Action(name="ReadAuditEvents", kwargs={"event_type": "INGESTION_DEADLINE_SET"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CONFIG_INGESTION_2025-07"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_CONFIG_INGESTION_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_INGESTION_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CONFIG_INGESTION_2025-07"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_094",
        instruction=(
            "Schedule a November-2025 backfill cutoff and ensure readiness. End state: confirm that project settings include backfill_cutoff='2025-11-20T18:00:00Z' and can be retrieved; ensure audit log entry 'BACKFILL_CUTOFF_SET' with message 'Backfill cutoff applied for late November runs.' is present; confirm that a QC report labeled 'QC_CONFIG_BACKFILL_2025-11' (pdf) is stored and accessible."
        ),
        actions=[
            Action(name="PatchProjectSettings", kwargs={"updates": {"backfill_cutoff": "2025-11-20T18:00:00Z"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "backfill_cutoff"}),

            Action(name="AppendAuditEvent", kwargs={"event_type": "BACKFILL_CUTOFF_SET",
                                                      "message": "Backfill cutoff applied for late November runs."}),
            Action(name="ReadAuditEvents", kwargs={"event_type": "BACKFILL_CUTOFF_SET"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-11"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-11",
                                                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-11.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-11"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_095",
        instruction=(
            "Establish a July-2025 model retrain window and verify readiness. Final condition: project settings display retrain_window_start='2025-07-01T00:00:00Z' and retrain_window_end='2025-07-31T23:59:59Z'; audit log contains 'MODEL_RETRAIN_WINDOW_SET' with the note 'July retrain window applied.'; a QC report titled 'QC_CONFIG_RETRAIN_2025-07' (pdf) is logged and can be retrieved."
        ),
        actions=[
            Action(name="PatchProjectSettings", kwargs={"updates": {"retrain_window_start": "2025-07-01T00:00:00Z",
                                                                      "retrain_window_end": "2025-07-31T23:59:59Z"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "retrain_window_start"}),
            Action(name="ReadProjectSettings", kwargs={"key": "retrain_window_end"}),

            Action(name="AppendAuditEvent",
                   kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET", "message": "July retrain window applied."}),
            Action(name="ReadAuditEvents", kwargs={"event_type": "MODEL_RETRAIN_WINDOW_SET"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-07"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_RETRAIN_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CONFIG_RETRAIN_2025-07"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_096",
        instruction=(
            "Organize an urban flood dataset 'urban_flood_v1' for July-2025. Final condition: feature bundle 'urban_flood_v1' (version '1.0') with columns ['rainfall','drainage_capacity','flood_risk'] is registered; file '/features/urban_flood_v1.parquet' is present and accessible; QC report titled 'QC_URBAN_FLOOD_2025-07' (pdf) is provided; stakeholder output 'Urban Flood Jul 2025' (audience 'internal') includes a link to 'https://storage.example.com/reports/QC_URBAN_FLOOD_2025-07.pdf'."
        ),
        actions=[
            Action(name="RegisterFeatureBundle", kwargs={"feature_set_name": "urban_flood_v1", "version": "1.0",
                                                           "columns": ["rainfall", "drainage_capacity", "flood_risk"]}),
            Action(name="ReadFeatureBundle", kwargs={"feature_set_name": "urban_flood_v1"}),

            Action(name="RegisterFileEntry",
                   kwargs={"path": "/features/urban_flood_v1.parquet", "mime_type": "application/parquet"}),
            Action(name="RetrieveFileEntry", kwargs={"path": "/features/urban_flood_v1.parquet"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_URBAN_FLOOD_2025-07"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_URBAN_FLOOD_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_URBAN_FLOOD_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_URBAN_FLOOD_2025-07"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "Urban Flood Jul 2025", "audience": "internal",
                           "artifact_path": "https://storage.example.com/reports/QC_URBAN_FLOOD_2025-07.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "Urban Flood Jul 2025"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_097",
        instruction=(
            "Establish an October-2025 backfill cutoff and confirm the system's status. Final condition: project configurations include backfill_cutoff='2025-10-18T17:00:00Z'; audit log entry 'BACKFILL_CUTOFF_CONFIRMED' with message 'October backfill cutoff finalized.' is present; QC report 'QC_CONFIG_BACKFILL_2025-10' (pdf) is stored and accessible."
        ),
        actions=[
            Action(name="PatchProjectSettings", kwargs={"updates": {"backfill_cutoff": "2025-10-18T17:00:00Z"}}),
            Action(name="ReadProjectSettings", kwargs={"key": "backfill_cutoff"}),

            Action(name="AppendAuditEvent",
                   kwargs={"event_type": "BACKFILL_CUTOFF_CONFIRMED", "message": "October backfill cutoff finalized."}),
            Action(name="ReadAuditEvents", kwargs={"event_type": "BACKFILL_CUTOFF_CONFIRMED"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-10"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-10",
                                                    "figure_path": "https://storage.example.com/reports/QC_CONFIG_BACKFILL_2025-10.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_CONFIG_BACKFILL_2025-10"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_098",
        instruction=(
            "Compile tidal range data for July-2025, ensure QC is validated, and distribute a note to the local authority. Final condition: processed series 'tide_range_2025-07' records three values [('2025-07-05T00:00:00Z', 2.67), ('2025-07-18T00:00:00Z', 3.02), ('2025-07-31T00:00:00Z', 2.88)] and can be retrieved; a QC document 'QC_TIDE_RANGE_2025-07' (pdf) is generated and accessible; a stakeholder deliverable 'July 2025 Tidal Range Brief' (audience 'municipal') references that QC file."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "tide_range_2025-07", "items": [
                {"timestamp": "2025-07-05T00:00:00Z", "value": 2.67},
                {"timestamp": "2025-07-18T00:00:00Z", "value": 3.02},
                {"timestamp": "2025-07-31T00:00:00Z", "value": 2.88}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "tide_range_2025-07"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_TIDE_RANGE_2025-07"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_TIDE_RANGE_2025-07",
                                                    "figure_path": "https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_TIDE_RANGE_2025-07"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "July 2025 Tidal Range Brief", "audience": "municipal",
                           "artifact_path": "https://storage.example.com/reports/QC_TIDE_RANGE_2025-07.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "July 2025 Tidal Range Brief"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_099",
        instruction=(
            "Handle the calculation of mean tidal levels for August-2025, perform a QC check, and deliver a summary for state agencies. End state: processed series 'tide_mean_2025-08' holds three records [('2025-08-04T00:00:00Z', 1.87), ('2025-08-17T00:00:00Z', 2.01), ('2025-08-30T00:00:00Z', 1.95)] and is available; QC output 'QC_TIDE_MEAN_2025-08' (pdf) is saved; a stakeholder note 'August 2025 Mean Tide Brief' (audience 'state') references the QC document."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "tide_mean_2025-08", "items": [
                {"timestamp": "2025-08-04T00:00:00Z", "value": 1.87},
                {"timestamp": "2025-08-17T00:00:00Z", "value": 2.01},
                {"timestamp": "2025-08-30T00:00:00Z", "value": 1.95}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "tide_mean_2025-08"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_TIDE_MEAN_2025-08"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_TIDE_MEAN_2025-08",
                                                    "figure_path": "https://storage.example.com/reports/QC_TIDE_MEAN_2025-08.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_TIDE_MEAN_2025-08"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "August 2025 Mean Tide Brief", "audience": "state",
                           "artifact_path": "https://storage.example.com/reports/QC_TIDE_MEAN_2025-08.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "August 2025 Mean Tide Brief"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v5",
        user_id="ds_ops_100",
        instruction=(
            "Initiate the preparation of tidal minimum readings for May-2025, ensure QC validation, and compose a report for coastal teams. End state: processed series 'tide_min_2025-05' contains three entries [('2025-05-03T00:00:00Z', 0.42), ('2025-05-16T00:00:00Z', 0.35), ('2025-05-29T00:00:00Z', 0.50)] retrievable from storage; QC record 'QC_TIDE_MIN_2025-05' (pdf) is archived; a stakeholder artifact 'May 2025 Tide Min Summary' (audience 'coastal') points to the QC file."
        ),
        actions=[
            Action(name="WriteProcessedSeries", kwargs={"series_name": "tide_min_2025-05", "items": [
                {"timestamp": "2025-05-03T00:00:00Z", "value": 0.42},
                {"timestamp": "2025-05-16T00:00:00Z", "value": 0.35},
                {"timestamp": "2025-05-29T00:00:00Z", "value": 0.50}
            ]}),
            Action(name="ReadProcessedSeries", kwargs={"series_name": "tide_min_2025-05"}),

            Action(name="RenderQcReport", kwargs={"figure_label": "QC_TIDE_MIN_2025-05"}),
            Action(name="RecordQcReport", kwargs={"figure_label": "QC_TIDE_MIN_2025-05",
                                                    "figure_path": "https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf",
                                                    "artifact_type": "pdf"}),
            Action(name="ReadQcReport", kwargs={"figure_label": "QC_TIDE_MIN_2025-05"}),

            Action(name="RecordStakeholderArtifact",
                   kwargs={"output_label": "May 2025 Tide Min Summary", "audience": "coastal",
                           "artifact_path": "https://storage.example.com/reports/QC_TIDE_MIN_2025-05.pdf"}),
            Action(name="ReadStakeholderArtifact", kwargs={"output_label": "May 2025 Tide Min Summary"}),
        ],
        outputs=[]
    )
]
