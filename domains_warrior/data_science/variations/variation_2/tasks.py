from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="task_1",
        instruction=(
            "You are a data-science automation agent. Compile the current status for San Francisco "
            "by applying the City Status Compilation Protocol using model simple_model."
            "Use 2024-03-17T10:45:00Z as the printed timestamp for the terminal log entry and the processed dataset summary from the CSV located at /data/processed/timeseries_sf_weather.csv."
        ),
        actions=[
            Action(name="get_project_config_by_city",
                   kwargs={"target_city": "San Francisco"}),
            Action(name="get_geocoding_result_by_city",
                   kwargs={"query_city": "San Francisco"}),
            Action(
                name="get_stations_by_location",
                kwargs={"query_latitude": 37.7749,
                        "query_longitude": -122.4194, "radius_km": 50.0}
            ),
            Action(
                name="get_processed_timeseries_summary",
                kwargs={"csv_path": "/data/processed/timeseries_sf_weather.csv"}
            ),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(
                name="append_terminal_log_entry",
                kwargs={
                    "command": "status_compilation_san-francisco",
                    "exit_code": 0,
                    "stdout": "",
                    "stderr": "",
                    "printed_message": "status_compilation_san-francisco completed",
                    "printed_ts": "2024-03-17T10:45:00Z"
                }
            ),
        ],
        outputs=[{
            "city": "San Francisco",
            "primary_station_id": "9414290",
            "timeseries": {"csv_path": "/data/processed/timeseries_sf_weather.csv", "row_count": 168},
            "predictions": {
                "model_name": "simple_model",
                "csv_path": "/processed_data/predictions_simple.csv",
                "row_count": 34,
                "columns": ["proba", "pred"]
            },
            "metrics": {"model_name": "simple_model", "auc": 0.79, "accuracy": 0.76},
            "logged": {
                "command": "status_compilation_san-francisco",
                "exit_code": 0,
                "printed_message": "status_compilation_san-francisco completed",
                "printed_ts": "2024-03-17T10:45:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_2",
        instruction=(
            "You are a data-science automation agent. Compile the current status for Boston by applying the City Status Compilation Protocol for the window 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z using model boston_harbor_model. Apply the following override: "
            "set the primary station to 8443970 only if the tide predictions method for that station is 'harmonic_analysis'; otherwise use 8447930. "
            "Return the model AUC and Accuracy and the predictions CSV path."
            "Use 2024-03-01T13:18:00Z as the printed timestamp for the terminal log entry and the processed dataset summary from the CSV located at /data/processed/timeseries_boston_weather.csv"

        ),
        actions=[
            Action(name="get_project_config_by_city",
                   kwargs={"target_city": "Boston"}),
            Action(name="get_geocoding_result_by_city",
                   kwargs={"query_city": "Boston"}),
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:18:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "primary_station_id": "8443970",
            "timeseries": {"csv_path": "/data/processed/timeseries_boston_weather.csv", "row_count": 120},
            "predictions": {
                "model_name": "boston_harbor_model",
                "csv_path": "/data/processed/predictions_boston.csv",
                "row_count": 24,
                "columns": ["proba", "pred"]
            },
            "metrics": {"model_name": "boston_harbor_model", "auc": 0.73, "accuracy": 0.81},
            "logged": {
                "command": "status_compilation_boston",
                "exit_code": 0,
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:18:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_3",
        instruction=(
            "You are a data-science automation agent. Select the best San Francisco model between flood_risk_sf_v1 and flood_risk_sf_v2 by applying the Model Variant Selection Protocol with this override: "
            "if the AUC difference is below 0.01, prefer the variant with the most recent metrics timestamp. Return the chosen model name and the predictions CSV path."
            "Use 2024-03-18T15:45:00Z as the printed timestamp for the terminal log entry."

        ),
        actions=[
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v1"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(
                name="append_terminal_log_entry",
                kwargs={
                    "command": "model_selection_san-francisco",
                    "exit_code": 0,
                    "stdout": "",
                    "stderr": "",
                    "printed_message": "model_selection_san-francisco completed",
                    "printed_ts": "2024-03-18T15:45:00Z"
                }
            ),
        ],
        outputs=[{
            "chosen_model_name": "flood_risk_sf_v2",
            "predictions_csv_path": "/results/predictions_sf_v2.csv"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_4",
        instruction=(
            "You are a data-science automation agent. Produce a risk snapshot for San Francisco by applying the City Risk Snapshot Protocol with this override: "
            "if water levels datum for station 9414290 is 'MLLW' in the window 2024-02-14T00:00:00Z to 2024-03-15T00:00:00Z, set the primary station to 9414290; otherwise use 9414750. "
            "Use the flood_risk_sf_v2 variant for the snapshot. Return the chosen station id, the model AUC and Accuracy, the predictions CSV path, "
            "and the processed dataset summary from the CSV located at /data/processed/timeseries_sf_weather.csv. "
            "Use 2024-03-18T15:45:00Z as the printed timestamp for the terminal log entry and the processed dataset summary from the CSV located at /data/processed/timeseries_sf_weather.csv."
        ),
        actions=[
            Action(
                name="get_stations_by_location",
                kwargs={"query_latitude": 37.7749,
                        "query_longitude": -122.4194, "radius_km": 50.0}
            ),
            Action(
                name="get_water_levels_window",
                kwargs={
                    "station_id": "9414290",
                    "window_start_ts": "2024-02-14T00:00:00Z",
                    "window_end_ts": "2024-03-15T00:00:00Z"
                }
            ),
            Action(
                name="get_processed_timeseries_summary",
                kwargs={"csv_path": "/data/processed/timeseries_sf_weather.csv"}
            ),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_sf_v2"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(
                name="append_terminal_log_entry",
                kwargs={
                    "command": "risk_snapshot_san-francisco",
                    "exit_code": 0,
                    "stdout": "",
                    "stderr": "",
                    "printed_message": "risk_snapshot_san-francisco completed",
                    "printed_ts": "2024-03-18T15:45:00Z"
                }
            ),
        ],
        outputs=[{
            "primary_station_id": "9414290",
            "metrics": {
                "auc": 0.89,
                "accuracy": 0.85
            },
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "csv_path": "/data/processed/timeseries_sf_weather.csv",
                "columns": [
                    "timestamp",
                    "tide_pred_m",
                    "wind_speed_ms",
                    "precipitation_mm_hr",
                    "pressure_hpa",
                    "temperature_c",
                    "high_risk_flag"
                ],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_5",
        instruction=(
            "You are a data-science automation agent. Produce a station confirmation snapshot for Miami by applying the Datum-and-Method Station Confirmation Protocol with this override: "
            "if the water levels datum for station 8723214 is 'NAVD88' in the window 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z but its tide predictions method in the window 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z is not 'harmonic', use backup station 8723170; otherwise keep 8723214. "
            "Use the flood_risk_miami_v1 variant. Return the chosen station id, the model AUC and Accuracy, the predictions CSV path, and the processed dataset summary from /data/processed/timeseries_miami_weather.csv (columns, row_count, min_timestamp, max_timestamp). "
            "Use the configured station search distance from project_config for Miami and use 2024-02-02T15:45:00Z as the printed timestamp for the terminal log entry. "
            "Use coordinates 25.7617,-80.1918 and radius 25.0 for the station search."
        ),
        actions=[
            # Candidate stations (deterministic coords + radius from project_config)
            Action(
                name="get_stations_by_location",
                kwargs={"query_latitude": 25.7617,
                        "query_longitude": -80.1918, "radius_km": 25.0}
            ),

            # Validate datum condition on 8723214
            Action(
                name="get_water_levels_window",
                kwargs={
                    "station_id": "8723214",
                    "window_start_ts": "2024-02-01T00:00:00Z",
                    "window_end_ts": "2024-02-02T00:00:00Z"
                }
            ),

            # Validate method condition on 8723214
            Action(
                name="get_tide_predictions_window",
                kwargs={
                    "station_id": "8723214",
                    "window_start_ts": "2024-02-01T00:00:00Z",
                    "window_end_ts": "2024-02-02T00:00:00Z"
                }
            ),

            # Summarize processed dataset (explicit CSV path from instruction)
            Action(
                name="get_processed_timeseries_summary",
                kwargs={"csv_path": "/data/processed/timeseries_miami_weather.csv"}
            ),

            # Retrieve model artifacts (Miami)
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_miami_v1"}),
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "flood_risk_miami_v1"}),

            # Deterministic terminal log
            Action(
                name="append_terminal_log_entry",
                kwargs={
                    "command": "dmsc_snapshot_miami",
                    "exit_code": 0,
                    "stdout": "",
                    "stderr": "",
                    "printed_message": "dmsc_snapshot_miami completed",
                    "printed_ts": "2024-02-02T15:45:00Z"
                }
            ),
        ],
        outputs=[{
            "chosen_station_id": "8723214",
            "metrics": {"auc": 0.73, "accuracy": 0.75},
            "predictions_csv_path": "/results/predictions_miami_v1.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "tide_pred_m",
                    "wind_speed_ms",
                    "precipitation_mm_hr",
                    "pressure_hpa",
                    "temperature_c"
                ],
                "row_count": 96,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-05T00:00:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_6",
        instruction=(
            "You are a data-science automation agent. Decide a promotion between San Francisco and Miami by applying the Cross-City AUC-Gap Promotion Protocol with these overrides: "
            "use an AUC gap threshold of 0.12; if the absolute AUC difference between flood_risk_sf_v2 and flood_risk_miami_v1 is below 0.12, prefer the city whose validated station condition passes; otherwise choose the city with higher AUC. "
            "For San Francisco, validate that tide predictions for station 9414290 use method 'harmonic' in the window 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z. "
            "For Miami, validate that water levels for station 8723214 have datum 'NAVD88' in the window 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z. "
            "Return the chosen city, the model AUC and Accuracy, the predictions CSV path, and the processed dataset summary from /data/processed/timeseries_<city>_weather.csv (columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "Use the configured station search distances from project_config and use 2024-03-18T15:45:00Z as the printed timestamp for the terminal log entry. "
            "Use coordinates 37.7749,-122.4194 and radius 50.0 for San Francisco and coordinates 25.7617,-80.1918 and radius 25.0 for Miami."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_sf_v2"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_miami_v1"}),
            # Action(name="get_predictions_by_model_name", kwargs={
            #     "model_name": "flood_risk_miami_v1"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(
                name="append_terminal_log_entry",
                kwargs={
                    "command": "ccap_promotion_san-francisco-miami",
                    "exit_code": 0,
                    "stdout": "",
                    "stderr": "",
                    "printed_message": "ccap_promotion_san-francisco-miami completed",
                    "printed_ts": "2024-03-18T15:45:00Z"
                }
            ),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "csv_path": "/data/processed/timeseries_sf_weather.csv",
                "columns": [
                    "timestamp",
                    "tide_pred_m",
                    "wind_speed_ms",
                    "precipitation_mm_hr",
                    "pressure_hpa",
                    "temperature_c",
                    "high_risk_flag"
                ],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_7",
        instruction=(
            "You are a data-science automation agent. Determine the primary station for Miami by applying the Primary Station Determination Protocol with this override: "
            "if water levels datum for station 8723214 is 'NAVD88' in the window 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z, select 8723214; otherwise select 8723170. "
            "Return the chosen station id, the model AUC and Accuracy for flood_risk_miami_v1, the predictions CSV path, and the processed dataset summary from /data/processed/timeseries_miami_weather.csv including columns, row_count, min_timestamp, and max_timestamp. "
            "Use coordinates 25.7617,-80.1918 with radius 25.0 for station search and use 2024-02-02T15:45:00Z as the printed timestamp for the terminal log entry."
        ),
        actions=[
            Action(
                name="get_stations_by_location",
                kwargs={"query_latitude": 25.7617,
                        "query_longitude": -80.1918, "radius_km": 25.0}
            ),
            Action(
                name="get_water_levels_window",
                kwargs={
                    "station_id": "8723214",
                    "window_start_ts": "2024-02-01T00:00:00Z",
                    "window_end_ts": "2024-02-02T00:00:00Z"
                }
            ),
            Action(
                name="get_processed_timeseries_summary",
                kwargs={"csv_path": "/data/processed/timeseries_miami_weather.csv"}
            ),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_miami_v1"}),
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "flood_risk_miami_v1"}),
            Action(
                name="append_terminal_log_entry",
                kwargs={
                    "command": "station_determination_miami",
                    "exit_code": 0,
                    "stdout": "",
                    "stderr": "",
                    "printed_message": "station_determination_miami completed",
                    "printed_ts": "2024-02-02T15:45:00Z"
                }
            ),
        ],
        outputs=[{
            "primary_station_id": "8723214",
            "metrics": {"auc": 0.73, "accuracy": 0.75},
            "predictions_csv_path": "/results/predictions_miami_v1.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "tide_pred_m",
                    "wind_speed_ms",
                    "precipitation_mm_hr",
                    "pressure_hpa",
                    "temperature_c"
                ],
                "row_count": 96,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-05T00:00:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_8",
        instruction=(
            "You are a data-science automation agent. Determine the primary station for Seattle by applying the Primary Station Determination Protocol with this override: "
            "if no dataset split timestamp exists for the city, use the processed dataset creation time as the printed timestamp for the terminal log entry. "
            "Validate station 9447130 against tide predictions for the window 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z before confirming selection. "
            "Return the chosen station id, the processed dataset CSV path and row_count, the processed dataset summary from /data/processed/timeseries_seattle_weather.csv and the terminal log confirmation fields {command, exit_code, printed_message, printed_ts}. "
            "Use coordinates 47.6062,-122.3321 with radius 60.0 for station search."
        ),
        actions=[
            Action(
                name="get_stations_by_location",
                kwargs={"query_latitude": 47.6062,
                        "query_longitude": -122.3321, "radius_km": 60.0}
            ),
            Action(
                name="get_tide_predictions_window",
                kwargs={
                    "station_id": "9447130",
                    "window_start_ts": "2024-02-01T00:00:00Z",
                    "window_end_ts": "2024-02-08T00:00:00Z"
                }
            ),
            Action(
                name="get_processed_timeseries_summary",
                kwargs={"csv_path": "/data/processed/timeseries_seattle_weather.csv"}
            ),
            Action(
                name="append_terminal_log_entry",
                kwargs={
                    "command": "station_determination_seattle",
                    "exit_code": 0,
                    "stdout": "",
                    "stderr": "",
                    "printed_message": "station_determination_seattle completed",
                    "printed_ts": "2024-02-01T15:25:00Z"
                }
            ),
        ],
        outputs=[{
            "primary_station_id": "9447130",
            "timeseries": {
                "csv_path": "/data/processed/timeseries_seattle_weather.csv",
                "row_count": 240
            },
            "logged": {
                "command": "station_determination_seattle",
                "exit_code": 0,
                "printed_message": "station_determination_seattle completed",
                "printed_ts": "2024-02-01T15:25:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_9",
        instruction=(
            "You are a data‑science automation agent. You need to decide between Seattle and San Francisco for model promotion under the Cross‑City AUC‑Gap Promotion Protocol "
            "while honoring policy precedence and determinism. You apply an absolute AUC‑gap threshold of 0.05; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Seattle constraints: you use coordinates 47.6062,-122.3321 with a 60.0 km coverage radius; you validate tide predictions using method 'harmonic_analysis' for station 9447130 "
            "from 2024‑02‑01T00:00:00Z through 2024‑02‑08T00:00:00Z; you reference /data/processed/timeseries_seattle_weather.csv and model simple_model. "
            "San Francisco constraints: you use coordinates 37.7749,-122.4194 with a 50.0 km coverage radius; you validate tide predictions using method 'harmonic_analysis' for station 9414290 "
            "from 2024‑03‑15T00:00:00Z through 2024‑03‑22T00:00:00Z; you reference /data/processed/timeseries_sf_weather.csv and model flood_risk_sf_v2. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. For auditability, you include a completion record labeled 'ccap_promotion_seattle-san-francisco' "
            "with exit_code 0 and printed timestamp 2024‑03‑18T16:34:10Z."
        ),
        actions=[
            # Seattle validations & metrics
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            # San Francisco validations & metrics
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_sf_v2"}),
            # Winner artifacts (San Francisco)
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Audit log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_seattle-san-francisco",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_seattle-san-francisco completed",
                "printed_ts": "2024-03-18T16:34:10Z"
            }),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "tide_pred_m", "wind_speed_ms", "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_seattle-san-francisco",
                "exit_code": 0,
                "printed_message": "ccap_promotion_seattle-san-francisco completed",
                "printed_ts": "2024-03-18T16:34:10Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_10",
        instruction=(
            "You are a data‑science automation agent. You need to produce a comparative risk snapshot between Miami and Boston by applying the Multi‑City Comparative Snapshot Protocol "
            "while honoring policy precedence and determinism. Prefer higher AUC; if AUCs are equal, prefer higher Accuracy. "
            "Miami constraints: coordinates 25.7617,-80.1918 (radius 25.0 km); validate water levels with datum 'NAVD88' for station 8723214 from 2024‑02‑01T00:00:00Z to 2024‑02‑02T00:00:00Z; "
            "dataset /data/processed/timeseries_miami_weather.csv; model flood_risk_miami_v1. "
            "Boston constraints: coordinates 42.3601,-71.0589 (radius 40.0 km); validate tide predictions using method 'harmonic_analysis' for station 8443970 from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z; "
            "dataset /data/processed/timeseries_boston_weather.csv; model boston_harbor_model. "
            "Return the winning_city and, for each city, the model metrics (AUC and Accuracy), the predictions CSV path, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, you include a completion record labeled 'multi_snapshot_miami-boston' with exit_code 0 and printed timestamp 2024‑03‑01T14:15:20Z."
        ),
        actions=[
            # Miami
            Action(name="get_stations_by_location", kwargs={"query_latitude": 25.7617,"query_longitude": -80.1918,"radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={"station_id": "8723214","window_start_ts":"2024-02-01T00:00:00Z","window_end_ts":"2024-02-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={"model_name": "flood_risk_miami_v1"}),
            Action(name="get_predictions_by_model_name", kwargs={"model_name": "flood_risk_miami_v1"}),
            Action(name="get_processed_timeseries_summary", kwargs={"csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            # Boston
            Action(name="get_stations_by_location", kwargs={"query_latitude": 42.3601,"query_longitude": -71.0589,"radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={"station_id": "8443970","window_start_ts":"2024-03-01T00:00:00Z","window_end_ts":"2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={"model_name": "boston_harbor_model"}),
            Action(name="get_predictions_by_model_name", kwargs={"model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={"csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "multi_snapshot_miami-boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "multi_snapshot_miami-boston completed",
                "printed_ts": "2024-03-01T14:15:20Z"
            }),
        ],
        outputs=[{
            "winning_city": "Boston",
            "miami": {
                "metrics": {"auc": 0.73, "accuracy": 0.75},
                "predictions_csv_path": "/results/predictions_miami_v1.csv",
                "processed_dataset_summary": {
                    "columns": ["timestamp","tide_pred_m","wind_speed_ms","precipitation_mm_hr","pressure_hpa","temperature_c"],
                    "row_count": 96,
                    "min_timestamp": "2024-02-01T00:00:00Z",
                    "max_timestamp": "2024-02-05T00:00:00Z"
                }
            },
            "boston": {
                "metrics": {"auc": 0.73, "accuracy": 0.81},
                "predictions_csv_path": "/data/processed/predictions_boston.csv",
                "processed_dataset_summary": {
                    "columns": ["timestamp","ice_coverage_pct","snow_depth_mm","temperature_feels_like_c","pressure_tendency_hpa_3h","high_risk_flag"],
                    "row_count": 120,
                    "min_timestamp": "2024-03-01T00:00:00Z",
                    "max_timestamp": "2024-03-06T00:00:00Z"
                }
            },
            "terminal_log": {
                "command": "multi_snapshot_miami-boston",
                "exit_code": 0,
                "printed_message": "multi_snapshot_miami-boston completed",
                "printed_ts": "2024-03-01T14:15:20Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_11",
        instruction=(
            "You are the model owner for San Francisco. Apply the Model Variant Selection Protocol with these policy overrides: "
            "limit candidates to 'flood_risk_sf_v1' and 'flood_risk_sf_v2'; require AUC ≥ 0.88 as the primary criterion and use accuracy and the newest generated timestamp as tie-breakers; "
            "require NOAA evidence from station 9414290 with harmonic tide predictions for 2024-03-15T00:00:00Z–2024-03-22T00:00:00Z and MLLW water-level history for 2024-02-14T00:00:00Z–2024-03-15T00:00:00Z; "
            "confirm feature schema availability at '/processed_data/features.csv'; "
            "record a single deterministic terminal_log entry with command 'model_selection_sf', exit_code 0, stdout '', stderr '', printed_message 'model_selection_sf completed', and printed_ts '2024-03-18T15:45:00Z' derived from the selected model's generated timestamp; "
            "provide a concise decision naming the selected model and citing the evidence used."
        ),
        actions=[
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_sf_v1"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_sf_v2"}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9414290",
                "window_start_ts": "2024-03-15T00:00:00Z",
                "window_end_ts": "2024-03-22T00:00:00Z"
            }),
            Action(name="get_water_levels_window", kwargs={
                "station_id": "9414290",
                "window_start_ts": "2024-02-14T00:00:00Z",
                "window_end_ts": "2024-03-15T00:00:00Z"
            }),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/processed_data/features.csv"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "model_selection_sf",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "model_selection_sf completed",
                "printed_ts": "2024-03-18T15:45:00Z"
            })
        ],
        outputs=[{
            "selected_model": "flood_risk_sf_v2",
            "policy": {"primary_metric": "AUC", "min_auc": 0.88, "tie_breakers": ["accuracy", "generated_ts(desc)"]},
            "evidence": {
                "station_id": "9414290",
                "tide_window": ["2024-03-15T00:00:00Z", "2024-03-22T00:00:00Z"],
                "water_level_window": ["2024-02-14T00:00:00Z", "2024-03-15T00:00:00Z"],
                "features_csv_path": "/processed_data/features.csv"
            },
            "timestamp": "2024-03-18T15:45:00Z"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_12",
        instruction=(
            "You are a data-science automation agent. Apply the City Risk Snapshot Protocol for Miami with the override that you must confirm water levels datum NAVD88 for station 8723214 in the window 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z and select flood_risk_miami_v1 as the model. Use /data/processed/timeseries_miami_weather.csv for the processed dataset summary and register the snapshot completion in the terminal log using 2024-02-02T15:45:00Z as printed_ts. Return the snapshot including chosen station id, model AUC and accuracy, predictions CSV path, and the processed dataset summary."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_miami_v1"}),
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "flood_risk_miami_v1"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "risk_snapshot_miami", "exit_code": 0, "stdout": "", "stderr": "", "printed_message": "risk_snapshot_miami completed", "printed_ts": "2024-02-02T15:45:00Z"
            }),
        ],
        outputs=[{
            "primary_station_id": "8723214",
            "metrics": {"auc": 0.73, "accuracy": 0.75},
            "predictions_csv_path": "/results/predictions_miami_v1.csv",
            "processed_dataset_summary": {"csv_path": "/data/processed/timeseries_miami_weather.csv", "row_count": 96, "min_timestamp": "2024-02-01T00:00:00Z", "max_timestamp": "2024-02-05T00:00:00Z"}
        }]
    ),
    Task(
        annotator="0",
        user_id="task_13",
        instruction=(
            "You are a data-science automation agent. Apply the Model Variant Selection Protocol for San Francisco with the override that if the AUC difference is below 0.01 prefer the most recent metrics.generated_ts between flood_risk_sf_v1 and flood_risk_sf_v2. Register the selection in the terminal log using 2024-03-18T15:45:00Z as printed_ts. Return the chosen model name and its predictions CSV path."
        ),
        actions=[
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_sf_v1"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_sf_v2"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "model_selection_san-francisco", "exit_code": 0, "stdout": "", "stderr": "", "printed_message": "model_selection_san-francisco completed", "printed_ts": "2024-03-18T15:45:00Z"
            }),
        ],
        outputs=[{"chosen_model_name": "flood_risk_sf_v2",
                  "predictions_csv_path": "/results/predictions_sf_v2.csv"}]
    ),
    Task(
        annotator="0",
        user_id="task_14",
        instruction=(
            "You are a data-science automation agent. Apply the Datum-and-Method Station Confirmation Protocol for Boston with the overrides that you must validate water levels datum NAVD88 for station 8443970 in the window 2024-02-15T00:00:00Z to 2024-03-16T00:00:00Z and method harmonic_analysis for tide predictions in the window 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z. Use /data/processed/timeseries_boston_weather.csv for the processed dataset summary, retrieve boston_harbor_model metrics and predictions, and register completion in the terminal log using 2024-03-01T13:18:00Z as printed_ts. Return the confirmation snapshot with chosen station id, metrics, predictions path, and processed dataset summary."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-02-15T00:00:00Z", "window_end_ts": "2024-03-16T00:00:00Z"}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "dmsc_snapshot_boston", "exit_code": 0, "stdout": "", "stderr": "", "printed_message": "dmsc_snapshot_boston completed", "printed_ts": "2024-03-01T13:18:00Z"
            }),
        ],
        outputs=[{
            "chosen_station_id": "8443970",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {"csv_path": "/data/processed/timeseries_boston_weather.csv", "row_count": 120, "min_timestamp": "2024-03-01T00:00:00Z", "max_timestamp": "2024-03-06T00:00:00Z"}
        }]
    ),
    Task(
        annotator="0",
        user_id="task_15",
        instruction=(
            "You are a data‑science automation agent. You need to produce a comparative risk snapshot between Seattle and Boston by applying the Multi‑City Comparative Snapshot Protocol "
            "while honoring policy precedence and determinism. Prefer higher AUC; if AUCs are equal, prefer higher Accuracy. "
            "Seattle constraints: coordinates 47.6062,-122.3321 (radius 60.0 km); validate tide predictions using method 'harmonic_analysis' for station 9447130 from 2024‑02‑01T00:00:00Z to 2024‑02‑08T00:00:00Z; "
            "dataset /data/processed/timeseries_seattle_weather.csv; model simple_model. "
            "Boston constraints: coordinates 42.3601,-71.0589 (radius 40.0 km); validate tide predictions using method 'harmonic_analysis' for station 8443970 from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z; "
            "dataset /data/processed/timeseries_boston_weather.csv; model boston_harbor_model. "
            "Return the winning_city and, for each city, the model metrics (AUC and Accuracy), the predictions CSV path, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, you include a completion record labeled 'multi_snapshot_seattle-boston' with exit_code 0, stdout '', stderr '', "
            "printed_message 'multi_snapshot_seattle-boston completed', and printed timestamp 2024‑03‑01T14:14:40Z."
        ),
        actions=[
            # Seattle
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Boston
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "multi_snapshot_seattle-boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "multi_snapshot_seattle-boston completed",
                "printed_ts": "2024-03-01T14:14:40Z"
            }),
        ],
        outputs=[{
            "winning_city": "Seattle",
            "seattle": {
                "metrics": {"auc": 0.79, "accuracy": 0.76},
                "predictions_csv_path": "/processed_data/predictions_simple.csv",
                "processed_dataset_summary": {
                    "columns": ["timestamp", "rainfall_intensity_mmh", "wave_height_m", "lunar_phase_pct", "daylight_hours", "high_risk_flag"],
                    "row_count": 240,
                    "min_timestamp": "2024-02-01T00:00:00Z",
                    "max_timestamp": "2024-02-11T00:00:00Z"
                }
            },
            "boston": {
                "metrics": {"auc": 0.73, "accuracy": 0.81},
                "predictions_csv_path": "/data/processed/predictions_boston.csv",
                "processed_dataset_summary": {
                    "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                    "row_count": 120,
                    "min_timestamp": "2024-03-01T00:00:00Z",
                    "max_timestamp": "2024-03-06T00:00:00Z"
                }
            },
            "terminal_log": {
                "command": "multi_snapshot_seattle-boston",
                "exit_code": 0,
                "printed_message": "multi_snapshot_seattle-boston completed",
                "printed_ts": "2024-03-01T14:14:40Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_16",
        instruction=(
            "You are a data-science automation agent. Apply the Datum-and-Method Station Confirmation Protocol for Boston with the override that if the tide predictions method for station 8443970 is 'harmonic_analysis' in the window 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z and its water levels datum is 'NAVD88' in the same window then keep 8443970, otherwise use backup station 8447930. "
            "Use the processed dataset at /data/processed/timeseries_boston_weather.csv and the boston_harbor_model variant, "
            "publish an audit receipt using /data/processed/predictions_boston.csv and /processed_data/metrics_boston.csv with generated_ts equal to 2024-03-01T14:02:00Z, "
            "and register the confirmation in the terminal log with command 'dmsc_snapshot_boston' using printed_ts 2024-03-01T14:02:00Z. "
            "Return the chosen station id, the model AUC and Accuracy, the predictions CSV path, and the processed dataset summary."
        ),
        actions=[
            # READS
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            # WRITES
            Action(name="publish_stakeholder_outputs", kwargs={
                "predictions_final_csv_path": "/data/processed/predictions_boston.csv",
                "metrics_summary_csv_path": "/processed_data/metrics_boston.csv",
                "generated_ts": "2024-03-01T14:02:00Z"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "dmsc_snapshot_boston", "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "dmsc_snapshot_boston completed", "printed_ts": "2024-03-01T14:02:00Z"})
        ],
        outputs=[{
            "chosen_station_id": "8443970",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {"csv_path": "/data/processed/timeseries_boston_weather.csv", "row_count": 120}
        }]
    ),
    Task(
        annotator="0",
        user_id="task_17",
        instruction=(
            "You are a data-science automation agent. Apply the City Status Compilation Protocol for San Francisco with the overrides that the primary station must be 9414290 if the tide predictions method is 'harmonic' in the window 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z, otherwise use 9414750, "
            "and the terminal log printed_ts must be taken from the metrics.generated_ts of flood_risk_sf_v2. "
            "Use coordinates 37.7749,-122.4194 with radius 50.0, and the processed dataset at /data/processed/timeseries_sf_weather.csv with the model flood_risk_sf_v2. "
            "Return the city, the primary_station_id, the predictions CSV path, the model AUC and Accuracy, and the terminal log confirmation."
        ),
        actions=[
            # READS
            Action(name="get_project_config_by_city",
                   kwargs={"target_city": "San Francisco"}),
            Action(name="get_geocoding_result_by_city",
                   kwargs={"query_city": "San Francisco"}),
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # WRITE (LOG)
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_san-francisco", "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "status_compilation_san-francisco completed", "printed_ts": "2024-03-18T15:45:00Z"})
        ],
        outputs=[{
            "city": "San Francisco",
            "primary_station_id": "9414290",
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "logged": {
                "command": "status_compilation_san-francisco",
                "exit_code": 0,
                "printed_message": "status_compilation_san-francisco completed",
                "printed_ts": "2024-03-18T15:45:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_18",
        instruction=(
            "You are a data-science automation agent. Apply the City Status Compilation Protocol for Miami with the override that the primary station must be 8723214 if its water levels datum is 'NAVD88' in the window 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z, otherwise use 8723170, "
            "and the terminal log printed_ts must be 2024-02-02T11:45:00Z. Use the processed dataset at /data/processed/timeseries_miami_weather.csv with the model flood_risk_miami_v1. "
            "Return the city, the primary_station_id, the predictions CSV path, the model AUC and Accuracy, and the terminal log confirmation."
        ),
        actions=[
            Action(name="get_project_config_by_city",
                   kwargs={"target_city": "Miami"}),
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            Action(name="append_terminal_log_entry", kwargs={"command": "status_compilation_miami", "exit_code": 0, "stdout": "",
                   "stderr": "", "printed_message": "status_compilation_miami completed", "printed_ts": "2024-02-02T11:45:00Z"})
        ],
        outputs=[{
            "city": "Miami",
            "primary_station_id": "8723214",
            "predictions_csv_path": "/results/predictions_miami_v1.csv",
            "metrics": {"auc": 0.73, "accuracy": 0.75},
            "logged": {"command": "status_compilation_miami", "exit_code": 0, "printed_message": "status_compilation_miami completed", "printed_ts": "2024-02-02T11:45:00Z"}
        }]
    ),
    Task(
        annotator="0",
        user_id="task_19",
        instruction=(
            "You are a data‑science automation agent. You need to decide between Miami and San Francisco for model promotion under the Cross‑City AUC‑Gap Promotion Protocol "
            "while honoring policy precedence and determinism. You apply an absolute AUC‑gap threshold of 0.05; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Miami constraints: coordinates 25.7617,-80.1918 with a 25.0 km coverage radius; validate water levels with datum 'NAVD88' for station 8723214 from 2024‑02‑01T00:00:00Z to 2024‑02‑02T00:00:00Z; "
            "dataset /data/processed/timeseries_miami_weather.csv; model flood_risk_miami_v1. "
            "San Francisco constraints: coordinates 37.7749,-122.4194 with a 50.0 km coverage radius; validate tide predictions using method 'harmonic_analysis' for station 9414290 from 2024‑03‑15T00:00:00Z to 2024‑03‑22T00:00:00Z; "
            "dataset /data/processed/timeseries_sf_weather.csv; model flood_risk_sf_v2. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. For auditability, you include a completion record labeled 'ccap_promotion_miami-san-francisco' "
            "with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_miami-san-francisco completed', and printed timestamp 2024‑03‑18T16:33:10Z."
        ),
        actions=[
            # Miami validations & metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # San Francisco validations & metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # Winner: San Francisco
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_miami-san-francisco",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_miami-san-francisco completed",
                "printed_ts": "2024-03-18T16:33:10Z"
            }),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "tide_pred_m", "wind_speed_ms", "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_miami-san-francisco",
                "exit_code": 0,
                "printed_message": "ccap_promotion_miami-san-francisco completed",
                "printed_ts": "2024-03-18T16:33:10Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_20",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a status snapshot for Seattle while complying with policy precedence and determinism. "
            "You operate with the following constraints: the city reference is Seattle at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; "
            "the primary station is NOAA 9447130 subject to verification that tide predictions use method 'harmonic' and are available from "
            "2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; the processed dataset is located at /data/processed/timeseries_seattle_weather.csv; "
            "the model of record is simple_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics "
            "(AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for "
            "/data/processed/timeseries_seattle_weather.csv. "
            "For auditability, the audit trail includes a completion entry labeled 'status_compilation_seattle' with message "
            "'status_compilation_seattle completed', exit_code 0, and printed timestamp 2024-02-01T15:25:00Z."
        ),
        actions=[
            # Station neighborhood context (non-procedural instruction specifies constraints only)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062,
                "query_longitude": -122.3321,
                "radius_km": 60.0
            }),
            # Verify tide predictions method/window for the designated primary station
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Summarize the processed dataset
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            # Model artifacts (model of record defined in the instruction)
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "simple_model"
            }),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "simple_model"
            }),
            # Deterministic audit trail entry (instruction specifies required fields, not the tool)
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-01T15:25:00Z"
            }),
        ],
        outputs=[{
            "city": "Seattle",
            "primary_station_id": "9447130",
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "processed_dataset_summary": {
                "csv_path": "/data/processed/timeseries_seattle_weather.csv",
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-01T15:25:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_21",
        instruction=(
            "You are a data‑science automation agent. Your objective is to prepare a time‑based dataset split for Boston while honoring policy precedence and determinism. "
            "You operate under the Modeling & Risk Protocol — Data Preparation (Time‑Based Partitioning Rule), selecting this policy explicitly for partitioning. "
            "You work with the processed dataset at /data/processed/timeseries_boston_weather.csv (covering 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z, row_count 120). "
            "You apply the Boston test‑fraction defined by policy; if multiple values are permitted, you resolve the choice via the city‑level override to 0.25. "
            "You record the split deterministically using the split timestamp 2024‑03‑01T13:20:00Z and the canonical naming convention for Boston split summaries defined by policy. "
            "Your deliverable is a structured, machine‑verifiable summary of the split and a brief overview of the referenced processed dataset; you do not enumerate tool names or prescribe steps. "
            "For auditability, you include a completion record labeled 'dataset_split_boston' with exit_code 0 and printed timestamp 2024‑03‑01T13:20:00Z."
        ),
        actions=[
            # Read the processed dataset summary (Boston)
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Create the deterministic time-based split using the dataset's row_count
            Action(name="create_time_based_dataset_split", kwargs={
                "processed_csv_path": "/data/processed/timeseries_boston_weather.csv",
                "test_fraction": 0.25,
                "split_summary_json_path": "/processed_data/split_summary_boston.json",
                "split_ts": "2024-03-01T13:20:00Z"
            }),
            # Deterministic audit trail entry
            Action(name="append_terminal_log_entry", kwargs={
                "command": "dataset_split_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_boston completed",
                "printed_ts": "2024-03-01T13:20:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "dataset_split": {
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 90,
                "test_index_count": 30,
                "split_summary_json_path": "/processed_data/split_summary_boston.json"
            },
            "processed_dataset_summary": {
                "csv_path": "/data/processed/timeseries_boston_weather.csv",
                "columns": [
                    "timestamp",
                    "ice_coverage_pct",
                    "snow_depth_mm",
                    "temperature_feels_like_c",
                    "pressure_tendency_hpa_3h",
                    "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "dataset_split_boston",
                "exit_code": 0,
                "printed_message": "dataset_split_boston completed",
                "printed_ts": "2024-03-01T13:20:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_22",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a model readiness snapshot for Boston while complying with policy precedence and determinism. "
            "You operate with the following constraints: the primary coastal station is NOAA 8443970 whose tide predictions use method "
            "'harmonic_analysis' and are available from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; the processed dataset is located at "
            "/data/processed/timeseries_boston_weather.csv covering 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z with row_count 120; "
            "the model of record is boston_harbor_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics "
            "(AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for "
            "/data/processed/timeseries_boston_weather.csv. "
            "For auditability, the trail includes a completion entry labeled 'model_readiness_boston' with message "
            "'model_readiness_boston completed', exit_code 0, and printed timestamp 2024-03-01T13:22:00Z."
        ),
        actions=[
            # Model metrics and predictions for the declared model of record
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"
            }),
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "boston_harbor_model"
            }),
            # Processed dataset summary
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "model_readiness_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "model_readiness_boston completed",
                "printed_ts": "2024-03-01T13:22:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "primary_station_id": "8443970",
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "processed_dataset_summary": {
                "csv_path": "/data/processed/timeseries_boston_weather.csv",
                "columns": [
                    "timestamp",
                    "ice_coverage_pct",
                    "snow_depth_mm",
                    "temperature_feels_like_c",
                    "pressure_tendency_hpa_3h",
                    "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "model_readiness_boston",
                "exit_code": 0,
                "printed_message": "model_readiness_boston completed",
                "printed_ts": "2024-03-01T13:22:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_23",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Seattle and Boston for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.04; when the gap is below this threshold, you prefer the city whose "
            "validated station condition passes; if both pass, you choose the city with the most recent metrics.generated_ts. "
            "City constraints: Seattle uses primary coastal station NOAA 9447130 with tide predictions using method 'harmonic_analysis' "
            "available from 2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z, processed dataset at "
            "/data/processed/timeseries_seattle_weather.csv, and model of record simple_model. "
            "Boston uses primary coastal station NOAA 8443970 with tide predictions using method 'harmonic_analysis' available from "
            "2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z, processed dataset at /data/processed/timeseries_boston_weather.csv, "
            "and model of record boston_harbor_model. "
            "Your deliverable returns only the chosen city along with its model metrics (AUC and Accuracy), the predictions CSV path "
            "for the chosen model, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, include a completion record labeled 'ccap_promotion_seattle-boston' with exit_code 0 and printed timestamp "
            "2024-02-08T12:00:00Z."
        ),
        actions=[
            # Validate Seattle window/method, gather Seattle metrics
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),

            # Validate Boston window/method, gather Boston metrics
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),

            # Decision (gap 0.79 vs 0.73 >= 0.04) ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record (correct protocol command name)
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-02-08T12:00:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0,
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-02-08T12:00:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_24",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a status snapshot for Seattle while complying with policy precedence and determinism. "
            "You operate with the following constraints: the city is Seattle at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; "
            "the primary coastal station is resolved under policy from that location context and must validate tide predictions using method "
            "'harmonic_analysis' available from 2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; "
            "the processed dataset is located at /data/processed/timeseries_seattle_weather.csv covering 2024-02-01T00:00:00Z to "
            "2024-02-11T00:00:00Z with row_count 240; the model of record is simple_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics "
            "(AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for "
            "/data/processed/timeseries_seattle_weather.csv. "
            "For auditability, include a completion record labeled 'status_snapshot_seattle' with exit_code 0 and printed timestamp "
            "2024-02-08T12:15:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062,
                "query_longitude": -122.3321,
                "radius_km": 60.0
            }),
            # Validate tide predictions method/window for the resolved primary station (9447130)
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_snapshot_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_snapshot_seattle completed",
                "printed_ts": "2024-02-08T12:15:00Z"
            }),
        ],
        outputs=[{
            "city": "Seattle",
            "primary_station_id": "9447130",
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_snapshot_seattle",
                "exit_code": 0,
                "printed_message": "status_snapshot_seattle completed",
                "printed_ts": "2024-02-08T12:15:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_25",
        instruction=(
            "You are a data‑science automation agent. Your objective is to prepare a time‑based dataset split for Seattle while honoring "
            "policy precedence and determinism. You operate under the Modeling & Risk Protocol — Data Preparation (Time‑Based Partitioning Rule), "
            "selecting this policy explicitly for partitioning. You work with the processed dataset at /data/processed/timeseries_seattle_weather.csv "
            "(covering 2024‑02‑01T00:00:00Z to 2024‑02‑11T00:00:00Z, row_count 240). You apply the Seattle test‑fraction defined by policy; "
            "where multiple values are permitted, you resolve the choice via the city‑level override to 0.20. "
            "You record the split deterministically using the split timestamp 2024‑02‑08T12:20:00Z and the canonical naming convention for "
            "Seattle split summaries defined by policy. Your deliverable is a structured, machine‑verifiable summary of the split and a brief "
            "overview of the referenced processed dataset; you do not enumerate tool names or prescribe steps. For auditability, include a "
            "completion record labeled 'dataset_split_seattle' with exit_code 0 and printed timestamp 2024‑02‑08T12:20:00Z."
        ),
        actions=[
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="create_time_based_dataset_split", kwargs={
                "processed_csv_path": "/data/processed/timeseries_seattle_weather.csv",
                "test_fraction": 0.20,
                "split_summary_json_path": "/processed_data/split_summary_seattle.json",
                "split_ts": "2024-02-08T12:20:00Z"
            }),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "dataset_split_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_seattle completed",
                "printed_ts": "2024-02-08T12:20:00Z"
            }),
        ],
        outputs=[{
            "city": "Seattle",
            "dataset_split": {
                "method": "time_based",
                "test_fraction": 0.20,
                "train_index_count": 192,
                "test_index_count": 48,
                "split_summary_json_path": "/processed_data/split_summary_seattle.json"
            },
            "processed_dataset_summary": {
                "csv_path": "/data/processed/timeseries_seattle_weather.csv",
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "dataset_split_seattle",
                "exit_code": 0,
                "printed_message": "dataset_split_seattle completed",
                "printed_ts": "2024-02-08T12:20:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_26",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Boston and Miami for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.05; when the gap is below this threshold, you prefer the city whose "
            "validated station condition passes; if both pass, you choose the city with the most recent metrics.generated_ts. "
            "City constraints: Boston is at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station must be "
            "resolved from that location context and validate tide predictions using method 'harmonic_analysis' available from "
            "2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; the processed dataset is /data/processed/timeseries_boston_weather.csv "
            "(window 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, row_count 120); the model of record is boston_harbor_model. "
            "Miami is at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station must be resolved from that "
            "location context and validate water levels with datum 'NAVD88' available from 2024-02-01T00:00:00Z through 2024-02-02T00:00:00Z; "
            "the processed dataset is /data/processed/timeseries_miami_weather.csv; the model of record is flood_risk_miami_v1. "
            "Your deliverable returns only the chosen city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, "
            "and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, include a completion record labeled 'ccap_promotion_boston-miami' with exit_code 0 and printed timestamp 2024-03-01T13:18:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Boston)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601,
                "query_longitude": -71.0589,
                "radius_km": 40.0
            }),
            # Validate Boston tide window/method
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Boston metrics
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),

            # Resolve candidate stations per policy (Miami)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 25.7617,
                "query_longitude": -80.1918,
                "radius_km": 25.0
            }),
            # Validate Miami water‑levels datum/window
            Action(name="get_water_levels_window", kwargs={
                "station_id": "8723214",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-02T00:00:00Z"
            }),
            # Miami metrics
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_miami_v1"}),

            # Decision (AUC tie → Boston by recency); fetch chosen artifacts only
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),

            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_boston-miami",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_boston-miami completed",
                "printed_ts": "2024-03-01T13:18:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Boston",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "ice_coverage_pct",
                    "snow_depth_mm",
                    "temperature_feels_like_c",
                    "pressure_tendency_hpa_3h",
                    "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_boston-miami",
                "exit_code": 0,
                "printed_message": "ccap_promotion_boston-miami completed",
                "printed_ts": "2024-03-01T13:18:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_27",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a status snapshot for Boston while complying with policy precedence and determinism. "
            "You operate with the following constraints: the city is Boston at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; "
            "the primary coastal station is resolved under policy from that location context and must validate tide predictions using method "
            "'harmonic_analysis' available from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; "
            "the processed dataset is located at /data/processed/timeseries_boston_weather.csv covering 2024-03-01T00:00:00Z to "
            "2024-03-06T00:00:00Z with row_count 120; the model of record is boston_harbor_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics "
            "(AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for "
            "/data/processed/timeseries_boston_weather.csv. "
            "For auditability, include a completion record labeled 'status_snapshot_boston' with exit_code 0 and printed timestamp "
            "2024-03-01T13:21:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601,
                "query_longitude": -71.0589,
                "radius_km": 40.0
            }),
            # Validate tide predictions method/window for the resolved primary station (8443970)
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_snapshot_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_snapshot_boston completed",
                "printed_ts": "2024-03-01T13:21:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "primary_station_id": "8443970",
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "ice_coverage_pct",
                    "snow_depth_mm",
                    "temperature_feels_like_c",
                    "pressure_tendency_hpa_3h",
                    "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_snapshot_boston",
                "exit_code": 0,
                "printed_message": "status_snapshot_boston completed",
                "printed_ts": "2024-03-01T13:21:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_28",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to compile a model readiness snapshot for Seattle while honoring policy precedence and determinism. "
            "You operate with the following constraints: the city is Seattle at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; "
            "the primary coastal station is resolved from that location context under policy and must validate tide predictions using method "
            "'harmonic_analysis' available from 2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; "
            "the processed dataset is located at /data/processed/timeseries_seattle_weather.csv covering 2024-02-01T00:00:00Z to "
            "2024-02-11T00:00:00Z with row_count 240; the model of record is simple_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics "
            "(AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for "
            "/data/processed/timeseries_seattle_weather.csv. "
            "For auditability, include a completion record labeled 'model_readiness_seattle' with exit_code 0 and printed timestamp "
            "2024-02-08T12:18:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062,
                "query_longitude": -122.3321,
                "radius_km": 60.0
            }),
            # Validate tide predictions method/window for the resolved primary station (9447130)
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "model_readiness_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "model_readiness_seattle completed",
                "printed_ts": "2024-02-08T12:18:00Z"
            }),
        ],
        outputs=[{
            "city": "Seattle",
            "primary_station_id": "9447130",
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "model_readiness_seattle",
                "exit_code": 0,
                "printed_message": "model_readiness_seattle completed",
                "printed_ts": "2024-02-08T12:18:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_29",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Seattle and Miami for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.05; when the gap is below this threshold, you prefer the city whose "
            "validated station condition passes; if both pass, you choose the city with the most recent metrics.generated_ts. "
            "City constraints: Seattle is at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station must be "
            "resolved from that location context and validate tide predictions using method 'harmonic_analysis' available from "
            "2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; the processed dataset is /data/processed/timeseries_seattle_weather.csv "
            "(window 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the model of record is simple_model. "
            "Miami is at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station must be resolved from that "
            "location context and validate water levels with datum 'NAVD88' available from 2024-02-01T00:00:00Z through 2024-02-02T00:00:00Z; "
            "the processed dataset is /data/processed/timeseries_miami_weather.csv; the model of record is flood_risk_miami_v1. "
            "Your deliverable returns only the chosen city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, "
            "and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, include a completion record labeled 'ccap_promotion_seattle-miami' with exit_code 0 and printed timestamp 2024-02-08T12:10:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Seattle)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062,
                "query_longitude": -122.3321,
                "radius_km": 60.0
            }),
            # Validate Seattle tide window/method
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Seattle metrics
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),

            # Resolve candidate stations per policy (Miami)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 25.7617,
                "query_longitude": -80.1918,
                "radius_km": 25.0
            }),
            # Validate Miami water‑levels datum/window
            Action(name="get_water_levels_window", kwargs={
                "station_id": "8723214",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-02T00:00:00Z"
            }),
            # Miami metrics
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_miami_v1"}),

            # Decision (AUC 0.79 vs 0.73 ≥ 0.05) ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T12:10:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0,
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T12:10:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_30",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a status snapshot for Boston while complying with policy precedence and determinism. "
            "You operate with the following constraints: the city is Boston at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; "
            "the primary coastal station is resolved under policy from that location context and must validate tide predictions using method "
            "'harmonic_analysis' available from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; "
            "the processed dataset is located at /data/processed/timeseries_boston_weather.csv covering 2024-03-01T00:00:00Z to "
            "2024-03-06T00:00:00Z with row_count 120; the model of record is boston_harbor_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics "
            "(AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for "
            "/data/processed/timeseries_boston_weather.csv. "
            "For auditability, include a completion record labeled 'status_snapshot_boston' with exit_code 0 and printed timestamp "
            "2024-03-01T13:24:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601,
                "query_longitude": -71.0589,
                "radius_km": 40.0
            }),
            # Validate tide predictions method/window for the resolved primary station (8443970)
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_snapshot_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_snapshot_boston completed",
                "printed_ts": "2024-03-01T13:24:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "primary_station_id": "8443970",
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "ice_coverage_pct",
                    "snow_depth_mm",
                    "temperature_feels_like_c",
                    "pressure_tendency_hpa_3h",
                    "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_snapshot_boston",
                "exit_code": 0,
                "printed_message": "status_snapshot_boston completed",
                "printed_ts": "2024-03-01T13:24:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_31",
        instruction=(
            "You are a data‑science automation agent. Your objective is to prepare a time‑based dataset split for Boston while honoring "
            "policy precedence and determinism. You operate under the Modeling & Risk Protocol — Data Preparation (Time‑Based Partitioning Rule), "
            "selecting this policy explicitly for partitioning. You work with the processed dataset at /data/processed/timeseries_boston_weather.csv "
            "(covering 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z, row_count 120). You apply the Boston test‑fraction defined by policy; "
            "where multiple values are permitted, you resolve the choice via the city‑level override to 0.30. "
            "You record the split deterministically using the split timestamp 2024‑03‑01T13:24:00Z and the canonical naming convention for "
            "Boston split summaries defined by policy. Your deliverable is a structured, machine‑verifiable summary of the split and a brief "
            "overview of the referenced processed dataset; you do not enumerate tool names or prescribe steps. For auditability, include a "
            "completion record labeled 'dataset_split_boston_v2' with exit_code 0 and printed timestamp 2024‑03‑01T13:24:00Z."
        ),
        actions=[
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            Action(name="create_time_based_dataset_split", kwargs={
                "processed_csv_path": "/data/processed/timeseries_boston_weather.csv",
                "test_fraction": 0.30,
                "split_summary_json_path": "/processed_data/split_summary_boston_v2.json",
                "split_ts": "2024-03-01T13:24:00Z"
            }),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "dataset_split_boston_v2",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_boston_v2 completed",
                "printed_ts": "2024-03-01T13:24:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "dataset_split": {
                "method": "time_based",
                "test_fraction": 0.30,
                "train_index_count": 84,
                "test_index_count": 36,
                "split_summary_json_path": "/processed_data/split_summary_boston_v2.json"
            },
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "ice_coverage_pct",
                    "snow_depth_mm",
                    "temperature_feels_like_c",
                    "pressure_tendency_hpa_3h",
                    "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "dataset_split_boston_v2",
                "exit_code": 0,
                "printed_message": "dataset_split_boston_v2 completed",
                "printed_ts": "2024-03-01T13:24:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_32",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a status snapshot for Seattle while honoring policy precedence and determinism. "
            "You operate with the following constraints: the city is Seattle at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; "
            "the primary coastal station is resolved from that location context under policy and must validate tide predictions using method "
            "'harmonic_analysis' available from 2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; "
            "the processed dataset is located at /data/processed/timeseries_seattle_weather.csv covering 2024-02-01T00:00:00Z to "
            "2024-02-11T00:00:00Z with row_count 240; the model of record is simple_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics "
            "(AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for "
            "/data/processed/timeseries_seattle_weather.csv. "
            "For auditability, you include a completion record labeled 'status_compilation_seattle' with exit_code 0 and printed timestamp "
            "2024-02-08T12:22:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062,
                "query_longitude": -122.3321,
                "radius_km": 60.0
            }),
            # Validate tide predictions method/window for the resolved primary station (9447130)
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            # Deterministic audit record (protocol‑aligned command name)
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-08T12:22:00Z"
            }),
        ],
        outputs=[{
            "city": "Seattle",
            "primary_station_id": "9447130",
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-08T12:22:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_33",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Seattle and Boston for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.06; when the gap is below this threshold, you prefer the city whose "
            "validated station condition passes; if both pass, you choose the city with the most recent metrics.generated_ts. "
            "City constraints: Seattle is at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station must be "
            "resolved from that location context and validate tide predictions using method 'harmonic_analysis' available from "
            "2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; the processed dataset is /data/processed/timeseries_seattle_weather.csv "
            "(window 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the model of record is simple_model. "
            "Boston is at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station must be resolved from that "
            "location context and validate tide predictions using method 'harmonic_analysis' available from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; "
            "the processed dataset is /data/processed/timeseries_boston_weather.csv (window 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, row_count 120); "
            "the model of record is boston_harbor_model. "
            "Your deliverable returns only the chosen city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, "
            "and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, include a completion record labeled 'ccap_promotion_seattle-boston' with exit_code 0 and printed timestamp "
            "2024-02-08T12:30:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Seattle)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062,
                "query_longitude": -122.3321,
                "radius_km": 60.0
            }),
            # Validate Seattle tide window/method
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Seattle metrics
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),

            # Resolve candidate stations per policy (Boston)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601,
                "query_longitude": -71.0589,
                "radius_km": 40.0
            }),
            # Validate Boston tide window/method
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Boston metrics
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),

            # Decision (gap 0.79 vs 0.73 not below 0.06) ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-02-08T12:30:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0,
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-02-08T12:30:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_34",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Seattle and Miami for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.04; when the gap is below this threshold, you prefer the city whose "
            "validated station condition passes; if both pass, you choose the city with the most recent metrics.generated_ts. "
            "City constraints: Seattle is at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station is "
            "resolved from that location context and must validate tide predictions using method 'harmonic_analysis' available from "
            "2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; the processed dataset is /data/processed/timeseries_seattle_weather.csv "
            "(window 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the model of record is simple_model. "
            "Miami is at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station is resolved from that "
            "location context and must validate water levels with datum 'NAVD88' available from 2024-02-01T00:00:00Z through 2024-02-02T00:00:00Z; "
            "the processed dataset is /data/processed/timeseries_miami_weather.csv; the model of record is flood_risk_miami_v1. "
            "Your deliverable returns only the chosen city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, "
            "and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, you include a completion record labeled 'ccap_promotion_seattle-miami' with exit_code 0 and printed timestamp "
            "2024-02-08T12:35:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Seattle)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate Seattle tide window/method
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Seattle metrics
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),

            # Resolve candidate stations per policy (Miami)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0
            }),
            # Validate Miami water‑levels datum/window
            Action(name="get_water_levels_window", kwargs={
                "station_id": "8723214",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-02T00:00:00Z"
            }),
            # Miami metrics
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_miami_v1"}),

            # Decision ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T12:35:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0,
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T12:35:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_35",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a status snapshot for Seattle while honoring policy precedence and determinism. "
            "You operate with the following constraints: the city is Seattle at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; "
            "the primary coastal station is resolved from that location context under policy and must validate tide predictions using method "
            "'harmonic_analysis' available from 2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; "
            "the processed dataset is located at /data/processed/timeseries_seattle_weather.csv covering 2024-02-01T00:00:00Z to "
            "2024-02-11T00:00:00Z with row_count 240; the model of record is simple_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics "
            "(AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for "
            "/data/processed/timeseries_seattle_weather.csv. "
            "For auditability, you include a completion record labeled 'status_compilation_seattle' with exit_code 0 and printed timestamp "
            "2024-02-08T12:40:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate tide predictions method/window for the resolved primary station (9447130)
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-08T12:40:00Z"
            }),
        ],
        outputs=[{
            "city": "Seattle",
            "primary_station_id": "9447130",
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-08T12:40:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_36",
        instruction=(
            "You are a data‑science automation agent. Your objective is to prepare a time‑based dataset split for Seattle while honoring "
            "policy precedence and determinism. You operate under the Modeling & Risk Protocol — Data Preparation (Time‑Based Partitioning Rule), "
            "selecting this policy explicitly for partitioning. You work with the processed dataset at /data/processed/timeseries_seattle_weather.csv "
            "(covering 2024‑02‑01T00:00:00Z to 2024‑02‑11T00:00:00Z, row_count 240). You apply the Seattle test‑fraction defined by policy; "
            "where multiple values are permitted, you resolve the choice via the city‑level override to 0.25. "
            "You record the split deterministically using the split timestamp 2024‑02‑08T12:25:00Z and the canonical naming convention for "
            "Seattle split summaries defined by policy. Your deliverable is a structured, machine‑verifiable summary of the split and a brief "
            "overview of the referenced processed dataset; you do not enumerate tool names or prescribe steps. For auditability, you include a "
            "completion record labeled 'dataset_split_seattle_v2' with exit_code 0 and printed timestamp 2024‑02‑08T12:25:00Z."
        ),
        actions=[
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="create_time_based_dataset_split", kwargs={
                "processed_csv_path": "/data/processed/timeseries_seattle_weather.csv",
                "test_fraction": 0.25,
                "split_summary_json_path": "/processed_data/split_summary_seattle_v2.json",
                "split_ts": "2024-02-08T12:25:00Z"
            }),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "dataset_split_seattle_v2",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_seattle_v2 completed",
                "printed_ts": "2024-02-08T12:25:00Z"
            }),
        ],
        outputs=[{
            "city": "Seattle",
            "dataset_split": {
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 180,
                "test_index_count": 60,
                "split_summary_json_path": "/processed_data/split_summary_seattle_v2.json"
            },
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "dataset_split_seattle_v2",
                "exit_code": 0,
                "printed_message": "dataset_split_seattle_v2 completed",
                "printed_ts": "2024-02-08T12:25:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_37",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a status snapshot for Boston while honoring policy precedence and determinism. "
            "You operate with the following constraints: the city is Boston at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; "
            "the primary coastal station is resolved from that location context under policy and must validate tide predictions using method "
            "'harmonic_analysis' available from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; "
            "the processed dataset is located at /data/processed/timeseries_boston_weather.csv covering 2024-03-01T00:00:00Z to "
            "2024-03-06T00:00:00Z with row_count 120; the model of record is boston_harbor_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics "
            "(AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for "
            "/data/processed/timeseries_boston_weather.csv. "
            "For auditability, you include a completion record labeled 'status_compilation_boston' with exit_code 0 and printed timestamp "
            "2024-03-01T13:26:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate tide predictions method/window for the resolved primary station (8443970)
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:26:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "primary_station_id": "8443970",
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "ice_coverage_pct",
                    "snow_depth_mm",
                    "temperature_feels_like_c",
                    "pressure_tendency_hpa_3h",
                    "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_compilation_boston",
                "exit_code": 0,
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:26:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_38",
        instruction=(
            "You are a data‑science automation agent. You need to produce a comparative risk snapshot between Boston and San Francisco by applying the Multi‑City Comparative Snapshot Protocol "
            "while honoring policy precedence and determinism. Prefer higher AUC; if AUCs are equal, prefer higher Accuracy. "
            "Boston constraints: coordinates 42.3601,-71.0589 (radius 40.0 km); validate tide predictions using method 'harmonic' for station 8443970 from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z; "
            "dataset /data/processed/timeseries_boston_weather.csv; model boston_harbor_model. "
            "San Francisco constraints: coordinates 37.7749,-122.4194 (radius 50.0 km); validate tide predictions using method 'harmonic' for station 9414290 from 2024‑03‑15T00:00:00Z to 2024‑03‑22T00:00:00Z; "
            "dataset /data/processed/timeseries_sf_weather.csv; model flood_risk_sf_v2. "
            "Return the winning_city and, for each city, the model metrics (AUC and Accuracy), the predictions CSV path, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, you include a completion record labeled 'multi_snapshot_boston-san-francisco' with exit_code 0, stdout '', stderr '', "
            "printed_message 'multi_snapshot_boston-san-francisco completed', and printed timestamp 2024‑03‑18T16:32:40Z."
        ),
        actions=[
            # Boston
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # San Francisco
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "multi_snapshot_boston-san-francisco",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "multi_snapshot_boston-san-francisco completed",
                "printed_ts": "2024-03-18T16:32:40Z"
            }),
        ],
        outputs=[{
            "winning_city": "San Francisco",
            "boston": {
                "metrics": {"auc": 0.73, "accuracy": 0.81},
                "predictions_csv_path": "/data/processed/predictions_boston.csv",
                "processed_dataset_summary": {
                    "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                    "row_count": 120,
                    "min_timestamp": "2024-03-01T00:00:00Z",
                    "max_timestamp": "2024-03-06T00:00:00Z"
                }
            },
            "san_francisco": {
                "metrics": {"auc": 0.89, "accuracy": 0.85},
                "predictions_csv_path": "/results/predictions_sf_v2.csv",
                "processed_dataset_summary": {
                    "columns": ["timestamp", "tide_pred_m", "wind_speed_ms", "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"],
                    "row_count": 168,
                    "min_timestamp": "2024-03-15T00:00:00Z",
                    "max_timestamp": "2024-03-22T00:00:00Z"
                }
            },
            "terminal_log": {
                "command": "multi_snapshot_boston-san-francisco",
                "exit_code": 0,
                "printed_message": "multi_snapshot_boston-san-francisco completed",
                "printed_ts": "2024-03-18T16:32:40Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_39",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Seattle and Boston for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.05; when the gap is below this threshold, you prefer the city whose "
            "validated station condition passes; if both pass, you choose the city with the most recent metrics.generated_ts. "
            "City constraints: Seattle is at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station is "
            "resolved from that location context and must validate tide predictions using method 'harmonic_analysis' available from "
            "2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; the processed dataset is /data/processed/timeseries_seattle_weather.csv "
            "(window 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the model of record is simple_model. "
            "Boston is at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station is resolved from that "
            "location context and must validate tide predictions using method 'harmonic_analysis' available from 2024-03-01T00:00:00Z through "
            "2024-03-02T00:00:00Z; the processed dataset is /data/processed/timeseries_boston_weather.csv "
            "(window 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, row_count 120); the model of record is boston_harbor_model. "
            "Your deliverable returns only the chosen city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, "
            "and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, you include a completion record labeled 'ccap_promotion_seattle-boston' with exit_code 0 and printed timestamp "
            "2024-02-08T12:45:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Seattle)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate Seattle tide window/method
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Seattle metrics
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),

            # Resolve candidate stations per policy (Boston)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate Boston tide window/method
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Boston metrics
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),

            # Decision (AUC 0.79 vs 0.73 ≥ 0.05) ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-02-08T12:45:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0,
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-02-08T12:45:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_40",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a status snapshot for Seattle while honoring policy precedence and determinism. "
            "You operate with the following constraints: the city is Seattle at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; "
            "the primary coastal station is resolved from that location context under policy and must validate tide predictions using method "
            "'harmonic_analysis' available from 2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; "
            "the processed dataset is located at /data/processed/timeseries_seattle_weather.csv covering 2024-02-01T00:00:00Z to "
            "2024-02-11T00:00:00Z with row_count 240; the model of record is simple_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics "
            "(AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for "
            "/data/processed/timeseries_seattle_weather.csv. "
            "For auditability, you include a completion record labeled 'status_compilation_seattle' with exit_code 0 and printed timestamp "
            "2024-02-08T12:50:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate tide predictions method/window for the resolved primary station (9447130)
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-08T12:50:00Z"
            }),
        ],
        outputs=[{
            "city": "Seattle",
            "primary_station_id": "9447130",
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-08T12:50:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_41",
        instruction=(
            "You are a data‑science automation agent. Your objective is to prepare a time‑based dataset split for Boston while honoring "
            "policy precedence and determinism. You operate under the Modeling & Risk Protocol — Data Preparation (Time‑Based Partitioning Rule), "
            "selecting this policy explicitly for partitioning. You work with the processed dataset at /data/processed/timeseries_boston_weather.csv "
            "(covering 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z, row_count 120). You apply the Boston test‑fraction defined by policy; "
            "where multiple values are permitted, you resolve the choice via the city‑level override to 0.20. "
            "You record the split deterministically using the split timestamp 2024‑03‑01T13:27:00Z and the canonical naming convention for "
            "Boston split summaries defined by policy. Your deliverable is a structured, machine‑verifiable summary of the split and a brief "
            "overview of the referenced processed dataset; you do not enumerate tool names or prescribe steps. For auditability, you include a "
            "completion record labeled 'dataset_split_boston_v3' with exit_code 0 and printed timestamp 2024‑03‑01T13:27:00Z."
        ),
        actions=[
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            Action(name="create_time_based_dataset_split", kwargs={
                "processed_csv_path": "/data/processed/timeseries_boston_weather.csv",
                "test_fraction": 0.20,
                "split_summary_json_path": "/processed_data/split_summary_boston_v3.json",
                "split_ts": "2024-03-01T13:27:00Z"
            }),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "dataset_split_boston_v3",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_boston_v3 completed",
                "printed_ts": "2024-03-01T13:27:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "dataset_split": {
                "method": "time_based",
                "test_fraction": 0.20,
                "train_index_count": 96,
                "test_index_count": 24,
                "split_summary_json_path": "/processed_data/split_summary_boston_v3.json"
            },
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "ice_coverage_pct",
                    "snow_depth_mm",
                    "temperature_feels_like_c",
                    "pressure_tendency_hpa_3h",
                    "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "dataset_split_boston_v3",
                "exit_code": 0,
                "printed_message": "dataset_split_boston_v3 completed",
                "printed_ts": "2024-03-01T13:27:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_42",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a status snapshot for Boston while honoring policy precedence and determinism. "
            "You operate with the following constraints: the city is Boston at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; "
            "the primary coastal station is resolved from that location context under policy and must validate tide predictions using method "
            "'harmonic_analysis' available from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; "
            "the processed dataset is located at /data/processed/timeseries_boston_weather.csv covering 2024-03-01T00:00:00Z to "
            "2024-03-06T00:00:00Z with row_count 120; the model of record is boston_harbor_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics "
            "(AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for "
            "/data/processed/timeseries_boston_weather.csv. "
            "For auditability, you include a completion record labeled 'status_compilation_boston' with exit_code 0 and printed timestamp "
            "2024-03-01T13:28:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate tide predictions method/window for the resolved primary station (8443970)
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:28:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "primary_station_id": "8443970",
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "ice_coverage_pct",
                    "snow_depth_mm",
                    "temperature_feels_like_c",
                    "pressure_tendency_hpa_3h",
                    "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_compilation_boston",
                "exit_code": 0,
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:28:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_43",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Seattle and Miami for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.05; when the gap is below this threshold, you prefer the city whose "
            "validated station condition passes; if both pass, you choose the city with the most recent metrics.generated_ts. "
            "City constraints: Seattle is at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station is "
            "resolved from that location context and must validate tide predictions using method 'harmonic_analysis' available from "
            "2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; the processed dataset is /data/processed/timeseries_seattle_weather.csv "
            "(window 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the model of record is simple_model. "
            "Miami is at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station is resolved from that "
            "location context and must validate water levels with datum 'NAVD88' available from 2024-02-01T00:00:00Z through 2024-02-02T00:00:00Z; "
            "the processed dataset is /data/processed/timeseries_miami_weather.csv; the model of record is flood_risk_miami_v1. "
            "Your deliverable returns only the chosen city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, "
            "and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, you include a completion record labeled 'ccap_promotion_seattle-miami' with exit_code 0 and printed timestamp "
            "2024-02-08T12:55:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Seattle)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate Seattle tide window/method
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Seattle metrics
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),

            # Resolve candidate stations per policy (Miami)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0
            }),
            # Validate Miami water‑levels datum/window
            Action(name="get_water_levels_window", kwargs={
                "station_id": "8723214",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-02T00:00:00Z"
            }),
            # Miami metrics
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_miami_v1"}),

            # Decision (AUC 0.79 vs 0.73 ≥ 0.05) ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T12:55:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0,
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T12:55:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_44",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Seattle and Boston for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.03; when the gap is below this threshold, you prefer the city whose "
            "validated station condition passes; if both pass, you choose the city with the most recent metrics.generated_ts. "
            "City constraints: Seattle is at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station is "
            "resolved from that location context and must validate tide predictions using method 'harmonic_analysis' available from "
            "2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; the processed dataset is /data/processed/timeseries_seattle_weather.csv "
            "(window 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the model of record is simple_model. "
            "Boston is at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station is resolved from that "
            "location context and must validate tide predictions using method 'harmonic_analysis' available from 2024-03-01T00:00:00Z through "
            "2024-03-02T00:00:00Z; the processed dataset is /data/processed/timeseries_boston_weather.csv "
            "(window 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, row_count 120); the model of record is boston_harbor_model. "
            "Your deliverable returns only the chosen city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, "
            "and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, you include a completion record labeled 'ccap_promotion_seattle-boston' with exit_code 0 and printed timestamp "
            "2024-02-08T12:58:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Seattle)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate Seattle tide window/method
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Seattle metrics
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),

            # Resolve candidate stations per policy (Boston)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate Boston tide window/method
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Boston metrics
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),

            # Decision ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-02-08T12:58:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0,
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-02-08T12:58:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_45",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Boston and Miami for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.02; when the gap is below this threshold, you prefer the city whose "
            "validated station condition passes; if both pass, you choose the city with the most recent metrics.generated_ts. "
            "City constraints: Boston is at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station is resolved "
            "from that location context and must validate tide predictions using method 'harmonic_analysis' available from 2024-03-01T00:00:00Z "
            "through 2024-03-02T00:00:00Z; the processed dataset is /data/processed/timeseries_boston_weather.csv "
            "(window 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, row_count 120); the model of record is boston_harbor_model. "
            "Miami is at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station is resolved from that location "
            "context and must validate water levels with datum 'NAVD88' available from 2024-02-01T00:00:00Z through 2024-02-02T00:00:00Z; "
            "the processed dataset is /data/processed/timeseries_miami_weather.csv; the model of record is flood_risk_miami_v1. "
            "Your deliverable returns only the chosen city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, "
            "and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, you include a completion record labeled 'ccap_promotion_boston-miami' with exit_code 0 and printed timestamp "
            "2024-03-01T13:18:00Z."
        ),
        actions=[
            # Resolve stations (Boston)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate Boston tide window/method; gather Boston metrics
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),

            # Resolve stations (Miami)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0
            }),
            # Validate Miami datum/window; gather Miami metrics
            Action(name="get_water_levels_window", kwargs={
                "station_id": "8723214",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-02T00:00:00Z"
            }),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_miami_v1"}),

            # Decision (AUC tie, both pass, choose Boston by recency); fetch chosen artifacts only
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),

            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_boston-miami",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_boston-miami completed",
                "printed_ts": "2024-03-01T13:18:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Boston",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "ice_coverage_pct",
                    "snow_depth_mm",
                    "temperature_feels_like_c",
                    "pressure_tendency_hpa_3h",
                    "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_boston-miami",
                "exit_code": 0,
                "printed_message": "ccap_promotion_boston-miami completed",
                "printed_ts": "2024-03-01T13:18:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_46",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a status snapshot for Boston while honoring policy precedence and determinism. "
            "You operate with the following constraints: the city is Boston at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; "
            "the primary coastal station is resolved from that location context under policy and must validate tide predictions using method "
            "'harmonic_analysis' available from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; "
            "the processed dataset is located at /data/processed/timeseries_boston_weather.csv covering 2024-03-01T00:00:00Z to "
            "2024-03-06T00:00:00Z with row_count 120; the model of record is boston_harbor_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics "
            "(AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for "
            "/data/processed/timeseries_boston_weather.csv. "
            "For auditability, you include a completion record labeled 'status_compilation_boston' with exit_code 0 and printed timestamp "
            "2024-03-01T13:33:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate tide predictions method/window for the resolved primary station (8443970)
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:33:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "primary_station_id": "8443970",
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "ice_coverage_pct",
                    "snow_depth_mm",
                    "temperature_feels_like_c",
                    "pressure_tendency_hpa_3h",
                    "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_compilation_boston",
                "exit_code": 0,
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:33:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_47",
        instruction=(
            "You are a data‑science automation agent. Your objective is to prepare a time‑based dataset split for Seattle while honoring "
            "policy precedence and determinism. You operate under the Modeling & Risk Protocol — Data Preparation (Time‑Based Partitioning Rule), "
            "selecting this policy explicitly for partitioning. You work with the processed dataset at /data/processed/timeseries_seattle_weather.csv "
            "(covering 2024‑02‑01T00:00:00Z to 2024‑02‑11T00:00:00Z, row_count 240). You apply the Seattle test‑fraction defined by policy; "
            "where multiple values are permitted, you resolve the choice via the city‑level override to 0.22. "
            "You record the split deterministically using the split timestamp 2024‑02‑08T12:27:00Z and the canonical naming convention for "
            "Seattle split summaries defined by policy. Your deliverable is a structured, machine‑verifiable summary of the split and a brief "
            "overview of the referenced processed dataset; you do not enumerate tool names or prescribe steps. For auditability, you include a "
            "completion record labeled 'dataset_split_seattle_v3' with exit_code 0 and printed timestamp 2024‑02‑08T12:27:00Z."
        ),
        actions=[
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="create_time_based_dataset_split", kwargs={
                "processed_csv_path": "/data/processed/timeseries_seattle_weather.csv",
                "test_fraction": 0.22,
                "split_summary_json_path": "/processed_data/split_summary_seattle_v3.json",
                "split_ts": "2024-02-08T12:27:00Z"
            }),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "dataset_split_seattle_v3",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_seattle_v3 completed",
                "printed_ts": "2024-02-08T12:27:00Z"
            }),
        ],
        outputs=[{
            "city": "Seattle",
            "dataset_split": {
                "method": "time_based",
                "test_fraction": 0.22,
                "train_index_count": 188,
                "test_index_count": 52,
                "split_summary_json_path": "/processed_data/split_summary_seattle_v3.json"
            },
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "dataset_split_seattle_v3",
                "exit_code": 0,
                "printed_message": "dataset_split_seattle_v3 completed",
                "printed_ts": "2024-02-08T12:27:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_48",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a status snapshot for Seattle while honoring policy precedence and determinism. "
            "You operate with the following constraints: the city is Seattle at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; "
            "the primary coastal station is resolved from that location context under policy and must validate tide predictions using method "
            "'harmonic_analysis' available from 2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; "
            "the processed dataset is located at /data/processed/timeseries_seattle_weather.csv covering 2024-02-01T00:00:00Z to "
            "2024-02-11T00:00:00Z with row_count 240; the model of record is simple_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics "
            "(AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for "
            "/data/processed/timeseries_seattle_weather.csv. "
            "For auditability, you include a completion record labeled 'status_compilation_seattle' with exit_code 0 and printed timestamp "
            "2024-02-08T12:53:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate tide predictions method/window for the resolved primary station (9447130)
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-08T12:53:00Z"
            }),
        ],
        outputs=[{
            "city": "Seattle",
            "primary_station_id": "9447130",
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-08T12:53:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_49",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Seattle and Miami for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.10; when the gap is below this threshold, you prefer the city whose "
            "validated station condition passes; if both pass, you choose the city with the most recent metrics.generated_ts. "
            "City constraints: Seattle is at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station is "
            "resolved from that location context and must validate tide predictions using method 'harmonic_analysis' available from "
            "2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; the processed dataset is /data/processed/timeseries_seattle_weather.csv "
            "(window 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the model of record is simple_model. "
            "Miami is at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station is resolved from that "
            "location context and must validate water levels with datum 'NAVD88' available from 2024-02-01T00:00:00Z through 2024-02-02T00:00:00Z; "
            "the processed dataset is /data/processed/timeseries_miami_weather.csv; the model of record is flood_risk_miami_v1. "
            "Your deliverable returns only the chosen city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, "
            "and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, you include a completion record labeled 'ccap_promotion_seattle-miami' with exit_code 0 and printed timestamp "
            "2024-02-08T12:57:00Z."
        ),
        actions=[
            # Resolve stations (Seattle)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate Seattle tide window/method; gather Seattle metrics
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),

            # Resolve stations (Miami)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0
            }),
            # Validate Miami datum/window; gather Miami metrics
            Action(name="get_water_levels_window", kwargs={
                "station_id": "8723214",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-02T00:00:00Z"
            }),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_miami_v1"}),

            # Decision (gap 0.79 vs 0.73 < 0.10 → pick by recency; Seattle more recent) ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T12:57:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0,
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T12:57:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_50",
        instruction=(
            "You are a data‑science automation agent. Your objective is to prepare a time‑based dataset split for Boston while honoring "
            "policy precedence and determinism. You operate under the Modeling & Risk Protocol — Data Preparation (Time‑Based Partitioning Rule), "
            "selecting this policy explicitly for partitioning. You work with the processed dataset at /data/processed/timeseries_boston_weather.csv "
            "(covering 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z, row_count 120). You apply the Boston test‑fraction defined by policy; "
            "where multiple values are permitted, you resolve the choice via the city‑level override to 0.28. "
            "You record the split deterministically using the split timestamp 2024‑03‑01T13:30:00Z and the canonical naming convention for "
            "Boston split summaries defined by policy. Your deliverable is a structured, machine‑verifiable summary of the split and a brief "
            "overview of the referenced processed dataset; you do not enumerate tool names or prescribe steps. For auditability, you include a "
            "completion record labeled 'dataset_split_boston_v4' with exit_code 0 and printed timestamp 2024‑03‑01T13:30:00Z."
        ),
        actions=[
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            Action(name="create_time_based_dataset_split", kwargs={
                "processed_csv_path": "/data/processed/timeseries_boston_weather.csv",
                "test_fraction": 0.28,
                "split_summary_json_path": "/processed_data/split_summary_boston_v4.json",
                "split_ts": "2024-03-01T13:30:00Z"
            }),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "dataset_split_boston_v4",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_boston_v4 completed",
                "printed_ts": "2024-03-01T13:30:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "dataset_split": {
                "method": "time_based",
                "test_fraction": 0.28,
                "train_index_count": 87,
                "test_index_count": 33,
                "split_summary_json_path": "/processed_data/split_summary_boston_v4.json"
            },
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "ice_coverage_pct",
                    "snow_depth_mm",
                    "temperature_feels_like_c",
                    "pressure_tendency_hpa_3h",
                    "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "dataset_split_boston_v4",
                "exit_code": 0,
                "printed_message": "dataset_split_boston_v4 completed",
                "printed_ts": "2024-03-01T13:30:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_51",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a status snapshot for Boston while honoring policy precedence and determinism. "
            "You operate with the following constraints: the city is Boston at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; "
            "the primary coastal station is resolved from that location context under policy and must validate tide predictions using method "
            "'harmonic_analysis' available from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; "
            "the processed dataset is located at /data/processed/timeseries_boston_weather.csv covering 2024-03-01T00:00:00Z to "
            "2024-03-06T00:00:00Z with row_count 120; the model of record is boston_harbor_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics "
            "(AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for "
            "/data/processed/timeseries_boston_weather.csv. "
            "For auditability, you include a completion record labeled 'status_compilation_boston' with exit_code 0 and printed timestamp "
            "2024-03-01T13:35:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate tide predictions method/window for the resolved primary station (8443970)
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:35:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "primary_station_id": "8443970",
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "ice_coverage_pct",
                    "snow_depth_mm",
                    "temperature_feels_like_c",
                    "pressure_tendency_hpa_3h",
                    "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_compilation_boston",
                "exit_code": 0,
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:35:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_52",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Boston and Seattle for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.05; when the gap is below this threshold, you prefer the city whose "
            "validated station condition passes; if both pass, you choose the city with the most recent metrics.generated_ts. "
            "City constraints: Boston is at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station is "
            "resolved from that location context and must validate tide predictions using method 'harmonic_analysis' available from "
            "2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; the processed dataset is /data/processed/timeseries_boston_weather.csv "
            "(window 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, row_count 120); the model of record is boston_harbor_model. "
            "Seattle is at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station is resolved from that "
            "location context and must validate tide predictions using method 'harmonic_analysis' available from 2024-02-01T00:00:00Z through "
            "2024-02-08T00:00:00Z; the processed dataset is /data/processed/timeseries_seattle_weather.csv "
            "(window 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the model of record is simple_model. "
            "Your deliverable returns only the chosen city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, "
            "and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, you include a completion record labeled 'ccap_promotion_boston-seattle' with exit_code 0 and printed timestamp "
            "2024-03-01T13:36:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Boston)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate Boston tide window/method; gather Boston metrics
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),

            # Resolve candidate stations per policy (Seattle)
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate Seattle tide window/method; gather Seattle metrics
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),

            # Decision (gap 0.79 vs 0.73 ≥ 0.05) ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_boston-seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_boston-seattle completed",
                "printed_ts": "2024-03-01T13:36:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_boston-seattle",
                "exit_code": 0,
                "printed_message": "ccap_promotion_boston-seattle completed",
                "printed_ts": "2024-03-01T13:36:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_53",
        instruction=(
            "You are a data‑science automation agent. Your objective is to prepare a time‑based dataset split for Seattle while honoring "
            "policy precedence and determinism. You operate under the Modeling & Risk Protocol — Data Preparation (Time‑Based Partitioning Rule), "
            "selecting this policy explicitly for partitioning. You work with the processed dataset at /data/processed/timeseries_seattle_weather.csv "
            "(covering 2024‑02‑01T00:00:00Z to 2024‑02‑11T00:00:00Z, row_count 240). You apply the Seattle test‑fraction defined by policy; "
            "where multiple values are permitted, you resolve the choice via the city‑level override to 0.18. "
            "You record the split deterministically using the split timestamp 2024‑02‑08T12:29:00Z and the canonical naming convention for "
            "Seattle split summaries defined by policy. Your deliverable is a structured, machine‑verifiable summary of the split and a brief "
            "overview of the referenced processed dataset; you do not enumerate tool names or prescribe steps. For auditability, you include a "
            "completion record labeled 'dataset_split_seattle_v4' with exit_code 0 and printed timestamp 2024‑02‑08T12:29:00Z."
        ),
        actions=[
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="create_time_based_dataset_split", kwargs={
                "processed_csv_path": "/data/processed/timeseries_seattle_weather.csv",
                "test_fraction": 0.18,
                "split_summary_json_path": "/processed_data/split_summary_seattle_v4.json",
                "split_ts": "2024-02-08T12:29:00Z"
            }),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "dataset_split_seattle_v4",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_seattle_v4 completed",
                "printed_ts": "2024-02-08T12:29:00Z"
            }),
        ],
        outputs=[{
            "city": "Seattle",
            "dataset_split": {
                "method": "time_based",
                "test_fraction": 0.18,
                "train_index_count": 197,
                "test_index_count": 43,
                "split_summary_json_path": "/processed_data/split_summary_seattle_v4.json"
            },
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "rainfall_intensity_mmh",
                    "wave_height_m",
                    "lunar_phase_pct",
                    "daylight_hours",
                    "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "dataset_split_seattle_v4",
                "exit_code": 0,
                "printed_message": "dataset_split_seattle_v4 completed",
                "printed_ts": "2024-02-08T12:29:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_54",
        instruction=(
            "You are a data-science automation agent. You determine the primary NOAA station for Boston by applying the Primary Station Determination Protocol with these constraints: "
            "you use coordinates 42.3601,-71.0589 and radius 40.0 from project_config; you require that station 8443970 has tide predictions method 'harmonic_analysis' in the window 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z before finalizing the default 'primary' selection; "
            "you summarize the processed dataset from /data/processed/timeseries_boston_weather.csv; you use the boston_harbor_model as the active model for metrics and predictions; "
            "and you register completion in the terminal log with command 'station_determination_boston', exit_code 0, stdout '' and stderr '' and printed_ts equal to the dataset split timestamp 2024-03-01T13:18:00Z. "
            "Return exactly these fields: primary_station_id; metrics {auc, accuracy}; predictions_csv_path; processed_dataset_summary {columns, row_count, min_timestamp, max_timestamp}; and logged {command, exit_code, printed_message, printed_ts}."
        ),
        actions=[
            Action(
                name="get_stations_by_location",
                kwargs={"query_latitude": 42.3601,
                        "query_longitude": -71.0589, "radius_km": 40.0}
            ),
            Action(
                name="get_tide_predictions_window",
                kwargs={
                    "station_id": "8443970",
                    "window_start_ts": "2024-03-01T00:00:00Z",
                    "window_end_ts": "2024-03-02T00:00:00Z"
                }
            ),
            Action(
                name="get_processed_timeseries_summary",
                kwargs={"csv_path": "/data/processed/timeseries_boston_weather.csv"}
            ),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(
                name="append_terminal_log_entry",
                kwargs={
                    "command": "station_determination_boston",
                    "exit_code": 0,
                    "stdout": "",
                    "stderr": "",
                    "printed_message": "station_determination_boston completed",
                    "printed_ts": "2024-03-01T13:18:00Z"
                }
            ),
        ],
        outputs=[{
            "primary_station_id": "8443970",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp",
                    "ice_coverage_pct",
                    "snow_depth_mm",
                    "temperature_feels_like_c",
                    "pressure_tendency_hpa_3h",
                    "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "logged": {
                "command": "station_determination_boston",
                "exit_code": 0,
                "printed_message": "station_determination_boston completed",
                "printed_ts": "2024-03-01T13:18:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_55",
        instruction=(
            "You are a data-science automation agent. You need to select the best model variant for San Francisco by applying the Model Variant Selection Protocol with this override: "
            "if the AUC difference between flood_risk_sf_v1 and flood_risk_sf_v2 is below 0.02, prefer the variant with the newer metrics.generated_ts. "
            "Register the selection in the terminal log using '2024-03-18T15:45:00Z' as printed_ts. "
            "Return the chosen_model_name and the predictions_csv_path."
        ),
        actions=[
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v1"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "model_selection_san-francisco", "exit_code": 0,
                "stdout": "", "stderr": "",
                "printed_message": "model_selection_san-francisco completed",
                "printed_ts": "2024-03-18T15:45:00Z"
            }),
        ],
        outputs=[{
            "chosen_model_name": "flood_risk_sf_v2",
            "predictions_csv_path": "/results/predictions_sf_v2.csv"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_56",
        instruction=(
            "You are a data-science automation agent. You need to determine the primary NOAA station for San Francisco by applying the Primary Station Determination Protocol with this override: "
            "validate tide predictions for station 9414290 in the window 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z before confirming the selection. "
            "Use the processed dataset summary from /data/processed/timeseries_sf_weather.csv and the active model flood_risk_sf_v2. "
            "Register the decision in the terminal log using command 'station_determination_san-francisco' with printed_ts '2024-03-18T15:45:00Z'. "
            "Return the chosen station id, the processed_dataset_summary (columns, row_count, min_timestamp, max_timestamp), the model AUC and Accuracy, the predictions_csv_path, and the terminal log confirmation."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9414290",
                "window_start_ts": "2024-03-15T00:00:00Z",
                "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "station_determination_san-francisco", "exit_code": 0,
                "stdout": "", "stderr": "",
                "printed_message": "station_determination_san-francisco completed",
                "printed_ts": "2024-03-18T15:45:00Z"
            }),
        ],
        outputs=[{
            "primary_station_id": "9414290",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp", "tide_pred_m", "wind_speed_ms",
                    "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"
                ],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            },
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "logged": {
                "command": "station_determination_san-francisco",
                "exit_code": 0,
                "printed_message": "station_determination_san-francisco completed",
                "printed_ts": "2024-03-18T15:45:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_57",
        instruction=(
            "You are a data-science automation agent. You need to produce a risk snapshot for Boston by applying the City Risk Snapshot Protocol with this override: "
            "if water levels datum for station 8443970 is 'NAVD88' in the window 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, set the primary station to 8443970; otherwise use 8447930. "
            "Use the model boston_harbor_model and the processed dataset at /data/processed/timeseries_boston_weather.csv. "
            "Register completion in the terminal log using command 'risk_snapshot_boston' with printed_ts '2024-03-01T13:18:00Z'. "
            "Return the chosen station id, the model AUC and Accuracy, the predictions_csv_path, the processed_dataset_summary (columns, row_count, min_timestamp, max_timestamp), and the terminal log confirmation."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_water_levels_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "risk_snapshot_boston", "exit_code": 0,
                "stdout": "", "stderr": "",
                "printed_message": "risk_snapshot_boston completed",
                "printed_ts": "2024-03-01T13:18:00Z"
            }),
        ],
        outputs=[{
            "primary_station_id": "8443970",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp", "ice_coverage_pct", "snow_depth_mm",
                    "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "logged": {
                "command": "risk_snapshot_boston",
                "exit_code": 0,
                "printed_message": "risk_snapshot_boston completed",
                "printed_ts": "2024-03-01T13:18:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_58",
        instruction=(
            "You are a data‑science automation agent. You need to produce a comparative risk snapshot between Boston and Seattle by applying the Multi‑City Comparative Snapshot Protocol "
            "while honoring policy precedence and determinism. "
            "Boston constraints: you use coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; you confirm tide predictions using method 'harmonic_analysis' for station 8443970 "
            "from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; you reference /data/processed/timeseries_boston_weather.csv and model boston_harbor_model. "
            "Seattle constraints: you use coordinates 47.6062,-122.3321 with a 60.0 km coverage radius; you confirm tide predictions using method 'harmonic_analysis' for station 9447130 "
            "from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; you reference /data/processed/timeseries_seattle_weather.csv and model simple_model. "
            "Return the winning_city and, for each city, the model metrics (AUC and Accuracy), the predictions CSV path, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp). For auditability, you include a completion record labeled 'multi_snapshot_boston-seattle' with exit_code 0, stdout '', stderr '', "
            "printed_message 'multi_snapshot_boston-seattle completed', and printed timestamp 2024-03-01T14:12:50Z."
        ),
        actions=[
            # Boston
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Seattle
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "multi_snapshot_boston-seattle",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "multi_snapshot_boston-seattle completed",
                "printed_ts": "2024-03-01T14:12:50Z"
            }),
        ],
        outputs=[{
            "winning_city": "Seattle",
            "boston": {
                "metrics": {"auc": 0.73, "accuracy": 0.81},
                "predictions_csv_path": "/data/processed/predictions_boston.csv",
                "processed_dataset_summary": {
                    "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                    "row_count": 120,
                    "min_timestamp": "2024-03-01T00:00:00Z",
                    "max_timestamp": "2024-03-06T00:00:00Z"
                }
            },
            "seattle": {
                "metrics": {"auc": 0.79, "accuracy": 0.76},
                "predictions_csv_path": "/processed_data/predictions_simple.csv",
                "processed_dataset_summary": {
                    "columns": ["timestamp", "rainfall_intensity_mmh", "wave_height_m", "lunar_phase_pct", "daylight_hours", "high_risk_flag"],
                    "row_count": 240,
                    "min_timestamp": "2024-02-01T00:00:00Z",
                    "max_timestamp": "2024-02-11T00:00:00Z"
                }
            },
            "terminal_log": {
                "command": "multi_snapshot_boston-seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "multi_snapshot_boston-seattle completed",
                "printed_ts": "2024-03-01T14:12:50Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_59",
        instruction=(
            "You are a data‑science automation agent. You need to decide between Boston and Miami for model promotion under the Cross‑City AUC‑Gap Promotion Protocol "
            "while honoring policy precedence and determinism. You apply an absolute AUC‑gap threshold of 0.04; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Boston constraints: you use coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; you validate tide predictions using method 'harmonic_analysis' for station 8443970 "
            "from 2024‑03‑01T00:00:00Z through 2024‑03‑02T00:00:00Z; you reference /data/processed/timeseries_boston_weather.csv and model boston_harbor_model. "
            "Miami constraints: you use coordinates 25.7617,-80.1918 with a 25.0 km coverage radius; you validate water levels with datum 'NAVD88' for station 8723214 "
            "from 2024‑02‑01T00:00:00Z through 2024‑02‑02T00:00:00Z; you reference /data/processed/timeseries_miami_weather.csv and model flood_risk_miami_v1. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. For auditability, you include a completion record labeled 'ccap_promotion_boston-miami' "
            "with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_boston-miami completed', and printed timestamp 2024‑03‑01T14:13:30Z."
        ),
        actions=[
            # Boston validations & metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            # Miami validations & metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Winner artifacts (Boston)
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Audit log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_boston-miami",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_boston-miami completed",
                "printed_ts": "2024-03-01T14:13:30Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Boston",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_boston-miami",
                "exit_code": 0,
                "printed_message": "ccap_promotion_boston-miami completed",
                "printed_ts": "2024-03-01T14:13:30Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_60",
        instruction=(
            "You are a data-science automation agent. You need to decide a promotion between San Francisco and Miami by applying the Cross-City AUC-Gap Promotion Protocol with this override: "
            "use an AUC gap threshold of 0.12; if |AUC(flood_risk_sf_v2) − AUC(flood_risk_miami_v1)| < 0.12, prefer the city whose validated station condition passes; otherwise choose the city with higher AUC. "
            "Validate for San Francisco that station 9414290 has tide predictions using method 'harmonic' in 2024-03-15T00:00:00Z–2024-03-22T00:00:00Z; "
            "validate for Miami that station 8723214 has water levels with datum 'NAVD88' in 2024-02-01T00:00:00Z–2024-02-02T00:00:00Z. "
            "If San Francisco is chosen, read the processed dataset summary from /data/processed/timeseries_sf_weather.csv; if Miami is chosen, read it from /data/processed/timeseries_miami_weather.csv. "
            "Register completion in the terminal log using command 'ccap_promotion_san-francisco-miami' with printed_ts '2024-03-18T15:45:00Z'. "
            "Return the chosen_city, its metrics (auc, accuracy), its predictions_csv_path, the processed_dataset_summary (columns, row_count, min_timestamp, max_timestamp), and the terminal log confirmation."
        ),
        actions=[
            # SF validations and artifacts
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9414290",
                "window_start_ts": "2024-03-15T00:00:00Z",
                "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # Miami validations and artifacts
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                "station_id": "8723214",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Winner artifacts (SF)
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_san-francisco-miami", "exit_code": 0,
                "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-miami completed",
                "printed_ts": "2024-03-18T15:45:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp", "tide_pred_m", "wind_speed_ms",
                    "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"
                ],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            },
            "logged": {
                "command": "ccap_promotion_san-francisco-miami",
                "exit_code": 0,
                "printed_message": "ccap_promotion_san-francisco-miami completed",
                "printed_ts": "2024-03-18T15:45:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_61",
        instruction=(
            "You are a data‑science automation agent. You need to decide between Miami and Seattle for model promotion under the Cross‑City AUC‑Gap Promotion Protocol "
            "while honoring policy precedence and determinism. You apply an absolute AUC‑gap threshold of 0.07; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Miami constraints: you use coordinates 25.7617,-80.1918 with a 25.0 km coverage radius; you validate water levels with datum 'NAVD88' for station 8723214 from 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z; "
            "you reference /data/processed/timeseries_miami_weather.csv and model flood_risk_miami_v1. "
            "Seattle constraints: you use coordinates 47.6062,-122.3321 with a 60.0 km coverage radius; you validate tide predictions using method 'harmonic_analysis' for station 9447130 from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; "
            "you reference /data/processed/timeseries_seattle_weather.csv and model simple_model. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. For auditability, you include a completion record labeled 'ccap_promotion_miami-seattle' with exit_code 0, stdout '', stderr '', "
            "printed_message 'ccap_promotion_miami-seattle completed', and printed timestamp 2024-02-08T13:04:55Z."
        ),
        actions=[
            # Miami
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Seattle
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            # Winner: Seattle
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_miami-seattle",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_miami-seattle completed",
                "printed_ts": "2024-02-08T13:04:55Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "rainfall_intensity_mmh", "wave_height_m", "lunar_phase_pct", "daylight_hours", "high_risk_flag"],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_miami-seattle",
                "exit_code": 0,
                "printed_message": "ccap_promotion_miami-seattle completed",
                "printed_ts": "2024-02-08T13:04:55Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_62",
        instruction=(
            "You are a data-science automation agent. You need to apply the System Audit and Provenance Protocol for San Francisco with these overrides: "
            "validate the exact terminal command \"jupyter nbconvert --to html notebooks/exploratory_analysis.ipynb\"; "
            "restrict MCP tool call retrieval to the 'gmail' server; "
            "use /processed_data/features.csv with model flood_risk_sf_v2 and verify the configuration text at /config/model_config.json; "
            "publish an audit receipt to stakeholder outputs using /results/predictions_sf_v2.csv and /results/metrics_sf_v2.csv with generated_ts equal to the metrics.generated_ts of flood_risk_sf_v2, "
            "and register the audit completion in the terminal log using the exact command 'audit_provenance_san-francisco' and the same metrics timestamp as printed_ts. "
            "Return the audit report including: 7-day weather forecast details, features record, model record, configuration file text, the validated terminal command result, the bounded MCP calls slice for server 'gmail', "
            "the Gmail message with subject 'San Francisco Flood Risk Analysis - Complete Results', the published receipt, and the terminal log confirmation."
        ),
        actions=[
            Action(name="get_weather_forecast_by_city", kwargs={
                   "city": "San Francisco", "horizon_days": 7}),
            Action(name="get_features_by_csv_path", kwargs={
                   "csv_path": "/processed_data/features.csv"}),
            Action(name="get_model_by_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            Action(name="get_file_text_by_path", kwargs={
                   "path": "/config/model_config.json"}),
            Action(name="get_terminal_log_command_result", kwargs={
                "command": "jupyter nbconvert --to html notebooks/exploratory_analysis.ipynb"}),
            Action(name="get_mcp_tool_calls_by_server",
                   kwargs={"server_name": "gmail"}),
            Action(name="get_gmail_message_by_subject", kwargs={
                "subject": "San Francisco Flood Risk Analysis - Complete Results"}),
            Action(name="publish_stakeholder_outputs", kwargs={
                "predictions_final_csv_path": "/results/predictions_sf_v2.csv",
                "metrics_summary_csv_path": "/results/metrics_sf_v2.csv",
                "generated_ts": "2024-03-18T15:45:00Z"
            }),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "audit_provenance_san-francisco", "exit_code": 0,
                "stdout": "", "stderr": "",
                "printed_message": "audit_provenance_san-francisco completed",
                "printed_ts": "2024-03-18T15:45:00Z"
            }),
        ],
        outputs=[{
            "weather": {"city": "San Francisco", "horizon_days": 7},
            "features": {"csv_path": "/processed_data/features.csv"},
            "model": {"model_name": "flood_risk_sf_v2"},
            "config_text": {"path": "/config/model_config.json"},
            "terminal": {"command": "jupyter nbconvert --to html notebooks/exploratory_analysis.ipynb"},
            "mcp_calls": {"server": "gmail"},
            "gmail_message": {"subject": "San Francisco Flood Risk Analysis - Complete Results"},
            "published": {
                "predictions_final_csv_path": "/results/predictions_sf_v2.csv",
                "metrics_summary_csv_path": "/results/metrics_sf_v2.csv",
                "generated_ts": "2024-03-18T15:45:00Z"
            },
            "logged": {
                "command": "audit_provenance_san-francisco",
                "exit_code": 0,
                "printed_message": "audit_provenance_san-francisco completed",
                "printed_ts": "2024-03-18T15:45:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_63",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Seattle and Miami for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.06; when the gap is below this threshold, you prefer the city whose "
            "validated station condition passes; if both pass, you choose the city with the most recent metrics.generated_ts. "
            "City constraints: Seattle is at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station is "
            "resolved from that location context and must validate tide predictions using method 'harmonic_analysis' available from "
            "2024‑02‑01T00:00:00Z through 2024‑02‑08T00:00:00Z; the processed dataset is /data/processed/timeseries_seattle_weather.csv "
            "(window 2024‑02‑01T00:00:00Z to 2024‑02‑11T00:00:00Z, row_count 240); the model of record is simple_model. "
            "Miami is at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station is resolved from that "
            "location context and must validate water levels with datum 'NAVD88' available from 2024‑02‑01T00:00:00Z through 2024‑02‑02T00:00:00Z; "
            "the processed dataset is /data/processed/timeseries_miami_weather.csv; the model of record is flood_risk_miami_v1. "
            "Your deliverable returns only the chosen city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, "
            "and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, include a completion record labeled 'ccap_promotion_seattle-miami' with exit_code 0 and printed timestamp "
            "2024‑02‑08T12:42:00Z."
        ),
        actions=[
            # Resolve & validate Seattle
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            # Resolve & validate Miami
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Winner artifacts (gap == 0.06 ⇒ not below threshold ⇒ choose higher AUC: Seattle)
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_seattle-miami", "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_seattle-miami completed", "printed_ts": "2024-02-08T12:42:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "rainfall_intensity_mmh", "wave_height_m", "lunar_phase_pct", "daylight_hours", "high_risk_flag"],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0,
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T12:42:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_64",
        instruction=(
            "You are a data‑science automation agent operating under the Primary Station Determination Protocol. "
            "You need to determine the primary NOAA station for Boston while honoring policy precedence and determinism. "
            "You use coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; you confirm that station 8443970 has tide predictions using method 'harmonic_analysis' in the window "
            "2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z and water levels with datum 'NAVD88' across 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z before confirming the primary selection. "
            "You reference /data/processed/timeseries_boston_weather.csv and model boston_harbor_model. "
            "Your deliverable includes the primary_station_id, the model metrics (AUC and Accuracy), the predictions CSV path, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp). For auditability, you include a completion record labeled 'station_determination_boston' "
            "with exit_code 0 and printed timestamp 2024‑03‑01T14:16:10Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={"query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={"station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_water_levels_window", kwargs={"station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_predictions_by_model_name", kwargs={"model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={"model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={"csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "station_determination_boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "station_determination_boston completed",
                "printed_ts": "2024-03-01T14:16:10Z"
            }),
        ],
        outputs=[{
            "primary_station_id": "8443970",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp","ice_coverage_pct","snow_depth_mm","temperature_feels_like_c","pressure_tendency_hpa_3h","high_risk_flag"],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "station_determination_boston",
                "exit_code": 0,
                "printed_message": "station_determination_boston completed",
                "printed_ts": "2024-03-01T14:16:10Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_65",
        instruction=(
            "You are a data‑science automation agent. Your objective is to prepare a time‑based dataset split for Seattle while honoring "
            "policy precedence and determinism. You operate under the Modeling & Risk Protocol — Data Preparation (Time‑Based Partitioning Rule), "
            "selecting this policy explicitly for partitioning. You work with the processed dataset at /data/processed/timeseries_seattle_weather.csv "
            "(covering 2024‑02‑01T00:00:00Z to 2024‑02‑11T00:00:00Z, row_count 240). You apply the Seattle test‑fraction defined by policy; "
            "where multiple values are permitted, you resolve the choice via the city‑level override to 0.15. "
            "You record the split deterministically using the split timestamp 2024‑02‑08T12:31:00Z and the canonical naming convention for "
            "Seattle split summaries defined by policy. Your deliverable is a structured, machine‑verifiable summary of the split and a brief "
            "overview of the referenced processed dataset; you do not enumerate tool names or prescribe steps. For auditability, include a "
            "completion record labeled 'dataset_split_seattle_v5' with exit_code 0 and printed timestamp 2024‑02‑08T12:31:00Z."
        ),
        actions=[
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="create_time_based_dataset_split", kwargs={
                "processed_csv_path": "/data/processed/timeseries_seattle_weather.csv",
                "test_fraction": 0.15,
                "split_summary_json_path": "/processed_data/split_summary_seattle_v5.json",
                "split_ts": "2024-02-08T12:31:00Z"
            }),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "dataset_split_seattle_v5", "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "dataset_split_seattle_v5 completed", "printed_ts": "2024-02-08T12:31:00Z"
            }),
        ],
        outputs=[{
            "city": "Seattle",
            "dataset_split": {"method": "time_based", "test_fraction": 0.15, "train_index_count": 204, "test_index_count": 36, "split_summary_json_path": "/processed_data/split_summary_seattle_v5.json"},
            "processed_dataset_summary": {
                "columns": ["timestamp", "rainfall_intensity_mmh", "wave_height_m", "lunar_phase_pct", "daylight_hours", "high_risk_flag"],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "dataset_split_seattle_v5",
                "exit_code": 0,
                "printed_message": "dataset_split_seattle_v5 completed",
                "printed_ts": "2024-02-08T12:31:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_66",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "You need to produce a status snapshot for Boston while honoring policy precedence and determinism. "
            "Use coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; confirm tide predictions using method 'harmonic_analysis' for station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z "
            "and water levels with datum 'NAVD88' from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z. "
            "Use /data/processed/timeseries_boston_weather.csv and model boston_harbor_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path, the model metrics (AUC and Accuracy), and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp). For auditability, you include a completion record labeled 'status_compilation_boston' with exit_code 0, stdout '', stderr '', "
            "printed_message 'status_compilation_boston completed', and printed timestamp 2024-03-01T14:07:00Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T14:07:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "primary_station_id": "8443970",
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "processed_dataset_summary": {
                "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_compilation_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T14:07:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_67",
        instruction=(
            "You are a data‑science automation agent. You need to decide between Boston and Seattle for model promotion under the Cross‑City AUC‑Gap Promotion Protocol "
            "while honoring policy precedence and determinism. You apply an absolute AUC‑gap threshold of 0.08; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Boston constraints: you use coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; you validate tide predictions using method 'harmonic_analysis' for station 8443970 "
            "from 2024‑03‑01T00:00:00Z through 2024‑03‑02T00:00:00Z; you reference /data/processed/timeseries_boston_weather.csv and model boston_harbor_model. "
            "Seattle constraints: you use coordinates 47.6062,-122.3321 with a 60.0 km coverage radius; you validate tide predictions using method 'harmonic_analysis' for station 9447130 "
            "from 2024‑02‑01T00:00:00Z through 2024‑02‑08T00:00:00Z; you reference /data/processed/timeseries_seattle_weather.csv and model simple_model. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. For auditability, you include a completion record labeled 'ccap_promotion_boston-seattle' "
            "with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_boston-seattle completed', and printed timestamp 2024‑03‑01T14:08:00Z."
        ),
        actions=[
            # Boston
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            # Seattle
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            # Winner: Seattle
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_boston-seattle",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_boston-seattle completed",
                "printed_ts": "2024-03-01T14:08:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "rainfall_intensity_mmh", "wave_height_m", "lunar_phase_pct", "daylight_hours", "high_risk_flag"],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_boston-seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_boston-seattle completed",
                "printed_ts": "2024-03-01T14:08:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_68",
        instruction=(
            "You are a data‑science automation agent. You need to decide between Seattle and Miami for model promotion under the Cross‑City AUC‑Gap Promotion Protocol "
            "while honoring policy precedence and determinism. You apply an absolute AUC‑gap threshold of 0.10; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Seattle constraints: coordinates 47.6062,-122.3321 with a 60.0 km coverage radius; validate tide predictions using method 'harmonic_analysis' for station 9447130 from 2024‑02‑01T00:00:00Z to 2024‑02‑08T00:00:00Z; "
            "processed dataset /data/processed/timeseries_seattle_weather.csv; model simple_model. "
            "Miami constraints: coordinates 25.7617,-80.1918 with a 25.0 km coverage radius; validate water levels with datum 'NAVD88' for station 8723214 from 2024‑02‑01T00:00:00Z to 2024‑02‑02T00:00:00Z; "
            "processed dataset /data/processed/timeseries_miami_weather.csv; model flood_risk_miami_v1. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. For auditability, you include a completion record labeled 'ccap_promotion_seattle-miami' with exit_code 0, stdout '', stderr '', "
            "printed_message 'ccap_promotion_seattle-miami completed', and printed timestamp 2024‑02‑08T13:02:00Z."
        ),
        actions=[
            # Seattle validations & metrics
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            # Miami validations & metrics
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_miami_v1"}),
            # Winner: Seattle
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T13:02:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "rainfall_intensity_mmh", "wave_height_m", "lunar_phase_pct", "daylight_hours", "high_risk_flag"],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0,
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T13:02:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_69",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "You need to produce a status snapshot for Boston while honoring policy precedence and determinism. "
            "You use coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; you confirm tide predictions using method 'harmonic_analysis' for station 8443970 "
            "from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z and water levels with datum 'NAVD88' from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z; "
            "you reference /data/processed/timeseries_boston_weather.csv and model boston_harbor_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics (AUC and Accuracy), and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp). For auditability, you include a completion record labeled 'status_compilation_boston' with exit_code 0, stdout '', stderr '', "
            "printed_message 'status_compilation_boston completed', and printed timestamp 2024-03-01T14:10:30Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T14:10:30Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "primary_station_id": "8443970",
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "processed_dataset_summary": {
                "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_compilation_boston",
                "exit_code": 0,
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T14:10:30Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_70",
        instruction=(
            "You are a data‑science automation agent. You need to decide between San Francisco and Miami for model promotion under the Cross‑City AUC‑Gap Promotion Protocol "
            "while honoring policy precedence and determinism. You apply an absolute AUC‑gap threshold of 0.06; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "San Francisco constraints: you use coordinates 37.7749,-122.4194 with a 50.0 km coverage radius; you validate tide predictions using method 'harmonic_analysis' for station 9414290 "
            "from 2024-03-15T00:00:00Z through 2024-03-22T00:00:00Z; you reference /data/processed/timeseries_sf_weather.csv and model flood_risk_sf_v2. "
            "Miami constraints: you use coordinates 25.7617,-80.1918 with a 25.0 km coverage radius; you validate water levels with datum 'NAVD88' for station 8723214 "
            "from 2024-02-01T00:00:00Z through 2024-02-02T00:00:00Z; you reference /data/processed/timeseries_miami_weather.csv and model flood_risk_miami_v1. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. For auditability, you include a completion record labeled 'ccap_promotion_san-francisco-miami' "
            "with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_san-francisco-miami completed', and printed timestamp 2024-03-18T16:28:10Z."
        ),
        actions=[
            # SF validations & metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # Miami validations & metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Winner artifacts (San Francisco)
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_san-francisco-miami",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-miami completed",
                "printed_ts": "2024-03-18T16:28:10Z"
            }),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "tide_pred_m", "wind_speed_ms", "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_san-francisco-miami",
                "exit_code": 0,
                "printed_message": "ccap_promotion_san-francisco-miami completed",
                "printed_ts": "2024-03-18T16:28:10Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_71",
        instruction=(
            "You are a data‑science automation agent. You need to decide between San Francisco and Boston for model promotion under the Cross‑City AUC‑Gap Promotion Protocol "
            "while honoring policy precedence and determinism. You apply an absolute AUC‑gap threshold of 0.07; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "San Francisco constraints: you use coordinates 37.7749,-122.4194 with a 50.0 km coverage radius; you validate tide predictions using method 'harmonic_analysis' for station 9414290 "
            "from 2024-03-15T00:00:00Z through 2024-03-22T00:00:00Z; you reference /data/processed/timeseries_sf_weather.csv and model flood_risk_sf_v2. "
            "Boston constraints: you use coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; you validate tide predictions using method 'harmonic_analysis' for station 8443970 "
            "from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; you reference /data/processed/timeseries_boston_weather.csv and model boston_harbor_model. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. For auditability, you include a completion record labeled 'ccap_promotion_san-francisco-boston' "
            "with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_san-francisco-boston completed', and printed timestamp 2024-03-18T16:21:00Z."
        ),
        actions=[
            # San Francisco
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_sf_v2"}),
            # Boston
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            # Winner: San Francisco
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_san-francisco-boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-boston completed",
                "printed_ts": "2024-03-18T16:21:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "tide_pred_m", "wind_speed_ms", "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_san-francisco-boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-boston completed",
                "printed_ts": "2024-03-18T16:21:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_72",
        instruction=(
            "You are a data‑science automation agent operating under the City Risk Snapshot Protocol. "
            "You need to produce a risk snapshot for Boston while honoring policy precedence and determinism. "
            "Use coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; confirm tide predictions using method 'harmonic_analysis' for station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z "
            "and water levels with datum 'NAVD88' from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z. "
            "Use /data/processed/timeseries_boston_weather.csv (row_count 120; coverage 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z) and model boston_harbor_model. "
            "Your deliverable includes the primary_station_id, the model metrics (AUC and Accuracy), the predictions CSV path, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, you include a completion record labeled 'risk_snapshot_boston' with exit_code 0, stdout '', stderr '', "
            "printed_message 'risk_snapshot_boston completed', and printed timestamp 2024-03-01T14:05:00Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_water_levels_window", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_predictions_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "risk_snapshot_boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "risk_snapshot_boston completed",
                "printed_ts": "2024-03-01T14:05:00Z"
            }),
        ],
        outputs=[{
            "primary_station_id": "8443970",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "risk_snapshot_boston",
                "exit_code": 0,
                "printed_message": "risk_snapshot_boston completed",
                "printed_ts": "2024-03-01T14:05:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_73",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between San Francisco and Boston for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.05; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "City constraints: San Francisco is at coordinates 37.7749,-122.4194 with a coverage radius of 50.0 km; the primary coastal station is resolved from that location context and must validate "
            "tide predictions using method 'harmonic' available from 2024-03-15T00:00:00Z through 2024-03-22T00:00:00Z; the processed dataset is "
            "/data/processed/timeseries_sf_weather.csv; the model of record is flood_risk_sf_v2. "
            "Boston is at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station is resolved from that location context and must validate "
            "tide predictions using method 'harmonic' available from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; the processed dataset is "
            "/data/processed/timeseries_boston_weather.csv; the model of record is boston_harbor_model. "
            "If San Francisco is chosen you read the processed‑dataset summary from /data/processed/timeseries_sf_weather.csv; if Boston is chosen you read it from "
            "/data/processed/timeseries_boston_weather.csv. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions_csv_path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, include a completion record labeled 'ccap_promotion_san-francisco-boston' with exit_code 0, stdout '', stderr '', "
            "printed_message 'ccap_promotion_san-francisco-boston completed', and printed timestamp 2024-03-18T15:55:00Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0
            }),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9414290",
                "window_start_ts": "2024-03-15T00:00:00Z",
                "window_end_ts": "2024-03-22T00:00:00Z"
            }),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),

            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),

            # Winner: San Francisco (AUC 0.89 > 0.73)
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"
            }),

            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_san-francisco-boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-boston completed",
                "printed_ts": "2024-03-18T15:55:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp", "tide_pred_m", "wind_speed_ms",
                    "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"
                ],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_san-francisco-boston",
                "exit_code": 0,
                "printed_message": "ccap_promotion_san-francisco-boston completed",
                "printed_ts": "2024-03-18T15:55:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_74",
        instruction=(
            "You are a data‑science automation agent. You need to decide between Seattle and Boston for model promotion under the Cross‑City AUC‑Gap Promotion Protocol "
            "while honoring policy precedence and determinism. You apply an absolute AUC‑gap threshold of 0.06; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Seattle constraints: coordinates 47.6062,-122.3321 with a 60.0 km coverage radius; validate tide predictions using method 'harmonic_analysis' for station 9447130 from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; "
            "dataset /data/processed/timeseries_seattle_weather.csv; model simple_model. "
            "Boston constraints: coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; validate tide predictions using method 'harmonic_analysis' for station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; "
            "dataset /data/processed/timeseries_boston_weather.csv; model boston_harbor_model. "
            "Return only the chosen_city, its model metrics (AUC and Accuracy), its predictions CSV path, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, you include a completion record labeled 'ccap_promotion_seattle-boston' with exit_code 0, stdout '', stderr '', "
            "printed_message 'ccap_promotion_seattle-boston completed', and printed timestamp 2024-03-01T14:06:00Z."
        ),
        actions=[
            # Seattle
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            # Boston
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            # Winner: Seattle
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-03-01T14:06:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "rainfall_intensity_mmh", "wave_height_m", "lunar_phase_pct", "daylight_hours", "high_risk_flag"],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0,
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-03-01T14:06:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_75",
        instruction=(
            "You are a data‑science automation agent. You need to produce a station confirmation snapshot for Boston by applying the Datum‑and‑Method Station Confirmation Protocol, "
            "honoring policy precedence and determinism. You operate with the following constraints: coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; "
            "the candidate station 8443970 must validate water levels with datum 'NAVD88' from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z and tide predictions with method 'harmonic_analysis' "
            "from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; the processed dataset is /data/processed/timeseries_boston_weather.csv; the model of record is boston_harbor_model. "
            "Your deliverable includes the chosen_station_id, the model metrics (AUC and Accuracy), the predictions_csv_path, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, include a completion record labeled 'dmsc_snapshot_boston' with exit_code 0, stdout '', stderr '', "
            "printed_message 'dmsc_snapshot_boston completed', and printed timestamp 2024-03-01T13:29:00Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            Action(name="get_water_levels_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-06T00:00:00Z"
            }),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "dmsc_snapshot_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dmsc_snapshot_boston completed",
                "printed_ts": "2024-03-01T13:29:00Z"
            }),
        ],
        outputs=[{
            "chosen_station_id": "8443970",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp", "ice_coverage_pct", "snow_depth_mm",
                    "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "dmsc_snapshot_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dmsc_snapshot_boston completed",
                "printed_ts": "2024-03-01T13:29:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_76",
        instruction=(
            "You are a data‑science automation agent. You need to determine the primary NOAA station for Seattle by applying the Primary Station Determination Protocol while honoring policy precedence and determinism. "
            "Use coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; confirm that station 9447130 has tide predictions using method 'harmonic_analysis' in the window "
            "2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z before confirming the primary selection. "
            "Use /data/processed/timeseries_seattle_weather.csv as the processed dataset and simple_model as the model of record. "
            "Your deliverable includes the primary_station_id, the model metrics (AUC and Accuracy), the predictions_csv_path, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, include a completion record labeled 'station_determination_seattle' with exit_code 0, stdout '', stderr '', "
            "printed_message 'station_determination_seattle completed', and printed timestamp 2024-02-08T12:46:00Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "station_determination_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "station_determination_seattle completed",
                "printed_ts": "2024-02-08T12:46:00Z"
            }),
        ],
        outputs=[{
            "primary_station_id": "9447130",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp", "rainfall_intensity_mmh", "wave_height_m",
                    "lunar_phase_pct", "daylight_hours", "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "station_determination_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "station_determination_seattle completed",
                "printed_ts": "2024-02-08T12:46:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_77",
        instruction=(
            "You are a data-science automation agent. Produce a comparative risk snapshot between San Francisco and Boston by applying the Multi-City Comparative Snapshot Protocol with these overrides: "
            "for San Francisco, confirm that tide predictions for station 9414290 in the window 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z use method 'harmonic'; "
            "for Boston, confirm that water levels for station 8443970 in the window 2024-02-15T00:00:00Z to 2024-03-16T00:00:00Z have datum 'NAVD88'; "
            "if the AUC difference between flood_risk_sf_v2 and boston_harbor_model is below 0.02, prefer the city whose validated station passes its check; otherwise choose the city with higher AUC. "
            "Return the chosen city, the model AUC and Accuracy, the predictions CSV path, and the processed dataset summary from /data/processed/timeseries_<city>_weather.csv for the chosen city. "
            "Use the configured station search distance from project_config for each city and use 2024-03-18T15:45:00Z as the printed timestamp for the terminal log entry. "
            "Use coordinates 37.7749,-122.4194 with radius 50.0 for San Francisco and coordinates 42.3601,-71.0589 with radius 40.0 for Boston."
        ),
        actions=[
            Action(name="get_project_config_by_city",
                   kwargs={"target_city": "San Francisco"}),
            Action(
                name="get_stations_by_location",
                kwargs={"query_latitude": 37.7749,
                        "query_longitude": -122.4194, "radius_km": 50.0}
            ),
            Action(
                name="get_tide_predictions_window",
                kwargs={
                    "station_id": "9414290",
                    "window_start_ts": "2024-03-15T00:00:00Z",
                    "window_end_ts": "2024-03-22T00:00:00Z"
                }
            ),
            Action(
                name="get_processed_timeseries_summary",
                kwargs={"csv_path": "/data/processed/timeseries_sf_weather.csv"}
            ),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "flood_risk_sf_v2"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_project_config_by_city",
                   kwargs={"target_city": "Boston"}),
            Action(
                name="get_stations_by_location",
                kwargs={"query_latitude": 42.3601,
                        "query_longitude": -71.0589, "radius_km": 40.0}
            ),
            Action(
                name="get_water_levels_window",
                kwargs={
                    "station_id": "8443970",
                    "window_start_ts": "2024-02-15T00:00:00Z",
                    "window_end_ts": "2024-03-16T00:00:00Z"
                }
            ),
            Action(
                name="get_processed_timeseries_summary",
                kwargs={"csv_path": "/data/processed/timeseries_boston_weather.csv"}
            ),
            Action(name="get_metrics_by_model_name", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(
                name="append_terminal_log_entry",
                kwargs={
                    "command": "multi_snapshot_san-francisco-boston",
                    "exit_code": 0,
                    "stdout": "",
                    "stderr": "",
                    "printed_message": "multi_snapshot_san-francisco-boston completed",
                    "printed_ts": "2024-03-18T15:45:00Z"
                }
            ),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "csv_path": "/data/processed/timeseries_sf_weather.csv",
                "columns": [
                    "timestamp",
                    "tide_pred_m",
                    "wind_speed_ms",
                    "precipitation_mm_hr",
                    "pressure_hpa",
                    "temperature_c",
                    "high_risk_flag"
                ],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="Task_78",
        instruction="You are the audit lead for San Francisco. Apply the System Audit and Provenance Protocol with the following overrides and constraints: restrict MCP evidence to the 'weather-api' server; accept NOAA station 9414290 with harmonic tide predictions for 2024-03-15T00:00:00Z–2024-03-22T00:00:00Z and MLLW water-level history for 2024-02-14T00:00:00Z–2024-03-15T00:00:00Z; include a 7-day weather forecast for San Francisco; require the Gmail message with subject 'Weekly Progress Update - Flood Prediction Project' as external communication proof; confirm that the training/evaluation run 'python src/models/train_model.py --config config/model_config.json' completed successfully; and finalize by recording the checkpoint 'promotion_sf_model' with exit_code 0, stdout 'promotion audit checkpoint', stderr 'none', printed_message 'promotion approved', and printed_ts '2024-03-17T12:50:00Z'. Provide a concise audit report that cites each evidence source and states whether the protocol criteria are satisfied.",
        actions=[
            Action(name="get_mcp_tool_calls_by_server",
                   kwargs={"server_name": "weather-api"}),
            Action(name="get_weather_forecast_by_city", kwargs={
                "city": "San Francisco", "horizon_days": 7}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9414290",
                "window_start_ts": "2024-03-15T00:00:00Z",
                "window_end_ts": "2024-03-22T00:00:00Z"
            }),
            Action(name="get_water_levels_window", kwargs={
                "station_id": "9414290",
                "window_start_ts": "2024-02-14T00:00:00Z",
                "window_end_ts": "2024-03-15T00:00:00Z"
            }),
            Action(name="get_gmail_message_by_subject", kwargs={
                "subject": "Weekly Progress Update - Flood Prediction Project"}),
            Action(name="get_terminal_log_command_result", kwargs={
                "command": "python src/models/train_model.py --config config/model_config.json"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "promotion_sf_model",
                "exit_code": 0,
                "stdout": "promotion audit checkpoint",
                "stderr": "none",
                "printed_message": "promotion approved",
                "printed_ts": "2024-03-17T12:50:00Z"
            })
        ],
        outputs=[{
            "mcp_scope": "weather-api",
            "forecast_city": "San Francisco",
            "noaa_station": "9414290",
            "tide_window": ["2024-03-15T00:00:00Z", "2024-03-22T00:00:00Z"],
            "water_level_window": ["2024-02-14T00:00:00Z", "2024-03-15T00:00:00Z"],
            "gmail_subject": "Weekly Progress Update - Flood Prediction Project",
            "validated_command": "python src/models/train_model.py --config config/model_config.json",
            "audit_checkpoint": {
                "command": "promotion_sf_model",
                "exit_code": 0,
                "stdout": "promotion audit checkpoint",
                "stderr": "none",
                "printed_message": "promotion approved",
                "printed_ts": "2024-03-17T12:50:00Z"
            },
            "protocol_status": "criteria evaluated with all evidence present"
        }]
    ),
    Task(
        annotator="0",
        user_id="task_79",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Boston and Seattle for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.04; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Boston constraints: coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; station validation requires tide predictions using method 'harmonic_analysis' available from "
            "2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; processed dataset /data/processed/timeseries_boston_weather.csv; model boston_harbor_model. "
            "Seattle constraints: coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; station validation requires tide predictions using method 'harmonic_analysis' available from "
            "2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; processed dataset /data/processed/timeseries_seattle_weather.csv; model simple_model. "
            "If Seattle is chosen you read the processed‑dataset summary from /data/processed/timeseries_seattle_weather.csv; if Boston is chosen you read it from "
            "/data/processed/timeseries_boston_weather.csv. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions_csv_path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, include a completion record labeled 'ccap_promotion_boston-seattle' with exit_code 0, stdout '', stderr '', "
            "printed_message 'ccap_promotion_boston-seattle completed', and printed timestamp 2024-03-01T13:40:00Z."
        ),
        actions=[
            # Boston
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),

            # Seattle
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),

            # Winner: Seattle
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_boston-seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_boston-seattle completed",
                "printed_ts": "2024-03-01T13:40:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp", "rainfall_intensity_mmh", "wave_height_m",
                    "lunar_phase_pct", "daylight_hours", "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_boston-seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_boston-seattle completed",
                "printed_ts": "2024-03-01T13:40:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_80",
        instruction=(
            "You are a data‑science automation agent. You need to produce a risk snapshot for Seattle by applying the City Risk Snapshot Protocol while honoring policy precedence and determinism. "
            "Use coordinates 47.6062,-122.3321 with coverage radius 60.0 km and confirm tide predictions using method 'harmonic_analysis' for station 9447130 in the window 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z. "
            "Use /data/processed/timeseries_seattle_weather.csv as the processed dataset and simple_model as the model of record. "
            "Your deliverable includes the primary_station_id, the model metrics (AUC and Accuracy), the predictions_csv_path, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, include a completion record labeled 'risk_snapshot_seattle' with exit_code 0, stdout '', stderr '', "
            "printed_message 'risk_snapshot_seattle completed', and printed timestamp 2024-02-08T12:47:00Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "risk_snapshot_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "risk_snapshot_seattle completed",
                "printed_ts": "2024-02-08T12:47:00Z"
            }),
        ],
        outputs=[{
            "primary_station_id": "9447130",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp", "rainfall_intensity_mmh", "wave_height_m",
                    "lunar_phase_pct", "daylight_hours", "high_risk_flag"
                ],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "risk_snapshot_seattle",
                "exit_code": 0,
                "printed_message": "risk_snapshot_seattle completed",
                "printed_ts": "2024-02-08T12:47:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_81",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a status snapshot for Boston while honoring policy precedence and determinism. "
            "Use coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km and confirm that the primary coastal station validates tide predictions using method "
            "'harmonic_analysis' from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z. "
            "Use /data/processed/timeseries_boston_weather.csv (row_count 120; coverage 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z) as the processed dataset and boston_harbor_model as the model of record. "
            "Your deliverable includes the city, the primary_station_id, the model metrics (AUC and Accuracy), the predictions_csv_path, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, include a completion record labeled 'status_compilation_boston' with exit_code 0, stdout '', stderr '', "
            "printed_message 'status_compilation_boston completed', and printed timestamp 2024-03-01T13:41:00Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:41:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "primary_station_id": "8443970",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {
                "columns": [
                    "timestamp", "ice_coverage_pct", "snow_depth_mm",
                    "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"
                ],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_compilation_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:41:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_82",
        instruction=(
            "You are a data‑science automation agent. Your objective is to produce a comparative risk snapshot between San Francisco and Seattle by applying the Multi‑City Comparative Snapshot Protocol, "
            "honoring policy precedence and determinism. "
            "San Francisco constraints: coordinates 37.7749,-122.4194 with coverage radius 50.0 km; validate tide predictions using method 'harmonic' from 2024‑03‑15T00:00:00Z to 2024‑03‑22T00:00:00Z; "
            "processed dataset /data/processed/timeseries_sf_weather.csv; model flood_risk_sf_v2. "
            "Seattle constraints: coordinates 47.6062,-122.3321 with coverage radius 60.0 km; validate tide predictions using method 'harmonic' from 2024‑02‑01T00:00:00Z to 2024‑02‑08T00:00:00Z; "
            "processed dataset /data/processed/timeseries_seattle_weather.csv; model simple_model. "
            "Return the winning_city and, for each city, the model metrics (AUC and Accuracy), the predictions_csv_path, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, you include a completion record labeled 'multi_snapshot_san-francisco-seattle' with exit_code 0 and printed timestamp 2024‑03‑18T16:20:00Z."
        ),
        actions=[
            # San Francisco
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),

            # Seattle
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),

            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "multi_snapshot_san-francisco-seattle",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "multi_snapshot_san-francisco-seattle completed",
                "printed_ts": "2024-03-18T16:20:00Z"
            }),
        ],
        outputs=[{
            "winning_city": "San Francisco",
            "san_francisco": {
                "metrics": {"auc": 0.89, "accuracy": 0.85},
                "predictions_csv_path": "/results/predictions_sf_v2.csv",
                "processed_dataset_summary": {
                    "columns": ["timestamp", "tide_pred_m", "wind_speed_ms", "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"],
                    "row_count": 168,
                    "min_timestamp": "2024-03-15T00:00:00Z",
                    "max_timestamp": "2024-03-22T00:00:00Z"
                }
            },
            "seattle": {
                "metrics": {"auc": 0.79, "accuracy": 0.76},
                "predictions_csv_path": "/processed_data/predictions_simple.csv",
                "processed_dataset_summary": {
                    "columns": ["timestamp", "rainfall_intensity_mmh", "wave_height_m", "lunar_phase_pct", "daylight_hours", "high_risk_flag"],
                    "row_count": 240,
                    "min_timestamp": "2024-02-01T00:00:00Z",
                    "max_timestamp": "2024-02-11T00:00:00Z"
                }
            },
            "terminal_log": {
                "command": "multi_snapshot_san-francisco-seattle",
                "exit_code": 0,
                "printed_message": "multi_snapshot_san-francisco-seattle completed",
                "printed_ts": "2024-03-18T16:20:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_83",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between San Francisco and Miami for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.09; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "San Francisco is at coordinates 37.7749,-122.4194 with a coverage radius of 50.0 km; the primary coastal station is resolved from that location context and must validate "
            "tide predictions using method 'harmonic_analysis' available from 2024‑03‑15T00:00:00Z through 2024‑03‑22T00:00:00Z; the processed dataset is "
            "/data/processed/timeseries_sf_weather.csv; the model of record is flood_risk_sf_v2. "
            "Miami is at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station is resolved from that location context and must validate "
            "water levels with datum 'NAVD88' available from 2024‑02‑01T00:00:00Z through 2024‑02‑02T00:00:00Z; the processed dataset is "
            "/data/processed/timeseries_miami_weather.csv; the model of record is flood_risk_miami_v1. "
            "If San Francisco is chosen you read the processed‑dataset summary from /data/processed/timeseries_sf_weather.csv; if Miami is chosen you read it from "
            "/data/processed/timeseries_miami_weather.csv. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions_csv_path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, include a completion record labeled 'ccap_promotion_san-francisco-miami' with exit_code 0, stdout '', stderr '', "
            "printed_message 'ccap_promotion_san-francisco-miami completed', and printed timestamp 2024‑03‑18T16:01:00Z."
        ),
        actions=[
            # San Francisco validations and metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),

            # Miami validations and metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_miami_v1"}),

            # Winner artifacts (AUC 0.89 − 0.73 ≥ 0.09 ⇒ San Francisco)
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),

            # Deterministic audit record
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_san-francisco-miami",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-miami completed",
                "printed_ts": "2024-03-18T16:01:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "tide_pred_m", "wind_speed_ms", "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_san-francisco-miami",
                "exit_code": 0,
                "printed_message": "ccap_promotion_san-francisco-miami completed",
                "printed_ts": "2024-03-18T16:01:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_84",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Boston and San Francisco for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.06; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Boston is at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station is resolved from that location context and must validate "
            "tide predictions using method 'harmonic_analysis' available from 2024‑03‑01T00:00:00Z through 2024‑03‑02T00:00:00Z; the processed dataset is "
            "/data/processed/timeseries_boston_weather.csv; the model of record is boston_harbor_model. "
            "San Francisco is at coordinates 37.7749,-122.4194 with a coverage radius of 50.0 km; the primary coastal station is resolved from that location context and must validate "
            "tide predictions using method 'harmonic_analysis' available from 2024‑03‑15T00:00:00Z through 2024‑03‑22T00:00:00Z; the processed dataset is "
            "/data/processed/timeseries_sf_weather.csv; the model of record is flood_risk_sf_v2. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions_csv_path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, include a completion record labeled 'ccap_promotion_boston-san-francisco' with exit_code 0, stdout '', stderr '', "
            "printed_message 'ccap_promotion_boston-san-francisco completed', and printed timestamp 2024‑03‑18T16:02:00Z."
        ),
        actions=[
            # Boston validation and metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),

            # San Francisco validation and metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),

            # Winner artifacts (AUC 0.89 − 0.73 ≥ 0.06 ⇒ San Francisco)
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),

            # Audit
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_boston-san-francisco",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_boston-san-francisco completed",
                "printed_ts": "2024-03-18T16:02:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "tide_pred_m", "wind_speed_ms", "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_boston-san-francisco",
                "exit_code": 0,
                "printed_message": "ccap_promotion_boston-san-francisco completed",
                "printed_ts": "2024-03-18T16:02:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_85",
        instruction=(
            "You are a data‑science automation agent operating under the City Risk Snapshot Protocol. "
            "Your objective is to produce a risk snapshot for Boston while honoring policy precedence and determinism. "
            "You operate with the following constraints: the city is Boston at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; "
            "you confirm tide predictions using method 'harmonic_analysis' for station 8443970 in the window 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z, "
            "and you confirm water levels with datum 'NAVD88' for the same station across 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z; "
            "the processed dataset is /data/processed/timeseries_boston_weather.csv (row_count 120; coverage 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z); "
            "the model of record is boston_harbor_model. "
            "Your deliverable includes the primary_station_id, the model metrics (AUC and Accuracy), the predictions_csv_path, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, include a completion record labeled 'risk_snapshot_boston' with exit_code 0, stdout '', stderr '', printed_message 'risk_snapshot_boston completed', "
            "and printed timestamp 2024‑03‑01T13:42:00Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_water_levels_window", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "risk_snapshot_boston", "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "risk_snapshot_boston completed", "printed_ts": "2024-03-01T13:42:00Z"
            }),
        ],
        outputs=[{
            "primary_station_id": "8443970",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "risk_snapshot_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "risk_snapshot_boston completed",
                "printed_ts": "2024-03-01T13:42:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_86",
        instruction=(
            "You are a data‑science automation agent operating under the City Status Compilation Protocol. "
            "Your objective is to produce a status snapshot for Boston while honoring policy precedence and determinism. "
            "You operate with these constraints: the city is Boston at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; "
            "you confirm tide predictions using method 'harmonic_analysis' for station 8443970 from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z and "
            "water levels with datum 'NAVD88' from 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z; "
            "the processed dataset is /data/processed/timeseries_boston_weather.csv (row_count 120; coverage 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z); "
            "the model of record is boston_harbor_model. "
            "Your deliverable includes the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics (AUC and Accuracy), "
            "and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, you include a completion record labeled 'status_compilation_boston' with printed timestamp 2024‑03‑01T14:02:00Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T14:02:00Z"
            }),
        ],
        outputs=[{
            "city": "Boston",
            "primary_station_id": "8443970",
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "processed_dataset_summary": {
                "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "status_compilation_boston",
                "exit_code": 0,
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T14:02:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_87",
        instruction=(
            "You are a data‑science automation agent operating under the City Risk Snapshot Protocol. "
            "Your objective is to produce a risk snapshot for Seattle while honoring policy precedence and determinism. "
            "You operate with these constraints: the city is Seattle at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; "
            "you confirm tide predictions using method 'harmonic_analysis' and water levels with datum 'NAVD88' for station 9447130 across "
            "2024‑02‑01T00:00:00Z to 2024‑02‑08T00:00:00Z; the processed dataset is /data/processed/timeseries_seattle_weather.csv "
            "(row_count 240; coverage 2024‑02‑01T00:00:00Z to 2024‑02‑11T00:00:00Z); the model of record is simple_model. "
            "Your deliverable includes the primary_station_id, the model metrics (AUC and Accuracy), the predictions CSV path, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, you include a completion record labeled 'risk_snapshot_seattle' with printed timestamp 2024‑02‑08T12:56:00Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "risk_snapshot_seattle",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "risk_snapshot_seattle completed",
                "printed_ts": "2024-02-08T12:56:00Z"
            }),
        ],
        outputs=[{
            "primary_station_id": "9447130",
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "processed_dataset_summary": {
                "columns": ["timestamp", "rainfall_intensity_mmh", "wave_height_m", "lunar_phase_pct", "daylight_hours", "high_risk_flag"],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "risk_snapshot_seattle",
                "exit_code": 0,
                "printed_message": "risk_snapshot_seattle completed",
                "printed_ts": "2024-02-08T12:56:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_88",
        instruction=(
            "You are a data‑science automation agent. Your objective is to determine the primary NOAA station for Boston by applying the Primary Station Determination Protocol while honoring policy precedence and determinism. "
            "Use coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; confirm that station 8443970 has tide predictions using method 'harmonic_analysis' in the window "
            "2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z and water levels with datum 'NAVD88' across 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z before confirming the primary selection. "
            "Use /data/processed/timeseries_boston_weather.csv as the processed dataset and boston_harbor_model as the model of record. "
            "Your deliverable includes the primary_station_id, the model metrics (AUC and Accuracy), the predictions_csv_path, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, you include a completion record labeled 'station_determination_boston' with exit_code 0 and printed timestamp 2024‑03‑01T14:03:00Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "station_determination_boston", "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "station_determination_boston completed", "printed_ts": "2024-03-01T14:03:00Z"
            }),
        ],
        outputs=[{
            "primary_station_id": "8443970",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "station_determination_boston",
                "exit_code": 0,
                "printed_message": "station_determination_boston completed",
                "printed_ts": "2024-03-01T14:03:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_89",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Miami and Boston for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.02; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Miami is at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station is resolved from that location context and must validate "
            "water levels with datum 'NAVD88' available from 2024‑02‑01T00:00:00Z through 2024‑02‑02T00:00:00Z; the processed dataset is "
            "/data/processed/timeseries_miami_weather.csv; the model of record is flood_risk_miami_v1. "
            "Boston is at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station is resolved from that location context and must validate "
            "tide predictions using method 'harmonic_analysis' available from 2024‑03‑01T00:00:00Z through 2024‑03‑02T00:00:00Z; the processed dataset is "
            "/data/processed/timeseries_boston_weather.csv; the model of record is boston_harbor_model. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions_csv_path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, you include a completion record labeled 'ccap_promotion_miami-boston' with exit_code 0 and printed timestamp 2024‑03‑01T14:04:00Z."
        ),
        actions=[
            # Miami validations & metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_miami_v1"}),

            # Boston validations & metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),

            # Winner artifacts (Boston by recency when gap < threshold and both pass)
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),

            # Audit
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_miami-boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_miami-boston completed",
                "printed_ts": "2024-03-01T14:04:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Boston",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_miami-boston",
                "exit_code": 0,
                "printed_message": "ccap_promotion_miami-boston completed",
                "printed_ts": "2024-03-01T14:04:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_179",
        instruction=(
            "You are a data‑science automation agent. You need to decide between Boston and San Francisco for model promotion under the Cross‑City AUC‑Gap Promotion Protocol "
            "while honoring policy precedence and determinism. You apply an absolute AUC‑gap threshold of 0.09; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Boston constraints: coordinates 42.3601,-71.0589 (radius 40.0 km); validate tide predictions using method 'harmonic_analysis' for station 8443970 from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z; "
            "dataset /data/processed/timeseries_boston_weather.csv; model boston_harbor_model. "
            "San Francisco constraints: coordinates 37.7749,-122.4194 (radius 50.0 km); validate tide predictions using method 'harmonic_analysis' for station 9414290 from 2024‑03‑15T00:00:00Z to 2024‑03‑22T00:00:00Z; "
            "dataset /data/processed/timeseries_sf_weather.csv; model flood_risk_sf_v2. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. For auditability, you include a completion record labeled 'ccap_promotion_boston-san-francisco' "
            "with exit_code 0 and printed timestamp 2024‑03‑18T16:36:00Z."
        ),
        actions=[
            # Boston validations & metrics
            Action(name="get_stations_by_location", kwargs={"query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={"station_id": "8443970","window_start_ts":"2024-03-01T00:00:00Z","window_end_ts":"2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={"model_name": "boston_harbor_model"}),
            # San Francisco validations & metrics
            Action(name="get_stations_by_location", kwargs={"query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={"station_id": "9414290","window_start_ts":"2024-03-15T00:00:00Z","window_end_ts":"2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={"model_name": "flood_risk_sf_v2"}),
            # Winner artifacts (San Francisco)
            Action(name="get_predictions_by_model_name", kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={"csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_boston-san-francisco",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_boston-san-francisco completed",
                "printed_ts": "2024-03-18T16:36:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp","tide_pred_m","wind_speed_ms","precipitation_mm_hr","pressure_hpa","temperature_c","high_risk_flag"],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_boston-san-francisco",
                "exit_code": 0,
                "printed_message": "ccap_promotion_boston-san-francisco completed",
                "printed_ts": "2024-03-18T16:36:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_91",
        instruction=(
            "You are a data‑science automation agent. You need to produce a comparative risk snapshot between Seattle and Boston by applying the Multi‑City Comparative Snapshot Protocol "
            "while honoring policy precedence and determinism. "
            "Seattle constraints: you use coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; you confirm tide predictions using method 'harmonic_analysis' for station 9447130 "
            "from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; you reference /data/processed/timeseries_seattle_weather.csv as the processed dataset and simple_model as the model of record. "
            "Boston constraints: you use coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; you confirm tide predictions using method 'harmonic_analysis' for station 8443970 "
            "from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; you reference /data/processed/timeseries_boston_weather.csv as the processed dataset and boston_harbor_model as the model of record. "
            "Your deliverable returns the winning_city and, for each city, the model metrics (AUC and Accuracy), the predictions CSV path, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp). For auditability, you include a completion record labeled 'multi_snapshot_seattle-boston' with a printed timestamp "
            "2024-03-01T13:44:00Z."
        ),
        actions=[
            # Seattle
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Boston
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "multi_snapshot_seattle-boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "multi_snapshot_seattle-boston completed",
                "printed_ts": "2024-03-01T13:44:00Z"
            }),
        ],
        outputs=[{
            "winning_city": "Seattle",
            "seattle": {
                "metrics": {"auc": 0.79, "accuracy": 0.76},
                "predictions_csv_path": "/processed_data/predictions_simple.csv",
                "processed_dataset_summary": {
                    "columns": ["timestamp", "rainfall_intensity_mmh", "wave_height_m", "lunar_phase_pct", "daylight_hours", "high_risk_flag"],
                    "row_count": 240,
                    "min_timestamp": "2024-02-01T00:00:00Z",
                    "max_timestamp": "2024-02-11T00:00:00Z"
                }
            },
            "boston": {
                "metrics": {"auc": 0.73, "accuracy": 0.81},
                "predictions_csv_path": "/data/processed/predictions_boston.csv",
                "processed_dataset_summary": {
                    "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                    "row_count": 120,
                    "min_timestamp": "2024-03-01T00:00:00Z",
                    "max_timestamp": "2024-03-06T00:00:00Z"
                }
            },
            "terminal_log": {
                "command": "multi_snapshot_seattle-boston",
                "exit_code": 0,
                "printed_message": "multi_snapshot_seattle-boston completed",
                "printed_ts": "2024-03-01T13:44:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_92",
        instruction=(
            "You are a data‑science automation agent. You need to decide between San Francisco and Seattle for model promotion under the Cross‑City AUC‑Gap Promotion Protocol "
            "while honoring policy precedence and determinism. You apply an absolute AUC‑gap threshold of 0.08; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "San Francisco constraints: you use coordinates 37.7749,-122.4194 with a coverage radius of 50.0 km; you confirm tide predictions using method 'harmonic_analysis' for station 9414290 "
            "from 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z; you reference /data/processed/timeseries_sf_weather.csv and model flood_risk_sf_v2. "
            "Seattle constraints: you use coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; you confirm tide predictions using method 'harmonic_analysis' for station 9447130 "
            "from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; you reference /data/processed/timeseries_seattle_weather.csv and model simple_model. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. For auditability, you include a completion record labeled 'ccap_promotion_san-francisco-seattle' with "
            "printed timestamp 2024-03-18T16:05:00Z."
        ),
        actions=[
            # SF validations and metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # Seattle validations and metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            # Winner artifacts (San Francisco)
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_san-francisco-seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-seattle completed",
                "printed_ts": "2024-03-18T16:05:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "tide_pred_m", "wind_speed_ms", "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_san-francisco-seattle",
                "exit_code": 0,
                "printed_message": "ccap_promotion_san-francisco-seattle completed",
                "printed_ts": "2024-03-18T16:05:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_93",
        instruction=(
            "You are a data‑science automation agent. You need to decide between Miami and Seattle for model promotion under the Cross‑City AUC‑Gap Promotion Protocol "
            "while honoring policy precedence and determinism. You apply an absolute AUC‑gap threshold of 0.05; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Miami constraints: you use coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; you validate water levels with datum 'NAVD88' for station 8723214 from 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z; "
            "you reference /data/processed/timeseries_miami_weather.csv and model flood_risk_miami_v1. "
            "Seattle constraints: you use coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; you confirm tide predictions using method 'harmonic_analysis' for station 9447130 from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; "
            "you reference /data/processed/timeseries_seattle_weather.csv and model simple_model. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. For auditability, you include a completion record labeled 'ccap_promotion_miami-seattle' with printed timestamp "
            "2024-02-08T12:58:30Z."
        ),
        actions=[
            # Miami validations and metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Seattle validations and metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            # Winner artifacts (Seattle)
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_miami-seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_miami-seattle completed",
                "printed_ts": "2024-02-08T12:58:30Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "rainfall_intensity_mmh", "wave_height_m", "lunar_phase_pct", "daylight_hours", "high_risk_flag"],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_miami-seattle",
                "exit_code": 0,
                "printed_message": "ccap_promotion_miami-seattle completed",
                "printed_ts": "2024-02-08T12:58:30Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_94",
        instruction=(
            "You are a data‑science automation agent operating under the City Risk Snapshot Protocol. "
            "Your objective is to produce a risk snapshot for Boston while honoring policy precedence and determinism. "
            "You operate with the following constraints: you use coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; "
            "you confirm tide predictions using method 'harmonic_analysis' for station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z and water levels with datum 'NAVD88' from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z; "
            "you reference /data/processed/timeseries_boston_weather.csv and model boston_harbor_model. "
            "Your deliverable includes the primary_station_id, the model metrics (AUC and Accuracy), the predictions CSV path, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp). For auditability, you include a completion record labeled 'risk_snapshot_boston' with exit_code 0 and printed timestamp 2024-03-01T13:55:00Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "risk_snapshot_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "risk_snapshot_boston completed",
                "printed_ts": "2024-03-01T13:55:00Z"
            }),
        ],
        outputs=[{
            "primary_station_id": "8443970",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "risk_snapshot_boston",
                "exit_code": 0,
                "printed_message": "risk_snapshot_boston completed",
                "printed_ts": "2024-03-01T13:55:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_95",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Boston and Miami for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.03; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Boston is at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station is resolved from that location context and must validate "
            "tide predictions using method 'harmonic_analysis' available from 2024‑03‑01T00:00:00Z through 2024‑03‑02T00:00:00Z; the processed dataset is "
            "/data/processed/timeseries_boston_weather.csv (window 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z, row_count 120); the model of record is boston_harbor_model. "
            "Miami is at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station is resolved from that location context and must validate "
            "water levels with datum 'NAVD88' available from 2024‑02‑01T00:00:00Z through 2024‑02‑02T00:00:00Z; the processed dataset is "
            "/data/processed/timeseries_miami_weather.csv (window 2024‑02‑01T00:00:00Z to 2024‑02‑05T00:00:00Z, row_count 96); the model of record is flood_risk_miami_v1. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions_csv_path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, you include a completion record labeled 'ccap_promotion_boston-miami' with printed timestamp 2024‑03‑01T13:59:00Z."
        ),
        actions=[
            # Boston validations & metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            # Miami validations & metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Winner: Boston (tie on AUC, both pass, Boston more recent)
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_boston-miami",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_boston-miami completed",
                "printed_ts": "2024-03-01T13:59:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Boston",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_boston-miami",
                "exit_code": 0,
                "printed_message": "ccap_promotion_boston-miami completed",
                "printed_ts": "2024-03-01T13:59:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_96",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between San Francisco and Boston for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.04; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "San Francisco is at coordinates 37.7749,-122.4194 (radius 50.0 km) and must validate tide predictions using method 'harmonic_analysis' from 2024‑03‑15T00:00:00Z to 2024‑03‑22T00:00:00Z; "
            "processed dataset /data/processed/timeseries_sf_weather.csv (row_count 168); model flood_risk_sf_v2. "
            "Boston is at coordinates 42.3601,-71.0589 (radius 40.0 km) and must validate tide predictions using method 'harmonic_analysis' from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z; "
            "processed dataset /data/processed/timeseries_boston_weather.csv (row_count 120); model boston_harbor_model. "
            "Return only the chosen_city, its metrics (AUC and Accuracy), its predictions_csv_path, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, you include a completion record labeled 'ccap_promotion_san-francisco-boston' with printed timestamp 2024‑03‑18T16:10:00Z."
        ),
        actions=[
            # SF
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # Boston
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            # Winner SF
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_san-francisco-boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-boston completed",
                "printed_ts": "2024-03-18T16:10:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "tide_pred_m", "wind_speed_ms", "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_san-francisco-boston",
                "exit_code": 0,
                "printed_message": "ccap_promotion_san-francisco-boston completed",
                "printed_ts": "2024-03-18T16:10:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_97",
        instruction=(
            "You are a data‑science automation agent. Your objective is to produce a comparative risk snapshot between Boston and Seattle by applying the Multi‑City Comparative Snapshot Protocol, "
            "honoring policy precedence and determinism. "
            "Boston constraints: coordinates 42.3601,-71.0589 with coverage radius 40.0 km; validate tide predictions using method 'harmonic_analysis' from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z; "
            "processed dataset /data/processed/timeseries_boston_weather.csv; model boston_harbor_model. "
            "Seattle constraints: coordinates 47.6062,-122.3321 with coverage radius 60.0 km; validate tide predictions using method 'harmonic_analysis' from 2024‑02‑01T00:00:00Z to 2024‑02‑08T00:00:00Z; "
            "processed dataset /data/processed/timeseries_seattle_weather.csv; model simple_model. "
            "Return the winning_city and, for each city, the model metrics (AUC and Accuracy), the predictions_csv_path, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, you include a completion record labeled 'multi_snapshot_boston-seattle' with printed timestamp 2024‑03‑01T13:57:30Z."
        ),
        actions=[
            # Boston
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Seattle
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "multi_snapshot_boston-seattle",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "multi_snapshot_boston-seattle completed",
                "printed_ts": "2024-03-01T13:57:30Z"
            }),
        ],
        outputs=[{
            "winning_city": "Seattle",
            "boston": {
                "metrics": {"auc": 0.73, "accuracy": 0.81},
                "predictions_csv_path": "/data/processed/predictions_boston.csv",
                "processed_dataset_summary": {
                    "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                    "row_count": 120,
                    "min_timestamp": "2024-03-01T00:00:00Z",
                    "max_timestamp": "2024-03-06T00:00:00Z"
                }
            },
            "seattle": {
                "metrics": {"auc": 0.79, "accuracy": 0.76},
                "predictions_csv_path": "/processed_data/predictions_simple.csv",
                "processed_dataset_summary": {
                    "columns": ["timestamp", "rainfall_intensity_mmh", "wave_height_m", "lunar_phase_pct", "daylight_hours", "high_risk_flag"],
                    "row_count": 240,
                    "min_timestamp": "2024-02-01T00:00:00Z",
                    "max_timestamp": "2024-02-11T00:00:00Z"
                }
            },
            "terminal_log": {
                "command": "multi_snapshot_boston-seattle",
                "exit_code": 0,
                "printed_message": "multi_snapshot_boston-seattle completed",
                "printed_ts": "2024-03-01T13:57:30Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_98",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Seattle and Boston for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.05; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Seattle constraints: coordinates 47.6062,-122.3321 (radius 60.0 km), tide predictions validation using method 'harmonic_analysis' from 2024‑02‑01T00:00:00Z to 2024‑02‑08T00:00:00Z; "
            "processed dataset /data/processed/timeseries_seattle_weather.csv; model simple_model. "
            "Boston constraints: coordinates 42.3601,-71.0589 (radius 40.0 km), tide predictions validation using method 'harmonic_analysis' from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z; "
            "processed dataset /data/processed/timeseries_boston_weather.csv; model boston_harbor_model. "
            "Return only the chosen_city along with its model metrics (AUC and Accuracy), the predictions_csv_path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, you include a completion record labeled 'ccap_promotion_seattle-boston' with printed timestamp 2024‑03‑01T13:58:15Z."
        ),
        actions=[
            # Seattle
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            # Boston
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            # Winner: Seattle
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-03-01T13:58:15Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Seattle",
            "metrics": {"auc": 0.79, "accuracy": 0.76},
            "predictions_csv_path": "/processed_data/predictions_simple.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "rainfall_intensity_mmh", "wave_height_m", "lunar_phase_pct", "daylight_hours", "high_risk_flag"],
                "row_count": 240,
                "min_timestamp": "2024-02-01T00:00:00Z",
                "max_timestamp": "2024-02-11T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0,
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-03-01T13:58:15Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_99",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between San Francisco and Miami for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.11; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "San Francisco is at coordinates 37.7749,-122.4194 with a coverage radius of 50.0 km; the primary coastal station is resolved from that location context and must validate "
            "tide predictions using method 'harmonic_analysis' available from 2024‑03‑15T00:00:00Z through 2024‑03‑22T00:00:00Z; the processed dataset is "
            "/data/processed/timeseries_sf_weather.csv; the model of record is flood_risk_sf_v2. "
            "Miami is at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station is resolved from that location context and must validate "
            "water levels with datum 'NAVD88' available from 2024‑02‑01T00:00:00Z through 2024‑02‑02T00:00:00Z; the processed dataset is "
            "/data/processed/timeseries_miami_weather.csv; the model of record is flood_risk_miami_v1. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions_csv_path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, you include a completion record labeled 'ccap_promotion_san-francisco-miami' with printed timestamp 2024‑03‑18T16:14:00Z."
        ),
        actions=[
            # San Francisco validations & metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # Miami validations & metrics
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Winner: San Francisco
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_san-francisco-miami",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-miami completed",
                "printed_ts": "2024-03-18T16:14:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "tide_pred_m", "wind_speed_ms", "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_san-francisco-miami",
                "exit_code": 0,
                "printed_message": "ccap_promotion_san-francisco-miami completed",
                "printed_ts": "2024-03-18T16:14:00Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_100",
        instruction=(
            "You are a data‑science automation agent operating under the Primary Station Determination Protocol. "
            "Your objective is to determine the primary NOAA station for Boston while honoring policy precedence and determinism. "
            "You operate with these constraints: the city is Boston at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; "
            "you confirm tide predictions using method 'harmonic_analysis' for station 8443970 in the window 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z and "
            "water levels with datum 'NAVD88' for the same station across 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z; "
            "the processed dataset is /data/processed/timeseries_boston_weather.csv (row_count 120; coverage 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z); "
            "the model of record is boston_harbor_model. "
            "Your deliverable includes the primary_station_id, the model metrics (AUC and Accuracy), the predictions CSV path, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp). "
            "For auditability, you include a completion record labeled 'station_determination_boston' with printed timestamp 2024‑03‑01T13:58:45Z."
        ),
        actions=[
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="get_water_levels_window", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="get_predictions_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="append_terminal_log_entry", kwargs={
                "command": "station_determination_boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "station_determination_boston completed",
                "printed_ts": "2024-03-01T13:58:45Z"
            }),
        ],
        outputs=[{
            "primary_station_id": "8443970",
            "predictions_csv_path": "/data/processed/predictions_boston.csv",
            "metrics": {"auc": 0.73, "accuracy": 0.81},
            "processed_dataset_summary": {
                "columns": ["timestamp", "ice_coverage_pct", "snow_depth_mm", "temperature_feels_like_c", "pressure_tendency_hpa_3h", "high_risk_flag"],
                "row_count": 120,
                "min_timestamp": "2024-03-01T00:00:00Z",
                "max_timestamp": "2024-03-06T00:00:00Z"
            },
            "terminal_log": {
                "command": "station_determination_boston",
                "exit_code": 0,
                "printed_message": "station_determination_boston completed",
                "printed_ts": "2024-03-01T13:58:45Z"
            }
        }]
    ),
    Task(
        annotator="0",
        user_id="task_101",
        instruction=(
            "You are a data‑science automation agent. Your objective is to decide between Seattle and San Francisco for model promotion "
            "under the Cross‑City AUC‑Gap Promotion Protocol while honoring policy precedence and determinism. "
            "You apply an absolute AUC‑gap threshold of 0.09; when the gap is below this threshold, you prefer the city whose validated station condition passes; "
            "if both pass, you choose the city with the most recent metrics.generated_ts. "
            "Seattle is at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; validate tide predictions using method 'harmonic_analysis' from 2024‑02‑01T00:00:00Z to 2024‑02‑08T00:00:00Z; "
            "processed dataset /data/processed/timeseries_seattle_weather.csv; model simple_model. "
            "San Francisco is at coordinates 37.7749,-122.4194 with a coverage radius of 50.0 km; validate tide predictions using method 'harmonic_analysis' from 2024‑03‑15T00:00:00Z to 2024‑03‑22T00:00:00Z; "
            "processed dataset /data/processed/timeseries_sf_weather.csv; model flood_risk_sf_v2. "
            "Your deliverable returns only the chosen_city along with its model metrics (AUC and Accuracy), the predictions_csv_path for the chosen model, and a processed‑dataset summary "
            "(columns, row_count, min_timestamp, max_timestamp) for the chosen city. "
            "For auditability, you include a completion record labeled 'ccap_promotion_seattle-san-francisco' with printed timestamp 2024‑03‑18T16:12:30Z."
        ),
        actions=[
            # Seattle
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="get_metrics_by_model_name",
                   kwargs={"model_name": "simple_model"}),
            # San Francisco
            Action(name="get_stations_by_location", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="get_tide_predictions_window", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="get_metrics_by_model_name", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # Winner: San Francisco
            Action(name="get_predictions_by_model_name",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="get_processed_timeseries_summary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="append_terminal_log_entry", kwargs={
                "command": "ccap_promotion_seattle-san-francisco",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_seattle-san-francisco completed",
                "printed_ts": "2024-03-18T16:12:30Z"
            }),
        ],
        outputs=[{
            "chosen_city": "San Francisco",
            "metrics": {"auc": 0.89, "accuracy": 0.85},
            "predictions_csv_path": "/results/predictions_sf_v2.csv",
            "processed_dataset_summary": {
                "columns": ["timestamp", "tide_pred_m", "wind_speed_ms", "precipitation_mm_hr", "pressure_hpa", "temperature_c", "high_risk_flag"],
                "row_count": 168,
                "min_timestamp": "2024-03-15T00:00:00Z",
                "max_timestamp": "2024-03-22T00:00:00Z"
            },
            "terminal_log": {
                "command": "ccap_promotion_seattle-san-francisco",
                "exit_code": 0,
                "printed_message": "ccap_promotion_seattle-san-francisco completed",
                "printed_ts": "2024-03-18T16:12:30Z"
            }
        }]
    )

]
