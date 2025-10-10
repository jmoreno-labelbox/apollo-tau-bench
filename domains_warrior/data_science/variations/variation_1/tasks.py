from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="ds_v1_001",
        instruction=(
            "You must record a Coos Bay intake baseline. End state: config 'Coos Bay' (UTC); geocoding 43.3670,-124.2170; proximity includes "
            "'9432780' set primary; observed water levels include '2025-05-03T02:00:00Z' = 1.02 (m); tide predictions include "
            "'2025-05-03T02:00:00Z' = 1.09 (m); merged artifact at 'processed_data/merged_timeseries_coosbay.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Coos Bay", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Coos Bay", "latitude": 43.3670, "longitude": -124.2170}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 43.3670, "query_longitude": -124.2170, "station_ids": ["9432780"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9432780"}),
            Action(name="store_water_levels", kwargs={"station_id": "9432780", "timestamps": ["2025-05-03T02:00:00Z"], "water_level_m": [1.02], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9432780", "timestamps": ["2025-05-03T02:00:00Z"], "tide_pred_m": [1.09], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_coosbay.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_002",
        instruction=(
            "You must create a Neah Bay intake baseline. End: config 'Neah Bay' (UTC); geocoding 48.3681,-124.6241; proximity includes '9443090' "
            "primary; observed '2025-05-05T00:00:00Z' = 0.97 (m); predictions '2025-05-05T00:00:00Z' = 1.04 (m); merged at "
            "'processed_data/merged_timeseries_neahbay.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Neah Bay", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Neah Bay", "latitude": 48.3681, "longitude": -124.6241}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 48.3681, "query_longitude": -124.6241, "station_ids": ["9443090"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9443090"}),
            Action(name="store_water_levels", kwargs={"station_id": "9443090", "timestamps": ["2025-05-05T00:00:00Z"], "water_level_m": [0.97], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9443090", "timestamps": ["2025-05-05T00:00:00Z"], "tide_pred_m": [1.04], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_neahbay.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_003",
        instruction=(
            "You must register a Tacoma intake baseline. End: config 'Tacoma' (UTC); geocoding 47.2529,-122.4443; proximity includes '9448000' primary; "
            "observed '2025-05-06T03:00:00Z' = 0.99 (m); predictions '2025-05-06T03:00:00Z' = 1.05 (m); merged at "
            "'processed_data/merged_timeseries_tacoma.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Tacoma", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Tacoma", "latitude": 47.2529, "longitude": -122.4443}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 47.2529, "query_longitude": -122.4443, "station_ids": ["9448000"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9448000"}),
            Action(name="store_water_levels", kwargs={"station_id": "9448000", "timestamps": ["2025-05-06T03:00:00Z"], "water_level_m": [0.99], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9448000", "timestamps": ["2025-05-06T03:00:00Z"], "tide_pred_m": [1.05], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_tacoma.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_004",
        instruction=(
            "You must create a Bellingham intake baseline. End: config 'Bellingham' (UTC); geocoding 48.7491,-122.4787; proximity includes '9449211' primary; "
            "observed '2025-05-07T00:00:00Z' = 1.02 (m); predictions '2025-05-07T00:00:00Z' = 1.09 (m); merged at "
            "'processed_data/merged_timeseries_bellingham.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Bellingham", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Bellingham", "latitude": 48.7491, "longitude": -122.4787}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 48.7491, "query_longitude": -122.4787, "station_ids": ["9449211"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9449211"}),
            Action(name="store_water_levels", kwargs={"station_id": "9449211", "timestamps": ["2025-05-07T00:00:00Z"], "water_level_m": [1.02], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9449211", "timestamps": ["2025-05-07T00:00:00Z"], "tide_pred_m": [1.09], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_bellingham.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_005",
        instruction=(
            "You must assemble an Astoria modeling bundle. End state: features at 'processed_data/features_astoria.csv' with "
            "['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-05-09T09:05:00Z'); "
            "config at 'processed_data/model_config_astoria.json' with classification_threshold_m 0.58 (created_ts '2025-05-09T09:06:00Z'); "
            "split at 'processed_data/split_astoria.json'; model 'astoria_lr_v1' at 'models/astoria_lr_v1.joblib'; predictions at "
            "'processed_data/preds_astoria_lr_v1.csv' (generated_ts '2025-05-09T10:30:00Z'); metrics at "
            "'processed_data/metrics_astoria_lr_v1.csv' (auc 0.70); and stakeholder references to those artifacts."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_astoria.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-05-09T09:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_astoria.json", "classification_threshold_m_nullable": 0.58, "created_ts": "2025-05-09T09:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_astoria.json"}),
            Action(name="register_model", kwargs={"model_name": "astoria_lr_v1", "model_path": "models/astoria_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "astoria_lr_v1", "predictions_csv_path": "processed_data/preds_astoria_lr_v1.csv", "generated_ts": "2025-05-09T10:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "astoria_lr_v1", "metrics_csv_path": "processed_data/metrics_astoria_lr_v1.csv", "auc_nullable": 0.70}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_astoria_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_astoria_lr_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_006",
        instruction=(
            "You must leave the database in a reproducible Pacifica baseline. By the end: a configuration row shows "
            "target_city 'Pacifica' with timezone 'UTC'; a geocoding record locates 'Pacifica' at 37.6138,-122.4869; "
            "a proximity result at those coordinates includes station '9414520', and you set it as the primary; observed "
            "water levels for '9414520' include the point '2025-02-01T00:00:00Z' = 1.05 (m); tide predictions for "
            "'9414520' include the point '2025-02-01T00:00:00Z' = 1.15 (m); and a processed artifact exists at "
            "'processed_data/merged_timeseries_pacifica.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Pacifica", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Pacifica", "latitude": 37.6138, "longitude": -122.4869
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 37.6138, "query_longitude": -122.4869, "station_ids": ["9414520"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9414520"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9414520",
                "timestamps": ["2025-02-01T00:00:00Z"],
                "water_level_m": [1.05],
                "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9414520",
                "timestamps": ["2025-02-01T00:00:00Z"],
                "tide_pred_m": [1.15],
                "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={
                "csv_path": "processed_data/merged_timeseries_pacifica.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_007",
        instruction=(
            "You must capture a Moss Landing intake baseline. By the end: configuration shows target_city 'Moss Landing' "
            "with timezone 'UTC'; geocoding pins 'Moss Landing' at 36.8067,-121.7896; a proximity record at those "
            "coordinates includes '9413450' which you set primary; observed water levels for '9413450' include "
            "'2025-02-03T03:00:00Z' = 0.92 (m); tide predictions for '9413450' include "
            "'2025-02-03T03:00:00Z' = 1.00 (m); and a processed artifact is present at "
            "'processed_data/merged_timeseries_moss.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Moss Landing", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Moss Landing", "latitude": 36.8067, "longitude": -121.7896
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 36.8067, "query_longitude": -121.7896, "station_ids": ["9413450"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9413450"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9413450",
                "timestamps": ["2025-02-03T03:00:00Z"],
                "water_level_m": [0.92],
                "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9413450",
                "timestamps": ["2025-02-03T03:00:00Z"],
                "tide_pred_m": [1.00],
                "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={
                "csv_path": "processed_data/merged_timeseries_moss.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_008",
        instruction=(
            "You must prepare a Capitola baseline. Final state: a config row has target_city 'Capitola' and timezone "
            "'UTC'; a geocoding record places 'Capitola' at 36.9750,-121.9540; a proximity result at those coordinates "
            "includes '9413830' and that station is primary; observed water levels for '9413830' include "
            "'2025-02-04T12:00:00Z' = 1.18 (m); tide predictions for '9413830' include "
            "'2025-02-04T12:00:00Z' = 1.22 (m); and a processed artifact is registered at "
            "'processed_data/merged_timeseries_capitola.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Capitola", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Capitola", "latitude": 36.9750, "longitude": -121.9540
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 36.9750, "query_longitude": -121.9540, "station_ids": ["9413830"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9413830"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9413830",
                "timestamps": ["2025-02-04T12:00:00Z"],
                "water_level_m": [1.18],
                "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9413830",
                "timestamps": ["2025-02-04T12:00:00Z"],
                "tide_pred_m": [1.22],
                "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={
                "csv_path": "processed_data/merged_timeseries_capitola.csv"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_009",
        instruction=(
            "You must register a Pescadero intake. Final state: configuration shows target_city 'Pescadero' with "
            "timezone 'UTC'; geocoding places 'Pescadero' at 37.2550,-122.3833; a proximity record at these "
            "coordinates includes '9415025' which is set primary; observed water levels for '9415025' include "
            "'2025-02-06T02:00:00Z' = 0.85 (m); tide predictions for '9415025' include "
            "'2025-02-06T02:00:00Z' = 0.90 (m); and a processed artifact is present at "
            "'processed_data/merged_timeseries_pescadero.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Pescadero", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Pescadero", "latitude": 37.2550, "longitude": -122.3833
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 37.2550, "query_longitude": -122.3833, "station_ids": ["9415025"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9415025"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9415025",
                "timestamps": ["2025-02-06T02:00:00Z"],
                "water_level_m": [0.85],
                "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9415025",
                "timestamps": ["2025-02-06T02:00:00Z"],
                "tide_pred_m": [0.90],
                "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={
                "csv_path": "processed_data/merged_timeseries_pescadero.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_010",
        instruction=(
            "You must capture an Aptos intake. The completed state shows: config with target_city 'Aptos' and timezone "
            "'UTC'; geocoding for 'Aptos' at 36.9772,-121.9009; a proximity record at those coordinates includes "
            "'9413748' which is set primary; observed water levels for '9413748' include "
            "'2025-02-08T01:00:00Z' = 1.05 (m); tide predictions for '9413748' include "
            "'2025-02-08T01:00:00Z' = 1.12 (m); and a processed artifact at "
            "'processed_data/merged_timeseries_aptos.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Aptos", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Aptos", "latitude": 36.9772, "longitude": -121.9009
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 36.9772, "query_longitude": -121.9009, "station_ids": ["9413748"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9413748"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9413748",
                "timestamps": ["2025-02-08T01:00:00Z"],
                "water_level_m": [1.05],
                "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9413748",
                "timestamps": ["2025-02-08T01:00:00Z"],
                "tide_pred_m": [1.12],
                "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={
                "csv_path": "processed_data/merged_timeseries_aptos.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_011",
        instruction=(
            "You must register a Santa Barbara baseline. End state: configuration shows target_city 'Santa Barbara' and "
            "timezone 'UTC'; geocoding locates 'Santa Barbara' at 34.4208,-119.6982; a proximity record at those "
            "coordinates includes '9411340' which is set primary; observed water levels for '9411340' include "
            "'2025-02-09T00:00:00Z' = 0.88 (m); tide predictions for '9411340' include "
            "'2025-02-09T00:00:00Z' = 0.95 (m); and a processed artifact exists at "
            "'processed_data/merged_timeseries_sb.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Santa Barbara", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Santa Barbara", "latitude": 34.4208, "longitude": -119.6982
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 34.4208, "query_longitude": -119.6982, "station_ids": ["9411340"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9411340"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9411340",
                "timestamps": ["2025-02-09T00:00:00Z"],
                "water_level_m": [0.88],
                "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9411340",
                "timestamps": ["2025-02-09T00:00:00Z"],
                "tide_pred_m": [0.95],
                "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={
                "csv_path": "processed_data/merged_timeseries_sb.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_012",
        instruction=(
            "You must complete a Ventura baseline. Finalized state: configuration lists target_city 'Ventura' with "
            "timezone 'UTC'; geocoding places 'Ventura' at 34.2746,-119.2290; a proximity entry at those coordinates "
            "includes '9411188' which becomes primary; observed water levels for '9411188' include "
            "'2025-02-10T04:00:00Z' = 0.91 (m); tide predictions for '9411188' include "
            "'2025-02-10T04:00:00Z' = 0.98 (m); and a processed artifact resides at "
            "'processed_data/merged_timeseries_ventura.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Ventura", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Ventura", "latitude": 34.2746, "longitude": -119.2290
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 34.2746, "query_longitude": -119.2290, "station_ids": ["9411188"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9411188"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9411188",
                "timestamps": ["2025-02-10T04:00:00Z"],
                "water_level_m": [0.91],
                "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9411188",
                "timestamps": ["2025-02-10T04:00:00Z"],
                "tide_pred_m": [0.98],
                "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={
                "csv_path": "processed_data/merged_timeseries_ventura.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_013",
        instruction=(
            "You must record a Monterey modeling bundle. The final state shows: features at "
            "'processed_data/features_mry.csv' with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] "
            "and generated_ts '2025-02-13T09:05:00Z'; a configuration at 'processed_data/model_config_mry.json' with "
            "classification_threshold_m 0.55 and created_ts '2025-02-13T09:06:00Z'; a split summary at "
            "'processed_data/split_mry.json'; a registered model named 'mry_lr_v1' stored at 'models/mry_lr_v1.joblib'; "
            "predictions at 'processed_data/preds_mry_lr_v1.csv' with generated_ts '2025-02-13T10:30:00Z'; metrics at "
            "'processed_data/metrics_mry_lr_v1.csv' (auc 0.73); and stakeholder references to those predictions/metrics."
        ),
        actions=[
            Action(name="store_features", kwargs={
                "csv_path": "processed_data/features_mry.csv",
                "feature_names": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "generated_ts": "2025-02-13T09:05:00Z"
            }),
            Action(name="write_model_config", kwargs={
                "saved_json_path": "processed_data/model_config_mry.json",
                "classification_threshold_m_nullable": 0.55,
                "created_ts": "2025-02-13T09:06:00Z"
            }),
            Action(name="create_time_based_split", kwargs={
                "split_summary_json_path": "processed_data/split_mry.json"
            }),
            Action(name="register_model", kwargs={
                "model_name": "mry_lr_v1",
                "model_path": "models/mry_lr_v1.joblib"
            }),
            Action(name="store_predictions", kwargs={
                "model_name": "mry_lr_v1",
                "predictions_csv_path": "processed_data/preds_mry_lr_v1.csv",
                "generated_ts": "2025-02-13T10:30:00Z"
            }),
            Action(name="store_metrics", kwargs={
                "model_name": "mry_lr_v1",
                "metrics_csv_path": "processed_data/metrics_mry_lr_v1.csv",
                "auc_nullable": 0.73
            }),
            Action(name="record_stakeholder_outputs", kwargs={
                "predictions_final_csv_path": "processed_data/preds_mry_lr_v1.csv",
                "metrics_summary_csv_path": "processed_data/metrics_mry_lr_v1.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_014",
        instruction=(
            "You must archive a Santa Cruz modeling bundle. End state: features at "
            "'processed_data/features_sc.csv' with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] and "
            "generated_ts '2025-02-14T09:05:00Z'; configuration at 'processed_data/model_config_sc.json' with "
            "classification_threshold_m 0.60 and created_ts '2025-02-14T09:06:00Z'; split summary at "
            "'processed_data/split_sc.json'; model 'sc_lr_v2' at 'models/sc_lr_v2.joblib'; predictions at "
            "'processed_data/preds_sc_lr_v2.csv' (generated_ts '2025-02-14T10:30:00Z'); metrics at "
            "'processed_data/metrics_sc_lr_v2.csv' (accuracy 0.69); and stakeholder references to those same artifacts."
        ),
        actions=[
            Action(name="store_features", kwargs={
                "csv_path": "processed_data/features_sc.csv",
                "feature_names": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "generated_ts": "2025-02-14T09:05:00Z"
            }),
            Action(name="write_model_config", kwargs={
                "saved_json_path": "processed_data/model_config_sc.json",
                "classification_threshold_m_nullable": 0.60,
                "created_ts": "2025-02-14T09:06:00Z"
            }),
            Action(name="create_time_based_split", kwargs={
                "split_summary_json_path": "processed_data/split_sc.json"
            }),
            Action(name="register_model", kwargs={
                "model_name": "sc_lr_v2",
                "model_path": "models/sc_lr_v2.joblib"
            }),
            Action(name="store_predictions", kwargs={
                "model_name": "sc_lr_v2",
                "predictions_csv_path": "processed_data/preds_sc_lr_v2.csv",
                "generated_ts": "2025-02-14T10:30:00Z"
            }),
            Action(name="store_metrics", kwargs={
                "model_name": "sc_lr_v2",
                "metrics_csv_path": "processed_data/metrics_sc_lr_v2.csv",
                "accuracy_nullable": 0.69
            }),
            Action(name="record_stakeholder_outputs", kwargs={
                "predictions_final_csv_path": "processed_data/preds_sc_lr_v2.csv",
                "metrics_summary_csv_path": "processed_data/metrics_sc_lr_v2.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_015",
        instruction=(
            "You must store a Pacifica modeling bundle. Final state: features at 'processed_data/features_pac.csv' "
            "with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] and generated_ts "
            "'2025-02-15T09:05:00Z'; configuration at 'processed_data/model_config_pac.json' with "
            "classification_threshold_m 0.58 and created_ts '2025-02-15T09:06:00Z'; split summary at "
            "'processed_data/split_pac.json'; model 'pac_rf_v1' at 'models/pac_rf_v1.joblib'; predictions at "
            "'processed_data/preds_pac_rf_v1.csv' (generated_ts '2025-02-15T10:30:00Z'); metrics at "
            "'processed_data/metrics_pac_rf_v1.csv' (auc 0.71); stakeholder references point to those paths."
        ),
        actions=[
            Action(name="store_features", kwargs={
                "csv_path": "processed_data/features_pac.csv",
                "feature_names": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "generated_ts": "2025-02-15T09:05:00Z"
            }),
            Action(name="write_model_config", kwargs={
                "saved_json_path": "processed_data/model_config_pac.json",
                "classification_threshold_m_nullable": 0.58,
                "created_ts": "2025-02-15T09:06:00Z"
            }),
            Action(name="create_time_based_split", kwargs={
                "split_summary_json_path": "processed_data/split_pac.json"
            }),
            Action(name="register_model", kwargs={
                "model_name": "pac_rf_v1",
                "model_path": "models/pac_rf_v1.joblib",
                "model_type": "random_forest"
            }),
            Action(name="store_predictions", kwargs={
                "model_name": "pac_rf_v1",
                "predictions_csv_path": "processed_data/preds_pac_rf_v1.csv",
                "generated_ts": "2025-02-15T10:30:00Z"
            }),
            Action(name="store_metrics", kwargs={
                "model_name": "pac_rf_v1",
                "metrics_csv_path": "processed_data/metrics_pac_rf_v1.csv",
                "auc_nullable": 0.71
            }),
            Action(name="record_stakeholder_outputs", kwargs={
                "predictions_final_csv_path": "processed_data/preds_pac_rf_v1.csv",
                "metrics_summary_csv_path": "processed_data/metrics_pac_rf_v1.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_016",
        instruction=(
            "You must register a Half Moon Bay modeling bundle. Finalized state: features at "
            "'processed_data/features_hmb.csv' with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] "
            "and generated_ts '2025-02-16T09:05:00Z'; configuration at 'processed_data/model_config_hmb.json' with "
            "classification_threshold_m 0.57 and created_ts '2025-02-16T09:06:00Z'; split summary at "
            "'processed_data/split_hmb.json'; model 'hmb_lr_v1' at 'models/hmb_lr_v1.joblib'; predictions at "
            "'processed_data/preds_hmb_lr_v1.csv' (generated_ts '2025-02-16T10:30:00Z'); metrics at "
            "'processed_data/metrics_hmb_lr_v1.csv' (accuracy 0.68); and stakeholder references to those artifacts."
        ),
        actions=[
            Action(name="store_features", kwargs={
                "csv_path": "processed_data/features_hmb.csv",
                "feature_names": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "generated_ts": "2025-02-16T09:05:00Z"
            }),
            Action(name="write_model_config", kwargs={
                "saved_json_path": "processed_data/model_config_hmb.json",
                "classification_threshold_m_nullable": 0.57,
                "created_ts": "2025-02-16T09:06:00Z"
            }),
            Action(name="create_time_based_split", kwargs={
                "split_summary_json_path": "processed_data/split_hmb.json"
            }),
            Action(name="register_model", kwargs={
                "model_name": "hmb_lr_v1",
                "model_path": "models/hmb_lr_v1.joblib"
            }),
            Action(name="store_predictions", kwargs={
                "model_name": "hmb_lr_v1",
                "predictions_csv_path": "processed_data/preds_hmb_lr_v1.csv",
                "generated_ts": "2025-02-16T10:30:00Z"
            }),
            Action(name="store_metrics", kwargs={
                "model_name": "hmb_lr_v1",
                "metrics_csv_path": "processed_data/metrics_hmb_lr_v1.csv",
                "accuracy_nullable": 0.68
            }),
            Action(name="record_stakeholder_outputs", kwargs={
                "predictions_final_csv_path": "processed_data/preds_hmb_lr_v1.csv",
                "metrics_summary_csv_path": "processed_data/metrics_hmb_lr_v1.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_017",
        instruction=(
            "You must store a Davenport modeling bundle. Final state: features at 'processed_data/features_dvp.csv' "
            "with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] and generated_ts "
            "'2025-02-17T09:05:00Z'; configuration at 'processed_data/model_config_dvp.json' with "
            "classification_threshold_m 0.59 and created_ts '2025-02-17T09:06:00Z'; split summary at "
            "'processed_data/split_dvp.json'; model 'dvp_lr_v1' at 'models/dvp_lr_v1.joblib'; predictions at "
            "'processed_data/preds_dvp_lr_v1.csv' (generated_ts '2025-02-17T10:30:00Z'); metrics at "
            "'processed_data/metrics_dvp_lr_v1.csv' (auc 0.72); and stakeholder references pointing to those paths."
        ),
        actions=[
            Action(name="store_features", kwargs={
                "csv_path": "processed_data/features_dvp.csv",
                "feature_names": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "generated_ts": "2025-02-17T09:05:00Z"
            }),
            Action(name="write_model_config", kwargs={
                "saved_json_path": "processed_data/model_config_dvp.json",
                "classification_threshold_m_nullable": 0.59,
                "created_ts": "2025-02-17T09:06:00Z"
            }),
            Action(name="create_time_based_split", kwargs={
                "split_summary_json_path": "processed_data/split_dvp.json"
            }),
            Action(name="register_model", kwargs={
                "model_name": "dvp_lr_v1",
                "model_path": "models/dvp_lr_v1.joblib"
            }),
            Action(name="store_predictions", kwargs={
                "model_name": "dvp_lr_v1",
                "predictions_csv_path": "processed_data/preds_dvp_lr_v1.csv",
                "generated_ts": "2025-02-17T10:30:00Z"
            }),
            Action(name="store_metrics", kwargs={
                "model_name": "dvp_lr_v1",
                "metrics_csv_path": "processed_data/metrics_dvp_lr_v1.csv",
                "auc_nullable": 0.72
            }),
            Action(name="record_stakeholder_outputs", kwargs={
                "predictions_final_csv_path": "processed_data/preds_dvp_lr_v1.csv",
                "metrics_summary_csv_path": "processed_data/metrics_dvp_lr_v1.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_018",
        instruction=(
            "You must assemble a Santa Barbara modeling bundle. Finalized state: features at "
            "'processed_data/features_sb.csv' with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] "
            "and generated_ts '2025-02-18T09:05:00Z'; configuration at 'processed_data/model_config_sb.json' with "
            "classification_threshold_m 0.61 and created_ts '2025-02-18T09:06:00Z'; split summary at "
            "'processed_data/split_sb.json'; model 'sb_lr_v1' at 'models/sb_lr_v1.joblib'; predictions at "
            "'processed_data/preds_sb_lr_v1.csv' (generated_ts '2025-02-18T10:30:00Z'); metrics at "
            "'processed_data/metrics_sb_lr_v1.csv' (accuracy 0.70); and stakeholder references to those paths."
        ),
        actions=[
            Action(name="store_features", kwargs={
                "csv_path": "processed_data/features_sb.csv",
                "feature_names": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "generated_ts": "2025-02-18T09:05:00Z"
            }),
            Action(name="write_model_config", kwargs={
                "saved_json_path": "processed_data/model_config_sb.json",
                "classification_threshold_m_nullable": 0.61,
                "created_ts": "2025-02-18T09:06:00Z"
            }),
            Action(name="create_time_based_split", kwargs={
                "split_summary_json_path": "processed_data/split_sb.json"
            }),
            Action(name="register_model", kwargs={
                "model_name": "sb_lr_v1",
                "model_path": "models/sb_lr_v1.joblib"
            }),
            Action(name="store_predictions", kwargs={
                "model_name": "sb_lr_v1",
                "predictions_csv_path": "processed_data/preds_sb_lr_v1.csv",
                "generated_ts": "2025-02-18T10:30:00Z"
            }),
            Action(name="store_metrics", kwargs={
                "model_name": "sb_lr_v1",
                "metrics_csv_path": "processed_data/metrics_sb_lr_v1.csv",
                "accuracy_nullable": 0.70
            }),
            Action(name="record_stakeholder_outputs", kwargs={
                "predictions_final_csv_path": "processed_data/preds_sb_lr_v1.csv",
                "metrics_summary_csv_path": "processed_data/metrics_sb_lr_v1.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_019",
        instruction=(
            "You must register a Ventura modeling bundle. Final state: features at 'processed_data/features_ven.csv' "
            "with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] and generated_ts "
            "'2025-02-19T09:05:00Z'; configuration at 'processed_data/model_config_ven.json' with "
            "classification_threshold_m 0.62 and created_ts '2025-02-19T09:06:00Z'; split summary at "
            "'processed_data/split_ven.json'; model 'ven_lr_v1' at 'models/ven_lr_v1.joblib'; predictions at "
            "'processed_data/preds_ven_lr_v1.csv' (generated_ts '2025-02-19T10:30:00Z'); metrics at "
            "'processed_data/metrics_ven_lr_v1.csv' (auc 0.70); and stakeholder references to those artifacts."
        ),
        actions=[
            Action(name="store_features", kwargs={
                "csv_path": "processed_data/features_ven.csv",
                "feature_names": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "generated_ts": "2025-02-19T09:05:00Z"
            }),
            Action(name="write_model_config", kwargs={
                "saved_json_path": "processed_data/model_config_ven.json",
                "classification_threshold_m_nullable": 0.62,
                "created_ts": "2025-02-19T09:06:00Z"
            }),
            Action(name="create_time_based_split", kwargs={
                "split_summary_json_path": "processed_data/split_ven.json"
            }),
            Action(name="register_model", kwargs={
                "model_name": "ven_lr_v1",
                "model_path": "models/ven_lr_v1.joblib"
            }),
            Action(name="store_predictions", kwargs={
                "model_name": "ven_lr_v1",
                "predictions_csv_path": "processed_data/preds_ven_lr_v1.csv",
                "generated_ts": "2025-02-19T10:30:00Z"
            }),
            Action(name="store_metrics", kwargs={
                "model_name": "ven_lr_v1",
                "metrics_csv_path": "processed_data/metrics_ven_lr_v1.csv",
                "auc_nullable": 0.70
            }),
            Action(name="record_stakeholder_outputs", kwargs={
                "predictions_final_csv_path": "processed_data/preds_ven_lr_v1.csv",
                "metrics_summary_csv_path": "processed_data/metrics_ven_lr_v1.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_020",
        instruction=(
            "You must finalize a Morro Bay modeling bundle. Final state: features at 'processed_data/features_morro.csv' "
            "with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] and generated_ts "
            "'2025-02-20T09:05:00Z'; configuration at 'processed_data/model_config_morro.json' with "
            "classification_threshold_m 0.63 and created_ts '2025-02-20T09:06:00Z'; split summary at "
            "'processed_data/split_morro.json'; model 'morro_lr_v1' at 'models/morro_lr_v1.joblib'; predictions at "
            "'processed_data/preds_morro_lr_v1.csv' (generated_ts '2025-02-20T10:30:00Z'); metrics at "
            "'processed_data/metrics_morro_lr_v1.csv' (accuracy 0.67); and stakeholder references to those paths."
        ),
        actions=[
            Action(name="store_features", kwargs={
                "csv_path": "processed_data/features_morro.csv",
                "feature_names": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "generated_ts": "2025-02-20T09:05:00Z"
            }),
            Action(name="write_model_config", kwargs={
                "saved_json_path": "processed_data/model_config_morro.json",
                "classification_threshold_m_nullable": 0.63,
                "created_ts": "2025-02-20T09:06:00Z"
            }),
            Action(name="create_time_based_split", kwargs={
                "split_summary_json_path": "processed_data/split_morro.json"
            }),
            Action(name="register_model", kwargs={
                "model_name": "morro_lr_v1",
                "model_path": "models/morro_lr_v1.joblib"
            }),
            Action(name="store_predictions", kwargs={
                "model_name": "morro_lr_v1",
                "predictions_csv_path": "processed_data/preds_morro_lr_v1.csv",
                "generated_ts": "2025-02-20T10:30:00Z"
            }),
            Action(name="store_metrics", kwargs={
                "model_name": "morro_lr_v1",
                "metrics_csv_path": "processed_data/metrics_morro_lr_v1.csv",
                "accuracy_nullable": 0.67
            }),
            Action(name="record_stakeholder_outputs", kwargs={
                "predictions_final_csv_path": "processed_data/preds_morro_lr_v1.csv",
                "metrics_summary_csv_path": "processed_data/metrics_morro_lr_v1.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_021",
        instruction=(
            "You must compile an Avila Beach modeling bundle. End state: features at "
            "'processed_data/features_avila.csv' with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] "
            "and generated_ts '2025-02-21T09:05:00Z'; configuration at 'processed_data/model_config_avila.json' with "
            "classification_threshold_m 0.56 and created_ts '2025-02-21T09:06:00Z'; split summary at "
            "'processed_data/split_avila.json'; model 'avila_lr_v1' at 'models/avila_lr_v1.joblib'; predictions at "
            "'processed_data/preds_avila_lr_v1.csv' (generated_ts '2025-02-21T10:30:00Z'); metrics at "
            "'processed_data/metrics_avila_lr_v1.csv' (auc 0.74); stakeholder references to those paths."
        ),
        actions=[
            Action(name="store_features", kwargs={
                "csv_path": "processed_data/features_avila.csv",
                "feature_names": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "generated_ts": "2025-02-21T09:05:00Z"
            }),
            Action(name="write_model_config", kwargs={
                "saved_json_path": "processed_data/model_config_avila.json",
                "classification_threshold_m_nullable": 0.56,
                "created_ts": "2025-02-21T09:06:00Z"
            }),
            Action(name="create_time_based_split", kwargs={
                "split_summary_json_path": "processed_data/split_avila.json"
            }),
            Action(name="register_model", kwargs={
                "model_name": "avila_lr_v1",
                "model_path": "models/avila_lr_v1.joblib"
            }),
            Action(name="store_predictions", kwargs={
                "model_name": "avila_lr_v1",
                "predictions_csv_path": "processed_data/preds_avila_lr_v1.csv",
                "generated_ts": "2025-02-21T10:30:00Z"
            }),
            Action(name="store_metrics", kwargs={
                "model_name": "avila_lr_v1",
                "metrics_csv_path": "processed_data/metrics_avila_lr_v1.csv",
                "auc_nullable": 0.74
            }),
            Action(name="record_stakeholder_outputs", kwargs={
                "predictions_final_csv_path": "processed_data/preds_avila_lr_v1.csv",
                "metrics_summary_csv_path": "processed_data/metrics_avila_lr_v1.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_022",
        instruction=(
            "You must register a coastal meta‑modeling bundle. End state: features at "
            "'processed_data/features_meta.csv' with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] "
            "and generated_ts '2025-02-22T09:05:00Z'; configuration at 'processed_data/model_config_meta.json' with "
            "classification_threshold_m 0.60 and created_ts '2025-02-22T09:06:00Z'; split summary at "
            "'processed_data/split_meta.json'; model 'coast_meta_v1' at 'models/coast_meta_v1.joblib'; predictions at "
            "'processed_data/preds_coast_meta_v1.csv' (generated_ts '2025-02-22T10:30:00Z'); metrics at "
            "'processed_data/metrics_coast_meta_v1.csv' (accuracy 0.71); and references to those predictions/metrics."
        ),
        actions=[
            Action(name="store_features", kwargs={
                "csv_path": "processed_data/features_meta.csv",
                "feature_names": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "generated_ts": "2025-02-22T09:05:00Z"
            }),
            Action(name="write_model_config", kwargs={
                "saved_json_path": "processed_data/model_config_meta.json",
                "classification_threshold_m_nullable": 0.60,
                "created_ts": "2025-02-22T09:06:00Z"
            }),
            Action(name="create_time_based_split", kwargs={
                "split_summary_json_path": "processed_data/split_meta.json"
            }),
            Action(name="register_model", kwargs={
                "model_name": "coast_meta_v1",
                "model_path": "models/coast_meta_v1.joblib"
            }),
            Action(name="store_predictions", kwargs={
                "model_name": "coast_meta_v1",
                "predictions_csv_path": "processed_data/preds_coast_meta_v1.csv",
                "generated_ts": "2025-02-22T10:30:00Z"
            }),
            Action(name="store_metrics", kwargs={
                "model_name": "coast_meta_v1",
                "metrics_csv_path": "processed_data/metrics_coast_meta_v1.csv",
                "accuracy_nullable": 0.71
            }),
            Action(name="record_stakeholder_outputs", kwargs={
                "predictions_final_csv_path": "processed_data/preds_coast_meta_v1.csv",
                "metrics_summary_csv_path": "processed_data/metrics_coast_meta_v1.csv"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_023",
        instruction=(
            "You must register literature for 'storm surge machine learning'. End state: search query "
            "'storm surge machine learning' lists result_item_ids ['ZOT-2001','ZOT-2002'] with search_ts "
            "'2025-02-24T12:00:00Z'; metadata titles ['Garcia 2019 Surge ML','Chen 2021 Ensemble Surge'] with "
            "fetched_ts '2025-02-24T12:10:00Z'; fulltext paths ['docs/lit/2001.pdf','docs/lit/2002.pdf'] with "
            "fetched_ts '2025-02-24T12:12:00Z'; and a manifest at 'docs/lit/manifest_surge.txt' contains "
            "'storm surge ML references'."
        ),
        actions=[
            Action(name="zotero_search_items", kwargs={
                "query": "storm surge machine learning",
                "result_item_ids": ["ZOT-2001", "ZOT-2002"],
                "search_ts": "2025-02-24T12:00:00Z"
            }),
            Action(name="zotero_item_metadata", kwargs={
                "item_ids": ["ZOT-2001", "ZOT-2002"],
                "titles": ["Garcia 2019 Surge ML", "Chen 2021 Ensemble Surge"],
                "fetched_ts": "2025-02-24T12:10:00Z"
            }),
            Action(name="zotero_item_fulltext", kwargs={
                "item_ids": ["ZOT-2001", "ZOT-2002"],
                "file_paths": ["docs/lit/2001.pdf", "docs/lit/2002.pdf"],
                "fetched_ts": "2025-02-24T12:12:00Z"
            }),
            Action(name="write_file_text", kwargs={
                "path": "docs/lit/manifest_surge.txt",
                "content": "storm surge ML references"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_024",
        instruction=(
            "You must record literature for 'sensor fusion coastal buoys'. End state: a search record with query "
            "'sensor fusion coastal buoys' lists ['ZOT-4001','ZOT-4003'] and search_ts '2025-02-26T12:00:00Z'; metadata "
            "has titles ['Diaz 2021 Multi‑Sensor Buoys','Singh 2024 Fusion at Sea'] with fetched_ts "
            "'2025-02-26T12:10:00Z'; fulltext paths are ['docs/lit/4001.pdf','docs/lit/4003.pdf'] with fetched_ts "
            "'2025-02-26T12:12:00Z'; and a manifest 'docs/lit/manifest_sensors.txt' contains "
            "'sensor fusion buoy references'."
        ),
        actions=[
            Action(name="zotero_search_items", kwargs={
                "query": "sensor fusion coastal buoys",
                "result_item_ids": ["ZOT-4001", "ZOT-4003"],
                "search_ts": "2025-02-26T12:00:00Z"
            }),
            Action(name="zotero_item_metadata", kwargs={
                "item_ids": ["ZOT-4001", "ZOT-4003"],
                "titles": ["Diaz 2021 Multi‑Sensor Buoys", "Singh 2024 Fusion at Sea"],
                "fetched_ts": "2025-02-26T12:10:00Z"
            }),
            Action(name="zotero_item_fulltext", kwargs={
                "item_ids": ["ZOT-4001", "ZOT-4003"],
                "file_paths": ["docs/lit/4001.pdf", "docs/lit/4003.pdf"],
                "fetched_ts": "2025-02-26T12:12:00Z"
            }),
            Action(name="write_file_text", kwargs={
                "path": "docs/lit/manifest_sensors.txt",
                "content": "sensor fusion buoy references"
            }),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_025",
        instruction=(
            "You must leave the database in a reproducible Crescent City baseline. By the end: a configuration row shows "
            "target_city 'Crescent City' with timezone 'UTC'; a geocoding record locates 'Crescent City' at 41.7558,-124.2017; "
            "a proximity result at those coordinates includes station '9419750', and you set it as the primary; observed water "
            "levels for '9419750' include the point '2025-03-01T00:00:00Z' = 1.02 (m); tide predictions for '9419750' include "
            "the point '2025-03-01T00:00:00Z' = 1.08 (m); and a processed artifact exists at 'processed_data/merged_timeseries_cc.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Crescent City", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Crescent City", "latitude": 41.7558, "longitude": -124.2017}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 41.7558, "query_longitude": -124.2017, "station_ids": ["9419750"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9419750"}),
            Action(name="store_water_levels", kwargs={"station_id": "9419750", "timestamps": ["2025-03-01T00:00:00Z"], "water_level_m": [1.02], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9419750", "timestamps": ["2025-03-01T00:00:00Z"], "tide_pred_m": [1.08], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_cc.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_026",
        instruction=(
            "You must register a Point Reyes intake baseline. Final state: configuration shows target_city 'Point Reyes' (timezone 'UTC'); "
            "geocoding places 'Point Reyes' at 38.0690,-122.8100; a proximity record there includes station '9415020', which you set as primary; "
            "observed water levels for '9415020' include '2025-03-03T06:00:00Z' = 1.11 (m); tide predictions for '9415020' include "
            "'2025-03-03T06:00:00Z' = 1.16 (m); and a processed artifact at 'processed_data/merged_timeseries_pointreyes.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Point Reyes", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Point Reyes", "latitude": 38.0690, "longitude": -122.8100}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 38.0690, "query_longitude": -122.8100, "station_ids": ["9415020"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9415020"}),
            Action(name="store_water_levels", kwargs={"station_id": "9415020", "timestamps": ["2025-03-03T06:00:00Z"], "water_level_m": [1.11], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9415020", "timestamps": ["2025-03-03T06:00:00Z"], "tide_pred_m": [1.16], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_pointreyes.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_027",
        instruction=(
            "You must store a San Mateo intake baseline. End state: configuration lists target_city 'San Mateo' with timezone 'UTC'; "
            "geocoding locates 'San Mateo' at 37.5629,-122.3255; a proximity result includes '9414521', which you mark primary; "
            "observed water levels for '9414521' include '2025-03-04T07:00:00Z' = 0.99 (m); tide predictions for '9414521' include "
            "'2025-03-04T07:00:00Z' = 1.05 (m); and a processed artifact at 'processed_data/merged_timeseries_sanmateo.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "San Mateo", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "San Mateo", "latitude": 37.5629, "longitude": -122.3255}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 37.5629, "query_longitude": -122.3255, "station_ids": ["9414521"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9414521"}),
            Action(name="store_water_levels", kwargs={"station_id": "9414521", "timestamps": ["2025-03-04T07:00:00Z"], "water_level_m": [0.99], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9414521", "timestamps": ["2025-03-04T07:00:00Z"], "tide_pred_m": [1.05], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_sanmateo.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_028",
        instruction=(
            "You must register a Santa Monica intake. By the end: configuration shows target_city 'Santa Monica' (timezone 'UTC'); "
            "geocoding sets 'Santa Monica' at 34.0195,-118.4912; a proximity record includes '9410840' and you set it primary; "
            "observed water levels for '9410840' include '2025-03-05T12:00:00Z' = 1.07 (m); tide predictions include "
            "'2025-03-05T12:00:00Z' = 1.15 (m); and a processed artifact is at 'processed_data/merged_timeseries_sm.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Santa Monica", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Santa Monica", "latitude": 34.0195, "longitude": -118.4912}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 34.0195, "query_longitude": -118.4912, "station_ids": ["9410840"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9410840"}),
            Action(name="store_water_levels", kwargs={"station_id": "9410840", "timestamps": ["2025-03-05T12:00:00Z"], "water_level_m": [1.07], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9410840", "timestamps": ["2025-03-05T12:00:00Z"], "tide_pred_m": [1.15], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_sm.csv"}),
        ],
        outputs=[],
    ),    
    Task(
        annotator="0",
        user_id="ds_v1_029",
        instruction=(
            "You must assemble a San Diego modeling bundle. End state: features at 'processed_data/features_sd.csv' with "
            "['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-13T09:05:00Z'); "
            "model config at 'processed_data/model_config_sd.json' with classification_threshold_m 0.58 "
            "(created_ts '2025-03-13T09:06:00Z'); a split summary at 'processed_data/split_sd.json'; "
            "model 'sd_lr_v1' at 'models/sd_lr_v1.joblib'; predictions at 'processed_data/preds_sd_lr_v1.csv' "
            "(generated_ts '2025-03-13T10:30:00Z'); metrics at 'processed_data/metrics_sd_lr_v1.csv' (auc 0.72); "
            "and stakeholder references to those same predictions/metrics."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_sd.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-03-13T09:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_sd.json", "classification_threshold_m_nullable": 0.58, "created_ts": "2025-03-13T09:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_sd.json"}),
            Action(name="register_model", kwargs={"model_name": "sd_lr_v1", "model_path": "models/sd_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "sd_lr_v1", "predictions_csv_path": "processed_data/preds_sd_lr_v1.csv", "generated_ts": "2025-03-13T10:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "sd_lr_v1", "metrics_csv_path": "processed_data/metrics_sd_lr_v1.csv", "auc_nullable": 0.72}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_sd_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_sd_lr_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_030",
        instruction=(
            "You must store a Los Angeles modeling bundle. Final state: features at 'processed_data/features_la.csv' "
            "with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-13T11:05:00Z'); "
            "config at 'processed_data/model_config_la.json' with classification_threshold_m 0.62 (created_ts '2025-03-13T11:06:00Z'); "
            "split summary at 'processed_data/split_la.json'; model 'la_rf_v1' (type 'random_forest') at 'models/la_rf_v1.joblib'; "
            "predictions at 'processed_data/preds_la_rf_v1.csv' (generated_ts '2025-03-13T12:30:00Z'); metrics at "
            "'processed_data/metrics_la_rf_v1.csv' (accuracy 0.71); and stakeholder references to those artifacts."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_la.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-03-13T11:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_la.json", "classification_threshold_m_nullable": 0.62, "created_ts": "2025-03-13T11:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_la.json"}),
            Action(name="register_model", kwargs={"model_name": "la_rf_v1", "model_path": "models/la_rf_v1.joblib", "model_type": "random_forest"}),
            Action(name="store_predictions", kwargs={"model_name": "la_rf_v1", "predictions_csv_path": "processed_data/preds_la_rf_v1.csv", "generated_ts": "2025-03-13T12:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "la_rf_v1", "metrics_csv_path": "processed_data/metrics_la_rf_v1.csv", "accuracy_nullable": 0.71}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_la_rf_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_la_rf_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_031",
        instruction=(
            "You must capture a San Diego intake baseline. End state: configuration shows target_city 'San Diego' (UTC); "
            "geocoding places 'San Diego' at 32.7157,-117.1611; a proximity result at those coordinates includes '9410170' which "
            "you set primary; observed water levels for '9410170' include '2025-03-15T00:00:00Z' = 0.98 (m); tide predictions include "
            "'2025-03-15T00:00:00Z' = 1.05 (m); and a processed artifact exists at 'processed_data/merged_timeseries_sd.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "San Diego", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "San Diego", "latitude": 32.7157, "longitude": -117.1611}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 32.7157, "query_longitude": -117.1611, "station_ids": ["9410170"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9410170"}),
            Action(name="store_water_levels", kwargs={"station_id": "9410170", "timestamps": ["2025-03-15T00:00:00Z"], "water_level_m": [0.98], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9410170", "timestamps": ["2025-03-15T00:00:00Z"], "tide_pred_m": [1.05], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_sd.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_032",
        instruction=(
            "You must record a La Jolla intake baseline. Final state: configuration shows target_city 'La Jolla' (UTC); "
            "geocoding anchors 'La Jolla' at 32.8328,-117.2713; a proximity record includes station '9410230' which you set primary; "
            "observed water levels for '9410230' include '2025-03-16T01:00:00Z' = 1.01 (m); tide predictions for '9410230' include "
            "'2025-03-16T01:00:00Z' = 1.09 (m); and a processed artifact is present at 'processed_data/merged_timeseries_lajolla.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "La Jolla", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "La Jolla", "latitude": 32.8328, "longitude": -117.2713}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 32.8328, "query_longitude": -117.2713, "station_ids": ["9410230"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9410230"}),
            Action(name="store_water_levels", kwargs={"station_id": "9410230", "timestamps": ["2025-03-16T01:00:00Z"], "water_level_m": [1.01], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9410230", "timestamps": ["2025-03-16T01:00:00Z"], "tide_pred_m": [1.09], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_lajolla.csv"}),
        ],
        outputs=[],
    ),    
    Task(
        annotator="0",
        user_id="ds_v1_033",
        instruction=(
            "You must log a compact anomaly check for station '9413830'. End state: an anomaly metrics row derived from "
            "water_level_series [1.3,1.4,1.5] and tide_prediction_series [1.2,1.3,1.4] is stored at "
            "'processed_data/anomaly_9413830_20250318.csv' (generated_ts '2025-03-18T09:00:00Z'); a QC figure is registered at "
            "'figures/qc/anomaly_9413830.png'; and the terminal log says 'QC: anomaly complete'."
        ),
        actions=[
            Action(name="compute_tide_anomaly_summary", kwargs={
                "station_id": "9413830",
                "water_level_series": [1.3, 1.4, 1.5],
                "tide_prediction_series": [1.2, 1.3, 1.4],
                "metrics_csv_path": "processed_data/anomaly_9413830_20250318.csv",
                "generated_ts": "2025-03-18T09:00:00Z"
            }),
            Action(name="register_qc_figure", kwargs={"figure_path": "figures/qc/anomaly_9413830.png", "description": "Max abs anomaly for 9413830"}),
            Action(name="append_terminal_log", kwargs={"command": "qc_anomaly:9413830", "printed_message": "QC: anomaly complete"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_034",
        instruction=(
            "You must publish release notes for the coastal model bundle (2025-03-19). End state: page 'PAGE-20250319-REL' titled "
            "'Coastal Model Release - 2025-03-19' exists (created_ts '2025-03-19T09:00:00Z'); sections "
            "['Release Notes','Changelog','Artifacts'] are present (updated_ts '2025-03-19T09:05:00Z'); properties JSON is set to "
            "'{\"model\":\"models/coast_meta_v1.joblib\",\"predictions\":\"processed_data/preds_coast_meta_v1.csv\",\"metrics\":\"processed_data/metrics_coast_meta_v1.csv\"}' "
            "(updated_ts '2025-03-19T09:10:00Z'); and an email to ['team@coastallab.org'] is sent as 'MSG-20250319-REL' "
            "(draft '2025-03-19T09:20:00Z', sent '2025-03-19T09:25:00Z')."
        ),
        actions=[
            Action(name="notion_create_page", kwargs={"page_id": "PAGE-20250319-REL", "title": "Coastal Model Release - 2025-03-19", "created_ts": "2025-03-19T09:00:00Z"}),
            Action(name="notion_append_sections", kwargs={"page_id": "PAGE-20250319-REL", "sections": ["Release Notes","Changelog","Artifacts"], "updated_ts": "2025-03-19T09:05:00Z"}),
            Action(name="notion_update_page_properties", kwargs={
                "page_id": "PAGE-20250319-REL",
                "properties_json": '{"model":"models/coast_meta_v1.joblib","predictions":"processed_data/preds_coast_meta_v1.csv","metrics":"processed_data/metrics_coast_meta_v1.csv"}',
                "updated_ts": "2025-03-19T09:10:00Z"
            }),
            Action(name="gmail_draft_email", kwargs={
                "draft_id": "DRAFT-20250319-REL",
                "subject": "Coastal Model Release - 2025-03-19",
                "recipients": ["team@coastallab.org"],
                "created_ts": "2025-03-19T09:20:00Z"
            }),
            Action(name="gmail_send_email", kwargs={"draft_id": "DRAFT-20250319-REL", "message_id": "MSG-20250319-REL", "sent_ts": "2025-03-19T09:25:00Z"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_035",
        instruction=(
            "You must compile a Crescent City modeling bundle. End state: features at 'processed_data/features_cc.csv' with "
            "['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-21T09:05:00Z'); "
            "config at 'processed_data/model_config_cc.json' with classification_threshold_m 0.57 (created_ts '2025-03-21T09:06:00Z'); "
            "split at 'processed_data/split_cc.json'; model 'cc_lr_v1' at 'models/cc_lr_v1.joblib'; predictions at "
            "'processed_data/preds_cc_lr_v1.csv' (generated_ts '2025-03-21T10:30:00Z'); metrics at 'processed_data/metrics_cc_lr_v1.csv' "
            "(accuracy 0.66); and stakeholder references to these artifacts."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_cc.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-03-21T09:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_cc.json", "classification_threshold_m_nullable": 0.57, "created_ts": "2025-03-21T09:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_cc.json"}),
            Action(name="register_model", kwargs={"model_name": "cc_lr_v1", "model_path": "models/cc_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "cc_lr_v1", "predictions_csv_path": "processed_data/preds_cc_lr_v1.csv", "generated_ts": "2025-03-21T10:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "cc_lr_v1", "metrics_csv_path": "processed_data/metrics_cc_lr_v1.csv", "accuracy_nullable": 0.66}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_cc_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_cc_lr_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_036",
        instruction=(
            "You must assemble an Eureka modeling bundle. End state: features at 'processed_data/features_eureka.csv' "
            "with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-21T11:05:00Z'); config "
            "at 'processed_data/model_config_eureka.json' with classification_threshold_m 0.59 (created_ts '2025-03-21T11:06:00Z'); "
            "split at 'processed_data/split_eureka.json'; model 'eureka_lr_v1' at 'models/eureka_lr_v1.joblib'; predictions at "
            "'processed_data/preds_eureka_lr_v1.csv' (generated_ts '2025-03-21T12:30:00Z'); metrics at "
            "'processed_data/metrics_eureka_lr_v1.csv' (auc 0.69); and stakeholder references to those paths."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_eureka.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-03-21T11:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_eureka.json", "classification_threshold_m_nullable": 0.59, "created_ts": "2025-03-21T11:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_eureka.json"}),
            Action(name="register_model", kwargs={"model_name": "eureka_lr_v1", "model_path": "models/eureka_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "eureka_lr_v1", "predictions_csv_path": "processed_data/preds_eureka_lr_v1.csv", "generated_ts": "2025-03-21T12:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "eureka_lr_v1", "metrics_csv_path": "processed_data/metrics_eureka_lr_v1.csv", "auc_nullable": 0.69}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_eureka_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_eureka_lr_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_037",
        instruction=(
            "You must assemble a Capitola modeling bundle. End state: features at 'processed_data/features_cap.csv' with "
            "['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-22T11:05:00Z'); config at "
            "'processed_data/model_config_cap.json' with classification_threshold_m 0.58 (created_ts '2025-03-22T11:06:00Z'); split at "
            "'processed_data/split_cap.json'; model 'cap_lr_v1' at 'models/cap_lr_v1.joblib'; predictions at "
            "'processed_data/preds_cap_lr_v1.csv' (generated_ts '2025-03-22T12:30:00Z'); metrics at "
            "'processed_data/metrics_cap_lr_v1.csv' (accuracy 0.68); and stakeholder references to those artifacts."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_cap.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-03-22T11:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_cap.json", "classification_threshold_m_nullable": 0.58, "created_ts": "2025-03-22T11:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_cap.json"}),
            Action(name="register_model", kwargs={"model_name": "cap_lr_v1", "model_path": "models/cap_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "cap_lr_v1", "predictions_csv_path": "processed_data/preds_cap_lr_v1.csv", "generated_ts": "2025-03-22T12:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "cap_lr_v1", "metrics_csv_path": "processed_data/metrics_cap_lr_v1.csv", "accuracy_nullable": 0.68}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_cap_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_cap_lr_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_038",
        instruction=(
            "You must register an experimental feature set and a split plan. End state: features at "
            "'processed_data/features_experimental.csv' with ['precip_6h_mm','surge_12h_max_m','pressure_trend_12h_hpa'] "
            "(generated_ts '2025-03-25T09:05:00Z'); a config at 'processed_data/model_config_experimental.json' with "
            "test_split_fraction 0.25 (created_ts '2025-03-25T09:06:00Z'); and a split summary at "
            "'processed_data/split_experimental.json' with test_fraction 0.25 and counts 750/250 "
            "(split_ts '2025-03-25T09:07:00Z')."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_experimental.csv", "feature_names": ["precip_6h_mm","surge_12h_max_m","pressure_trend_12h_hpa"], "generated_ts": "2025-03-25T09:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_experimental.json", "test_split_fraction_nullable": 0.25, "created_ts": "2025-03-25T09:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_experimental.json", "test_fraction": 0.25, "train_index_count": 750, "test_index_count": 250, "split_ts": "2025-03-25T09:07:00Z"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_039",
        instruction=(
            "You must produce a Pacifica high‑tide briefing (2025-03-25). End state: a page 'PAGE-20250325-HT1' titled "
            "'Pacifica High Tide - 2025-03-25' exists (created_ts '2025-03-25T09:00:00Z'); sections "
            "['Summary','Drivers','Next Steps'] are present (updated_ts '2025-03-25T09:05:00Z'); properties JSON equals "
            "'{\"predictions\":\"processed_data/preds_pac_rf_v1.csv\",\"metrics\":\"processed_data/metrics_pac_rf_v1.csv\",\"figure\":\"figures/qc/pac_high_tide.png\"}' "
            "(updated_ts '2025-03-25T09:10:00Z'); and an email to ['ops@pacifica.ca.us'] is sent as 'MSG-20250325-HT1' "
            "(draft '2025-03-25T09:20:00Z', sent '2025-03-25T09:25:00Z')."
        ),
        actions=[
            Action(name="notion_create_page", kwargs={"page_id": "PAGE-20250325-HT1", "title": "Pacifica High Tide - 2025-03-25", "created_ts": "2025-03-25T09:00:00Z"}),
            Action(name="notion_append_sections", kwargs={"page_id": "PAGE-20250325-HT1", "sections": ["Summary","Drivers","Next Steps"], "updated_ts": "2025-03-25T09:05:00Z"}),
            Action(name="notion_update_page_properties", kwargs={
                "page_id": "PAGE-20250325-HT1",
                "properties_json": '{"predictions":"processed_data/preds_pac_rf_v1.csv","metrics":"processed_data/metrics_pac_rf_v1.csv","figure":"figures/qc/pac_high_tide.png"}',
                "updated_ts": "2025-03-25T09:10:00Z"
            }),
            Action(name="gmail_draft_email", kwargs={"draft_id": "DRAFT-20250325-HT1", "subject": "Pacifica High Tide Briefing - 2025-03-25", "recipients": ["ops@pacifica.ca.us"], "created_ts": "2025-03-25T09:20:00Z"}),
            Action(name="gmail_send_email", kwargs={"draft_id": "DRAFT-20250325-HT1", "message_id": "MSG-20250325-HT1", "sent_ts": "2025-03-25T09:25:00Z"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_040",
        instruction=(
            "You must capture a Redwood City micro‑run. End state: configuration shows target_city 'Redwood City' (UTC); "
            "geocoding sets 37.4852,-122.2364 (canonical 'Redwood City, California'); a proximity record includes '9414523' and you set it primary; "
            "observed water levels for '9414523' include '2025-03-28T06:00:00Z' = 1.00 (m); tide predictions include "
            "'2025-03-28T06:00:00Z' = 1.06 (m); and a processed artifact exists at 'processed_data/merged_timeseries_rwc.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Redwood City", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Redwood City", "latitude": 37.4852, "longitude": -122.2364, "canonical_name": "Redwood City, California"}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 37.4852, "query_longitude": -122.2364, "station_ids": ["9414523"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9414523"}),
            Action(name="store_water_levels", kwargs={"station_id": "9414523", "timestamps": ["2025-03-28T06:00:00Z"], "water_level_m": [1.00], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9414523", "timestamps": ["2025-03-28T06:00:00Z"], "tide_pred_m": [1.06], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_rwc.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_041",
        instruction=(
            "You must capture a Long Beach intake baseline. End state: configuration shows target_city 'Long Beach' (UTC); "
            "geocoding places 'Long Beach' at 33.7701,-118.1937; a proximity record there includes '9410669', which you set as primary; "
            "observed water levels for '9410669' include '2025-03-01T03:00:00Z' = 0.97 (m); tide predictions include "
            "'2025-03-01T03:00:00Z' = 1.02 (m); and a processed artifact exists at 'processed_data/merged_timeseries_longbeach.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Long Beach", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Long Beach", "latitude": 33.7701, "longitude": -118.1937}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 33.7701, "query_longitude": -118.1937, "station_ids": ["9410669"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9410669"}),
            Action(name="store_water_levels", kwargs={"station_id": "9410669", "timestamps": ["2025-03-01T03:00:00Z"], "water_level_m": [0.97], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9410669", "timestamps": ["2025-03-01T03:00:00Z"], "tide_pred_m": [1.02], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_longbeach.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_042",
        instruction=(
            "You must register a Bodega Bay intake baseline. Final state: configuration shows target_city 'Bodega Bay' (UTC); "
            "geocoding places 'Bodega Bay' at 38.3337,-123.0486; a proximity record includes station '9416841' set primary; "
            "observed water levels include '2025-03-02T01:00:00Z' = 1.12 (m); tide predictions include '2025-03-02T01:00:00Z' = 1.18 (m); "
            "and a processed artifact at 'processed_data/merged_timeseries_bodega.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Bodega Bay", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Bodega Bay", "latitude": 38.3337, "longitude": -123.0486}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 38.3337, "query_longitude": -123.0486, "station_ids": ["9416841"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9416841"}),
            Action(name="store_water_levels", kwargs={"station_id": "9416841", "timestamps": ["2025-03-02T01:00:00Z"], "water_level_m": [1.12], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9416841", "timestamps": ["2025-03-02T01:00:00Z"], "tide_pred_m": [1.18], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_bodega.csv"}),
        ],
        outputs=[],
    ),
    
    Task(
        annotator="0",
        user_id="ds_v1_043",
        instruction=(
            "You must capture a Point Arena intake baseline. End state: configuration shows target_city 'Point Arena' (UTC); "
            "geocoding places 'Point Arena' at 38.9086,-123.7083; a proximity record includes '9416845' set primary; observed water "
            "levels for '9416845' include '2025-03-03T01:00:00Z' = 1.06 (m); tide predictions include '2025-03-03T01:00:00Z' = 1.13 (m); "
            "and a processed artifact at 'processed_data/merged_timeseries_pointarena.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Point Arena", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Point Arena", "latitude": 38.9086, "longitude": -123.7083}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 38.9086, "query_longitude": -123.7083, "station_ids": ["9416845"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9416845"}),
            Action(name="store_water_levels", kwargs={"station_id": "9416845", "timestamps": ["2025-03-03T01:00:00Z"], "water_level_m": [1.06], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9416845", "timestamps": ["2025-03-03T01:00:00Z"], "tide_pred_m": [1.13], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_pointarena.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_044",
        instruction=(
            "You must store a Fort Bragg intake baseline. End state: configuration shows target_city 'Fort Bragg' (UTC); "
            "geocoding anchors 39.4450,-123.8050; a proximity record includes '9416849' which you set primary; observed water levels "
            "include '2025-03-03T02:00:00Z' = 1.09 (m); tide predictions include '2025-03-03T02:00:00Z' = 1.16 (m); and a processed artifact "
            "exists at 'processed_data/merged_timeseries_fortbragg.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Fort Bragg", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Fort Bragg", "latitude": 39.4450, "longitude": -123.8050}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 39.4450, "query_longitude": -123.8050, "station_ids": ["9416849"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9416849"}),
            Action(name="store_water_levels", kwargs={"station_id": "9416849", "timestamps": ["2025-03-03T02:00:00Z"], "water_level_m": [1.09], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9416849", "timestamps": ["2025-03-03T02:00:00Z"], "tide_pred_m": [1.16], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_fortbragg.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_045",
        instruction=(
            "You must register a San Pedro intake baseline. Final state: configuration shows target_city 'San Pedro' (UTC); "
            "geocoding anchors 33.7358,-118.2923; a proximity entry at those coordinates includes '9410660' which you mark primary; "
            "observed water levels include '2025-03-04T00:00:00Z' = 0.95 (m); tide predictions include '2025-03-04T00:00:00Z' = 1.01 (m); "
            "and a processed artifact exists at 'processed_data/merged_timeseries_sanpedro.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "San Pedro", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "San Pedro", "latitude": 33.7358, "longitude": -118.2923}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 33.7358, "query_longitude": -118.2923, "station_ids": ["9410660"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9410660"}),
            Action(name="store_water_levels", kwargs={"station_id": "9410660", "timestamps": ["2025-03-04T00:00:00Z"], "water_level_m": [0.95], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9410660", "timestamps": ["2025-03-04T00:00:00Z"], "tide_pred_m": [1.01], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_sanpedro.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_046",
        instruction=(
            "You must capture a Huntington Beach intake baseline. End state: configuration lists target_city 'Huntington Beach' (UTC); "
            "geocoding pins 33.6595,-117.9988; a proximity record includes '9410647' set primary; observed water levels "
            "include '2025-03-04T01:00:00Z' = 1.00 (m); tide predictions include '2025-03-04T01:00:00Z' = 1.08 (m); and a merged artifact "
            "at 'processed_data/merged_timeseries_hb.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Huntington Beach", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Huntington Beach", "latitude": 33.6595, "longitude": -117.9988}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 33.6595, "query_longitude": -117.9988, "station_ids": ["9410647"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9410647"}),
            Action(name="store_water_levels", kwargs={"station_id": "9410647", "timestamps": ["2025-03-04T01:00:00Z"], "water_level_m": [1.00], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9410647", "timestamps": ["2025-03-04T01:00:00Z"], "tide_pred_m": [1.08], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_hb.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_047",
        instruction=(
            "You must assemble an Oceanside modeling bundle. End state: features at 'processed_data/features_oce.csv' with "
            "['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-05T09:05:00Z'); "
            "model config at 'processed_data/model_config_oce.json' with classification_threshold_m 0.59 (created_ts '2025-03-05T09:06:00Z'); "
            "a split summary at 'processed_data/split_oce.json'; model 'oce_lr_v1' at 'models/oce_lr_v1.joblib'; predictions at "
            "'processed_data/preds_oce_lr_v1.csv' (generated_ts '2025-03-05T10:30:00Z'); metrics at 'processed_data/metrics_oce_lr_v1.csv' "
            "(auc 0.70); and stakeholder references to those same artifacts."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_oce.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-03-05T09:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_oce.json", "classification_threshold_m_nullable": 0.59, "created_ts": "2025-03-05T09:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_oce.json"}),
            Action(name="register_model", kwargs={"model_name": "oce_lr_v1", "model_path": "models/oce_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "oce_lr_v1", "predictions_csv_path": "processed_data/preds_oce_lr_v1.csv", "generated_ts": "2025-03-05T10:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "oce_lr_v1", "metrics_csv_path": "processed_data/metrics_oce_lr_v1.csv", "auc_nullable": 0.70}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_oce_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_oce_lr_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_048",
        instruction=(
            "You must store a Long Beach modeling bundle. End state: features at 'processed_data/features_lb.csv' with "
            "['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-05T11:05:00Z'); "
            "config at 'processed_data/model_config_lb.json' with classification_threshold_m 0.61 (created_ts '2025-03-05T11:06:00Z'); "
            "split summary at 'processed_data/split_lb.json'; model 'lb_lr_v1' at 'models/lb_lr_v1.joblib'; predictions at "
            "'processed_data/preds_lb_lr_v1.csv' (generated_ts '2025-03-05T12:30:00Z'); metrics at "
            "'processed_data/metrics_lb_lr_v1.csv' (accuracy 0.69); and stakeholder references to those artifacts."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_lb.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-03-05T11:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_lb.json", "classification_threshold_m_nullable": 0.61, "created_ts": "2025-03-05T11:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_lb.json"}),
            Action(name="register_model", kwargs={"model_name": "lb_lr_v1", "model_path": "models/lb_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "lb_lr_v1", "predictions_csv_path": "processed_data/preds_lb_lr_v1.csv", "generated_ts": "2025-03-05T12:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "lb_lr_v1", "metrics_csv_path": "processed_data/metrics_lb_lr_v1.csv", "accuracy_nullable": 0.69}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_lb_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_lb_lr_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_049",
        instruction=(
            "You must assemble a Newport Beach modeling bundle. End state: features at 'processed_data/features_newport.csv' with "
            "['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-03-06T09:05:00Z'); "
            "config at 'processed_data/model_config_newport.json' with classification_threshold_m 0.58 (created_ts '2025-03-06T09:06:00Z'); "
            "split at 'processed_data/split_newport.json'; model 'newport_rf_v1' (type 'random_forest') at 'models/newport_rf_v1.joblib'; "
            "predictions at 'processed_data/preds_newport_rf_v1.csv' (generated_ts '2025-03-06T10:30:00Z'); metrics at "
            "'processed_data/metrics_newport_rf_v1.csv' (auc 0.71); and stakeholder references."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_newport.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-03-06T09:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_newport.json", "classification_threshold_m_nullable": 0.58, "created_ts": "2025-03-06T09:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_newport.json"}),
            Action(name="register_model", kwargs={"model_name": "newport_rf_v1", "model_path": "models/newport_rf_v1.joblib", "model_type": "random_forest"}),
            Action(name="store_predictions", kwargs={"model_name": "newport_rf_v1", "predictions_csv_path": "processed_data/preds_newport_rf_v1.csv", "generated_ts": "2025-03-06T10:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "newport_rf_v1", "metrics_csv_path": "processed_data/metrics_newport_rf_v1.csv", "auc_nullable": 0.71}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_newport_rf_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_newport_rf_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_050",
        instruction=(
            "You must compile a Bodega Bay modeling bundle. End state: features at 'processed_data/features_bodega.csv' "
            "(generated_ts '2025-03-06T11:05:00Z'); config at 'processed_data/model_config_bodega.json' with "
            "classification_threshold_m 0.60 (created_ts '2025-03-06T11:06:00Z'); split at 'processed_data/split_bodega.json'; "
            "model 'bodega_lr_v1' at 'models/bodega_lr_v1.joblib'; predictions at 'processed_data/preds_bodega_lr_v1.csv' "
            "(generated_ts '2025-03-06T12:30:00Z'); metrics at 'processed_data/metrics_bodega_lr_v1.csv' (accuracy 0.67); "
            "and stakeholder references."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_bodega.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-03-06T11:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_bodega.json", "classification_threshold_m_nullable": 0.60, "created_ts": "2025-03-06T11:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_bodega.json"}),
            Action(name="register_model", kwargs={"model_name": "bodega_lr_v1", "model_path": "models/bodega_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "bodega_lr_v1", "predictions_csv_path": "processed_data/preds_bodega_lr_v1.csv", "generated_ts": "2025-03-06T12:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "bodega_lr_v1", "metrics_csv_path": "processed_data/metrics_bodega_lr_v1.csv", "accuracy_nullable": 0.67}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_bodega_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_bodega_lr_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_051",
        instruction=(
            "You must register a Point Arena modeling bundle. End state: features at 'processed_data/features_pa.csv' "
            "(generated_ts '2025-03-07T09:05:00Z'); config at 'processed_data/model_config_pa.json' with "
            "classification_threshold_m 0.62 (created_ts '2025-03-07T09:06:00Z'); split at 'processed_data/split_pa.json'; "
            "model 'pa_lr_v1' at 'models/pa_lr_v1.joblib'; predictions at 'processed_data/preds_pa_lr_v1.csv' "
            "(generated_ts '2025-03-07T10:30:00Z'); metrics at 'processed_data/metrics_pa_lr_v1.csv' (auc 0.69); and stakeholder references."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_pa.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-03-07T09:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_pa.json", "classification_threshold_m_nullable": 0.62, "created_ts": "2025-03-07T09:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_pa.json"}),
            Action(name="register_model", kwargs={"model_name": "pa_lr_v1", "model_path": "models/pa_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "pa_lr_v1", "predictions_csv_path": "processed_data/preds_pa_lr_v1.csv", "generated_ts": "2025-03-07T10:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "pa_lr_v1", "metrics_csv_path": "processed_data/metrics_pa_lr_v1.csv", "auc_nullable": 0.69}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_pa_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_pa_lr_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_052",
        instruction=(
            "You must prepare stakeholder‑facing material for Santa Monica (2025-03-07). End state: a page 'PAGE-20250307-SM' titled "
            "'Santa Monica Flood Risk - 2025-03-07' exists (created_ts '2025-03-07T09:00:00Z'); sections "
            "['Summary','Drivers','Actions'] are present (updated_ts '2025-03-07T09:05:00Z'); properties equal the exact JSON "
            "'{\"predictions\":\"processed_data/preds_sm_v1.csv\",\"metrics\":\"processed_data/metrics_sm_v1.csv\",\"figure\":\"figures/qc/sm_overview.png\"}' "
            "(updated_ts '2025-03-07T09:10:00Z'); and an email draft 'DRAFT-20250307-SM' to ['ops@santamonica.gov'] is sent as "
            "'MSG-20250307-SM' (draft '2025-03-07T09:20:00Z', sent '2025-03-07T09:25:00Z')."
        ),
        actions=[
            Action(name="notion_create_page", kwargs={"page_id": "PAGE-20250307-SM", "title": "Santa Monica Flood Risk - 2025-03-07", "created_ts": "2025-03-07T09:00:00Z"}),
            Action(name="notion_append_sections", kwargs={"page_id": "PAGE-20250307-SM", "sections": ["Summary","Drivers","Actions"], "updated_ts": "2025-03-07T09:05:00Z"}),
            Action(name="notion_update_page_properties", kwargs={
                "page_id": "PAGE-20250307-SM",
                "properties_json": '{"predictions":"processed_data/preds_sm_v1.csv","metrics":"processed_data/metrics_sm_v1.csv","figure":"figures/qc/sm_overview.png"}',
                "updated_ts": "2025-03-07T09:10:00Z"
            }),
            Action(name="gmail_draft_email", kwargs={"draft_id": "DRAFT-20250307-SM", "subject": "Santa Monica Flood Risk - 2025-03-07", "recipients": ["ops@santamonica.gov"], "attachments_paths": ["figures/qc/sm_overview.png"], "created_ts": "2025-03-07T09:20:00Z"}),
            Action(name="gmail_send_email", kwargs={"draft_id": "DRAFT-20250307-SM", "message_id": "MSG-20250307-SM", "sent_ts": "2025-03-07T09:25:00Z"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_053",
        instruction=(
            "You must package stakeholder reporting for Los Angeles Outer Harbor (2025-03-08). End state: page 'PAGE-20250308-LAOH' "
            "titled 'LA Outer Harbor Flood Risk - 2025-03-08' exists (created_ts '2025-03-08T09:00:00Z'); sections "
            "['Summary','Risks','Recommendations'] are present (updated_ts '2025-03-08T09:05:00Z'); properties contain the exact JSON "
            "'{\"predictions\":\"processed_data/preds_laoh_v1.csv\",\"metrics\":\"processed_data/metrics_laoh_v1.csv\",\"artifacts\":\"artifacts/laoh_20250308.zip\"}' "
            "(updated_ts '2025-03-08T09:10:00Z'); and email draft 'DRAFT-20250308-LAOH' to ['harbor@lacity.org'] is sent as "
            "'MSG-20250308-LAOH' with the artifact attached (draft '2025-03-08T09:20:00Z', sent '2025-03-08T09:25:00Z')."
        ),
        actions=[
            Action(name="notion_create_page", kwargs={"page_id": "PAGE-20250308-LAOH", "title": "LA Outer Harbor Flood Risk - 2025-03-08", "created_ts": "2025-03-08T09:00:00Z"}),
            Action(name="notion_append_sections", kwargs={"page_id": "PAGE-20250308-LAOH", "sections": ["Summary","Risks","Recommendations"], "updated_ts": "2025-03-08T09:05:00Z"}),
            Action(name="notion_update_page_properties", kwargs={
                "page_id": "PAGE-20250308-LAOH",
                "properties_json": '{"predictions":"processed_data/preds_laoh_v1.csv","metrics":"processed_data/metrics_laoh_v1.csv","artifacts":"artifacts/laoh_20250308.zip"}',
                "updated_ts": "2025-03-08T09:10:00Z"
            }),
            Action(name="gmail_draft_email", kwargs={"draft_id": "DRAFT-20250308-LAOH", "subject": "LA Outer Harbor Flood Risk - 2025-03-08", "recipients": ["harbor@lacity.org"], "attachments_paths": ["artifacts/laoh_20250308.zip"], "created_ts": "2025-03-08T09:20:00Z"}),
            Action(name="gmail_send_email", kwargs={"draft_id": "DRAFT-20250308-LAOH", "message_id": "MSG-20250308-LAOH", "sent_ts": "2025-03-08T09:25:00Z"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_054",
        instruction=(
            "You must assemble a Newport (OR) modeling bundle. End: features 'processed_data/features_newportor.csv' (generated_ts '2025-05-09T11:05:00Z'); "
            "config 'processed_data/model_config_newportor.json' with classification_threshold_m 0.59 (created_ts '2025-05-09T11:06:00Z'); "
            "split 'processed_data/split_newportor.json'; model 'newportor_lr_v1' at 'models/newportor_lr_v1.joblib'; predictions "
            "'processed_data/preds_newportor_lr_v1.csv' (generated_ts '2025-05-09T12:30:00Z'); metrics "
            "'processed_data/metrics_newportor_lr_v1.csv' (accuracy 0.69); stakeholder references."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_newportor.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-05-09T11:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_newportor.json", "classification_threshold_m_nullable": 0.59, "created_ts": "2025-05-09T11:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_newportor.json"}),
            Action(name="register_model", kwargs={"model_name": "newportor_lr_v1", "model_path": "models/newportor_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "newportor_lr_v1", "predictions_csv_path": "processed_data/preds_newportor_lr_v1.csv", "generated_ts": "2025-05-09T12:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "newportor_lr_v1", "metrics_csv_path": "processed_data/metrics_newportor_lr_v1.csv", "accuracy_nullable": 0.69}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_newportor_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_newportor_lr_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_055",
        instruction=(
            "You must record a Sausalito intake baseline. End state: configuration shows target_city 'Sausalito' (UTC); "
            "geocoding anchors 37.8591,-122.4853; a proximity record includes '9414291' set primary; observed water levels include "
            "'2025-03-13T00:00:00Z' = 1.03 (m); tide predictions include '2025-03-13T00:00:00Z' = 1.10 (m); and a processed artifact "
            "at 'processed_data/merged_timeseries_sausalito.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Sausalito", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Sausalito", "latitude": 37.8591, "longitude": -122.4853}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 37.8591, "query_longitude": -122.4853, "station_ids": ["9414291"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9414291"}),
            Action(name="store_water_levels", kwargs={"station_id": "9414291", "timestamps": ["2025-03-13T00:00:00Z"], "water_level_m": [1.03], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9414291", "timestamps": ["2025-03-13T00:00:00Z"], "tide_pred_m": [1.10], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_sausalito.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_056",
        instruction=(
            "You must capture a Foster City intake baseline. End state: configuration lists target_city 'Foster City' (UTC); "
            "geocoding locates 37.5585,-122.2711; a proximity result includes '9414524' which you set primary; observed water levels "
            "include '2025-03-13T01:00:00Z' = 0.98 (m); tide predictions include '2025-03-13T01:00:00Z' = 1.04 (m); and a processed artifact "
            "exists at 'processed_data/merged_timeseries_fostercity.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Foster City", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Foster City", "latitude": 37.5585, "longitude": -122.2711}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 37.5585, "query_longitude": -122.2711, "station_ids": ["9414524"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9414524"}),
            Action(name="store_water_levels", kwargs={"station_id": "9414524", "timestamps": ["2025-03-13T01:00:00Z"], "water_level_m": [0.98], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9414524", "timestamps": ["2025-03-13T01:00:00Z"], "tide_pred_m": [1.04], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_fostercity.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_057",
        instruction=(
            "You must prepare stakeholder reporting for Richmond (2025-03-14). End state: a page 'PAGE-20250314-RICH' titled "
            "'Richmond Flood Risk - 2025-03-14' exists (created_ts '2025-03-14T09:00:00Z'); sections "
            "['Summary','Results','Next Steps'] are present (updated_ts '2025-03-14T09:05:00Z'); properties JSON equals "
            "'{\"predictions\":\"processed_data/preds_rich_v1.csv\",\"metrics\":\"processed_data/metrics_rich_v1.csv\",\"figure\":\"figures/qc/rich_overview.png\"}' "
            "(updated_ts '2025-03-14T09:10:00Z'); and an email to ['harbor@ci.richmond.ca.us'] is sent as 'MSG-20250314-RICH' "
            "(draft '2025-03-14T09:20:00Z', sent '2025-03-14T09:25:00Z')."
        ),
        actions=[
            Action(name="notion_create_page", kwargs={"page_id": "PAGE-20250314-RICH", "title": "Richmond Flood Risk - 2025-03-14", "created_ts": "2025-03-14T09:00:00Z"}),
            Action(name="notion_append_sections", kwargs={"page_id": "PAGE-20250314-RICH", "sections": ["Summary","Results","Next Steps"], "updated_ts": "2025-03-14T09:05:00Z"}),
            Action(name="notion_update_page_properties", kwargs={
                "page_id": "PAGE-20250314-RICH",
                "properties_json": '{"predictions":"processed_data/preds_rich_v1.csv","metrics":"processed_data/metrics_rich_v1.csv","figure":"figures/qc/rich_overview.png"}',
                "updated_ts": "2025-03-14T09:10:00Z"
            }),
            Action(name="gmail_draft_email", kwargs={"draft_id": "DRAFT-20250314-RICH", "subject": "Richmond Flood Risk - 2025-03-14", "recipients": ["harbor@ci.richmond.ca.us"], "created_ts": "2025-03-14T09:20:00Z"}),
            Action(name="gmail_send_email", kwargs={"draft_id": "DRAFT-20250314-RICH", "message_id": "MSG-20250314-RICH", "sent_ts": "2025-03-14T09:25:00Z"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_058",
        instruction=(
            "You must capture a Benicia intake baseline. End state: configuration lists target_city 'Benicia' (UTC); "
            "geocoding anchors 38.0494,-122.1586; a proximity record includes '9415144' set primary; observed water levels include "
            "'2025-03-15T00:00:00Z' = 0.92 (m); tide predictions include '2025-03-15T00:00:00Z' = 0.99 (m); and a merged artifact "
            "exists at 'processed_data/merged_timeseries_benicia.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Benicia", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Benicia", "latitude": 38.0494, "longitude": -122.1586}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 38.0494, "query_longitude": -122.1586, "station_ids": ["9415144"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9415144"}),
            Action(name="store_water_levels", kwargs={"station_id": "9415144", "timestamps": ["2025-03-15T00:00:00Z"], "water_level_m": [0.92], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9415144", "timestamps": ["2025-03-15T00:00:00Z"], "tide_pred_m": [0.99], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_benicia.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_059",
        instruction=(
            "You must compile an Alameda modeling bundle. End state: features at 'processed_data/features_alameda.csv' "
            "(generated_ts '2025-03-16T09:05:00Z'); config at 'processed_data/model_config_alameda.json' with "
            "classification_threshold_m 0.56 (created_ts '2025-03-16T09:06:00Z'); split at 'processed_data/split_alameda.json'; "
            "model 'alameda_lr_v1' at 'models/alameda_lr_v1.joblib'; predictions at 'processed_data/preds_alameda_lr_v1.csv' "
            "(generated_ts '2025-03-16T10:30:00Z'); metrics at 'processed_data/metrics_alameda_lr_v1.csv' (auc 0.72); and stakeholder references."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_alameda.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-03-16T09:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_alameda.json", "classification_threshold_m_nullable": 0.56, "created_ts": "2025-03-16T09:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_alameda.json"}),
            Action(name="register_model", kwargs={"model_name": "alameda_lr_v1", "model_path": "models/alameda_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "alameda_lr_v1", "predictions_csv_path": "processed_data/preds_alameda_lr_v1.csv", "generated_ts": "2025-03-16T10:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "alameda_lr_v1", "metrics_csv_path": "processed_data/metrics_alameda_lr_v1.csv", "auc_nullable": 0.72}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_alameda_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_alameda_lr_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_060",
        instruction=(
            "You must publish release notes for the South Coast model bundle (2025-03-17). End state: page 'PAGE-20250317-SC-REL' titled "
            "'South Coast Release - 2025-03-17' exists (created_ts '2025-03-17T09:00:00Z'); sections "
            "['Release Notes','Changelog','Artifacts'] are present (updated_ts '2025-03-17T09:05:00Z'); properties JSON is set to "
            "'{\"model\":\"models/southcoast_meta_v1.joblib\",\"predictions\":\"processed_data/preds_southcoast_meta_v1.csv\",\"metrics\":\"processed_data/metrics_southcoast_meta_v1.csv\"}' "
            "(updated_ts '2025-03-17T09:10:00Z'); and an email to ['team@southcoastlab.org'] is sent as 'MSG-20250317-SC-REL' "
            "(draft '2025-03-17T09:20:00Z', sent '2025-03-17T09:25:00Z')."
        ),
        actions=[
            Action(name="notion_create_page", kwargs={"page_id": "PAGE-20250317-SC-REL", "title": "South Coast Release - 2025-03-17", "created_ts": "2025-03-17T09:00:00Z"}),
            Action(name="notion_append_sections", kwargs={"page_id": "PAGE-20250317-SC-REL", "sections": ["Release Notes","Changelog","Artifacts"], "updated_ts": "2025-03-17T09:05:00Z"}),
            Action(name="notion_update_page_properties", kwargs={
                "page_id": "PAGE-20250317-SC-REL",
                "properties_json": '{"model":"models/southcoast_meta_v1.joblib","predictions":"processed_data/preds_southcoast_meta_v1.csv","metrics":"processed_data/metrics_southcoast_meta_v1.csv"}',
                "updated_ts": "2025-03-17T09:10:00Z"
            }),
            Action(name="gmail_draft_email", kwargs={"draft_id": "DRAFT-20250317-SC-REL", "subject": "South Coast Model Release - 2025-03-17", "recipients": ["team@southcoastlab.org"], "created_ts": "2025-03-17T09:20:00Z"}),
            Action(name="gmail_send_email", kwargs={"draft_id": "DRAFT-20250317-SC-REL", "message_id": "MSG-20250317-SC-REL", "sent_ts": "2025-03-17T09:25:00Z"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_061",
        instruction=(
            "You must establish a San Francisco intake baseline. End state: config shows target_city 'San Francisco' (UTC); "
            "geocoding anchors 'San Francisco' at 37.7749,-122.4194 (canonical 'San Francisco, California'); a proximity "
            "result at those coordinates includes station '9414291' which you set primary; observed water levels for "
            "'9414291' include '2025-04-01T06:00:00Z' = 1.03 (m); tide predictions for '9414291' include "
            "'2025-04-01T06:00:00Z' = 1.11 (m); and a processed artifact exists at "
            "'processed_data/merged_timeseries_sf.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "San Francisco", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "San Francisco", "latitude": 37.7749, "longitude": -122.4194,
                "canonical_name": "San Francisco, California"
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 37.7749, "query_longitude": -122.4194, "station_ids": ["9414291"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9414291"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9414291",
                "timestamps": ["2025-04-01T06:00:00Z"],
                "water_level_m": [1.03],
                "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9414291",
                "timestamps": ["2025-04-01T06:00:00Z"],
                "tide_pred_m": [1.11],
                "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_sf.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_062",
        instruction=(
            "You must capture a Long Beach intake baseline. End state: configuration shows target_city 'Long Beach' (UTC); "
            "geocoding at 33.7701,-118.1937 (canonical 'Long Beach, California'); proximity includes '9410660' set as primary; "
            "observed water levels for '9410660' include '2025-04-02T06:00:00Z' = 1.04 (m); tide predictions include "
            "'2025-04-02T06:00:00Z' = 1.15 (m); and a processed artifact at 'processed_data/merged_timeseries_lb.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Long Beach", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Long Beach", "latitude": 33.7701, "longitude": -118.1937,
                "canonical_name": "Long Beach, California"
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 33.7701, "query_longitude": -118.1937, "station_ids": ["9410660"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9410660"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9410660", "timestamps": ["2025-04-02T06:00:00Z"], "water_level_m": [1.04], "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9410660", "timestamps": ["2025-04-02T06:00:00Z"], "tide_pred_m": [1.15], "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_lb.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_063",
        instruction=(
            "You must create a Bodega Bay intake baseline. Final: config 'Bodega Bay' (UTC); geocoding 38.3338,-123.0486; "
            "proximity includes '9416018' set primary; observed water levels include '2025-04-04T02:00:00Z' = 0.95 (m); "
            "tide predictions include '2025-04-04T02:00:00Z' = 1.02 (m); merged artifact at "
            "'processed_data/merged_timeseries_bodega.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Bodega Bay", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Bodega Bay", "latitude": 38.3338, "longitude": -123.0486
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 38.3338, "query_longitude": -123.0486, "station_ids": ["9416018"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9416018"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9416018", "timestamps": ["2025-04-04T02:00:00Z"], "water_level_m": [0.95], "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9416018", "timestamps": ["2025-04-04T02:00:00Z"], "tide_pred_m": [1.02], "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_bodega.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_064",
        instruction=(
            "You must record a Fort Bragg intake baseline. Final: config 'Fort Bragg' (UTC); geocoding 39.4457,-123.8053; "
            "proximity includes '9417541' set primary; observed water levels include '2025-04-05T02:00:00Z' = 0.93 (m); "
            "tide predictions include '2025-04-05T02:00:00Z' = 1.01 (m); merged artifact at "
            "'processed_data/merged_timeseries_fortbragg.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Fort Bragg", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Fort Bragg", "latitude": 39.4457, "longitude": -123.8053
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 39.4457, "query_longitude": -123.8053, "station_ids": ["9417541"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9417541"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9417541", "timestamps": ["2025-04-05T02:00:00Z"], "water_level_m": [0.93], "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9417541", "timestamps": ["2025-04-05T02:00:00Z"], "tide_pred_m": [1.01], "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_fortbragg.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_065",
        instruction=(
            "You must prepare a Carpinteria intake baseline. Final: config 'Carpinteria' (UTC); geocoding 34.3989,-119.5185; "
            "proximity includes '9411341' set primary; observed water levels include '2025-04-08T04:00:00Z' = 0.92 (m); "
            "tide predictions include '2025-04-08T04:00:00Z' = 1.00 (m); merged artifact at "
            "'processed_data/merged_timeseries_carpinteria.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Carpinteria", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Carpinteria", "latitude": 34.3989, "longitude": -119.5185
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 34.3989, "query_longitude": -119.5185, "station_ids": ["9411341"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9411341"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9411341", "timestamps": ["2025-04-08T04:00:00Z"], "water_level_m": [0.92], "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9411341", "timestamps": ["2025-04-08T04:00:00Z"], "tide_pred_m": [1.00], "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_carpinteria.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_066",
        instruction=(
            "You must establish a Malibu intake baseline. Final: config 'Malibu' (UTC); geocoding 34.0259,-118.7798; "
            "proximity includes '9410841' primary; observed water levels include '2025-04-09T05:00:00Z' = 1.02 (m); "
            "tide predictions include '2025-04-09T05:00:00Z' = 1.10 (m); merged artifact at "
            "'processed_data/merged_timeseries_malibu.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Malibu", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Malibu", "latitude": 34.0259, "longitude": -118.7798
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 34.0259, "query_longitude": -118.7798, "station_ids": ["9410841"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9410841"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9410841", "timestamps": ["2025-04-09T05:00:00Z"], "water_level_m": [1.02], "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9410841", "timestamps": ["2025-04-09T05:00:00Z"], "tide_pred_m": [1.10], "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_malibu.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_067",
        instruction=(
            "You must register a Manhattan Beach intake. Final: config 'Manhattan Beach' (UTC); geocoding 33.8847,-118.4109; "
            "proximity includes '9410662' primary; observed water levels include '2025-04-10T05:00:00Z' = 1.01 (m); "
            "tide predictions include '2025-04-10T05:00:00Z' = 1.09 (m); merged artifact at "
            "'processed_data/merged_timeseries_manhattan.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Manhattan Beach", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Manhattan Beach", "latitude": 33.8847, "longitude": -118.4109
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 33.8847, "query_longitude": -118.4109, "station_ids": ["9410662"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9410662"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9410662", "timestamps": ["2025-04-10T05:00:00Z"], "water_level_m": [1.01], "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9410662", "timestamps": ["2025-04-10T05:00:00Z"], "tide_pred_m": [1.09], "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_manhattan.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_068",
        instruction=(
            "You must create an Oceanside intake baseline. Final: config 'Oceanside' (UTC); geocoding 33.1959,-117.3795; "
            "proximity includes '9410280' set primary; observed water levels include '2025-04-11T01:00:00Z' = 1.00 (m); "
            "tide predictions include '2025-04-11T01:00:00Z' = 1.08 (m); merged artifact at "
            "'processed_data/merged_timeseries_oceanside.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Oceanside", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Oceanside", "latitude": 33.1959, "longitude": -117.3795
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 33.1959, "query_longitude": -117.3795, "station_ids": ["9410280"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9410280"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9410280", "timestamps": ["2025-04-11T01:00:00Z"], "water_level_m": [1.00], "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9410280", "timestamps": ["2025-04-11T01:00:00Z"], "tide_pred_m": [1.08], "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_oceanside.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_069",
        instruction=(
            "You must record a Carlsbad intake baseline. Final: config 'Carlsbad' (UTC); geocoding 33.1581,-117.3506; "
            "proximity includes '9410240' primary; observed water levels include '2025-04-12T01:00:00Z' = 0.99 (m); "
            "tide predictions include '2025-04-12T01:00:00Z' = 1.07 (m); merged artifact at "
            "'processed_data/merged_timeseries_carlsbad.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Carlsbad", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={
                "query_city": "Carlsbad", "latitude": 33.1581, "longitude": -117.3506
            }),
            Action(name="store_noaa_station_search", kwargs={
                "query_latitude": 33.1581, "query_longitude": -117.3506, "station_ids": ["9410240"]
            }),
            Action(name="set_primary_station", kwargs={"station_id": "9410240"}),
            Action(name="store_water_levels", kwargs={
                "station_id": "9410240", "timestamps": ["2025-04-12T01:00:00Z"], "water_level_m": [0.99], "units": "m"
            }),
            Action(name="store_tide_predictions", kwargs={
                "station_id": "9410240", "timestamps": ["2025-04-12T01:00:00Z"], "tide_pred_m": [1.07], "units": "m"
            }),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_carlsbad.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_070",
        instruction=(
            "You must build a Bodega Bay modeling bundle. Final: features 'processed_data/features_bodega.csv' "
            "(generated_ts '2025-04-18T09:05:00Z'); config 'processed_data/model_config_bodega.json' with "
            "classification_threshold_m 0.61 (created_ts '2025-04-18T09:06:00Z'); split 'processed_data/split_bodega.json'; "
            "model 'bodega_lr_v1' at 'models/bodega_lr_v1.joblib'; predictions 'processed_data/preds_bodega_lr_v1.csv' "
            "(generated_ts '2025-04-18T10:30:00Z'); metrics 'processed_data/metrics_bodega_lr_v1.csv' (accuracy 0.69); "
            "and stakeholder references."
        ),
        actions=[
            Action(name="store_features", kwargs={
                "csv_path": "processed_data/features_bodega.csv",
                "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"],
                "generated_ts": "2025-04-18T09:05:00Z"
            }),
            Action(name="write_model_config", kwargs={
                "saved_json_path": "processed_data/model_config_bodega.json",
                "classification_threshold_m_nullable": 0.61,
                "created_ts": "2025-04-18T09:06:00Z"
            }),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_bodega.json"}),
            Action(name="register_model", kwargs={"model_name": "bodega_lr_v1", "model_path": "models/bodega_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={
                "model_name": "bodega_lr_v1", "predictions_csv_path": "processed_data/preds_bodega_lr_v1.csv",
                "generated_ts": "2025-04-18T10:30:00Z"
            }),
            Action(name="store_metrics", kwargs={
                "model_name": "bodega_lr_v1", "metrics_csv_path": "processed_data/metrics_bodega_lr_v1.csv", "accuracy_nullable": 0.69
            }),
            Action(name="record_stakeholder_outputs", kwargs={
                "predictions_final_csv_path": "processed_data/preds_bodega_lr_v1.csv",
                "metrics_summary_csv_path": "processed_data/metrics_bodega_lr_v1.csv"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_071",
        instruction=(
            "You must create a San Pedro modeling bundle. Final: features 'processed_data/features_sanpedro.csv' "
            "(generated_ts '2025-04-20T09:05:00Z'); config 'processed_data/model_config_sanpedro.json' with "
            "classification_threshold_m 0.60 (created_ts '2025-04-20T09:06:00Z'); split 'processed_data/split_sanpedro.json'; "
            "model 'sanpedro_rf_v1' (type 'random_forest') at 'models/sanpedro_rf_v1.joblib'; predictions "
            "'processed_data/preds_sanpedro_rf_v1.csv' (generated_ts '2025-04-20T10:30:00Z'); metrics "
            "'processed_data/metrics_sanpedro_rf_v1.csv' (accuracy 0.72); and stakeholder references."
        ),
        actions=[
            Action(name="store_features", kwargs={
                "csv_path": "processed_data/features_sanpedro.csv",
                "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"],
                "generated_ts": "2025-04-20T09:05:00Z"
            }),
            Action(name="write_model_config", kwargs={
                "saved_json_path": "processed_data/model_config_sanpedro.json",
                "classification_threshold_m_nullable": 0.60,
                "created_ts": "2025-04-20T09:06:00Z"
            }),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_sanpedro.json"}),
            Action(name="register_model", kwargs={
                "model_name": "sanpedro_rf_v1", "model_path": "models/sanpedro_rf_v1.joblib", "model_type": "random_forest"
            }),
            Action(name="store_predictions", kwargs={
                "model_name": "sanpedro_rf_v1", "predictions_csv_path": "processed_data/preds_sanpedro_rf_v1.csv",
                "generated_ts": "2025-04-20T10:30:00Z"
            }),
            Action(name="store_metrics", kwargs={
                "model_name": "sanpedro_rf_v1", "metrics_csv_path": "processed_data/metrics_sanpedro_rf_v1.csv",
                "accuracy_nullable": 0.72
            }),
            Action(name="record_stakeholder_outputs", kwargs={
                "predictions_final_csv_path": "processed_data/preds_sanpedro_rf_v1.csv",
                "metrics_summary_csv_path": "processed_data/metrics_sanpedro_rf_v1.csv"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_072",
        instruction=(
            "You must register an experimental 'gust/wave' feature set and split plan. End: features at "
            "'processed_data/features_gustwave.csv' with ['gust_6h_ms','wave_height_12h_max_m','pressure_trend_24h_hpa'] "
            "(generated_ts '2025-04-26T09:05:00Z'); model config at 'processed_data/model_config_gustwave.json' with "
            "test_split_fraction 0.30 (created_ts '2025-04-26T09:06:00Z'); and a split summary "
            "'processed_data/split_gustwave.json' with test_fraction 0.30 and counts 700/300 "
            "(split_ts '2025-04-26T09:07:00Z')."
        ),
        actions=[
            Action(name="store_features", kwargs={
                "csv_path": "processed_data/features_gustwave.csv",
                "feature_names": ["gust_6h_ms","wave_height_12h_max_m","pressure_trend_24h_hpa"],
                "generated_ts": "2025-04-26T09:05:00Z"
            }),
            Action(name="write_model_config", kwargs={
                "saved_json_path": "processed_data/model_config_gustwave.json",
                "test_split_fraction_nullable": 0.30,
                "created_ts": "2025-04-26T09:06:00Z"
            }),
            Action(name="create_time_based_split", kwargs={
                "split_summary_json_path": "processed_data/split_gustwave.json",
                "test_fraction": 0.30,
                "train_index_count": 700,
                "test_index_count": 300,
                "split_ts": "2025-04-26T09:07:00Z"
            }),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_073",
        instruction=(
            "You must capture a Berkeley intake baseline. End state: configuration shows target_city 'Berkeley' "
            "with timezone 'UTC'; geocoding anchors 'Berkeley' at 37.8716,-122.2727; a proximity search at those "
            "coordinates includes station '9414762' which you set primary; observed water levels for '9414762' include "
            "'2025-04-01T00:00:00Z' = 0.97 (m); tide predictions include '2025-04-01T00:00:00Z' = 1.03 (m); and a "
            "processed artifact exists at 'processed_data/merged_timeseries_berkeley.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Berkeley", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Berkeley", "latitude": 37.8716, "longitude": -122.2727}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 37.8716, "query_longitude": -122.2727, "station_ids": ["9414762"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9414762"}),
            Action(name="store_water_levels", kwargs={"station_id": "9414762", "timestamps": ["2025-04-01T00:00:00Z"], "water_level_m": [0.97], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9414762", "timestamps": ["2025-04-01T00:00:00Z"], "tide_pred_m": [1.03], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_berkeley.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_074",
        instruction=(
            "You must record an Oakland intake baseline. Final state: configuration shows target_city 'Oakland' (UTC); "
            "geocoding places 'Oakland' at 37.8044,-122.2711; a proximity record includes '9414764' which you mark primary; "
            "observed water levels for '9414764' include '2025-04-02T02:00:00Z' = 1.02 (m); tide predictions include "
            "'2025-04-02T02:00:00Z' = 1.08 (m); and a processed artifact exists at 'processed_data/merged_timeseries_oakland.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Oakland", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Oakland", "latitude": 37.8044, "longitude": -122.2711}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 37.8044, "query_longitude": -122.2711, "station_ids": ["9414764"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9414764"}),
            Action(name="store_water_levels", kwargs={"station_id": "9414764", "timestamps": ["2025-04-02T02:00:00Z"], "water_level_m": [1.02], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9414764", "timestamps": ["2025-04-02T02:00:00Z"], "tide_pred_m": [1.08], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_oakland.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_075",
        instruction=(
            "You must capture a Daly City intake baseline. End state: configuration lists target_city 'Daly City' (UTC); "
            "geocoding anchors 37.6879,-122.4702; a proximity result includes '9414570' which you set primary; observed water "
            "levels include '2025-04-02T03:00:00Z' = 1.01 (m); tide predictions include '2025-04-02T03:00:00Z' = 1.07 (m); "
            "and a processed artifact at 'processed_data/merged_timeseries_dalycity.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Daly City", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Daly City", "latitude": 37.6879, "longitude": -122.4702}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 37.6879, "query_longitude": -122.4702, "station_ids": ["9414570"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9414570"}),
            Action(name="store_water_levels", kwargs={"station_id": "9414570", "timestamps": ["2025-04-02T03:00:00Z"], "water_level_m": [1.01], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9414570", "timestamps": ["2025-04-02T03:00:00Z"], "tide_pred_m": [1.07], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_dalycity.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_076",
        instruction=(
            "You must register a Tiburon intake baseline. End state: configuration shows target_city 'Tiburon' (UTC); "
            "geocoding places 37.8735,-122.4569; a proximity record includes '9414444' set primary; observed water levels include "
            "'2025-04-02T04:00:00Z' = 0.99 (m); tide predictions include '2025-04-02T04:00:00Z' = 1.05 (m); and a processed artifact "
            "exists at 'processed_data/merged_timeseries_tiburon.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Tiburon", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Tiburon", "latitude": 37.8735, "longitude": -122.4569}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 37.8735, "query_longitude": -122.4569, "station_ids": ["9414444"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9414444"}),
            Action(name="store_water_levels", kwargs={"station_id": "9414444", "timestamps": ["2025-04-02T04:00:00Z"], "water_level_m": [0.99], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9414444", "timestamps": ["2025-04-02T04:00:00Z"], "tide_pred_m": [1.05], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_tiburon.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_077",
        instruction=(
            "You must capture a San Rafael intake baseline. Final state: configuration lists target_city 'San Rafael' (UTC); "
            "geocoding anchors 37.9735,-122.5311; a proximity result includes '9415071' set primary; observed water levels include "
            "'2025-04-03T01:00:00Z' = 0.96 (m); tide predictions include '2025-04-03T01:00:00Z' = 1.02 (m); and a merged artifact "
            "at 'processed_data/merged_timeseries_sanrafael.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "San Rafael", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "San Rafael", "latitude": 37.9735, "longitude": -122.5311}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 37.9735, "query_longitude": -122.5311, "station_ids": ["9415071"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9415071"}),
            Action(name="store_water_levels", kwargs={"station_id": "9415071", "timestamps": ["2025-04-03T01:00:00Z"], "water_level_m": [0.96], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9415071", "timestamps": ["2025-04-03T01:00:00Z"], "tide_pred_m": [1.02], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_sanrafael.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_078",
        instruction=(
            "You must record a Vallejo intake baseline. End state: configuration shows target_city 'Vallejo' (UTC); "
            "geocoding places 38.1041,-122.2566; a proximity record includes '9415142' set primary; observed water levels include "
            "'2025-04-03T02:00:00Z' = 0.94 (m); tide predictions include '2025-04-03T02:00:00Z' = 1.00 (m); and a processed artifact "
            "at 'processed_data/merged_timeseries_vallejo.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Vallejo", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Vallejo", "latitude": 38.1041, "longitude": -122.2566}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 38.1041, "query_longitude": -122.2566, "station_ids": ["9415142"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9415142"}),
            Action(name="store_water_levels", kwargs={"station_id": "9415142", "timestamps": ["2025-04-03T02:00:00Z"], "water_level_m": [0.94], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9415142", "timestamps": ["2025-04-03T02:00:00Z"], "tide_pred_m": [1.00], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_vallejo.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_079",
        instruction=(
            "You must capture a Port Hueneme intake baseline. End state: configuration lists target_city 'Port Hueneme' (UTC); "
            "geocoding anchors 34.1478,-119.1951; a proximity record includes '9411230' set primary; observed water levels include "
            "'2025-04-03T03:00:00Z' = 0.93 (m); tide predictions include '2025-04-03T03:00:00Z' = 0.99 (m); and a merged artifact "
            "exists at 'processed_data/merged_timeseries_porthueneme.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Port Hueneme", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Port Hueneme", "latitude": 34.1478, "longitude": -119.1951}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 34.1478, "query_longitude": -119.1951, "station_ids": ["9411230"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9411230"}),
            Action(name="store_water_levels", kwargs={"station_id": "9411230", "timestamps": ["2025-04-03T03:00:00Z"], "water_level_m": [0.93], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9411230", "timestamps": ["2025-04-03T03:00:00Z"], "tide_pred_m": [0.99], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_porthueneme.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_080",
        instruction=(
            "You must register an Oxnard intake baseline. Final state: configuration shows target_city 'Oxnard' (UTC); "
            "geocoding places 34.1975,-119.1771; a proximity result includes '9411231' which you set primary; observed water levels "
            "include '2025-04-03T04:00:00Z' = 0.95 (m); tide predictions include '2025-04-03T04:00:00Z' = 1.01 (m); and a processed artifact "
            "at 'processed_data/merged_timeseries_oxnard.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Oxnard", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Oxnard", "latitude": 34.1975, "longitude": -119.1771}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 34.1975, "query_longitude": -119.1771, "station_ids": ["9411231"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9411231"}),
            Action(name="store_water_levels", kwargs={"station_id": "9411231", "timestamps": ["2025-04-03T04:00:00Z"], "water_level_m": [0.95], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9411231", "timestamps": ["2025-04-03T04:00:00Z"], "tide_pred_m": [1.01], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_oxnard.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_081",
        instruction=(
            "You must capture a Carpinteria intake baseline. End state: configuration lists target_city 'Carpinteria' (UTC); "
            "geocoding anchors 34.3989,-119.5185; a proximity record includes '9411370' set primary; observed water levels include "
            "'2025-04-04T00:00:00Z' = 0.90 (m); tide predictions include '2025-04-04T00:00:00Z' = 0.96 (m); and a merged artifact "
            "exists at 'processed_data/merged_timeseries_carpinteria.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Carpinteria", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Carpinteria", "latitude": 34.3989, "longitude": -119.5185}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 34.3989, "query_longitude": -119.5185, "station_ids": ["9411370"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9411370"}),
            Action(name="store_water_levels", kwargs={"station_id": "9411370", "timestamps": ["2025-04-04T00:00:00Z"], "water_level_m": [0.90], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9411370", "timestamps": ["2025-04-04T00:00:00Z"], "tide_pred_m": [0.96], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_carpinteria.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_082",
        instruction=(
            "You must capture a Malibu intake baseline. End state: configuration shows target_city 'Malibu' (UTC); "
            "geocoding places 34.0259,-118.7798; a proximity record includes '9410844' set primary; observed water levels include "
            "'2025-04-04T01:00:00Z' = 1.04 (m); tide predictions include '2025-04-04T01:00:00Z' = 1.10 (m); and a processed artifact "
            "at 'processed_data/merged_timeseries_malibu.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Malibu", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Malibu", "latitude": 34.0259, "longitude": -118.7798}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 34.0259, "query_longitude": -118.7798, "station_ids": ["9410844"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9410844"}),
            Action(name="store_water_levels", kwargs={"station_id": "9410844", "timestamps": ["2025-04-04T01:00:00Z"], "water_level_m": [1.04], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9410844", "timestamps": ["2025-04-04T01:00:00Z"], "tide_pred_m": [1.10], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_malibu.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_083",
        instruction=(
            "You must register a Dana Point intake baseline. End state: configuration shows target_city 'Dana Point' (UTC); "
            "geocoding anchors 33.4669,-117.6981; a proximity record includes '9410667' set primary; observed water levels include "
            "'2025-04-05T00:00:00Z' = 1.00 (m); tide predictions include '2025-04-05T00:00:00Z' = 1.06 (m); and a merged artifact "
            "exists at 'processed_data/merged_timeseries_danapoint.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Dana Point", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Dana Point", "latitude": 33.4669, "longitude": -117.6981}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 33.4669, "query_longitude": -117.6981, "station_ids": ["9410667"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9410667"}),
            Action(name="store_water_levels", kwargs={"station_id": "9410667", "timestamps": ["2025-04-05T00:00:00Z"], "water_level_m": [1.00], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9410667", "timestamps": ["2025-04-05T00:00:00Z"], "tide_pred_m": [1.06], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_danapoint.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_084",
        instruction=(
            "You must capture a Del Mar intake baseline. End state: configuration shows target_city 'Del Mar' (UTC); "
            "geocoding places 32.9595,-117.2653; a proximity record includes '9410240' set primary; observed water levels include "
            "'2025-04-05T01:00:00Z' = 1.03 (m); tide predictions include '2025-04-05T01:00:00Z' = 1.09 (m); and a processed artifact "
            "exists at 'processed_data/merged_timeseries_delmar.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Del Mar", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Del Mar", "latitude": 32.9595, "longitude": -117.2653}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 32.9595, "query_longitude": -117.2653, "station_ids": ["9410240"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9410240"}),
            Action(name="store_water_levels", kwargs={"station_id": "9410240", "timestamps": ["2025-04-05T01:00:00Z"], "water_level_m": [1.03], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9410240", "timestamps": ["2025-04-05T01:00:00Z"], "tide_pred_m": [1.09], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_delmar.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_085",
        instruction=(
            "You must record an Imperial Beach intake baseline. End state: configuration lists target_city 'Imperial Beach' (UTC); "
            "geocoding anchors 32.5839,-117.1131; a proximity result includes '9410055' set primary; observed water levels include "
            "'2025-04-05T02:00:00Z' = 0.98 (m); tide predictions include '2025-04-05T02:00:00Z' = 1.04 (m); and a processed artifact "
            "at 'processed_data/merged_timeseries_imperialbeach.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Imperial Beach", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Imperial Beach", "latitude": 32.5839, "longitude": -117.1131}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 32.5839, "query_longitude": -117.1131, "station_ids": ["9410055"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9410055"}),
            Action(name="store_water_levels", kwargs={"station_id": "9410055", "timestamps": ["2025-04-05T02:00:00Z"], "water_level_m": [0.98], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9410055", "timestamps": ["2025-04-05T02:00:00Z"], "tide_pred_m": [1.04], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_imperialbeach.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_086",
        instruction=(
            "You must assemble a Berkeley modeling bundle. Final state: features at 'processed_data/features_berk.csv' "
            "with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-04-06T09:05:00Z'); "
            "config at 'processed_data/model_config_berk.json' with classification_threshold_m 0.59 (created_ts '2025-04-06T09:06:00Z'); "
            "split summary at 'processed_data/split_berk.json'; model 'berk_lr_v1' at 'models/berk_lr_v1.joblib'; predictions at "
            "'processed_data/preds_berk_lr_v1.csv' (generated_ts '2025-04-06T10:30:00Z'); metrics at "
            "'processed_data/metrics_berk_lr_v1.csv' (auc 0.71); and stakeholder references to those artifacts."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_berk.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-04-06T09:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_berk.json", "classification_threshold_m_nullable": 0.59, "created_ts": "2025-04-06T09:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_berk.json"}),
            Action(name="register_model", kwargs={"model_name": "berk_lr_v1", "model_path": "models/berk_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "berk_lr_v1", "predictions_csv_path": "processed_data/preds_berk_lr_v1.csv", "generated_ts": "2025-04-06T10:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "berk_lr_v1", "metrics_csv_path": "processed_data/metrics_berk_lr_v1.csv", "auc_nullable": 0.71}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_berk_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_berk_lr_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_087",
        instruction=(
            "You must assemble a Vallejo modeling bundle. End state: features at 'processed_data/features_val.csv' "
            "(generated_ts '2025-04-08T09:05:00Z'); config at 'processed_data/model_config_val.json' with "
            "classification_threshold_m 0.58 (created_ts '2025-04-08T09:06:00Z'); split at 'processed_data/split_val.json'; "
            "model 'val_lr_v1' at 'models/val_lr_v1.joblib'; predictions at 'processed_data/preds_val_lr_v1.csv' "
            "(generated_ts '2025-04-08T10:30:00Z'); metrics at 'processed_data/metrics_val_lr_v1.csv' (auc 0.70); and stakeholder references."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_val.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-04-08T09:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_val.json", "classification_threshold_m_nullable": 0.58, "created_ts": "2025-04-08T09:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_val.json"}),
            Action(name="register_model", kwargs={"model_name": "val_lr_v1", "model_path": "models/val_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "val_lr_v1", "predictions_csv_path": "processed_data/preds_val_lr_v1.csv", "generated_ts": "2025-04-08T10:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "val_lr_v1", "metrics_csv_path": "processed_data/metrics_val_lr_v1.csv", "auc_nullable": 0.70}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_val_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_val_lr_v1.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_088",
        instruction=(
            "You must compile a Port Hueneme modeling bundle. End state: features at 'processed_data/features_ph.csv' "
            "(generated_ts '2025-04-09T09:05:00Z'); config at 'processed_data/model_config_ph.json' with "
            "classification_threshold_m 0.57 (created_ts '2025-04-09T09:06:00Z'); split at 'processed_data/split_ph.json'; "
            "model 'ph_lr_v1' at 'models/ph_lr_v1.joblib'; predictions at 'processed_data/preds_ph_lr_v1.csv' "
            "(generated_ts '2025-04-09T10:30:00Z'); metrics at 'processed_data/metrics_ph_lr_v1.csv' (accuracy 0.67); and stakeholder references."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_ph.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-04-09T09:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_ph.json", "classification_threshold_m_nullable": 0.57, "created_ts": "2025-04-09T09:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_ph.json"}),
            Action(name="register_model", kwargs={"model_name": "ph_lr_v1", "model_path": "models/ph_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "ph_lr_v1", "predictions_csv_path": "processed_data/preds_ph_lr_v1.csv", "generated_ts": "2025-04-09T10:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "ph_lr_v1", "metrics_csv_path": "processed_data/metrics_ph_lr_v1.csv", "accuracy_nullable": 0.67}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_ph_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_ph_lr_v1.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_089",
        instruction=(
            "You must assemble a Malibu modeling bundle. End state: features at 'processed_data/features_mal.csv' "
            "(generated_ts '2025-04-10T09:05:00Z'); config at 'processed_data/model_config_mal.json' with "
            "classification_threshold_m 0.60 (created_ts '2025-04-10T09:06:00Z'); split at 'processed_data/split_mal.json'; "
            "model 'mal_rf_v1' (type 'random_forest') at 'models/mal_rf_v1.joblib'; predictions at "
            "'processed_data/preds_mal_rf_v1.csv' (generated_ts '2025-04-10T10:30:00Z'); metrics at "
            "'processed_data/metrics_mal_rf_v1.csv' (auc 0.72); and stakeholder references."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_mal.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-04-10T09:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_mal.json", "classification_threshold_m_nullable": 0.60, "created_ts": "2025-04-10T09:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_mal.json"}),
            Action(name="register_model", kwargs={"model_name": "mal_rf_v1", "model_path": "models/mal_rf_v1.joblib", "model_type": "random_forest"}),
            Action(name="store_predictions", kwargs={"model_name": "mal_rf_v1", "predictions_csv_path": "processed_data/preds_mal_rf_v1.csv", "generated_ts": "2025-04-10T10:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "mal_rf_v1", "metrics_csv_path": "processed_data/metrics_mal_rf_v1.csv", "auc_nullable": 0.72}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_mal_rf_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_mal_rf_v1.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_090",
        instruction=(
            "You must register an SF Bay meta‑model bundle. End state: features at 'processed_data/features_sfbay_meta.csv' "
            "with ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa'] (generated_ts '2025-04-11T09:05:00Z'); "
            "config at 'processed_data/model_config_sfbay_meta.json' with classification_threshold_m 0.60 "
            "(created_ts '2025-04-11T09:06:00Z'); split summary at 'processed_data/split_sfbay_meta.json'; model 'sfbay_meta_v1' "
            "at 'models/sfbay_meta_v1.joblib'; predictions at 'processed_data/preds_sfbay_meta_v1.csv' (generated_ts '2025-04-11T10:30:00Z'); "
            "metrics at 'processed_data/metrics_sfbay_meta_v1.csv' (accuracy 0.72); and stakeholder references."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_sfbay_meta.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-04-11T09:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_sfbay_meta.json", "classification_threshold_m_nullable": 0.60, "created_ts": "2025-04-11T09:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_sfbay_meta.json"}),
            Action(name="register_model", kwargs={"model_name": "sfbay_meta_v1", "model_path": "models/sfbay_meta_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "sfbay_meta_v1", "predictions_csv_path": "processed_data/preds_sfbay_meta_v1.csv", "generated_ts": "2025-04-11T10:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "sfbay_meta_v1", "metrics_csv_path": "processed_data/metrics_sfbay_meta_v1.csv", "accuracy_nullable": 0.72}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_sfbay_meta_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_sfbay_meta_v1.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_091",
        instruction=(
            "You must compile a Richmond modeling bundle. End state: features at 'processed_data/features_rich.csv' "
            "(generated_ts '2025-04-12T09:05:00Z'); config at 'processed_data/model_config_rich.json' with "
            "classification_threshold_m 0.58 (created_ts '2025-04-12T09:06:00Z'); split at 'processed_data/split_rich.json'; "
            "model 'rich_lr_v1' at 'models/rich_lr_v1.joblib'; predictions at 'processed_data/preds_rich_lr_v1.csv' "
            "(generated_ts '2025-04-12T10:30:00Z'); metrics at 'processed_data/metrics_rich_lr_v1.csv' (auc 0.71); and stakeholder references."
        ),
        actions=[
            Action(name="store_features", kwargs={"csv_path": "processed_data/features_rich.csv", "feature_names": ["precip_24h_mm","tide_anomaly_6h_max_m","pressure_drop_6h_hpa"], "generated_ts": "2025-04-12T09:05:00Z"}),
            Action(name="write_model_config", kwargs={"saved_json_path": "processed_data/model_config_rich.json", "classification_threshold_m_nullable": 0.58, "created_ts": "2025-04-12T09:06:00Z"}),
            Action(name="create_time_based_split", kwargs={"split_summary_json_path": "processed_data/split_rich.json"}),
            Action(name="register_model", kwargs={"model_name": "rich_lr_v1", "model_path": "models/rich_lr_v1.joblib"}),
            Action(name="store_predictions", kwargs={"model_name": "rich_lr_v1", "predictions_csv_path": "processed_data/preds_rich_lr_v1.csv", "generated_ts": "2025-04-12T10:30:00Z"}),
            Action(name="store_metrics", kwargs={"model_name": "rich_lr_v1", "metrics_csv_path": "processed_data/metrics_rich_lr_v1.csv", "auc_nullable": 0.71}),
            Action(name="record_stakeholder_outputs", kwargs={"predictions_final_csv_path": "processed_data/preds_rich_lr_v1.csv", "metrics_summary_csv_path": "processed_data/metrics_rich_lr_v1.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_092",
        instruction=(
            "You must prepare stakeholder reporting for Berkeley (2025-04-10). End state: a page 'PAGE-20250410-BERK' titled "
            "'Berkeley Flood Risk - 2025-04-10' exists (created_ts '2025-04-10T09:00:00Z'); sections "
            "['Summary','Results','Actions'] are present (updated_ts '2025-04-10T09:05:00Z'); properties equal the exact JSON "
            "'{\"predictions\":\"processed_data/preds_berk_lr_v1.csv\",\"metrics\":\"processed_data/metrics_berk_lr_v1.csv\",\"figure\":\"figures/qc/berkeley_overview.png\"}' "
            "(updated_ts '2025-04-10T09:10:00Z'); and an email draft 'DRAFT-20250410-BERK' to ['publicworks@cityofberkeley.info'] is sent as "
            "'MSG-20250410-BERK' (draft '2025-04-10T09:20:00Z', sent '2025-04-10T09:25:00Z')."
        ),
        actions=[
            Action(name="notion_create_page", kwargs={"page_id": "PAGE-20250410-BERK", "title": "Berkeley Flood Risk - 2025-04-10", "created_ts": "2025-04-10T09:00:00Z"}),
            Action(name="notion_append_sections", kwargs={"page_id": "PAGE-20250410-BERK", "sections": ["Summary","Results","Actions"], "updated_ts": "2025-04-10T09:05:00Z"}),
            Action(name="notion_update_page_properties", kwargs={
                "page_id": "PAGE-20250410-BERK",
                "properties_json": '{"predictions":"processed_data/preds_berk_lr_v1.csv","metrics":"processed_data/metrics_berk_lr_v1.csv","figure":"figures/qc/berkeley_overview.png"}',
                "updated_ts": "2025-04-10T09:10:00Z"
            }),
            Action(name="gmail_draft_email", kwargs={"draft_id": "DRAFT-20250410-BERK", "subject": "Berkeley Flood Risk - 2025-04-10", "recipients": ["publicworks@cityofberkeley.info"], "attachments_paths": ["figures/qc/berkeley_overview.png"], "created_ts": "2025-04-10T09:20:00Z"}),
            Action(name="gmail_send_email", kwargs={"draft_id": "DRAFT-20250410-BERK", "message_id": "MSG-20250410-BERK", "sent_ts": "2025-04-10T09:25:00Z"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_093",
        instruction=(
            "You must prepare stakeholder reporting for Oakland (2025-04-11). End state: a page 'PAGE-20250411-OAK' titled "
            "'Oakland Flood Risk - 2025-04-11' exists (created_ts '2025-04-11T09:00:00Z'); sections "
            "['Summary','Drivers','Next Steps'] are present (updated_ts '2025-04-11T09:05:00Z'); properties equal the exact JSON "
            "'{\"predictions\":\"processed_data/preds_oak_rf_v1.csv\",\"metrics\":\"processed_data/metrics_oak_rf_v1.csv\",\"figure\":\"figures/qc/oak_overview.png\"}' "
            "(updated_ts '2025-04-11T09:10:00Z'); and an email draft 'DRAFT-20250411-OAK' to ['resilience@oaklandca.gov'] is sent as "
            "'MSG-20250411-OAK' (draft '2025-04-11T09:20:00Z', sent '2025-04-11T09:25:00Z')."
        ),
        actions=[
            Action(name="notion_create_page", kwargs={"page_id": "PAGE-20250411-OAK", "title": "Oakland Flood Risk - 2025-04-11", "created_ts": "2025-04-11T09:00:00Z"}),
            Action(name="notion_append_sections", kwargs={"page_id": "PAGE-20250411-OAK", "sections": ["Summary","Drivers","Next Steps"], "updated_ts": "2025-04-11T09:05:00Z"}),
            Action(name="notion_update_page_properties", kwargs={
                "page_id": "PAGE-20250411-OAK",
                "properties_json": '{"predictions":"processed_data/preds_oak_rf_v1.csv","metrics":"processed_data/metrics_oak_rf_v1.csv","figure":"figures/qc/oak_overview.png"}',
                "updated_ts": "2025-04-11T09:10:00Z"
            }),
            Action(name="gmail_draft_email", kwargs={"draft_id": "DRAFT-20250411-OAK", "subject": "Oakland Flood Risk - 2025-04-11", "recipients": ["resilience@oaklandca.gov"], "attachments_paths": ["figures/qc/oak_overview.png"], "created_ts": "2025-04-11T09:20:00Z"}),
            Action(name="gmail_send_email", kwargs={"draft_id": "DRAFT-20250411-OAK", "message_id": "MSG-20250411-OAK", "sent_ts": "2025-04-11T09:25:00Z"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_094",
        instruction=(
            "You must publish release notes for the SF Bay model bundle (2025-04-12). End state: page 'PAGE-20250412-SFBAY-REL' "
            "titled 'SF Bay Release - 2025-04-12' exists (created_ts '2025-04-12T09:00:00Z'); sections "
            "['Release Notes','Changelog','Artifacts'] are present (updated_ts '2025-04-12T09:05:00Z'); properties JSON is set to "
            "'{\"model\":\"models/sfbay_meta_v1.joblib\",\"predictions\":\"processed_data/preds_sfbay_meta_v1.csv\",\"metrics\":\"processed_data/metrics_sfbay_meta_v1.csv\"}' "
            "(updated_ts '2025-04-12T09:10:00Z'); and an email to ['team@sfbaylab.org'] is sent as 'MSG-20250412-SFBAY-REL' "
            "(draft '2025-04-12T09:20:00Z', sent '2025-04-12T09:25:00Z')."
        ),
        actions=[
            Action(name="notion_create_page", kwargs={"page_id": "PAGE-20250412-SFBAY-REL", "title": "SF Bay Release - 2025-04-12", "created_ts": "2025-04-12T09:00:00Z"}),
            Action(name="notion_append_sections", kwargs={"page_id": "PAGE-20250412-SFBAY-REL", "sections": ["Release Notes","Changelog","Artifacts"], "updated_ts": "2025-04-12T09:05:00Z"}),
            Action(name="notion_update_page_properties", kwargs={
                "page_id": "PAGE-20250412-SFBAY-REL",
                "properties_json": '{"model":"models/sfbay_meta_v1.joblib","predictions":"processed_data/preds_sfbay_meta_v1.csv","metrics":"processed_data/metrics_sfbay_meta_v1.csv"}',
                "updated_ts": "2025-04-12T09:10:00Z"
            }),
            Action(name="gmail_draft_email", kwargs={"draft_id": "DRAFT-20250412-SFBAY-REL", "subject": "SF Bay Model Release - 2025-04-12", "recipients": ["team@sfbaylab.org"], "created_ts": "2025-04-12T09:20:00Z"}),
            Action(name="gmail_send_email", kwargs={"draft_id": "DRAFT-20250412-SFBAY-REL", "message_id": "MSG-20250412-SFBAY-REL", "sent_ts": "2025-04-12T09:25:00Z"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_095",
        instruction=(
            "You must register literature for 'coastal inundation LiDAR'. End state: search query "
            "'coastal inundation LiDAR' lists result_item_ids ['ZOT-6001','ZOT-6005'] with search_ts '2025-04-12T12:00:00Z'; "
            "metadata titles ['Smith 2020 LiDAR Coastal Mapping','Lee 2022 High-Res DEMs'] with fetched_ts '2025-04-12T12:10:00Z'; "
            "fulltext paths ['docs/lit/6001.pdf','docs/lit/6005.pdf'] with fetched_ts '2025-04-12T12:12:00Z'; and a manifest at "
            "'docs/lit/manifest_lidar.txt' contains 'LiDAR inundation mapping references'."
        ),
        actions=[
            Action(name="zotero_search_items", kwargs={"query": "coastal inundation LiDAR", "result_item_ids": ["ZOT-6001", "ZOT-6005"], "search_ts": "2025-04-12T12:00:00Z"}),
            Action(name="zotero_item_metadata", kwargs={"item_ids": ["ZOT-6001", "ZOT-6005"], "titles": ["Smith 2020 LiDAR Coastal Mapping", "Lee 2022 High-Res DEMs"], "fetched_ts": "2025-04-12T12:10:00Z"}),
            Action(name="zotero_item_fulltext", kwargs={"item_ids": ["ZOT-6001", "ZOT-6005"], "file_paths": ["docs/lit/6001.pdf", "docs/lit/6005.pdf"], "fetched_ts": "2025-04-12T12:12:00Z"}),
            Action(name="write_file_text", kwargs={"path": "docs/lit/manifest_lidar.txt", "content": "LiDAR inundation mapping references"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_096",
        instruction=(
            "You must record literature for 'ensemble downscaling coastal extremes'. End state: a search record with query "
            "'ensemble downscaling coastal extremes' lists ['ZOT-6101','ZOT-6108'] (search_ts '2025-04-12T12:20:00Z'); metadata "
            "has titles ['Martinez 2020 Downscaling Extremes','Zhao 2023 Multi‑Model Coastal Ensemble'] (fetched_ts '2025-04-12T12:30:00Z'); "
            "fulltexts at ['docs/lit/6101.pdf','docs/lit/6108.pdf'] (fetched_ts '2025-04-12T12:32:00Z'); and a manifest "
            "'docs/lit/manifest_downscaling.txt' contains 'ensemble downscaling references'."
        ),
        actions=[
            Action(name="zotero_search_items", kwargs={"query": "ensemble downscaling coastal extremes", "result_item_ids": ["ZOT-6101", "ZOT-6108"], "search_ts": "2025-04-12T12:20:00Z"}),
            Action(name="zotero_item_metadata", kwargs={"item_ids": ["ZOT-6101", "ZOT-6108"], "titles": ["Martinez 2020 Downscaling Extremes", "Zhao 2023 Multi-Model Coastal Ensemble"], "fetched_ts": "2025-04-12T12:30:00Z"}),
            Action(name="zotero_item_fulltext", kwargs={"item_ids": ["ZOT-6101", "ZOT-6108"], "file_paths": ["docs/lit/6101.pdf", "docs/lit/6108.pdf"], "fetched_ts": "2025-04-12T12:32:00Z"}),
            Action(name="write_file_text", kwargs={"path": "docs/lit/manifest_downscaling.txt", "content": "ensemble downscaling references"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_097",
        instruction=(
            "You must capture a Marin City intake baseline. End state: configuration shows target_city 'Marin City' (UTC); "
            "geocoding anchors 37.8686,-122.5089; a proximity record includes '9414255' set primary; observed water levels include "
            "'2025-04-14T00:00:00Z' = 0.95 (m); tide predictions include '2025-04-14T00:00:00Z' = 1.01 (m); and a processed artifact "
            "exists at 'processed_data/merged_timeseries_marincity.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Marin City", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Marin City", "latitude": 37.8686, "longitude": -122.5089}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 37.8686, "query_longitude": -122.5089, "station_ids": ["9414255"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9414255"}),
            Action(name="store_water_levels", kwargs={"station_id": "9414255", "timestamps": ["2025-04-14T00:00:00Z"], "water_level_m": [0.95], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9414255", "timestamps": ["2025-04-14T00:00:00Z"], "tide_pred_m": [1.01], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_marincity.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_098",
        instruction=(
            "You must record a Richmond intake baseline. End state: configuration shows target_city 'Richmond' (UTC); "
            "geocoding places 37.9358,-122.3477; a proximity record includes '9414763' set primary; observed water levels include "
            "'2025-04-14T01:00:00Z' = 0.97 (m); tide predictions include '2025-04-14T01:00:00Z' = 1.03 (m); and a processed artifact "
            "at 'processed_data/merged_timeseries_richmond.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Richmond", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Richmond", "latitude": 37.9358, "longitude": -122.3477}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 37.9358, "query_longitude": -122.3477, "station_ids": ["9414763"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9414763"}),
            Action(name="store_water_levels", kwargs={"station_id": "9414763", "timestamps": ["2025-04-14T01:00:00Z"], "water_level_m": [0.97], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9414763", "timestamps": ["2025-04-14T01:00:00Z"], "tide_pred_m": [1.03], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_richmond.csv"}),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="ds_v1_099",
        instruction=(
            "You must capture a San Francisco intake baseline. End state: configuration lists target_city 'San Francisco' (UTC); "
            "geocoding anchors 37.7749,-122.4194; a proximity record includes '9414292' set primary; observed water levels include "
            "'2025-04-15T00:00:00Z' = 1.06 (m); tide predictions include '2025-04-15T00:00:00Z' = 1.12 (m); and a processed artifact "
            "exists at 'processed_data/merged_timeseries_sf.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "San Francisco", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "San Francisco", "latitude": 37.7749, "longitude": -122.4194}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 37.7749, "query_longitude": -122.4194, "station_ids": ["9414292"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9414292"}),
            Action(name="store_water_levels", kwargs={"station_id": "9414292", "timestamps": ["2025-04-15T00:00:00Z"], "water_level_m": [1.06], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9414292", "timestamps": ["2025-04-15T00:00:00Z"], "tide_pred_m": [1.12], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_sf.csv"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="ds_v1_100",
        instruction=(
            "You must establish an Astoria intake baseline. End state: configuration shows target_city 'Astoria' (timezone 'UTC'); "
            "geocoding places 'Astoria' at 46.1879,-123.8313; a proximity result at those coordinates includes station '9439040' "
            "which is set primary; observed water levels for '9439040' include '2025-05-01T00:00:00Z' = 1.03 (m); tide predictions "
            "include '2025-05-01T00:00:00Z' = 1.10 (m); and a processed artifact exists at 'processed_data/merged_timeseries_astoria.csv'."
        ),
        actions=[
            Action(name="set_project_config", kwargs={"target_city": "Astoria", "timezone_default": "UTC"}),
            Action(name="store_geocoding_result", kwargs={"query_city": "Astoria", "latitude": 46.1879, "longitude": -123.8313}),
            Action(name="store_noaa_station_search", kwargs={"query_latitude": 46.1879, "query_longitude": -123.8313, "station_ids": ["9439040"]}),
            Action(name="set_primary_station", kwargs={"station_id": "9439040"}),
            Action(name="store_water_levels", kwargs={"station_id": "9439040", "timestamps": ["2025-05-01T00:00:00Z"], "water_level_m": [1.03], "units": "m"}),
            Action(name="store_tide_predictions", kwargs={"station_id": "9439040", "timestamps": ["2025-05-01T00:00:00Z"], "tide_pred_m": [1.10], "units": "m"}),
            Action(name="compute_and_store_merged_timeseries", kwargs={"csv_path": "processed_data/merged_timeseries_astoria.csv"}),
        ],
        outputs=[],
    ),
]
