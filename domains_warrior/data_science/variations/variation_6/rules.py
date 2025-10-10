RULES = [
    # Merge Window Protocol (MWP)
    "Merge Window Protocol (MWP): Given (city, station_id, analysis window [start_ts,end_ts], water-level lookback [lookback_start, analysis_start]) the assistant must: "
    "(1) obtain weather forecasts for the city covering the analysis window from weather_forecasts; "
    "(2) obtain tide predictions for the station_id covering the analysis window from tide_predictions; "
    "(3) obtain observed water levels for the station_id covering the lookback window from water_levels; "
    "(4) create a single ETL run record in etl_runs that canonically summarizes these inputs and one merged output artifact.",
    "MWP canonical derivations (deterministic): "
    "city_slug := canonical slug for the city (use mapping in tools); "
    "run_id := f\"etl_{city_slug}_{start_ts[:10].replace('-','')}_{end_ts[:10].replace('-','')}_merge_v1\"; "
    "input_paths := [f\"/data/raw/weather_{city_slug}_{start_ts[:10].replace('-','')}.json\", f\"/data/raw/tide_pred_{station_id}.json\", f\"/data/raw/water_levels_{station_id}.json\"]; "
    "output_paths := [f\"/processed_data/merged_timeseries_{city_slug}_{start_ts[:10].replace('-','')}_{end_ts[:10].replace('-','')}.csv\"]; "
    "started_ts='2024-03-16T14:00:00Z', finished_ts_nullable='2024-03-16T14:22:00Z'. The instructions may overwrite started_ts and finished_ts_nullable, messages and required outputs when specified in the task instruction."
    "messages := [f\"Merged weather and tide predictions for {start_ts[:10]}..{end_ts[:10]}.\", f\"Attached observed water levels lookback {lookback_start[:10]}..{analysis_start[:10]}.\", \"Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa.\"]; "
    "The ETL record must include only: run_id, input_paths, output_paths, started_ts, finished_ts_nullable, messages. Do not include any other fields.",
    # Split Protocol (SP)
    "Split Protocol (SP): Given (city, method, test_fraction, split_ts), the assistant must: "
    "(1) resolve the canonical processed timeseries path as /data/processed/timeseries_{city_slug}_weather.csv; "
    "(2) read its total row_count from processed_timeseries; "
    "(3) compute train_index_count = floor(row_count * (1 - test_fraction)) and test_index_count = row_count - train_index_count; "
    "(4) derive split_summary_json_path = f\"/data/splits/{city_slug}_{method}_split_{split_ts[:10].replace('-', '')}.json\"; "
    "(5) write a record into dataset_split with exactly: {method, test_fraction, train_index_count, test_index_count, split_summary_json_path, split_ts}. "
    "The assistant must not invent any other fields.",
    # Feature Validation Protocol (FVP)
    "Feature Validation Protocol (FVP): Given (city, model_name), the assistant must: (1) resolve the canonical city_slug; (2) read the model's required feature_names from models; (3) read available feature columns and created_ts from /processed_data/features.csv; (4) compute present and missing feature sets, counts, and coverage = present/required; (5) create one ETL run record in etl_runs that summarizes inputs and one output artifact.",
    "FVP canonical derivations:",
    "city_slug := canonical slug for the city.",
    "features_csv_path := '/processed_data/features.csv'.",
    "ymd := created_ts[:10].replace('-', '').",
    "run_id := f'fv_{city_slug}_{model_name}_{ymd}_v1'.",
    "feature_validation_json_path := f'/processed_data/feature_validation_{city_slug}_{model_name}_{ymd}.json'.",
    "started_ts='2024-03-17T10:20:00Z', finished_ts_nullable='2024-03-17T10:25:00Z'. The instructions may overwrite started_ts and finished_ts_nullable, messages and required outputs when specified in the task instruction.",
    "messages := three strings that state (a) present/required counts, (b) sorted missing feature names or 'none', (c) validated file path.",
    "The ETL record must include only: run_id, input_paths, output_paths, started_ts, finished_ts_nullable, messages. Do not include any other fields.",
    "FVP messages must be exactly three strings: (1) 'Feature validation for {model_name}: {present_count}/{required_count} required features present.' (2) 'Missing features: ' followed by the missing feature names sorted lexicographically and separated by ', ' or 'none' if empty. (3) 'Validated file: {feature_validation_json_path}'.",
    # Model Training & Evaluation Protocol (MTP)
    "Model Training & Evaluation Protocol (MTP): Given (city, station_id, model_name, analysis window [start_ts,end_ts], split_ts), the assistant must: (1) resolve canonical city_slug; (2) create one ETL run record in etl_runs summarizing inputs and outputs for a deterministic training/evaluation; (3) report stored model metrics without recomputation.",
    "MTP canonical derivations:",
    "city_slug := canonical slug for the city.",
    "run_id := f\"mt_{city_slug}_{model_name}_{start_ts[:10].replace('-','')}_{end_ts[:10].replace('-','')}_v1\";",
    "input_paths := [f\"/processed_data/merged_timeseries_{city_slug}_{start_ts[:10].replace('-','')}_{end_ts[:10].replace('-','')}.csv\", \"/processed_data/features.csv\", f\"/data/splits/{city_slug}_time_based_split_{split_ts[:10].replace('-', '')}.json\"];",
    "output_paths := [f\"/models/{model_name}.pkl\", f\"/processed_data/metrics_summary_{model_name}_{end_ts[:10].replace('-','')}.csv\"];",
    "started_ts='2024-03-17T09:30:00Z', finished_ts_nullable='2024-03-17T11:15:00Z'. The instructions may overwrite started_ts and finished_ts_nullable, messages and required outputs when specified in the task instruction.",
    "messages := [\"Training samples: 134\", \"Test samples: 34\", f\"Model saved to: /models/{model_name}.pkl\"];",
    "The ETL record must include only: run_id, input_paths, output_paths, started_ts, finished_ts_nullable, messages. Do not include any other fields.",
    "MTP messages must be exactly three strings: 'Training samples: {train}', 'Test samples: {test}', 'Model saved to: {model_path}'."
]
