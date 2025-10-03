from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="task_1",
        instruction=(
            "You are a data-science automation agent. Assemble the current status for Oakland by following the City Status Compilation Protocol using model simple_model. Utilize 2024-03-17T10:45:00Z as the printed timestamp for the terminal log entry and the processed dataset summary from the CSV found at /data/processed/timeseries_sf_weather.csv."
        ),
        actions=[
            Action(name="GetProjectConfigByCity",
                   kwargs={"target_city": "Oakland"}),
            Action(name="GetGeocodingResultByCity",
                   kwargs={"query_city": "Oakland"}),
            Action(
                name="GetStationsByLocation",
                kwargs={"query_latitude": 37.7749,
                        "query_longitude": -122.4194, "radius_km": 50.0}
            ),
            Action(
                name="GetProcessedTimeseriesSummary",
                kwargs={"csv_path": "/data/processed/timeseries_sf_weather.csv"}
            ),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(
                name="AppendTerminalLogEntry",
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
            "city": "Oakland",
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
            "You are a data-science automation agent. Gather the current status for Providence by implementing the City Status Compilation Protocol for the timeframe 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z using model boston_harbor_model. Implement the following override: designate the primary station to 8443970 only if the tide predictions method for that station is 'harmonic_analysis'; otherwise opt for 8447930. Provide the model AUC and Accuracy and the predictions CSV path. Use 2024-03-01T13:18:00Z as the printed timestamp for the terminal log entry and the processed dataset summary from the CSV located at /data/processed/timeseries_boston_weather.csv"
        ),
        actions=[
            Action(name="GetProjectConfigByCity",
                   kwargs={"target_city": "Providence"}),
            Action(name="GetGeocodingResultByCity",
                   kwargs={"query_city": "Providence"}),
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:18:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "You serve as a data-science automation agent. Identify the optimal Oakland model by deciding between flood_risk_sf_v1 and flood_risk_sf_v2, utilizing the Model Variant Selection Protocol with this exception: if the AUC difference is less than 0.01, select the variant with the latest metrics timestamp. Provide the name of the selected model and the path to the predictions CSV. Log the timestamp as 2024-03-18T15:45:00Z for the terminal entry."
        ),
        actions=[
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v1"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(
                name="AppendTerminalLogEntry",
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
            "As a data-science automation agent, generate a risk snapshot for Oakland by implementing the City Risk Snapshot Protocol with this condition: when the water levels datum for station 9414290 is recorded as 'MLLW' between 2024-02-14T00:00:00Z and 2024-03-15T00:00:00Z, designate 9414290 as the primary station; if not, utilize 9414750. Choose the flood_risk_sf_v2 variant for the snapshot. Provide the selected station ID, the model AUC and Accuracy, the predictions CSV path, and a summary of the processed dataset from the CSV found at /data/processed/timeseries_sf_weather.csv. Use 2024-03-18T15:45:00Z as the timestamp in the terminal log entry and reference the processed dataset summary from the CSV located at /data/processed/timeseries_sf_weather.csv."
        ),
        actions=[
            Action(
                name="GetStationsByLocation",
                kwargs={"query_latitude": 37.7749,
                        "query_longitude": -122.4194, "radius_km": 50.0}
            ),
            Action(
                name="GetWaterLevelsWindow",
                kwargs={
                    "station_id": "9414290",
                    "window_start_ts": "2024-02-14T00:00:00Z",
                    "window_end_ts": "2024-03-15T00:00:00Z"
                }
            ),
            Action(
                name="GetProcessedTimeseriesSummary",
                kwargs={"csv_path": "/data/processed/timeseries_sf_weather.csv"}
            ),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_sf_v2"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(
                name="AppendTerminalLogEntry",
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
            "Serve as a data-science automation agent. Create a station confirmation snapshot for Orlando by implementing the Datum-and-Method Station Confirmation Protocol with the following override: if the water levels datum for station 8723214 is 'NAVD88' within the period 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z but its tide predictions method within that same time frame is not 'harmonic', employ backup station 8723170; otherwise, retain 8723214. Employ the flood_risk_miami_v1 variant. Provide the selected station id, the model AUC and Accuracy, the predictions CSV path, and the processed dataset summary from /data/processed/timeseries_miami_weather.csv (columns, row_count, min_timestamp, max_timestamp). Utilize the configured station search distance from project_config for Orlando and use 2024-02-02T15:45:00Z as the timestamp to be printed for the terminal log entry. Apply coordinates 25.7617,-80.1918 and a radius of 25.0 for the station search."
        ),
        actions=[
            # Candidate stations (deterministic coords + radius from project_config)
            Action(
                name="GetStationsByLocation",
                kwargs={"query_latitude": 25.7617,
                        "query_longitude": -80.1918, "radius_km": 25.0}
            ),

            # Validate datum condition on 8723214
            Action(
                name="GetWaterLevelsWindow",
                kwargs={
                    "station_id": "8723214",
                    "window_start_ts": "2024-02-01T00:00:00Z",
                    "window_end_ts": "2024-02-02T00:00:00Z"
                }
            ),

            # Validate method condition on 8723214
            Action(
                name="GetTidePredictionsWindow",
                kwargs={
                    "station_id": "8723214",
                    "window_start_ts": "2024-02-01T00:00:00Z",
                    "window_end_ts": "2024-02-02T00:00:00Z"
                }
            ),

            # Summarize processed dataset (explicit CSV path from instruction)
            Action(
                name="GetProcessedTimeseriesSummary",
                kwargs={"csv_path": "/data/processed/timeseries_miami_weather.csv"}
            ),

            # Retrieve model artifacts (Miami)
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_miami_v1"}),
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "flood_risk_miami_v1"}),

            # Deterministic terminal log
            Action(
                name="AppendTerminalLogEntry",
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
            "Function as a data-science automation agent. Elect a promotion between Oakland and Orlando by utilizing the Cross-City AUC-Gap Promotion Protocol with these specified overrides: apply an AUC gap benchmark of 0.12; should the absolute AUC discrepancy between flood_risk_sf_v2 and flood_risk_miami_v1 be less than 0.12, favor the city with the passing validated station condition; otherwise, opt for the city with the superior AUC. Confirm that for Oakland, the tide predictions for station 9414290 employ method 'harmonic' during the interval 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z. For Orlando, verify that water levels for station 8723214 possess datum 'NAVD88' in the span 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z. Deliver the selected city, the model AUC and Accuracy, the predictions CSV path, and the processed dataset summary from /data/processed/timeseries_<city>_weather.csv (columns, row_count, min_timestamp, max_timestamp) applicable to the selected city. Implement the configured station search distances from project_config and apply 2024-03-18T15:45:00Z as the timestamp for the terminal log entry. Set coordinates 37.7749,-122.4194 and a radius of 50.0 for Oakland and coordinates 25.7617,-80.1918 and a radius of 25.0 for Orlando."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_sf_v2"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_miami_v1"}),
            # Action(name="GetPredictionsByModelName", kwargs={
            #     "model_name": "flood_risk_miami_v1"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(
                name="AppendTerminalLogEntry",
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
            "chosen_city": "Oakland",
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
            "Act as a data-science automation agent. Identify the main station for Orlando by implementing the Primary Station Determination Protocol with this exception: if the water levels datum for station 8723214 is 'NAVD88' within the timeframe 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z, pick 8723214; if not, choose 8723170. Provide the selected station id, the model AUC and Accuracy for flood_risk_miami_v1, the path to the predictions CSV, and the summary of the processed dataset from /data/processed/timeseries_miami_weather.csv, including columns, row_count, min_timestamp, and max_timestamp. Apply coordinates 25.7617,-80.1918 with a radius of 25.0 for station search and record 2024-02-02T15:45:00Z as the timestamp for the terminal log output."
        ),
        actions=[
            Action(
                name="GetStationsByLocation",
                kwargs={"query_latitude": 25.7617,
                        "query_longitude": -80.1918, "radius_km": 25.0}
            ),
            Action(
                name="GetWaterLevelsWindow",
                kwargs={
                    "station_id": "8723214",
                    "window_start_ts": "2024-02-01T00:00:00Z",
                    "window_end_ts": "2024-02-02T00:00:00Z"
                }
            ),
            Action(
                name="GetProcessedTimeseriesSummary",
                kwargs={"csv_path": "/data/processed/timeseries_miami_weather.csv"}
            ),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_miami_v1"}),
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "flood_risk_miami_v1"}),
            Action(
                name="AppendTerminalLogEntry",
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
            "Function as a data-science automation agent. Ascertain the main station for Portland by carrying out the Primary Station Determination Protocol with this exception: if no dataset split timestamp is found for the city, utilize the processed dataset creation time as the timestamp for the terminal log output. Verify station 9447130 against tide predictions during the period 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z before confirming its selection. Deliver the chosen station id, the location and row_count of the processed dataset CSV, the summary of the processed dataset from /data/processed/timeseries_seattle_weather.csv and the terminal log confirmation fields {command, exit_code, printed_message, printed_ts}. Utilize coordinates 47.6062,-122.3321 with a radius of 60.0 for station search."
        ),
        actions=[
            Action(
                name="GetStationsByLocation",
                kwargs={"query_latitude": 47.6062,
                        "query_longitude": -122.3321, "radius_km": 60.0}
            ),
            Action(
                name="GetTidePredictionsWindow",
                kwargs={
                    "station_id": "9447130",
                    "window_start_ts": "2024-02-01T00:00:00Z",
                    "window_end_ts": "2024-02-08T00:00:00Z"
                }
            ),
            Action(
                name="GetProcessedTimeseriesSummary",
                kwargs={"csv_path": "/data/processed/timeseries_seattle_weather.csv"}
            ),
            Action(
                name="AppendTerminalLogEntry",
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
            "As an automated data-science agent, your task is to choose between Portland and Oakland for advancing the model under the Cross-City AUC-Gap Promotion Protocol while adhering to policy precedence and determinism. Implement a fixed AUC-gap threshold of 0.05; if the gap is under this threshold, prefer the city where the validated station condition is met; if both are satisfactory, select the city with the most recent metrics.generated_ts. For Portland, apply constraints: utilize coordinates 47.6062,-122.3321 with a 60.0 km coverage radius; conduct tide prediction validation using the 'harmonic_analysis' method for station 9447130 from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; refer to /data/processed/timeseries_seattle_weather.csv and simple_model. For Oakland, apply constraints: utilize coordinates 37.7749,-122.4194 with a 50.0 km coverage radius; conduct tide prediction validation using the 'harmonic_analysis' method for station 9414290 from 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z; refer to /data/processed/timeseries_sf_weather.csv and flood_risk_sf_v2. Your output delivers only the selected city along with its model metrics (AUC and Accuracy), the chosen model's predictions CSV path, and a summary of the processed dataset (columns, row_count, min_timestamp, max_timestamp) for the selected city. For review purposes, add a completion record with the label 'ccap_promotion_seattle-san-francisco', exit_code 0, and printed timestamp 2024-03-18T16:34:10Z."
        ),
        actions=[
            # Portland validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            # Oakland validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_sf_v2"}),
            # Winner artifacts (San Francisco)
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Audit log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_seattle-san-francisco",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_seattle-san-francisco completed",
                "printed_ts": "2024-03-18T16:34:10Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Oakland",
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
            "Acting as a data-science automation agent, create a comparative risk snapshot for Orlando and Providence by implementing the Multi-City Comparative Snapshot Protocol, maintaining policy precedence and determinism. Favor the higher AUC; if AUCs are identical, prefer greater Accuracy. Miami's constraints include: coordinates 25.7617,-80.1918 with a 25.0 km radius; validate water levels against datum 'NAVD88' for station 8723214 from 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z; use dataset /data/processed/timeseries_miami_weather.csv; employ model flood_risk_miami_v1. Boston's constraints include: coordinates 42.3601,-71.0589 with a 40.0 km radius; validate tide predictions using 'harmonic_analysis' for station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; use dataset /data/processed/timeseries_boston_weather.csv; employ model boston_harbor_model. Output the winning city, and for each city, list the model metrics (AUC and Accuracy), predictions CSV path, and a processed dataset summary (columns, row_count, min_timestamp, max_timestamp). For documentation, include a completion record labeled 'multi_snapshot_miami-boston', with exit_code 0 and the printed timestamp 2024-03-01T14:15:20Z."
        ),
        actions=[
            # Orlando
            Action(name="GetStationsByLocation", kwargs={"query_latitude": 25.7617,"query_longitude": -80.1918,"radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={"station_id": "8723214","window_start_ts":"2024-02-01T00:00:00Z","window_end_ts":"2024-02-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={"model_name": "flood_risk_miami_v1"}),
            Action(name="GetPredictionsByModelName", kwargs={"model_name": "flood_risk_miami_v1"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={"csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            # Providence
            Action(name="GetStationsByLocation", kwargs={"query_latitude": 42.3601,"query_longitude": -71.0589,"radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={"station_id": "8443970","window_start_ts":"2024-03-01T00:00:00Z","window_end_ts":"2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={"model_name": "boston_harbor_model"}),
            Action(name="GetPredictionsByModelName", kwargs={"model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={"csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "multi_snapshot_miami-boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "multi_snapshot_miami-boston completed",
                "printed_ts": "2024-03-01T14:15:20Z"
            }),
        ],
        outputs=[{
            "winning_city": "Providence",
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
            "As the model owner for Oakland, manage the application of the Model Variant Selection Protocol with these policy amendments: restrict candidates to 'flood_risk_sf_v1' and 'flood_risk_sf_v2'; ensure AUC ≥ 0.88 as the main criterion, using accuracy and the latest generated timestamp to break ties; verify NOAA evidence from station 9414290 with harmonic tide forecasts for 2024-03-15T00:00:00Z–2024-03-22T00:00:00Z, along with MLLW water-level data for 2024-02-14T00:00:00Z–2024-03-15T00:00:00Z; ensure feature schema is accessible at '/processed_data/features.csv'; log a single deterministic terminal entry with command 'model_selection_sf', exit_code 0, stdout '', stderr '', printed_message 'model_selection_sf completed', and printed_ts '2024-03-18T15:45:00Z', based on the chosen model's generated timestamp; deliver a succinct decision naming the selected model and referencing the evidence employed."
        ),
        actions=[
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_sf_v1"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_sf_v2"}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9414290",
                "window_start_ts": "2024-03-15T00:00:00Z",
                "window_end_ts": "2024-03-22T00:00:00Z"
            }),
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "9414290",
                "window_start_ts": "2024-02-14T00:00:00Z",
                "window_end_ts": "2024-03-15T00:00:00Z"
            }),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/processed_data/features.csv"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "Act as a data-science automation agent. Oversee the application of the City Risk Snapshot Protocol for Orlando with an exception that requires confirmation of water levels using datum NAVD88 for station 8723214 from 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z, and choose flood_risk_miami_v1 as the model. Utilize /data/processed/timeseries_miami_weather.csv for the processed dataset summary and document the snapshot completion in the terminal log with 2024-02-02T15:45:00Z as printed_ts. Provide the snapshot including selected station id, model AUC and accuracy, predictions CSV path, and the processed dataset summary."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_miami_v1"}),
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "flood_risk_miami_v1"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "As a data-science automation agent, handle the Model Variant Selection Protocol for Oakland. Implement an override where, if the AUC difference is less than 0.01, the most recent metrics.generated_ts between flood_risk_sf_v1 and flood_risk_sf_v2 should be prioritized. Record the selected model in the terminal log with 2024-03-18T15:45:00Z as printed_ts. Provide the chosen model name and the path to its predictions CSV."
        ),
        actions=[
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_sf_v1"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_sf_v2"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "As a data-science automation agent, coordinate the Datum-and-Method Station Confirmation Protocol for Providence. Include overrides requiring the validation of water levels datum NAVD88 for station 8443970 within the time frame 2024-02-15T00:00:00Z to 2024-03-16T00:00:00Z and the method harmonic_analysis for tide predictions from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z. Utilize /data/processed/timeseries_boston_weather.csv for summarizing the processed dataset, acquire boston_harbor_model metrics and predictions, and log the completion using 2024-03-01T13:18:00Z as printed_ts. Submit the confirmation snapshot along with the chosen station id, metrics, predictions path, and processed dataset summary."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-02-15T00:00:00Z", "window_end_ts": "2024-03-16T00:00:00Z"}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "As a data-science automation agent, your task is to generate a comparative risk snapshot between Portland and Providence following the Multi-City Comparative Snapshot Protocol, ensuring policy precedence and determinism are adhered to. Favor a higher AUC, and if AUC values are the same, opt for higher Accuracy. Portland parameters include: coordinates at 47.6062,-122.3321 (radius 60.0 km); validate tide predictions through 'harmonic_analysis' for station 9447130 from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; utilize dataset /data/processed/timeseries_seattle_weather.csv; employ simple_model. Providence parameters encompass: coordinates at 42.3601,-71.0589 (radius 40.0 km); validate tide predictions via 'harmonic_analysis' for station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; use dataset /data/processed/timeseries_boston_weather.csv; apply boston_harbor_model. Provide the winning_city, and for each city, detail the model metrics (AUC and Accuracy), the path to predictions CSV, and a summary of the processed-dataset (columns, row_count, min_timestamp, max_timestamp). Ensure auditability by submitting a completion record titled 'multi_snapshot_seattle-boston' with exit_code 0, stdout '', stderr '', message 'multi_snapshot_seattle-boston completed', and timestamp 2024-03-01T14:14:40Z."
        ),
        actions=[
            # Portland
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Providence
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "multi_snapshot_seattle-boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "multi_snapshot_seattle-boston completed",
                "printed_ts": "2024-03-01T14:14:40Z"
            }),
        ],
        outputs=[{
            "winning_city": "Portland",
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
            "Functioning as a data-science automation agent, execute the Datum-and-Method Station Confirmation Protocol for Providence with the condition that if the tide predictions method for station 8443970 is 'harmonic_analysis' during the period 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z and its water levels are referenced to datum 'NAVD88' in the same timeframe, retain 8443970; otherwise, switch to backup station 8447930. Work with the processed dataset located at /data/processed/timeseries_boston_weather.csv and the boston_harbor_model variant, publish an audit receipt involving /data/processed/predictions_boston.csv and /processed_data/metrics_boston.csv with a generated_ts of 2024-03-01T14:02:00Z, and log the confirmation in the terminal with the command 'dmsc_snapshot_boston' and printed_ts 2024-03-01T14:02:00Z. Report the selected station id, the model's AUC and Accuracy, the path to the predictions CSV, and a summary of the processed dataset."
        ),
        actions=[
            # READS
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            # WRITES
            Action(name="PublishStakeholderOutputs", kwargs={
                "predictions_final_csv_path": "/data/processed/predictions_boston.csv",
                "metrics_summary_csv_path": "/processed_data/metrics_boston.csv",
                "generated_ts": "2024-03-01T14:02:00Z"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "As a data-science automation agent, handle the City Status Compilation Protocol for Oakland by applying the overrides where the primary station should be 9414290 if the tide predictions method is 'harmonic' within the timeframe of 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z; otherwise, use 9414750. The terminal log printed_ts must be sourced from the metrics.generated_ts of flood_risk_sf_v2. Utilize coordinates 37.7749,-122.4194 with a radius of 50.0, along with the processed dataset located at /data/processed/timeseries_sf_weather.csv with the flood_risk_sf_v2 model. Provide the city, the primary_station_id, the predictions CSV path, the model AUC and Accuracy, and confirm the terminal log."
        ),
        actions=[
            # READS
            Action(name="GetProjectConfigByCity",
                   kwargs={"target_city": "Oakland"}),
            Action(name="GetGeocodingResultByCity",
                   kwargs={"query_city": "Oakland"}),
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # WRITE (LOG)
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_san-francisco", "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "status_compilation_san-francisco completed", "printed_ts": "2024-03-18T15:45:00Z"})
        ],
        outputs=[{
            "city": "Oakland",
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
            "As a data-science automation agent, coordinate the City Status Compilation Protocol for Orlando using the override where the primary station should be 8723214 if its water levels datum is 'NAVD88' during the period 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z; otherwise, select 8723170. The terminal log printed_ts must be 2024-02-02T11:45:00Z. Deploy the processed dataset at /data/processed/timeseries_miami_weather.csv with the model flood_risk_miami_v1. Return details including the city, the primary_station_id, the predictions CSV path, the model AUC and Accuracy, and confirm the terminal log."
        ),
        actions=[
            Action(name="GetProjectConfigByCity",
                   kwargs={"target_city": "Orlando"}),
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            Action(name="AppendTerminalLogEntry", kwargs={"command": "status_compilation_miami", "exit_code": 0, "stdout": "",
                   "stderr": "", "printed_message": "status_compilation_miami completed", "printed_ts": "2024-02-02T11:45:00Z"})
        ],
        outputs=[{
            "city": "Orlando",
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
            "As a data-science automation agent, your task is to choose between Orlando and Oakland for model promotion under the Cross-City AUC-Gap Promotion Protocol, adhering to policy precedence and determinism. An absolute AUC-gap threshold of 0.05 is in use; if the gap is under this threshold, prioritize the city with a valid station condition; if both meet this condition, select the city with the most recent metrics.generated_ts. Orlando specifics: location at 25.7617,-80.1918 with a 25.0 km coverage area; verify water levels referencing 'NAVD88' at station 8723214 from 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z; available dataset in /data/processed/timeseries_miami_weather.csv; model flood_risk_miami_v1. Oakland specifics: location at 37.7749,-122.4194 within a 50.0 km coverage range; validate tide forecasts using 'harmonic_analysis' at station 9414290 from 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z; dataset present in /data/processed/timeseries_sf_weather.csv; model flood_risk_sf_v2. Your output should list only the chosen_city alongside its model metrics (AUC and Accuracy), the CSV path for predictions of the chosen model, and a summary of the processed dataset (columns, row_count, min_timestamp, max_timestamp) for the selected city. For auditing purposes, submit a completion record marked 'ccap_promotion_miami-san-francisco' with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_miami-san-francisco completed', and a printed timestamp 2024-03-18T16:33:10Z."
        ),
        actions=[
            # Orlando validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Oakland validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # Winner: Oakland
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_miami-san-francisco",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_miami-san-francisco completed",
                "printed_ts": "2024-03-18T16:33:10Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Oakland",
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
            "Your role as a data-science automation agent is to generate a status snapshot for Portland, following the City Status Compilation Protocol while observing policy precedence and determinism. The constraints are: Portland is the city of reference at 47.6062,-122.3321 with a 60.0 km coverage scope; the key station is NOAA 9447130, requiring confirmation that tide forecasts use the 'harmonic' method and cover the period from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; processed data is accessible at /data/processed/timeseries_seattle_weather.csv; the model employed is simple_model. Your deliverables comprise the city name, primary_station_id, the predictions CSV link for the specified model, the model metrics (AUC and Accuracy), and a summary of the processed dataset details (columns, row_count, min_timestamp, max_timestamp) for /data/processed/timeseries_seattle_weather.csv. For ensuring auditability, record a completion entry called 'status_compilation_seattle' along with the message 'status_compilation_seattle completed', exit_code 0, and a printed timestamp of 2024-02-01T15:25:00Z."
        ),
        actions=[
            # Station neighborhood context (non-procedural instruction specifies constraints only)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062,
                "query_longitude": -122.3321,
                "radius_km": 60.0
            }),
            # Verify tide predictions method/window for the designated primary station
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Summarize the processed dataset
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            # Model artifacts (model of record defined in the instruction)
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "simple_model"
            }),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "simple_model"
            }),
            # Deterministic audit trail entry (instruction specifies required fields, not the tool)
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-01T15:25:00Z"
            }),
        ],
        outputs=[{
            "city": "Portland",
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
            "You function as a data-science automation agent. Your goal is to organize a time-based dataset split for Providence while adhering to policy precedence and determinism. You follow the Modeling & Risk Protocol — Data Preparation (Time-Based Partitioning Rule), explicitly choosing this policy for partitioning. You utilize the processed dataset located at /data/processed/timeseries_boston_weather.csv (covering 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, row_count 120). Apply the Providence test-fraction defined by policy; if multiple values are allowed, resolve the choice using the city-level override to 0.25. Record the split deterministically with the split timestamp 2024-03-01T13:20:00Z and use the canonical naming convention for Providence split summaries as dictated by policy. Your deliverable is a structured, machine-verifiable summary of the split and a brief overview of the referenced processed dataset; refrain from listing tool names or prescribing steps. For audit purposes, include a completion record labeled 'dataset_split_boston' with exit_code 0 and printed timestamp 2024-03-01T13:20:00Z."
        ),
        actions=[
            # Read the processed dataset summary (Boston)
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Create the deterministic time-based split using the dataset's row_count
            Action(name="CreateTimeBasedDatasetSplit", kwargs={
                "processed_csv_path": "/data/processed/timeseries_boston_weather.csv",
                "test_fraction": 0.25,
                "split_summary_json_path": "/processed_data/split_summary_boston.json",
                "split_ts": "2024-03-01T13:20:00Z"
            }),
            # Deterministic audit trail entry
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "dataset_split_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_boston completed",
                "printed_ts": "2024-03-01T13:20:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "You are acting as a data-science automation agent under the City Status Compilation Protocol. The aim is to create a model readiness snapshot for Providence while following policy precedence and determinism. Operate with these constraints: the primary coastal station is NOAA 8443970 with tide predictions using method 'harmonic_analysis' available from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; the processed dataset is situated at /data/processed/timeseries_boston_weather.csv, covering 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z with row_count 120; the model of record is boston_harbor_model. Your deliverable should include the city, the primary_station_id, the predictions CSV path for the referenced model, the model metrics (AUC and Accuracy), and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) for /data/processed/timeseries_boston_weather.csv. For audit purposes, the trail must include a completion entry labeled 'model_readiness_boston' with message 'model_readiness_boston completed', exit_code 0, and the printed timestamp 2024-03-01T13:22:00Z."
        ),
        actions=[
            # Model metrics and predictions for the declared model of record
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"
            }),
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "boston_harbor_model"
            }),
            # Processed dataset summary
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "model_readiness_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "model_readiness_boston completed",
                "printed_ts": "2024-03-01T13:22:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "As a data‑science automation agent, your target is to choose between Portland and Providence for model promotion according to the Cross‑City AUC‑Gap Promotion Protocol, ensuring adherence to policy precedence and determinism. Implement an absolute AUC‑gap threshold of 0.04; if the gap is under this threshold, favor the city whose validated station condition succeeds; if both cities qualify, select the one with the most recently updated metrics.generated_ts. City conditions: Portland utilizes primary coastal station NOAA 9447130 with tide predictions through 'harmonic_analysis' available from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z, with the processed dataset at /data/processed/timeseries_seattle_weather.csv, using the model simple_model. Providence operates with primary coastal station NOAA 8443970, tide predictions via 'harmonic_analysis' from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z, processed dataset at /data/processed/timeseries_boston_weather.csv, and the model boston_harbor_model. Submit only the selected city with its model metrics (AUC and Accuracy), the path to predictions CSV for the chosen model, and a processed‑dataset synopsis (columns, row_count, min_timestamp, max_timestamp) for the selected city. Ensure auditability by including a completion record tagged 'ccap_promotion_seattle-boston' with exit_code 0 and printed timestamp 2024-02-08T12:00:00Z."
        ),
        actions=[
            # Validate Portland window/method, gather Portland metrics
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),

            # Validate Providence window/method, gather Providence metrics
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),

            # Decision (gap 0.79 vs 0.73 >= 0.04) ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record (correct protocol command name)
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-02-08T12:00:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "Functioning as a data‑science automation agent under the City Status Compilation Protocol, your mission is to create a status snapshot for Portland while adhering to policy precedence and determinism. Follow these directives: select Portland at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station must be resolved per policy in that location context, confirming tide predictions using 'harmonic_analysis' available between 2024-02-01T00:00:00Z and 2024-02-08T00:00:00Z; the processed dataset is found at /data/processed/timeseries_seattle_weather.csv, spanning 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z with row_count 240; the designated model is simple_model. Include in your submission the city, primary_station_id, the predictions CSV path for the intended model, the model metrics (AUC and Accuracy), and a synopsis of the processed dataset (columns, row_count, min_timestamp, max_timestamp) for /data/processed/timeseries_seattle_weather.csv. To maintain auditability, attach a completion record marked 'status_snapshot_seattle' with exit_code 0 and printed timestamp 2024-02-08T12:15:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062,
                "query_longitude": -122.3321,
                "radius_km": 60.0
            }),
            # Validate tide predictions method/window for the resolved primary station (9447130)
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_snapshot_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_snapshot_seattle completed",
                "printed_ts": "2024-02-08T12:15:00Z"
            }),
        ],
        outputs=[{
            "city": "Portland",
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
            "As a data-science automation agent, your task is to set up a time-based dataset split for Portland while following policy precedence and ensuring determinism. You adhere to the Modeling & Risk Protocol — Data Preparation (Time-Based Partitioning Rule), specifically selecting this policy for partitioning. You process the dataset found at /data/processed/timeseries_seattle_weather.csv (spanning from 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, with a row_count of 240). Utilize the Portland test-fraction as specified by policy; if multiple values are allowed, finalize your choice with the city-level override to 0.20. Log the split deterministically using the split timestamp 2024-02-08T12:20:00Z and follow the canonical naming convention for Portland split summaries as per policy. Provide a structured, machine-verifiable summary of the split along with a brief overview of the processed dataset; refrain from listing tool names or outlining steps. For audit purposes, include a completion record named 'dataset_split_seattle' with an exit_code of 0 and a printed timestamp of 2024-02-08T12:20:00Z."
        ),
        actions=[
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="CreateTimeBasedDatasetSplit", kwargs={
                "processed_csv_path": "/data/processed/timeseries_seattle_weather.csv",
                "test_fraction": 0.20,
                "split_summary_json_path": "/processed_data/split_summary_seattle.json",
                "split_ts": "2024-02-08T12:20:00Z"
            }),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "dataset_split_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_seattle completed",
                "printed_ts": "2024-02-08T12:20:00Z"
            }),
        ],
        outputs=[{
            "city": "Portland",
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
            "As a data-science automation agent, your goal is to choose between Providence and Orlando for model promotion, following the Cross-City AUC-Gap Promotion Protocol while adhering to policy precedence and maintaining determinism. Implement an absolute AUC-gap threshold of 0.05; if the gap is below this threshold, prioritize the city with a validated station condition; if both are validated, prefer the city with the most recent metrics.generated_ts. City's specific criteria: Providence is located at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station must be identified from that location context and verify tide predictions using the 'harmonic_analysis' method available from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; the processed dataset is located at /data/processed/timeseries_boston_weather.csv (time window 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, with a row_count of 120); the model of record is boston_harbor_model. Orlando is positioned at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station must be identified from that location context and verify water levels with datum 'NAVD88' available from 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z; the processed dataset is at /data/processed/timeseries_miami_weather.csv; the model of record is flood_risk_miami_v1. Deliver the selected city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) for the selected city. For accountability, include a completion record titled 'ccap_promotion_boston-miami' with an exit_code of 0 and a printed timestamp of 2024-03-01T13:18:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Boston)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601,
                "query_longitude": -71.0589,
                "radius_km": 40.0
            }),
            # Validate Providence tide window/method
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Providence metrics
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),

            # Resolve candidate stations per policy (Miami)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 25.7617,
                "query_longitude": -80.1918,
                "radius_km": 25.0
            }),
            # Validate Orlando water‑levels datum/window
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "8723214",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-02T00:00:00Z"
            }),
            # Orlando metrics
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_miami_v1"}),

            # Decision (AUC tie → Providence by recency); fetch chosen artifacts only
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),

            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_boston-miami",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_boston-miami completed",
                "printed_ts": "2024-03-01T13:18:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Providence",
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
            "As a data‑science automation agent following the City Status Compilation Protocol, your task is to generate a status snapshot for Providence, ensuring you adhere to policy precedence and determinism. Here are your parameters: the city is Providence with coordinates 42.3601,-71.0589 and a coverage area of 40.0 km; the primary coastal station must be identified based on policy from that location context and use 'harmonic_analysis' to validate tide predictions, available from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; the dataset you'll process is at /data/processed/timeseries_boston_weather.csv, spanning 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z with a row_count of 120; the designated model is boston_harbor_model. Your assignment requires including the city, the primary_station_id, the predictions CSV path for the indicated model, the model metrics (AUC and Accuracy), and a summary of the processed-dataset (columns, row_count, min_timestamp, max_timestamp) for /data/processed/timeseries_boston_weather.csv. Ensure auditability by including a completion record labeled 'status_snapshot_boston' with exit_code 0 and printed timestamp 2024-03-01T13:21:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601,
                "query_longitude": -71.0589,
                "radius_km": 40.0
            }),
            # Validate tide predictions method/window for the resolved primary station (8443970)
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_snapshot_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_snapshot_boston completed",
                "printed_ts": "2024-03-01T13:21:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "As a data‑science automation agent under the City Status Compilation Protocol, your aim is to assemble a model readiness snapshot for Portland while adhering to policy precedence and determinism. Your operations are bound by these constraints: the city is Portland at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station must be resolved under policy from that location context, validating tide predictions using 'harmonic_analysis', available from 2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; the dataset you'll evaluate is located at /data/processed/timeseries_seattle_weather.csv covering 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z with a row_count of 240; the model of record is simple_model. Your deliverable must encompass the city, the primary_station_id, the predictions CSV path for the specified model, the model metrics (AUC and Accuracy), and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) for /data/processed/timeseries_seattle_weather.csv. For audit purposes, include a completion record labeled 'model_readiness_seattle' with exit_code 0 and printed timestamp 2024-02-08T12:18:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062,
                "query_longitude": -122.3321,
                "radius_km": 60.0
            }),
            # Validate tide predictions method/window for the resolved primary station (9447130)
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "model_readiness_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "model_readiness_seattle completed",
                "printed_ts": "2024-02-08T12:18:00Z"
            }),
        ],
        outputs=[{
            "city": "Portland",
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
            "Act as a data‑science automation agent. Your task is to choose between Portland and Orlando for model promotion according to the Cross‑City AUC‑Gap Promotion Protocol, considering policy precedence and determinism. Implement an absolute AUC‑gap threshold of 0.05; if the gap is smaller, favor the city whose validated station condition is met; in cases where both are met, select the city with the latest metrics.generated_ts. City details: Portland is located at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station must be identified from this situational context and validate tide predictions using 'harmonic_analysis' from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; the processed data file is /data/processed/timeseries_seattle_weather.csv (window 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the reference model is simple_model. Orlando is positioned at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; resolve the primary coastal station from this locality and validate water levels with datum 'NAVD88' available from 2024-02-01T00:00:00Z through 2024-02-02T00:00:00Z; the processed data file is /data/processed/timeseries_miami_weather.csv; the reference model is flood_risk_miami_v1. Your output should present only the selected city with its model metrics (AUC and Accuracy), the path to the predictions CSV for the chosen model, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the selected city. Ensure auditability by including a completion record labeled 'ccap_promotion_seattle-miami' with exit_code 0 and printed timestamp 2024-02-08T12:10:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Seattle)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062,
                "query_longitude": -122.3321,
                "radius_km": 60.0
            }),
            # Validate Portland tide window/method
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Portland metrics
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),

            # Resolve candidate stations per policy (Miami)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 25.7617,
                "query_longitude": -80.1918,
                "radius_km": 25.0
            }),
            # Validate Orlando water‑levels datum/window
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "8723214",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-02T00:00:00Z"
            }),
            # Orlando metrics
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_miami_v1"}),

            # Decision (AUC 0.79 vs 0.73 ≥ 0.05) ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T12:10:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "Operate as a data‑science automation agent adhering to the City Status Compilation Protocol. Your aim is to create a status snapshot for Providence while observing policy precedence and determinism. Work within these constraints: the city is Providence at coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; identify the primary coastal station as per policy from this location context and ensure tide predictions are validated using 'harmonic_analysis' from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; find the processed dataset at /data/processed/timeseries_boston_weather.csv covering from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z with row_count 120; the designated model is boston_harbor_model. Your output must comprise the city, the primary_station_id, the predictions CSV path for the cited model, the model's metrics (AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for /data/processed/timeseries_boston_weather.csv. Maintain auditability by attaching a completion record marked 'status_snapshot_boston' with exit_code 0 and printed timestamp 2024-03-01T13:24:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601,
                "query_longitude": -71.0589,
                "radius_km": 40.0
            }),
            # Validate tide predictions method/window for the resolved primary station (8443970)
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_snapshot_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_snapshot_boston completed",
                "printed_ts": "2024-03-01T13:24:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "Act as a data-science automation agent. Your goal is to organize a time-based dataset split for Providence while adhering to policy precedence and determinism. You function within the Modeling & Risk Protocol — Data Preparation (Time-Based Partitioning Rule), utilizing this policy explicitly for partitioning purposes. Handle the processed dataset located at /data/processed/timeseries_boston_weather.csv (ranging from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, row_count 120). Implement the Providence test-fraction as dictated by policy; where multiple values are allowed, choose via the city-level override to 0.30. Log the split deterministically using the split timestamp 2024-03-01T13:24:00Z and employ the canonical naming convention for Providence split summaries as per policy. Your output is a structured, machine-verifiable summary of the split and a concise synopsis of the referenced processed dataset; avoid listing tool names or dictating steps. For audit purposes, include a completion record labeled 'dataset_split_boston_v2' with exit_code 0 and printed timestamp 2024-03-01T13:24:00Z."
        ),
        actions=[
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            Action(name="CreateTimeBasedDatasetSplit", kwargs={
                "processed_csv_path": "/data/processed/timeseries_boston_weather.csv",
                "test_fraction": 0.30,
                "split_summary_json_path": "/processed_data/split_summary_boston_v2.json",
                "split_ts": "2024-03-01T13:24:00Z"
            }),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "dataset_split_boston_v2",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_boston_v2 completed",
                "printed_ts": "2024-03-01T13:24:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "Function as a data-science automation agent under the City Status Compilation Protocol. Your task is to generate a status snapshot for Portland while respecting policy precedence and determinism. Operate with the following constraints: the city is Portland at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; deduce the primary coastal station from this location context under policy and verify tide predictions using method 'harmonic_analysis' available from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; the processed dataset can be found at /data/processed/timeseries_seattle_weather.csv covering 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z with row_count 240; the official model is simple_model. Your deliverable encompasses the city, the primary_station_id, the predictions CSV path for the given model, the model metrics (AUC and Accuracy), and a summarized version of the processed dataset (columns, row_count, min_timestamp, max_timestamp) for /data/processed/timeseries_seattle_weather.csv. For auditing, append a completion record labeled 'status_compilation_seattle' with exit_code 0 and printed timestamp 2024-02-08T12:22:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062,
                "query_longitude": -122.3321,
                "radius_km": 60.0
            }),
            # Validate tide predictions method/window for the resolved primary station (9447130)
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            # Deterministic audit record (protocol‑aligned command name)
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-08T12:22:00Z"
            }),
        ],
        outputs=[{
            "city": "Portland",
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
            "Acting as a data-science automation agent, your goal is to choose between Portland and Providence for model promotion under the Cross-City AUC-Gap Promotion Protocol while adhering to policy precedence and determinism. You utilize an absolute AUC-gap threshold of 0.06; if the gap is below this threshold, prioritize the city whose validated station condition is satisfied; if both conditions are met, select the city with the latest metrics.generated_ts. City specifications: Portland is situated at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station must be determined from this location and validate tide predictions using the 'harmonic_analysis' method available from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; the processed dataset is /data/processed/timeseries_seattle_weather.csv (window from 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the registered model is simple_model. Providence is positioned at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station must be determined from this location and validate tide predictions using the 'harmonic_analysis' method available from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; the processed dataset is /data/processed/timeseries_boston_weather.csv (window from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, row_count 120); the registered model is boston_harbor_model. Your output should only include the selected city with its model metrics (AUC and Accuracy), the CSV path for the chosen model's predictions, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) for the selected city. For transparency, provide a completion record tagged 'ccap_promotion_seattle-boston' with exit_code 0 and printed timestamp 2024-02-08T12:30:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Seattle)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062,
                "query_longitude": -122.3321,
                "radius_km": 60.0
            }),
            # Validate Portland tide window/method
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Portland metrics
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),

            # Resolve candidate stations per policy (Boston)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601,
                "query_longitude": -71.0589,
                "radius_km": 40.0
            }),
            # Validate Providence tide window/method
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Providence metrics
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),

            # Decision (gap 0.79 vs 0.73 not below 0.06) ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-02-08T12:30:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "As a data-science automation agent, your task is to select between Portland and Orlando for model promotion under the Cross-City AUC-Gap Promotion Protocol while adhering to policy precedence and determinism. Utilize an absolute AUC-gap threshold of 0.04; if the gap is lower than this threshold, prioritize the city whose validated station condition fulfills; if both fulfill, choose the city with the most recent metrics.generated_ts. City parameters: Portland is located at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station is resolved from this location context and must validate tide predictions using the 'harmonic_analysis' method available from 2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; the processed dataset is /data/processed/timeseries_seattle_weather.csv (window 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the designated model is simple_model. Orlando is positioned at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station is resolved from this location context and must validate water levels with datum 'NAVD88' available from 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z; the processed dataset is /data/processed/timeseries_miami_weather.csv; the registered model is flood_risk_miami_v1. Your output returns only the selected city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. For audit purposes, ensure you include a completion record marked 'ccap_promotion_seattle-miami' with exit_code 0 and printed timestamp 2024-02-08T12:35:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Seattle)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate Portland tide window/method
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Portland metrics
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),

            # Resolve candidate stations per policy (Miami)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0
            }),
            # Validate Orlando water‑levels datum/window
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "8723214",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-02T00:00:00Z"
            }),
            # Orlando metrics
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_miami_v1"}),

            # Decision ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T12:35:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "You function as a data-science automation agent following the City Status Compilation Protocol. Your task is to create a status snapshot for Portland while adhering to policy precedence and determinism. You work within these constraints: the city is Portland with coordinates 47.6062,-122.3321 and a coverage radius of 60.0 km; the main coastal station is determined from that location context under policy and must verify tide predictions using the method 'harmonic_analysis' available from 2024-02-01T00:00:00Z through 2024-02-08T00:00:00Z; the processed dataset is situated at /data/processed/timeseries_seattle_weather.csv covering 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z with row_count 240; the designated model is simple_model. Your output includes the city, the primary_station_id, the predictions CSV path for the specified model, the model metrics (AUC and Accuracy), and a summary of the processed dataset (columns, row_count, min_timestamp, max_timestamp) for /data/processed/timeseries_seattle_weather.csv. For audit purposes, you include a completion record marked 'status_compilation_seattle' with exit_code 0 and printed timestamp 2024-02-08T12:40:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate tide predictions method/window for the resolved primary station (9447130)
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-08T12:40:00Z"
            }),
        ],
        outputs=[{
            "city": "Portland",
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
            "Your role is as a data-science automation agent. Your goal is to formulate a time-based dataset split for Portland, maintaining policy precedence and determinism. You are guided by the Modeling & Risk Protocol — Data Preparation (Time-Based Partitioning Rule), implementing this policy specifically for partitioning. You handle the processed dataset at /data/processed/timeseries_seattle_weather.csv (extending from 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, with row_count 240). You apply the Portland test-fraction as defined by policy; if multiple values are allowed, you apply the city-level override to 0.25. You record the split deterministically using the split timestamp 2024-02-08T12:25:00Z and follow the canonical naming convention for Portland split summaries mandated by policy. Your output is a structured, machine-verifiable summary of the split along with a brief review of the referenced processed dataset; you refrain from listing tool names or outlining steps. For audit purposes, you attach a completion record tagged 'dataset_split_seattle_v2' with exit_code 0 and printed timestamp 2024-02-08T12:25:00Z."
        ),
        actions=[
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="CreateTimeBasedDatasetSplit", kwargs={
                "processed_csv_path": "/data/processed/timeseries_seattle_weather.csv",
                "test_fraction": 0.25,
                "split_summary_json_path": "/processed_data/split_summary_seattle_v2.json",
                "split_ts": "2024-02-08T12:25:00Z"
            }),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "dataset_split_seattle_v2",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_seattle_v2 completed",
                "printed_ts": "2024-02-08T12:25:00Z"
            }),
        ],
        outputs=[{
            "city": "Portland",
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
            "As a data-science automation agent functioning under the City Status Compilation Protocol, your task is to develop a status snapshot for Providence while maintaining adherence to policy precedence and determinism. Operate within these parameters: the designated city is Providence located at coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; the main coastal station should be determined from that location context in compliance with policy, and must authenticate tide predictions using the 'harmonic_analysis' method available from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; access the processed dataset at /data/processed/timeseries_boston_weather.csv covering the period from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z with a total of 120 rows; the official model in use is boston_harbor_model. Your submission should include the city, the primary_station_id, the predictions CSV path for the specified model, the model metrics (AUC and Accuracy), and a summary of the processed dataset (columns, row_count, min_timestamp, max_timestamp) for /data/processed/timeseries_boston_weather.csv. For audit trail purposes, provide a completion record titled 'status_compilation_boston' with exit_code 0 and the timestamp 2024-03-01T13:26:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate tide predictions method/window for the resolved primary station (8443970)
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:26:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "Under the role of a data-science automation agent, generate a comparative risk snapshot between Providence and Oakland adhering to the Multi-City Comparative Snapshot Protocol, ensuring alignment with policy precedence and determinism. Opt for higher AUC, and if the AUCs are identical, choose based on higher Accuracy. Parameters for Boston: coordinates 42.3601,-71.0589 (radius 40.0 km); use 'harmonic' method for tide prediction validation at station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; dataset /data/processed/timeseries_boston_weather.csv; model boston_harbor_model. Parameters for San Francisco: coordinates 37.7749,-122.4194 (radius 50.0 km); use 'harmonic' method for tide prediction validation at station 9414290 from 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z; dataset /data/processed/timeseries_sf_weather.csv; model flood_risk_sf_v2. Report the winning_city, and for each city, provide the model metrics (AUC and Accuracy), the path of the predictions CSV, and a summary of the processed dataset (columns, row_count, min_timestamp, max_timestamp). To ensure clarity in audit processes, include a completion record marked 'multi_snapshot_boston-san-francisco' with exit_code 0, an empty stdout and stderr, printed_message 'multi_snapshot_boston-san-francisco completed', and the printed timestamp 2024-03-18T16:32:40Z."
        ),
        actions=[
            # Providence
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Oakland
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "multi_snapshot_boston-san-francisco",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "multi_snapshot_boston-san-francisco completed",
                "printed_ts": "2024-03-18T16:32:40Z"
            }),
        ],
        outputs=[{
            "winning_city": "Oakland",
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
            "You function as a data‑science automation agent. Your aim is to determine whether Portland or Providence should be selected for model promotion, following the Cross‑City AUC‑Gap Promotion Protocol while adhering to policy precedence and determinism. Apply an absolute AUC‑gap threshold of 0.05; if the gap is less than this threshold, prioritize the city whose validated station condition is met; if both conditions are satisfied, prefer the city with the latest metrics.generated_ts. City specifics: Portland is positioned at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; identify the primary coastal station based on that locale and ensure tide predictions are validated using 'harmonic_analysis' available from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; the dataset in question is /data/processed/timeseries_seattle_weather.csv (coverage 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); utilize the simple_model. Boston's coordinates are 42.3601,-71.0589 with a 40.0 km range; derive the primary coastal station using that locale and ensure tide predictions through 'harmonic_analysis' from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; dataset used is /data/processed/timeseries_boston_weather.csv (window 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, row_count 120); employ the boston_harbor_model. Your output should expressly include the selected city alongside its model metrics (AUC and Accuracy), the predictions CSV path for the model chosen, and a concise processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. Ensure auditability by attaching a completion record identified as 'ccap_promotion_seattle-boston' with exit_code 0 and timestamp 2024-02-08T12:45:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Seattle)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate Portland tide window/method
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Portland metrics
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),

            # Resolve candidate stations per policy (Boston)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate Providence tide window/method
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Providence metrics
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),

            # Decision (AUC 0.79 vs 0.73 ≥ 0.05) ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-02-08T12:45:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "Acting as a data‑science automation agent, your task under the City Status Compilation Protocol is to compile a status capture for Portland while respecting policy precedence and determinism. Operate under these parameters: Portland is fixed at coordinates 47.6062,-122.3321, encompassing a 60.0 km radius; pinpoint the primary coastal station per location policy dictates, and valid tide predictions should be confirmed using 'harmonic_analysis' available from 2024-02-01T00:00:00Z until 2024-02-08T00:00:00Z; the suitable dataset is found at /data/processed/timeseries_seattle_weather.csv, encompassing 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z with a row_count of 240; apply the simple_model. Your report should include the city, the primary_station_id, the referenced model's predictions CSV path, the model metrics (AUC and Accuracy), and an outlined processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for /data/processed/timeseries_seattle_weather.csv. Guarantee auditability by incorporating a completion log labeled as 'status_compilation_seattle' with an exit_code 0 and timestamp 2024-02-08T12:50:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate tide predictions method/window for the resolved primary station (9447130)
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-08T12:50:00Z"
            }),
        ],
        outputs=[{
            "city": "Portland",
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
            "You are a data-science automation agent. Your task is to organize a time-based dataset division for Providence while adhering to policy precedence and determinism. You function under the Modeling & Risk Protocol — Data Preparation (Time-Based Partitioning Rule), explicitly choosing this policy for partitioning. Your resource is the processed dataset at /data/processed/timeseries_boston_weather.csv (spanning 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, row_count 120). You implement the Providence test-fraction outlined by policy; if there are multiple values allowed, resolve the selection using the city-level override to 0.20. Record the split deterministically with the split timestamp 2024-03-01T13:27:00Z and the standard naming convention for Providence split summaries as defined by policy. Your output should be a structured, machine-verifiable summary of the split along with a brief overview of the processed dataset; avoid listing tool names or prescribing steps. For audit purposes, include a completion record titled 'dataset_split_boston_v3' with exit_code 0 and printed timestamp 2024-03-01T13:27:00Z."
        ),
        actions=[
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            Action(name="CreateTimeBasedDatasetSplit", kwargs={
                "processed_csv_path": "/data/processed/timeseries_boston_weather.csv",
                "test_fraction": 0.20,
                "split_summary_json_path": "/processed_data/split_summary_boston_v3.json",
                "split_ts": "2024-03-01T13:27:00Z"
            }),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "dataset_split_boston_v3",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_boston_v3 completed",
                "printed_ts": "2024-03-01T13:27:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "You are a data-science automation agent functioning under the City Status Compilation Protocol. Your goal is to create a status snapshot for Providence while respecting policy precedence and determinism. Operate with the following parameters: the city is Providence at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; identify the primary coastal station from that location context under policy, ensuring to validate tide predictions using method 'harmonic_analysis' available from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; locate the processed dataset at /data/processed/timeseries_boston_weather.csv covering 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z with row_count 120; the official model is boston_harbor_model. Your deliverable should include the city, the primary_station_id, the path to the predictions CSV for the referenced model, the model metrics (AUC and Accuracy), and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) for /data/processed/timeseries_boston_weather.csv. For auditability, provide a completion record entitled 'status_compilation_boston' with exit_code 0 and printed timestamp 2024-03-01T13:28:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate tide predictions method/window for the resolved primary station (8443970)
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:28:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "As a data&#8209;science automation agent, your objective is to choose between Portland and Orlando for model promotion under the Cross&#8209;City AUC&#8209;Gap Promotion Protocol while adhering to policy precedence and determinism. Utilize an absolute AUC&#8209;gap threshold of 0.05; if the gap is below this threshold, favor the city where the validated station condition is met; if both conditions are met, opt for the city with the latest metrics.generated_ts. City specifics: Portland is located at coordinates 47.6062,-122.3321, with a coverage radius of 60.0 km; the main coastal station must validate tide predictions using the 'harmonic_analysis' method, available from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; the processed dataset is /data/processed/timeseries_seattle_weather.csv (window 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the model in use is simple_model. Orlando is positioned at 25.7617,-80.1918, with a coverage radius of 25.0 km; its main coastal station must validate water levels with datum 'NAVD88', available from 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z; the processed dataset is /data/processed/timeseries_miami_weather.csv; the model in use is flood_risk_miami_v1. Your deliverable should return only the selected city along with its model metrics (AUC and Accuracy), the predictions CSV path for the selected model, and a processed&#8209;dataset summary (columns, row_count, min_timestamp, max_timestamp) for that city. For auditability, include a completion record titled 'ccap_promotion_seattle-miami' with exit_code 0 and printed timestamp 2024-02-08T12:55:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Seattle)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate Portland tide window/method
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Portland metrics
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),

            # Resolve candidate stations per policy (Miami)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0
            }),
            # Validate Orlando water‑levels datum/window
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "8723214",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-02T00:00:00Z"
            }),
            # Orlando metrics
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_miami_v1"}),

            # Decision (AUC 0.79 vs 0.73 ≥ 0.05) ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T12:55:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "As a data&#8209;science automation agent, your task is to choose between Portland and Providence for model promotion under the Cross&#8209;City AUC&#8209;Gap Promotion Protocol while adhering to policy precedence and determinism. Utilize an absolute AUC&#8209;gap threshold of 0.03; if the gap is below this threshold, favor the city where the validated station condition is met; if both conditions are met, opt for the city with the most recent metrics.generated_ts. City specifics: Portland is situated at coordinates 47.6062,-122.3321, with a coverage radius of 60.0 km; the main coastal station must validate tide predictions using the 'harmonic_analysis' method, available from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; the processed dataset is /data/processed/timeseries_seattle_weather.csv (window 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the model in use is simple_model. Providence is positioned at 42.3601,-71.0589, with a coverage radius of 40.0 km; its main coastal station must validate tide predictions using the 'harmonic_analysis' method, available from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; the processed dataset is /data/processed/timeseries_boston_weather.csv (window 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, row_count 120); the model in use is boston_harbor_model. Your deliverable should only include the selected city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed&#8209;dataset summary (columns, row_count, min_timestamp, max_timestamp) for that city. For auditability, include a completion record titled 'ccap_promotion_seattle-boston' with exit_code 0 and printed timestamp 2024-02-08T12:58:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Seattle)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate Portland tide window/method
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Portland metrics
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),

            # Resolve candidate stations per policy (Boston)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate Providence tide window/method
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Providence metrics
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),

            # Decision ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-02-08T12:58:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "You function as a data-science automation agent. Your task is to choose between Providence and Orlando for model promotion under the Cross-City AUC-Gap Promotion Protocol, adhering to policy precedence and determinism. Implement an absolute AUC-gap threshold of 0.02; when the gap is beneath this threshold, favor the city with validated station conditions; if both conditions are met, select the city with the latest metrics.generated_ts. City constraints: Providence is located at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station must confirm tide predictions using the 'harmonic_analysis' method available from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; the dataset processed is /data/processed/timeseries_boston_weather.csv (window 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, row_count 120); the model of record is boston_harbor_model. Orlando is at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station must validate water levels with datum 'NAVD88' available from 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z; the dataset processed is /data/processed/timeseries_miami_weather.csv; the model of record is flood_risk_miami_v1. Your output returns only the selected city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a summary of the processed dataset (columns, row_count, min_timestamp, max_timestamp) for the chosen city. For audit purposes, you provide a completion record labeled 'ccap_promotion_boston-miami' with exit_code 0 and printed timestamp 2024-03-01T13:18:00Z."
        ),
        actions=[
            # Resolve stations (Boston)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate Providence tide window/method; gather Providence metrics
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),

            # Resolve stations (Miami)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0
            }),
            # Validate Orlando datum/window; gather Orlando metrics
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "8723214",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-02T00:00:00Z"
            }),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_miami_v1"}),

            # Decision (AUC tie, both pass, choose Providence by recency); fetch chosen artifacts only
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),

            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_boston-miami",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_boston-miami completed",
                "printed_ts": "2024-03-01T13:18:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Providence",
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
            "You serve as a data-science automation agent adhering to the City Status Compilation Protocol. Your mission is to compile a status snapshot for Providence while observing policy precedence and determinism. Operate with these constraints: the city of interest is Providence at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; under policy, the primary coastal station must confirm tide predictions using the 'harmonic_analysis' method available from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; the dataset processed is accessible at /data/processed/timeseries_boston_weather.csv covering 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z with a row_count of 120; the model of record is boston_harbor_model. Your deliverable must include the city, the primary_station_id, the model's predictions CSV path, the model metrics (AUC and Accuracy), and a summary of the processed dataset (columns, row_count, min_timestamp, max_timestamp) for /data/processed/timeseries_boston_weather.csv. For audit transparency, incorporate a completion record labeled 'status_compilation_boston' with exit_code 0 and printed timestamp 2024-03-01T13:33:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate tide predictions method/window for the resolved primary station (8443970)
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:33:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "As a data-science automation agent, your task is to prepare a dataset split based on time for Portland, ensuring that you adhere to policy precedence and determinism. You function under the Modeling & Risk Protocol — Data Preparation (Time-Based Partitioning Rule), explicitly choosing this policy for partitioning. You handle the processed dataset located at /data/processed/timeseries_seattle_weather.csv (spanning from 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, comprising 240 rows). The Portland test-fraction defined by policy is applied; when multiple values are possible, determine the decision using the city-level override to 0.22. Document the split deterministically with the timestamp 2024-02-08T12:27:00Z, following the canonical naming convention for Portland split summaries outlined by policy. Your output is a structured, machine-verifiable summary of the split with a brief overview of the processed dataset. Do not list tool names or prescribe specific steps. For audit purposes, include a completion record labeled 'dataset_split_seattle_v3' with exit_code 0 and printed timestamp 2024-02-08T12:27:00Z."
        ),
        actions=[
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="CreateTimeBasedDatasetSplit", kwargs={
                "processed_csv_path": "/data/processed/timeseries_seattle_weather.csv",
                "test_fraction": 0.22,
                "split_summary_json_path": "/processed_data/split_summary_seattle_v3.json",
                "split_ts": "2024-02-08T12:27:00Z"
            }),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "dataset_split_seattle_v3",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_seattle_v3 completed",
                "printed_ts": "2024-02-08T12:27:00Z"
            }),
        ],
        outputs=[{
            "city": "Portland",
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
            "Functioning as a data-science automation agent under the City Status Compilation Protocol, your aim is to compile a status snapshot for Portland while maintaining policy precedence and determinism. You work within these constraints: the city is Portland with coordinates 47.6062,-122.3321 and a coverage radius of 60.0 km; the primary coastal station is chosen based on that location context under policy and must validate tide predictions using the 'harmonic_analysis' method, available from 2024-02-01T00:00:00Z until 2024-02-08T00:00:00Z; access the processed dataset at /data/processed/timeseries_seattle_weather.csv covering from 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z with a row_count of 240; the model of record is simple_model. Your task includes the city, the primary_station_id, the predictions CSV path for the listed model, the model metrics (AUC and Accuracy), and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) pertaining to /data/processed/timeseries_seattle_weather.csv. For audit purposes, add a completion record labeled 'status_compilation_seattle' with exit_code 0 and printed timestamp 2024-02-08T12:53:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate tide predictions method/window for the resolved primary station (9447130)
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_seattle completed",
                "printed_ts": "2024-02-08T12:53:00Z"
            }),
        ],
        outputs=[{
            "city": "Portland",
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
            "As a data-science automation agent, your task is to choose between Portland and Orlando for model promotion based on the Cross-City AUC-Gap Promotion Protocol, ensuring adherence to policy precedence and determinism. You use an absolute AUC-gap threshold of 0.10; if the gap is beneath this threshold, opt for the city where the validated station condition is met; if both conditions are satisfied, select the city with the latest metrics.generated_ts. City specifics: Portland is located at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the main coastal station here must verify tide predictions using 'harmonic_analysis', available from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; the dataset used is /data/processed/timeseries_seattle_weather.csv (window 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the designated model is simple_model. Orlando is positioned at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; its primary coastal station must confirm water levels with the 'NAVD88' datum, available from 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z; the dataset in use is /data/processed/timeseries_miami_weather.csv; the model of choice is flood_risk_miami_v1. Your output should include only the selected city with its model metrics (AUC and Accuracy), the path to the predictions CSV for the chosen model, and a processed dataset summary (columns, row_count, min_timestamp, max_timestamp) for that city. To ensure auditability, provide a completion record named 'ccap_promotion_seattle-miami' with exit_code 0 and a timestamp of 2024-02-08T12:57:00Z."
        ),
        actions=[
            # Resolve stations (Seattle)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate Portland tide window/method; gather Portland metrics
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),

            # Resolve stations (Miami)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0
            }),
            # Validate Orlando datum/window; gather Orlando metrics
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "8723214",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-02T00:00:00Z"
            }),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_miami_v1"}),

            # Decision (gap 0.79 vs 0.73 < 0.10 → pick by recency; Portland more recent) ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T12:57:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "As a data-science automation agent, your role is to devise a time-based dataset split for Providence, maintaining adherence to policy precedence and determinism. Operate under the Modeling & Risk Protocol — Data Preparation (Time-Based Partitioning Rule) by selecting this policy explicitly for partitioning processes. Utilize the dataset processed at /data/processed/timeseries_boston_weather.csv (range 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, row_count 120). Implement the Providence test-fraction specified by policy; if multiple values are allowed, apply the city-level override to 0.28. Record the split deterministically using the timestamp 2024-03-01T13:30:00Z, adhering to the canonical naming convention for Providence split summaries as defined by policy. Deliver a structured, machine-verifiable summary of the split along with a concise description of the referenced processed dataset; do not specify tool names or steps. For audit purposes, include a completion record marked 'dataset_split_boston_v4' with an exit_code 0 and a recorded timestamp of 2024-03-01T13:30:00Z."
        ),
        actions=[
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            Action(name="CreateTimeBasedDatasetSplit", kwargs={
                "processed_csv_path": "/data/processed/timeseries_boston_weather.csv",
                "test_fraction": 0.28,
                "split_summary_json_path": "/processed_data/split_summary_boston_v4.json",
                "split_ts": "2024-03-01T13:30:00Z"
            }),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "dataset_split_boston_v4",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_boston_v4 completed",
                "printed_ts": "2024-03-01T13:30:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "Acting as a data-science automation agent within the City Status Compilation Protocol, your task is to generate a status snapshot for Providence, adhering to policy precedence and determinism. Operate with these constraints: Providence is designated at coordinates 42.3601,-71.0589, maintaining a coverage radius of 40.0 km; the primary coastal station must be resolved from that context and needs to validate tide predictions using the 'harmonic_analysis' method available between 2024-03-01T00:00:00Z and 2024-03-02T00:00:00Z; the processed dataset is located at /data/processed/timeseries_boston_weather.csv, covering from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z with 120 entries; the authoritative model is boston_harbor_model. Your output should include the city, primary_station_id, predictions CSV path for the mentioned model, the model metrics (AUC and Accuracy), and a summary of the processed dataset (columns, row_count, min_timestamp, max_timestamp) for /data/processed/timeseries_boston_weather.csv. Ensure auditability by providing a completion record labeled 'status_compilation_boston', with an exit_code 0 and a printed timestamp of 2024-03-01T13:35:00Z."
        ),
        actions=[
            # Resolve candidate stations from location context (policy requirement)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate tide predictions method/window for the resolved primary station (8443970)
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            # Model artifacts and dataset summary
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:35:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "Functioning as a data-science automation agent, your mission is to choose between Providence and Portland for model promotion in line with the Cross-City AUC-Gap Promotion Protocol, maintaining policy precedence and determinism. Implement an absolute AUC-gap threshold of 0.05; if the gap is under this level, prioritize the city where the validated station condition is met; if both cities fulfill this criterion, select the one with the latest metrics.generated_ts. City parameters: Providence is situated at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; its primary coastal station is resolved from that context and must validate tide predictions using the 'harmonic_analysis' method available between 2024-03-01T00:00:00Z and 2024-03-02T00:00:00Z; the processed dataset is found at /data/processed/timeseries_boston_weather.csv (covering the period from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, with 120 rows); its designated model is boston_harbor_model. Portland is positioned at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; the primary coastal station must be resolved in that context and validate tide predictions using the 'harmonic_analysis' method available between 2024-02-01T00:00:00Z and 2024-02-08T00:00:00Z; the processed dataset is located at /data/processed/timeseries_seattle_weather.csv (covering the window from 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, with 240 entries); its specified model is simple_model. Your output should present only the selected city along with its model metrics (AUC and Accuracy), the predictions CSV path for the selected model, and a summary of the processed dataset (columns, row_count, min_timestamp, max_timestamp) for that city. Ensure auditability by including a completion record labeled 'ccap_promotion_boston-seattle', with an exit_code 0 and a printed timestamp of 2024-03-01T13:36:00Z."
        ),
        actions=[
            # Resolve candidate stations per policy (Boston)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            # Validate Providence tide window/method; gather Providence metrics
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),

            # Resolve candidate stations per policy (Seattle)
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            # Validate Portland tide window/method; gather Portland metrics
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),

            # Decision (gap 0.79 vs 0.73 ≥ 0.05) ⇒ choose Seattle; fetch chosen artifacts only
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_boston-seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_boston-seattle completed",
                "printed_ts": "2024-03-01T13:36:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "You function as a data‑science automation agent. Your aim is to prepare a time‑based dataset division for Portland while respecting policy precedence and determinism. You operate under the Modeling & Risk Protocol — Data Preparation (Time‑Based Partitioning Rule), explicitly selecting this policy for partitioning. You handle the processed dataset at /data/processed/timeseries_seattle_weather.csv (covering 2024‑02‑01T00:00:00Z to 2024‑02‑11T00:00:00Z, row_count 240). You apply the Portland test‑fraction defined by policy; where multiple values are allowed, you resolve the choice via the city‑level override to 0.18. You document the split deterministically using the split timestamp 2024‑02‑08T12:29:00Z and the canonical naming convention for Portland split summaries defined by policy. Your deliverable is a structured, machine‑verifiable summary of the split and a brief overview of the referenced processed dataset; you do not list tool names or dictate steps. For auditability, you include a completion record labeled 'dataset_split_seattle_v4' with exit_code 0 and printed timestamp 2024‑02‑08T12:29:00Z."
        ),
        actions=[
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="CreateTimeBasedDatasetSplit", kwargs={
                "processed_csv_path": "/data/processed/timeseries_seattle_weather.csv",
                "test_fraction": 0.18,
                "split_summary_json_path": "/processed_data/split_summary_seattle_v4.json",
                "split_ts": "2024-02-08T12:29:00Z"
            }),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "dataset_split_seattle_v4",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "dataset_split_seattle_v4 completed",
                "printed_ts": "2024-02-08T12:29:00Z"
            }),
        ],
        outputs=[{
            "city": "Portland",
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
            "You act as a data-science automation agent. You determine the primary NOAA station for Providence by applying the Primary Station Determination Protocol with these constraints: you utilize coordinates 42.3601,-71.0589 and a radius of 40.0 from project_config; you require that station 8443970 employs the tide predictions method 'harmonic_analysis' in the window 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z before concluding the default 'primary' selection; you provide a summary of the processed dataset from /data/processed/timeseries_boston_weather.csv; you engage the boston_harbor_model as the active model for metrics and predictions; and you record completion in the terminal log with command 'station_determination_boston', exit_code 0, stdout '' and stderr '' and printed_ts equal to the dataset split timestamp 2024-03-01T13:18:00Z. Return exactly these fields: primary_station_id; metrics {auc, accuracy}; predictions_csv_path; processed_dataset_summary {columns, row_count, min_timestamp, max_timestamp}; and logged {command, exit_code, printed_message, printed_ts}."
        ),
        actions=[
            Action(
                name="GetStationsByLocation",
                kwargs={"query_latitude": 42.3601,
                        "query_longitude": -71.0589, "radius_km": 40.0}
            ),
            Action(
                name="GetTidePredictionsWindow",
                kwargs={
                    "station_id": "8443970",
                    "window_start_ts": "2024-03-01T00:00:00Z",
                    "window_end_ts": "2024-03-02T00:00:00Z"
                }
            ),
            Action(
                name="GetProcessedTimeseriesSummary",
                kwargs={"csv_path": "/data/processed/timeseries_boston_weather.csv"}
            ),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(
                name="AppendTerminalLogEntry",
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
            "As a data-science automation agent, handle the selection of the optimal model variant for Oakland by employing the Model Variant Selection Protocol. Note this condition: should the AUC difference between flood_risk_sf_v1 and flood_risk_sf_v2 be less than 0.02, favor the variant with the more recent metrics.generated_ts. Record the choice in the terminal log using '2024-03-18T15:45:00Z' as printed_ts. Provide the chosen_model_name and the predictions_csv_path."
        ),
        actions=[
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v1"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "Acting as a data-science automation agent, coordinate the identification of the primary NOAA station for Oakland by utilizing the Primary Station Determination Protocol with this condition: verify tide predictions for station 9414290 within the period from 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z ahead of confirming the choice. Use the processed dataset summary from /data/processed/timeseries_sf_weather.csv and the active model flood_risk_sf_v2. Log the decision in the terminal using the command 'station_determination_san-francisco' with printed_ts '2024-03-18T15:45:00Z'. Return the chosen station id, the processed_dataset_summary (columns, row_count, min_timestamp, max_timestamp), the model AUC and Accuracy, the predictions_csv_path, and the terminal log confirmation."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9414290",
                "window_start_ts": "2024-03-15T00:00:00Z",
                "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "You function as a data-science automation agent. Your task is to create a risk snapshot for Providence by implementing the City Risk Snapshot Protocol with this override: if water levels datum for station 8443970 is 'NAVD88' during the period 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z, designate the primary station as 8443970; if not, utilize 8447930. Utilize the model boston_harbor_model and the processed dataset at /data/processed/timeseries_boston_weather.csv. Record completion in the terminal log with the command 'risk_snapshot_boston' and the printed_ts '2024-03-01T13:18:00Z'. Provide the selected station id, the model AUC and Accuracy, the predictions_csv_path, the processed_dataset_summary (columns, row_count, min_timestamp, max_timestamp), and the terminal log confirmation."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "As a data-science automation agent, your requirement is to generate a comparative risk snapshot between Providence and Portland by executing the Multi-City Comparative Snapshot Protocol, adhering to policy precedence and determinism. Providence specifications: apply coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; confirm tide predictions utilizing method 'harmonic_analysis' for station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; reference /data/processed/timeseries_boston_weather.csv and model boston_harbor_model. Portland specifics: employ coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; validate tide predictions through method 'harmonic_analysis' for station 9447130 from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; refer to /data/processed/timeseries_seattle_weather.csv and model simple_model. Return the winning_city and, for each city, include the model metrics (AUC and Accuracy), the predictions CSV path, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp). For auditability, ensure a completion record is labeled 'multi_snapshot_boston-seattle' with exit_code 0, stdout '', stderr '', printed_message 'multi_snapshot_boston-seattle completed', and the printed timestamp 2024-03-01T14:12:50Z."
        ),
        actions=[
            # Providence
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Portland
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "multi_snapshot_boston-seattle",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "multi_snapshot_boston-seattle completed",
                "printed_ts": "2024-03-01T14:12:50Z"
            }),
        ],
        outputs=[{
            "winning_city": "Portland",
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
            "As a data-science automation agent, determine whether Providence or Orlando should be selected for the model promotion in line with the Cross-City AUC-Gap Promotion Protocol while adhering to policy precedence and predictability. Employ a set AUC-gap threshold of 0.04; select the city whose validated station condition is successful if the gap is less than this limit; in cases both conditions are successful, choose based on the city with the latest metrics.generated_ts. Providence specifics: operate using coordinates 42.3601,-71.0589 within a 40.0 km coverage area; assure tide predictions validation employing 'harmonic_analysis' for station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; refer to /data/processed/timeseries_boston_weather.csv and the boston_harbor_model. Orlando specifics: operate with coordinates 25.7617,-80.1918 within a 25.0 km coverage area; ensure validation of water levels using datum 'NAVD88' for station 8723214 from 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z; refer to /data/processed/timeseries_miami_weather.csv and the flood_risk_miami_v1 model. Your output should display only the selected city along with its model metrics (AUC and Accuracy), the designated predictions CSV path for the selected model, and a summary of the processed dataset (columns, row_count, min_timestamp, max_timestamp) of the selected city. For auditing, attach a completion record tagged 'ccap_promotion_boston-miami' including exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_boston-miami completed', and the timestamp noted as 2024-03-01T14:13:30Z."
        ),
        actions=[
            # Providence validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            # Orlando validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Winner artifacts (Boston)
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Audit log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_boston-miami",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_boston-miami completed",
                "printed_ts": "2024-03-01T14:13:30Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Providence",
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
            "Acting as a data-science automation agent, make a promotion choice between Oakland and Orlando by using the Cross-City AUC-Gap Promotion Protocol with this adjustment: employ an AUC gap threshold of 0.12; when |AUC(flood_risk_sf_v2) - AUC(flood_risk_miami_v1)| is less than 0.12, select the city with a passing validated station condition; otherwise opt for the city with a superior AUC. Ensure for Oakland that station 9414290 confirms tide predictions by method 'harmonic' during 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z; validate for Orlando that station 8723214 meets water levels with datum 'NAVD88' for 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z. If Oakland ends up being selected, extract the summary of the processed dataset from /data/processed/timeseries_sf_weather.csv; if Orlando is selected, obtain it from /data/processed/timeseries_miami_weather.csv. Log the completion in the terminal using command 'ccap_promotion_san-francisco-miami' with printed_ts '2024-03-18T15:45:00Z'. Deliver the chosen_city, its metrics (auc, accuracy), its predictions_csv_path, the processed_dataset_summary (columns, row_count, min_timestamp, max_timestamp), and the terminal log confirmation."
        ),
        actions=[
            # SF validations and artifacts
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9414290",
                "window_start_ts": "2024-03-15T00:00:00Z",
                "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # Orlando validations and artifacts
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "8723214",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Winner artifacts (SF)
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_san-francisco-miami", "exit_code": 0,
                "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-miami completed",
                "printed_ts": "2024-03-18T15:45:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Oakland",
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
            "As a data-science automation agent, your task is to select between Orlando and Portland for model promotion according to the Cross-City AUC-Gap Promotion Protocol, ensuring adherence to policy precedence and determinism. Utilize an absolute AUC-gap threshold of 0.07; if the gap is below this value, prioritize the city where the validated station condition is satisfactory; if both succeed, select the city with the latest metrics.generated_ts. For Orlando, apply constraints by using coordinates 25.7617,-80.1918 with a 25.0 km coverage radius; validate water levels against datum 'NAVD88' for station 8723214 spanning 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z; refer to /data/processed/timeseries_miami_weather.csv and model flood_risk_miami_v1. For Portland, apply constraints by using coordinates 47.6062,-122.3321 with a 60.0 km coverage radius; validate tide predictions via method 'harmonic_analysis' for station 9447130 from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; refer to /data/processed/timeseries_seattle_weather.csv and model simple_model. The deliverable should contain only the chosen_city along with its model metrics (AUC and Accuracy), the path to predictions CSV for the selected model, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) for the selected city. Ensure auditability by including a completion record labeled 'ccap_promotion_miami-seattle' with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_miami-seattle completed', and printed timestamp 2024-02-08T13:04:55Z."
        ),
        actions=[
            # Orlando
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Portland
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            # Winner: Portland
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_miami-seattle",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_miami-seattle completed",
                "printed_ts": "2024-02-08T13:04:55Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "As a data-science automation agent, it is necessary to implement the System Audit and Provenance Protocol for Oakland, taking into account these specific overrides: confirm the precise terminal command \"jupyter nbconvert --to html notebooks/exploratory_analysis.ipynb\"; limit MCP tool call retrieval solely to the 'gmail' server; employ /processed_data/features.csv with model flood_risk_sf_v2 and authenticate the configuration text at /config/model_config.json; disseminate an audit receipt to stakeholder outputs using /results/predictions_sf_v2.csv and /results/metrics_sf_v2.csv, ensuring generated_ts matches the metrics.generated_ts of flood_risk_sf_v2, and log the audit completion in the terminal using the command 'audit_provenance_san-francisco' paired with the identical metrics timestamp as printed_ts. Provide the audit report including: details of a 7-day weather forecast, a features record, the model record, configuration file text, the validated terminal command outcome, the MCP calls slice constrained to the 'gmail' server, the Gmail message with subject 'San Francisco Flood Risk Analysis - Complete Results', the issued receipt, and the terminal log verification."
        ),
        actions=[
            Action(name="GetWeatherForecastByCity", kwargs={
                   "city": "Oakland", "horizon_days": 7}),
            Action(name="GetFeaturesByCsvPath", kwargs={
                   "csv_path": "/processed_data/features.csv"}),
            Action(name="GetModelByName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            Action(name="GetFileTextByPath", kwargs={
                   "path": "/config/model_config.json"}),
            Action(name="GetTerminalLogCommandResult", kwargs={
                "command": "jupyter nbconvert --to html notebooks/exploratory_analysis.ipynb"}),
            Action(name="GetMcpToolCallsByServer",
                   kwargs={"server_name": "gmail"}),
            Action(name="GetGmailMessageBySubject", kwargs={
                "subject": "San Francisco Flood Risk Analysis - Complete Results"}),
            Action(name="PublishStakeholderOutputs", kwargs={
                "predictions_final_csv_path": "/results/predictions_sf_v2.csv",
                "metrics_summary_csv_path": "/results/metrics_sf_v2.csv",
                "generated_ts": "2024-03-18T15:45:00Z"
            }),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "audit_provenance_san-francisco", "exit_code": 0,
                "stdout": "", "stderr": "",
                "printed_message": "audit_provenance_san-francisco completed",
                "printed_ts": "2024-03-18T15:45:00Z"
            }),
        ],
        outputs=[{
            "weather": {"city": "Oakland", "horizon_days": 7},
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
            "You function as a data-science automation agent. Your goal is to select either Portland or Orlando for model promotion according to the Cross-City AUC-Gap Promotion Protocol, ensuring adherence to policy precedence and determinism. An absolute AUC-gap threshold of 0.06 is applied; if the gap is under this threshold, prioritize the city with a validated station condition; if both qualify, choose based on the most recent metrics.generated_ts. City constraints: Portland is located at coordinates 47.6062,-122.3321 with a 60.0 km coverage radius; the primary coastal station is identified from the location context and must verify tide predictions using 'harmonic_analysis' available from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; the dataset processed is /data/processed/timeseries_seattle_weather.csv (window 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z, row_count 240); the reference model is simple_model. Orlando is located at coordinates 25.7617,-80.1918 with a 25.0 km coverage radius; the primary coastal station is identified from the location context and must validate water levels with 'NAVD88' datum accessible from 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z; the dataset processed is /data/processed/timeseries_miami_weather.csv; the reference model is flood_risk_miami_v1. Your task returns only the selected city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. For audit purposes, provide a completion record titled 'ccap_promotion_seattle-miami' with exit_code 0 and printed timestamp 2024-02-08T12:42:00Z."
        ),
        actions=[
            # Resolve & validate Portland
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            # Resolve & validate Orlando
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Winner artifacts (gap == 0.06 ⇒ not below threshold ⇒ choose higher AUC: Portland)
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_seattle-miami", "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_seattle-miami completed", "printed_ts": "2024-02-08T12:42:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "You serve as a data-science automation agent executing the Primary Station Determination Protocol. Your task is to identify Boston's primary NOAA station while maintaining policy precedence and determinism. Using coordinates 42.3601,-71.0589 with a 40.0 km coverage radius, ensure station 8443970 offers tide predictions through 'harmonic_analysis' from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z and water levels with 'NAVD88' datum from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z prior to confirming the primary choice. Refer to /data/processed/timeseries_boston_weather.csv and the model boston_harbor_model. Your deliverable should contain the primary_station_id, the model metrics (AUC and Accuracy), the predictions CSV path, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp). For audit purposes, include a completion record labeled 'station_determination_boston' with exit_code 0 and printed timestamp 2024-03-01T14:16:10Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={"query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={"station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetWaterLevelsWindow", kwargs={"station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetPredictionsByModelName", kwargs={"model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={"model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={"csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "You function as a data‑science automation agent. Your aim is to establish a time‑based dataset partition for Portland while adhering to policy precedence and determinism. You follow the Modeling & Risk Protocol — Data Preparation (Time‑Based Partitioning Rule), deliberately choosing this policy for partitioning. You handle the processed dataset at /data/processed/timeseries_seattle_weather.csv (spanning 2024‑02‑01T00:00:00Z to 2024‑02‑11T00:00:00Z, row_count 240). Apply the Portland test‑fraction as specified by policy; where multiple values are feasible, use the city‑level override to 0.15. Record the split deterministically using the split timestamp 2024‑02‑08T12:31:00Z and apply the canonical naming convention for Portland split summaries as per policy. Your output is a structured, machine‑verifiable summary of the split along with a brief description of the referenced processed dataset; tool names or step prescriptions are not enumerated. For audit purposes, include a completion record labeled 'dataset_split_seattle_v5' with exit_code 0 and printed timestamp 2024‑02‑08T12:31:00Z."
        ),
        actions=[
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="CreateTimeBasedDatasetSplit", kwargs={
                "processed_csv_path": "/data/processed/timeseries_seattle_weather.csv",
                "test_fraction": 0.15,
                "split_summary_json_path": "/processed_data/split_summary_seattle_v5.json",
                "split_ts": "2024-02-08T12:31:00Z"
            }),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "dataset_split_seattle_v5", "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "dataset_split_seattle_v5 completed", "printed_ts": "2024-02-08T12:31:00Z"
            }),
        ],
        outputs=[{
            "city": "Portland",
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
            "As a data‑science automation agent, your task is to generate a status snapshot for Providence while observing policy precedence and determinism. Employ coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; verify tide forecasts using method 'harmonic_analysis' for station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z and assess water levels with datum 'NAVD88' from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z. Operate on /data/processed/timeseries_boston_weather.csv and utilize model boston_harbor_model. Your task includes the city, the primary_station_id, the predictions CSV path, the model metrics (AUC and Accuracy), and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). For audit purposes, include a completion record labeled 'status_compilation_boston' with exit_code 0, stdout '', stderr '', printed_message 'status_compilation_boston completed', and a timestamp printed at 2024-03-01T14:07:00Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T14:07:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "You are a data‑science automation agent. Your task is to choose between Providence and Portland for model promotion under the Cross‑City AUC‑Gap Promotion Protocol while respecting policy precedence and determinism. An absolute AUC‑gap threshold of 0.08 is applied; if the gap is below this threshold, favor the city with a passing validated station condition; if both conditions pass, select the city with the latest metrics.generated_ts. Providence setup: use coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; validate tide predictions with 'harmonic_analysis' for station 8443970 from 2024‑03‑01T00:00:00Z through 2024‑03‑02T00:00:00Z; reference /data/processed/timeseries_boston_weather.csv and model boston_harbor_model. Portland setup: use coordinates 47.6062,-122.3321 with a 60.0 km coverage radius; validate tide predictions with 'harmonic_analysis' for station 9447130 from 2024‑02‑01T00:00:00Z through 2024‑02‑08T00:00:00Z; reference /data/processed/timeseries_seattle_weather.csv and model simple_model. The deliverable includes only the chosen_city with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a summary of the processed‑dataset (columns, row_count, min_timestamp, max_timestamp) for the selected city. For audit purposes, incorporate a completion record tagged 'ccap_promotion_boston-seattle' with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_boston-seattle completed', and a printed timestamp 2024‑03‑01T14:08:00Z."
        ),
        actions=[
            # Providence
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            # Portland
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            # Winner: Portland
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_boston-seattle",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_boston-seattle completed",
                "printed_ts": "2024-03-01T14:08:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "You are a data‑science automation agent. Your task is to choose between Portland and Orlando for model promotion under the Cross‑City AUC‑Gap Promotion Protocol while respecting policy precedence and determinism. An absolute AUC‑gap threshold of 0.10 is applied; if the gap is below this threshold, favor the city with a passing validated station condition; if both pass, select the city with the latest metrics.generated_ts. Portland setup: coordinates 47.6062,-122.3321 with a 60.0 km coverage radius; validate tide predictions using 'harmonic_analysis' for station 9447130 from 2024‑02‑01T00:00:00Z to 2024‑02‑08T00:00:00Z; processed dataset /data/processed/timeseries_seattle_weather.csv; model simple_model. Orlando setup: coordinates 25.7617,-80.1918 with a 25.0 km coverage radius; validate water levels using datum 'NAVD88' for station 8723214 from 2024‑02‑01T00:00:00Z to 2024‑02‑02T00:00:00Z; processed dataset /data/processed/timeseries_miami_weather.csv; model flood_risk_miami_v1. The deliverable includes only the chosen_city with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a summary of the processed‑dataset (columns, row_count, min_timestamp, max_timestamp) for the chosen city. For audit purposes, incorporate a completion record tagged 'ccap_promotion_seattle-miami' with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_seattle-miami completed', and a printed timestamp 2024‑02‑08T13:02:00Z."
        ),
        actions=[
            # Portland validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            # Orlando validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_miami_v1"}),
            # Winner: Portland
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_seattle-miami",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_seattle-miami completed",
                "printed_ts": "2024-02-08T13:02:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "As a data-science automation agent functioning under the City Status Compilation Protocol, your task is to create a status snapshot for Providence, following policy precedence and determinism. You will utilize the coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km. Confirm tide predictions through the 'harmonic_analysis' method for station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z, and check water levels using datum 'NAVD88' from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z. Reference /data/processed/timeseries_boston_weather.csv and employ the boston_harbor_model. The deliverable should encompass the city, primary_station_id, the path to predictions CSV for the respective model, model metrics (AUC and Accuracy), and a processed-dataset summary (including columns, row_count, min_timestamp, max_timestamp). For audit purposes, submit a completion record tagged 'status_compilation_boston' with exit_code 0, stdout '', stderr '', printed_message 'status_compilation_boston completed', and a printed timestamp of 2024-03-01T14:10:30Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T14:10:30Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "Act as a data-science automation agent tasked to determine whether Oakland or Orlando should be selected for model promotion under the Cross-City AUC-Gap Promotion Protocol while maintaining policy precedence and determinism. An absolute AUC-gap threshold of 0.06 should be applied; if the gap is below this threshold, favour the city whose validated station condition is met; if both satisfy conditions, choose based on the most recent metrics.generated_ts. For Oakland, apply 37.7749,-122.4194 coordinates with a 50.0 km coverage radius and validate tide predictions via 'harmonic_analysis' for station 9414290 from 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z. Reference /data/processed/timeseries_sf_weather.csv and use the model flood_risk_sf_v2. For Orlando, work with coordinates 25.7617,-80.1918 with a 25.0 km coverage radius; validate water levels using datum 'NAVD88' for station 8723214 from 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z. Use /data/processed/timeseries_miami_weather.csv and the model flood_risk_miami_v1. The deliverable should only return the chosen_city along with its model metrics (AUC and Accuracy), the predictions CSV path for the chosen model, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) for the selected city. To ensure auditability, include a completion record labeled 'ccap_promotion_san-francisco-miami' with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_san-francisco-miami completed', and a printed timestamp of 2024-03-18T16:28:10Z."
        ),
        actions=[
            # SF validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # Orlando validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Winner artifacts (San Francisco)
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_san-francisco-miami",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-miami completed",
                "printed_ts": "2024-03-18T16:28:10Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Oakland",
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
            "As a data-science automation agent, your task is to choose between Oakland and Providence for model promotion under the Cross-City AUC-Gap Promotion Protocol while ensuring adherence to policy precedence and determinism. Apply an absolute AUC-gap threshold of 0.07; if the gap is less than this threshold, favor the city whose validated station condition is successful; if both are successful, select the city with the latest metrics.generated_ts. Oakland constraints: operate with coordinates 37.7749,-122.4194 within a 50.0 km coverage radius; validate tide predictions using the 'harmonic_analysis' method for station 9414290 from 2024-03-15T00:00:00Z through 2024-03-22T00:00:00Z; reference /data/processed/timeseries_sf_weather.csv and model flood_risk_sf_v2. Providence constraints: work with coordinates 42.3601,-71.0589 within a 40.0 km coverage radius; validate tide predictions using the 'harmonic_analysis' method for station 8443970 from 2024-03-01T00:00:00Z through 2024-03-02T00:00:00Z; reference /data/processed/timeseries_boston_weather.csv and model boston_harbor_model. Return only the chosen_city along with its model metrics (AUC and Accuracy), the predictions CSV path for the selected model, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. For auditability, provide a completion record labeled 'ccap_promotion_san-francisco-boston' with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_san-francisco-boston completed', and printed timestamp 2024-03-18T16:21:00Z."
        ),
        actions=[
            # Oakland
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_sf_v2"}),
            # Providence
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            # Winner: Oakland
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_san-francisco-boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-boston completed",
                "printed_ts": "2024-03-18T16:21:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Oakland",
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
            "Function as a data-science automation agent under the City Risk Snapshot Protocol. Generate a risk snapshot for Providence while maintaining compliance with policy precedence and determinism. Utilize coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; verify tide predictions using the 'harmonic_analysis' method for station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z and water levels with datum 'NAVD88' from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z. Utilize /data/processed/timeseries_boston_weather.csv (row_count 120; coverage 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z) and model boston_harbor_model. Include in the deliverable the primary_station_id, the model metrics (AUC and Accuracy), the predictions CSV path, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp). For auditability, attach a completion record labeled 'risk_snapshot_boston' with exit_code 0, stdout '', stderr '', printed_message 'risk_snapshot_boston completed', and printed timestamp 2024-03-01T14:05:00Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetPredictionsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "You are a data-science automation agent. Your task is to select between Oakland and Providence for model promotion under the Cross-City AUC-Gap Promotion Protocol while adhering to policy precedence and determinism. An absolute AUC-gap threshold of 0.05 is applied; when the gap falls under this threshold, favor the city whose validated station condition succeeds; if both succeed, choose the city with the latest metrics.generated_ts. City constraints: Oakland is located at coordinates 37.7749,-122.4194 with a coverage radius of 50.0 km; the primary coastal station is determined from that location context and must validate tide predictions using the 'harmonic' method available from 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z; the processed dataset is /data/processed/timeseries_sf_weather.csv; the official model is flood_risk_sf_v2. Providence is located at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station is determined from that location context and must validate tide predictions using the 'harmonic' method available from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; the processed dataset is /data/processed/timeseries_boston_weather.csv; the official model is boston_harbor_model. If Oakland is selected, read the processed-dataset summary from /data/processed/timeseries_sf_weather.csv; if Providence is selected, read it from /data/processed/timeseries_boston_weather.csv. Your deliverable includes only the chosen_city along with its model metrics (AUC and Accuracy), the predictions_csv_path for the selected model, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) for the selected city. For auditability, provide a completion record labeled 'ccap_promotion_san-francisco-boston' with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_san-francisco-boston completed', and printed timestamp 2024-03-18T15:55:00Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0
            }),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9414290",
                "window_start_ts": "2024-03-15T00:00:00Z",
                "window_end_ts": "2024-03-22T00:00:00Z"
            }),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),

            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),

            # Winner: Oakland (AUC 0.89 > 0.73)
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"
            }),

            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_san-francisco-boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-boston completed",
                "printed_ts": "2024-03-18T15:55:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Oakland",
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
            "You are a data-science automation agent. Your task is to choose between Portland and Providence for model promotion under the Cross-City AUC-Gap Promotion Protocol while observing policy precedence and determinism. Apply an absolute AUC-gap threshold of 0.06; if the gap is below this threshold, favor the city whose validated station condition is met; if both are met, select the city with the most recent metrics.generated_ts. Portland details: coordinates 47.6062,-122.3321 with a 60.0 km coverage radius; validate tide predictions using the 'harmonic_analysis' method for station 9447130 from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; dataset /data/processed/timeseries_seattle_weather.csv; model is simple_model. Providence details: coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; validate tide predictions using the 'harmonic_analysis' method for station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; dataset /data/processed/timeseries_boston_weather.csv; model is boston_harbor_model. Provide only the chosen_city, its model metrics (AUC and Accuracy), its predictions CSV path, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp). To ensure auditability, you include a completion record labeled 'ccap_promotion_seattle-boston' with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_seattle-boston completed', and printed timestamp 2024-03-01T14:06:00Z."
        ),
        actions=[
            # Portland
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            # Providence
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            # Winner: Portland
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-03-01T14:06:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "As a data‑science automation agent, you are required to generate a station confirmation snapshot for Providence by applying the Datum‑and‑Method Station Confirmation Protocol, following policy precedence and determinism. Operate within these constraints: coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the candidate station 8443970 should confirm water levels with datum 'NAVD88' from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z and tide predictions using method 'harmonic_analysis' from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; the processed dataset path is /data/processed/timeseries_boston_weather.csv; utilize the model of record boston_harbor_model. Provide a deliverable inclusive of the chosen_station_id, the model metrics (AUC and Accuracy), the predictions_csv_path, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). Ensure auditability by including a completion record labeled 'dmsc_snapshot_boston' with exit_code 0, stdout '', stderr '', printed_message 'dmsc_snapshot_boston completed', and printed timestamp 2024-03-01T13:29:00Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-06T00:00:00Z"
            }),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "As a data‑science automation agent, it is your task to identify the primary NOAA station for Portland by implementing the Primary Station Determination Protocol, adhering to policy precedence and determinism. Work within these parameters: coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; ensure station 9447130 provides tide predictions using method 'harmonic_analysis' from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z prior to confirming the primary selection. The processed dataset should be /data/processed/timeseries_seattle_weather.csv, and use simple_model as the model of record. Deliver your findings including the primary_station_id, the model metrics (AUC and Accuracy), the predictions_csv_path, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). For audit purposes, include a completion record labeled 'station_determination_seattle' with exit_code 0, stdout '', stderr '', printed_message 'station_determination_seattle completed', and printed timestamp 2024-02-08T12:46:00Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "You function as a data-science automation agent. Coordinate a comparative risk snapshot between Oakland and Providence using the Multi-City Comparative Snapshot Protocol with the following adjustments: for Oakland, ensure the use of method 'harmonic' for tide predictions at station 9414290 during the period 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z; for Providence, confirm the water levels at station 8443970 within the window 2024-02-15T00:00:00Z to 2024-03-16T00:00:00Z adhere to datum 'NAVD88'. Should the AUC difference between flood_risk_sf_v2 and boston_harbor_model fall under 0.02, select the city whose validated station meets its condition; if not, opt for the city with the superior AUC. Return details of the selected city, including model AUC and Accuracy, the path to the predictions CSV, and the processed dataset summary from /data/processed/timeseries_<city>_weather.csv for the chosen location. Consider the configured station search distance from project_config for each city and utilize 2024-03-18T15:45:00Z as the timestamp for the terminal log entry. Apply coordinates 37.7749,-122.4194 with a radius of 50.0 for Oakland, and coordinates 42.3601,-71.0589 with a radius of 40.0 for Providence."
        ),
        actions=[
            Action(name="GetProjectConfigByCity",
                   kwargs={"target_city": "Oakland"}),
            Action(
                name="GetStationsByLocation",
                kwargs={"query_latitude": 37.7749,
                        "query_longitude": -122.4194, "radius_km": 50.0}
            ),
            Action(
                name="GetTidePredictionsWindow",
                kwargs={
                    "station_id": "9414290",
                    "window_start_ts": "2024-03-15T00:00:00Z",
                    "window_end_ts": "2024-03-22T00:00:00Z"
                }
            ),
            Action(
                name="GetProcessedTimeseriesSummary",
                kwargs={"csv_path": "/data/processed/timeseries_sf_weather.csv"}
            ),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "flood_risk_sf_v2"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProjectConfigByCity",
                   kwargs={"target_city": "Providence"}),
            Action(
                name="GetStationsByLocation",
                kwargs={"query_latitude": 42.3601,
                        "query_longitude": -71.0589, "radius_km": 40.0}
            ),
            Action(
                name="GetWaterLevelsWindow",
                kwargs={
                    "station_id": "8443970",
                    "window_start_ts": "2024-02-15T00:00:00Z",
                    "window_end_ts": "2024-03-16T00:00:00Z"
                }
            ),
            Action(
                name="GetProcessedTimeseriesSummary",
                kwargs={"csv_path": "/data/processed/timeseries_boston_weather.csv"}
            ),
            Action(name="GetMetricsByModelName", kwargs={
                "model_name": "boston_harbor_model"}),
            Action(
                name="AppendTerminalLogEntry",
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
            "chosen_city": "Oakland",
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
        instruction="You lead the audit for Oakland. Implement the System Audit and Provenance Protocol including these overrides and limitations: limit MCP evidence to the 'weather-api' server; accept NOAA station 9414290 with harmonic tide predictions from 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z and an MLLW water-level history from 2024-02-14T00:00:00Z to 2024-03-15T00:00:00Z; incorporate a 7-day weather forecast for San Francisco; mandate the Gmail message titled 'Weekly Progress Update - Flood Prediction Project' as evidence of external communication; verify successful completion of the training/evaluation run 'python src/models/train_model.py --config config/model_config.json'; and conclude by documenting the checkpoint 'promotion_sf_model' with exit_code 0, stdout 'promotion audit checkpoint', stderr 'none', printed_message 'promotion approved', and printed_ts '2024-03-17T12:50:00Z'. Prepare a concise audit report that references each source of evidence and determines whether the protocol standards are satisfied.",
        actions=[
            Action(name="GetMcpToolCallsByServer",
                   kwargs={"server_name": "weather-api"}),
            Action(name="GetWeatherForecastByCity", kwargs={
                "city": "Oakland", "horizon_days": 7}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9414290",
                "window_start_ts": "2024-03-15T00:00:00Z",
                "window_end_ts": "2024-03-22T00:00:00Z"
            }),
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "9414290",
                "window_start_ts": "2024-02-14T00:00:00Z",
                "window_end_ts": "2024-03-15T00:00:00Z"
            }),
            Action(name="GetGmailMessageBySubject", kwargs={
                "subject": "Weekly Progress Update - Flood Prediction Project"}),
            Action(name="GetTerminalLogCommandResult", kwargs={
                "command": "python src/models/train_model.py --config config/model_config.json"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "forecast_city": "Oakland",
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
            "As a data-science automation agent, your aim is to choose between Providence and Portland for model promotion adhering to the Cross-City AUC-Gap Promotion Protocol while following policy precedence and determinism. Implement an absolute AUC-gap threshold of 0.04; if the gap falls below this threshold, prioritize the city with validated station conditions; if both cities' stations validate, opt for the city with the latest metrics.generated_ts. Providence requirements include coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; station validation entails tide predictions using the 'harmonic_analysis' method available from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; utilize processed dataset /data/processed/timeseries_boston_weather.csv; and the model boston_harbor_model. For Portland, follow constraints including coordinates 47.6062,-122.3321 and a coverage radius of 60.0 km; verify station validation through tide predictions using the 'harmonic_analysis' method available from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; processed dataset /data/processed/timeseries_seattle_weather.csv; and model simple_model. If Portland is selected, consult the processed-dataset summary from /data/processed/timeseries_seattle_weather.csv; if Providence is selected, review it from /data/processed/timeseries_boston_weather.csv. Your output should provide only the chosen_city, including its model metrics (AUC and Accuracy), the predictions_csv_path for the chosen model, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) for the selected city. To ensure auditability, add a completion record tagged 'ccap_promotion_boston-seattle' with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_boston-seattle completed', and a printed timestamp 2024-03-01T13:40:00Z."
        ),
        actions=[
            # Providence
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),

            # Portland
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),

            # Winner: Portland
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),

            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_boston-seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_boston-seattle completed",
                "printed_ts": "2024-03-01T13:40:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "Assigned as a data-science automation agent, you are required to generate a risk snapshot for Portland by deploying the City Risk Snapshot Protocol while maintaining policy precedence and determinism. Utilize coordinates 47.6062,-122.3321 with a 60.0 km coverage radius, ensuring tide predictions using method 'harmonic_analysis' for station 9447130 during the period from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z. Implement /data/processed/timeseries_seattle_weather.csv as the processed dataset and simple_model as the designated model. Your deliverable must comprise the primary_station_id, the model metrics (AUC and Accuracy), the predictions_csv_path, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp). To facilitate auditability, append a completion record tagged 'risk_snapshot_seattle' with exit_code 0, stdout '', stderr '', printed_message 'risk_snapshot_seattle completed', and a printed timestamp 2024-02-08T12:47:00Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0
            }),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9447130",
                "window_start_ts": "2024-02-01T00:00:00Z",
                "window_end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "Act as a data-science automation agent guided by the City Status Compilation Protocol. Your task involves generating a status snapshot for Providence, adhering to policy precedence and determinism. Apply coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km, ensuring that the main coastal station confirms tide predictions through 'harmonic_analysis' between 2024-03-01T00:00:00Z and 2024-03-02T00:00:00Z. Utilize /data/processed/timeseries_boston_weather.csv (row_count 120; coverage 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z) as the processed dataset and boston_harbor_model as the authoritative model. Your output should incorporate the city, the primary_station_id, model metrics (AUC and Accuracy), the predictions_csv_path, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp). For audit purposes, provide a completion record tagged 'status_compilation_boston' with exit_code 0, stdout '', stderr '', printed_message 'status_compilation_boston completed', and timestamp 2024-03-01T13:41:00Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0
            }),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970",
                "window_start_ts": "2024-03-01T00:00:00Z",
                "window_end_ts": "2024-03-02T00:00:00Z"
            }),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"
            }),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T13:41:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "You are required to act as a data-science automation agent. Your goal is securing a comparative risk snapshot between Oakland and Portland, applying the Multi-City Comparative Snapshot Protocol while following policy precedence and determinism. Constraints for San Francisco: coordinates 37.7749,-122.4194 with a coverage radius of 50.0 km; confirm tide predictions via 'harmonic' from 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z; use dataset /data/processed/timeseries_sf_weather.csv; model flood_risk_sf_v2. Constraints for Seattle: coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; verify tide predictions using 'harmonic' from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; processed dataset /data/processed/timeseries_seattle_weather.csv; model simple_model. Present the winning_city, as well as for each city, model metrics (AUC and Accuracy), predictions_csv_path, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp). For audit purposes, incorporate a completion record named 'multi_snapshot_san-francisco-seattle' with exit_code 0 and printed timestamp 2024-03-18T16:20:00Z."
        ),
        actions=[
            # Oakland
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),

            # Portland
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),

            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "multi_snapshot_san-francisco-seattle",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "multi_snapshot_san-francisco-seattle completed",
                "printed_ts": "2024-03-18T16:20:00Z"
            }),
        ],
        outputs=[{
            "winning_city": "Oakland",
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
            "Act as a data‑science automation agent and determine the better choice between Oakland and Orlando for model promotion under the Cross‑City AUC‑Gap Promotion Protocol, ensuring adherence to policy precedence and determinism. Utilize an absolute AUC‑gap threshold of 0.09; if the gap is within this threshold, favor the city whose validated station condition is confirmed; if both conditions are met, select the city with the latest metrics.generated_ts. Oakland is located at coordinates 37.7749,-122.4194 with a 50.0 km coverage radius; the primary coastal station is derived from the location context and should validate tide predictions using the 'harmonic_analysis' method available from 2024‑03‑15T00:00:00Z to 2024‑03‑22T00:00:00Z; the processed dataset is /data/processed/timeseries_sf_weather.csv, and the model of record is flood_risk_sf_v2. Orlando is positioned at coordinates 25.7617,-80.1918 with a 25.0 km coverage radius; the primary coastal station is drawn from the location context and needs to validate water levels with the datum 'NAVD88' available from 2024‑02‑01T00:00:00Z to 2024‑02‑02T00:00:00Z; the processed dataset is /data/processed/timeseries_miami_weather.csv, and the model of record is flood_risk_miami_v1. If Oakland is chosen, consult the processed‑dataset summary from /data/processed/timeseries_sf_weather.csv; if Orlando is selected, use the summary from /data/processed/timeseries_miami_weather.csv. The output includes only the chosen_city with its model metrics (AUC and Accuracy), the predictions_csv_path for the chosen model, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the selected city. Ensure auditability by recording a completion record tagged 'ccap_promotion_san-francisco-miami' with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_san-francisco-miami completed', and the printed timestamp 2024‑03‑18T16:01:00Z."
        ),
        actions=[
            # Oakland validations and metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),

            # Orlando validations and metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_miami_v1"}),

            # Winner artifacts (AUC 0.89 − 0.73 ≥ 0.09 ⇒ Oakland)
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),

            # Deterministic audit record
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_san-francisco-miami",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-miami completed",
                "printed_ts": "2024-03-18T16:01:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Oakland",
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
            "Serve as a data‑science automation agent to choose between Providence and Oakland for model promotion under the Cross‑City AUC‑Gap Promotion Protocol, respecting policy precedence and determinism. Implement an absolute AUC‑gap threshold of 0.06; if the gap falls below this threshold, select the city with the successfully validated station condition; if both validate, pick the city with the most updated metrics.generated_ts. Providence is located at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; the primary coastal station is resolved from that location context and must validate tide predictions using the 'harmonic_analysis' method available from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z; the processed dataset is /data/processed/timeseries_boston_weather.csv, and the model of record is boston_harbor_model. Oakland is at coordinates 37.7749,-122.4194 with a coverage radius of 50.0 km; the primary coastal station is determined from that location context and should validate tide predictions using 'harmonic_analysis' available from 2024‑03‑15T00:00:00Z through 2024‑03‑22T00:00:00Z; the processed dataset is /data/processed/timeseries_sf_weather.csv, and the model of record is flood_risk_sf_v2. The output returns only the chosen_city with its model metrics (AUC and Accuracy), the predictions_csv_path for the selected model, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. Ensure traceability by recording a completion document labeled 'ccap_promotion_boston-san-francisco' with exit_code 0, stdout '', stderr '', printed_message 'ccap_promotion_boston-san-francisco completed', and a printed timestamp 2024‑03‑18T16:02:00Z."
        ),
        actions=[
            # Providence validation and metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),

            # Oakland validation and metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),

            # Winner artifacts (AUC 0.89 − 0.73 ≥ 0.06 ⇒ Oakland)
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),

            # Audit
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_boston-san-francisco",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_boston-san-francisco completed",
                "printed_ts": "2024-03-18T16:02:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Oakland",
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
            "As a data‑science automation agent functioning under the City Risk Snapshot Protocol, your task is to generate a risk snapshot for Providence while respecting policy precedence and determinism. You work with the following parameters: the city set as Providence with coordinates 42.3601,-71.0589 within a 40.0 km radius; validate tide forecasts using the 'harmonic_analysis' method for station 8443970 for the timeframe 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z, and verify water levels with datum 'NAVD88' at the same station spanning 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z; the processed dataset is /data/processed/timeseries_boston_weather.csv (row_count 120; range 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z); the main model utilized is boston_harbor_model. Your deliverable must comprise the primary_station_id, model metrics (AUC and Accuracy), the predictions_csv_path, and a summary of the processed‑dataset (columns, row_count, min_timestamp, max_timestamp). To ensure auditability, include a labeled completion record 'risk_snapshot_boston' with exit_code 0, stdout '', stderr '', printed_message 'risk_snapshot_boston completed', and a printed timestamp 2024‑03‑01T13:42:00Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetWaterLevelsWindow", kwargs={
                "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "Acting as a data‑science automation agent under the City Status Compilation Protocol, your objective is to produce a status snapshot for Providence ensuring compliance with policy precedence and determinism. You perform operations under these constraints: select Providence with coordinates 42.3601,-71.0589 maintaining a coverage radius of 40.0 km; validate tide forecasts using 'harmonic_analysis' for station 8443970 from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z and confirm water levels using datum 'NAVD88' from 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z; utilize the processed dataset at /data/processed/timeseries_boston_weather.csv (row_count 120; coverage 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z); employ the designated model boston_harbor_model. Your output must contain the city, the primary_station_id, the predictions CSV path related to the specified model, the model metrics (AUC and Accuracy), and a summary of the processed‑dataset (columns, row_count, min_timestamp, max_timestamp). To uphold auditability, include a completion note labeled 'status_compilation_boston' with an outputted timestamp 2024‑03‑01T14:02:00Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "status_compilation_boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "status_compilation_boston completed",
                "printed_ts": "2024-03-01T14:02:00Z"
            }),
        ],
        outputs=[{
            "city": "Providence",
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
            "As a data-science automation agent, you operate under the City Risk Snapshot Protocol, focusing on creating a risk snapshot for Portland while adhering to policy precedence and determinism. Act within the following constraints: the city is Portland with coordinates 47.6062,-122.3321 and a coverage radius of 60.0 km; verify tide predictions using the 'harmonic_analysis' method and water levels with datum 'NAVD88' for station 9447130 from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; process the dataset /data/processed/timeseries_seattle_weather.csv (row_count 240; coverage from 2024-02-01T00:00:00Z to 2024-02-11T00:00:00Z); the model of record is simple_model. Your deliverable should comprise the primary_station_id, model metrics (AUC and Accuracy), predictions CSV path, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp). To ensure auditability, include a completion record marked 'risk_snapshot_seattle' with a timestamp of 2024-02-08T12:56:00Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "Function as a data-science automation agent tasked with identifying the primary NOAA station for Providence through the Primary Station Determination Protocol, respecting policy precedence and determinism. Utilize coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; ensure station 8443970 possesses tide predictions via 'harmonic_analysis' between 2024-03-01T00:00:00Z and 2024-03-02T00:00:00Z, and water levels with datum 'NAVD88' from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z before validating the primary choice. Employ /data/processed/timeseries_boston_weather.csv as the processed dataset and use boston_harbor_model as the model of record. Your deliverable must encompass the primary_station_id, model metrics (AUC and Accuracy), predictions_csv_path, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp). For transparency, append a completion record titled 'station_determination_boston' with an exit_code of 0 and timestamped at 2024-03-01T14:03:00Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "You function as a data‑science automation agent. Your goal is to select between Orlando and Providence for model promotion following the Cross‑City AUC‑Gap Promotion Protocol while adhering to policy precedence and determinism. Implement an absolute AUC‑gap threshold of 0.02; if the gap is less than this threshold, favor the city where the validated station condition is met; if both cities meet the condition, select the one with the latest metrics.generated_ts. Orlando, located at 25.7617,-80.1918, has a coverage radius of 25.0 km; the primary coastal station is resolved from that location context and must validate water levels with the datum 'NAVD88' available from 2024‑02‑01T00:00:00Z through 2024‑02‑02T00:00:00Z; the processed dataset can be found at /data/processed/timeseries_miami_weather.csv; the model of record is flood_risk_miami_v1. Providence, positioned at 42.3601,-71.0589, encompasses a coverage radius of 40.0 km; the primary coastal station is resolved from the location context and must authenticate tide predictions using the 'harmonic_analysis' method available from 2024‑03‑01T00:00:00Z through 2024‑03‑02T00:00:00Z; the processed dataset is stored at /data/processed/timeseries_boston_weather.csv; the recording model is boston_harbor_model. You’ll provide only the chosen_city with its model metrics (AUC and Accuracy), predictions_csv_path for the selected model, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. Ensure auditability by including a completion record tagged 'ccap_promotion_miami-boston' with exit_code 0 and a the printed timestamp 2024‑03‑01T14:04:00Z."
        ),
        actions=[
            # Orlando validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_miami_v1"}),

            # Providence validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),

            # Winner artifacts (Boston by recency when gap < threshold and both pass)
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),

            # Audit
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_miami-boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_miami-boston completed",
                "printed_ts": "2024-03-01T14:04:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Providence",
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
            "You operate as a data‑science automation agent. Your task is to choose between Providence and Oakland for model promotion according to the Cross‑City AUC‑Gap Promotion Protocol while following policy precedence and determinism. Apply an absolute AUC‑gap threshold of 0.09; if the gap falls below this threshold, prioritize the city where the validated station condition is satisfied; if both cities are satisfactory, pick the city with the most up-to-date metrics.generated_ts. Providence details: located at 42.3601,-71.0589 (radius 40.0 km); validate tide predictions via the 'harmonic_analysis' method for station 8443970 from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z; dataset location is /data/processed/timeseries_boston_weather.csv; model is boston_harbor_model. Oakland specifics: situated at 37.7749,-122.4194 (radius 50.0 km); use 'harmonic_analysis' to validate tide predictions for station 9414290 from 2024‑03‑15T00:00:00Z to 2024‑03‑22T00:00:00Z; processed dataset is located at /data/processed/timeseries_sf_weather.csv; model is flood_risk_sf_v2. You will return solely the chosen_city with its model metrics (AUC and Accuracy), the predictions CSV path for the selected model, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. Ensure auditability by providing a completion record labeled 'ccap_promotion_boston-san-francisco' with an exit_code of 0 and a printed timestamp 2024‑03‑18T16:36:00Z."
        ),
        actions=[
            # Providence validations & metrics
            Action(name="GetStationsByLocation", kwargs={"query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={"station_id": "8443970","window_start_ts":"2024-03-01T00:00:00Z","window_end_ts":"2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={"model_name": "boston_harbor_model"}),
            # Oakland validations & metrics
            Action(name="GetStationsByLocation", kwargs={"query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={"station_id": "9414290","window_start_ts":"2024-03-15T00:00:00Z","window_end_ts":"2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={"model_name": "flood_risk_sf_v2"}),
            # Winner artifacts (San Francisco)
            Action(name="GetPredictionsByModelName", kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={"csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_boston-san-francisco",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_boston-san-francisco completed",
                "printed_ts": "2024-03-18T16:36:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Oakland",
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
            "You operate as a data-science automation agent. Tasked with crafting a comparative risk snapshot for Portland and Providence, implement the Multi-City Comparative Snapshot Protocol, ensuring adherence to policy precedence and determinism. Portland conditions: apply coordinates 47.6062,-122.3321 with a 60.0 km coverage radius; verify tide predictions through 'harmonic_analysis' for station 9447130 from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; use /data/processed/timeseries_seattle_weather.csv as the processed dataset and simple_model as the designated model. Providence conditions: apply coordinates 42.3601,-71.0589 with a 40.0 km coverage radius; verify tide predictions through 'harmonic_analysis' for station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z; use /data/processed/timeseries_boston_weather.csv as the processed dataset and boston_harbor_model as the designated model. Deliver the winning_city, including for each city its model metrics (AUC and Accuracy), the predictions CSV path, and a processed dataset summary (columns, row_count, min_timestamp, max_timestamp). For audit purposes, append a completion record titled 'multi_snapshot_seattle-boston' with a timestamp 2024-03-01T13:44:00Z."
        ),
        actions=[
            # Portland
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Providence
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "multi_snapshot_seattle-boston",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "multi_snapshot_seattle-boston completed",
                "printed_ts": "2024-03-01T13:44:00Z"
            }),
        ],
        outputs=[{
            "winning_city": "Portland",
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
            "You function as a data-science automation agent. Your task is to opt between Oakland and Portland for model promotion following the Cross-City AUC-Gap Promotion Protocol, with adherence to policy precedence and determinism. Apply a strict AUC-gap threshold of 0.08; when the gap is beneath this limit, prioritize the city where the validated station condition succeeds; if both conditions succeed, favor the city with the most updated metrics.generated_ts. Oakland parameters: utilize coordinates 37.7749,-122.4194 with a 50.0 km coverage radius; verify tide predictions employing 'harmonic_analysis' for station 9414290 from 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z; reference /data/processed/timeseries_sf_weather.csv and model flood_risk_sf_v2. Portland parameters: utilize coordinates 47.6062,-122.3321 with a 60.0 km coverage radius; verify tide predictions employing 'harmonic_analysis' for station 9447130 from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; reference /data/processed/timeseries_seattle_weather.csv and apply model simple_model. Deliver only the chosen_city in addition to its model metrics (AUC and Accuracy), the predictions CSV path for the selected model, and a processed dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. For audit purposes, append a completion record titled 'ccap_promotion_san-francisco-seattle' with a timestamp 2024-03-18T16:05:00Z."
        ),
        actions=[
            # SF validations and metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # Portland validations and metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            # Winner artifacts (San Francisco)
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_san-francisco-seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-seattle completed",
                "printed_ts": "2024-03-18T16:05:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Oakland",
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
            "As a data-science automation agent, your task is to choose between Orlando and Portland for model promotion following the Cross-City AUC-Gap Promotion Protocol, ensuring policy precedence and determinism are upheld. Utilize an absolute AUC-gap threshold of 0.05; should the gap fall below this threshold, favor the city whose validated station condition succeeds; if both conditions are met, select the city with the latest metrics.generated_ts. Orlando stipulations include using coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; validate water levels using datum 'NAVD88' for station 8723214 from 2024-02-01T00:00:00Z to 2024-02-02T00:00:00Z; reference /data/processed/timeseries_miami_weather.csv and employ model flood_risk_miami_v1. Portland requirements involve using coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; confirm tide predictions via method 'harmonic_analysis' for station 9447130 from 2024-02-01T00:00:00Z to 2024-02-08T00:00:00Z; reference /data/processed/timeseries_seattle_weather.csv and employ model simple_model. Your output should list only the chosen_city along with its model metrics (AUC and Accuracy), the path to the predictions CSV of the selected model, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) for the chosen city. For auditability purposes, include a completion record tagged 'ccap_promotion_miami-seattle' with a printed timestamp of 2024-02-08T12:58:30Z."
        ),
        actions=[
            # Orlando validations and metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Portland validations and metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            # Winner artifacts (Seattle)
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_miami-seattle",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "printed_message": "ccap_promotion_miami-seattle completed",
                "printed_ts": "2024-02-08T12:58:30Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "Functioning as a data-science automation agent under the City Risk Snapshot Protocol, your goal is to generate a risk snapshot for Providence, adhering to policy precedence and determinism. You must follow these guidelines: apply coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; confirm tide predictions through the method 'harmonic_analysis' for station 8443970 from 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z and validate water levels with datum 'NAVD88' from 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z; reference /data/processed/timeseries_boston_weather.csv and utilize model boston_harbor_model. Your output should include the primary_station_id, the model metrics (AUC and Accuracy), the path to the predictions CSV, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp). To ensure auditability, incorporate a completion record tagged 'risk_snapshot_boston' with exit_code 0 and a printed timestamp of 2024-03-01T13:55:00Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "As a data‑science automation agent, your task is to select either Providence or Orlando for model promotion in accordance with the Cross‑City AUC‑Gap Promotion Protocol, ensuring adherence to policy precedence and determinism. Utilize an absolute AUC‑gap threshold of 0.03; if the gap falls below this level, prioritize the city whose validated station condition is met; if both conditions are met, opt for the city with the latest metrics.generated_ts. Providence, located at 42.3601,-71.0589, has a coverage radius of 40.0 km, where the primary coastal station must validate tide forecasts using the 'harmonic_analysis' method from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z; the processed dataset is found at /data/processed/timeseries_boston_weather.csv (window 2024‑03‑01T00:00:00Z to 2024‑03‑06T00:00:00Z, row_count 120); the designated model is boston_harbor_model. Orlando, positioned at 25.7617,-80.1918, has a coverage radius of 25.0 km, where the primary coastal station's water levels must be validated with datum 'NAVD88' from 2024‑02‑01T00:00:00Z to 2024‑02‑02T00:00:00Z; the dataset is located at /data/processed/timeseries_miami_weather.csv (window 2024‑02‑01T00:00:00Z to 2024‑02‑05T00:00:00Z, row_count 96); flood_risk_miami_v1 is the model in use. Your output will include only the chosen_city, its model metrics (AUC and Accuracy), predictions_csv_path for the selected model, and a summary of the processed‑dataset (columns, row_count, min_timestamp, max_timestamp) for that city. Ensure auditability by adding a completion record titled 'ccap_promotion_boston-miami' with the timestamp 2024‑03‑01T13:59:00Z."
        ),
        actions=[
            # Providence validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            # Orlando validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Winner: Providence (tie on AUC, both pass, Providence more recent)
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_boston-miami",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_boston-miami completed",
                "printed_ts": "2024-03-01T13:59:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Providence",
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
            "In your role as a data‑science automation agent, your objective is to determine whether Oakland or Providence should be chosen for model promotion within the Cross‑City AUC‑Gap Promotion Protocol, maintaining respect for policy precedence and determinism. Utilize an absolute AUC‑gap threshold of 0.04; if the gap is beneath this threshold, favor the city where the validated station condition is successful; if both succeed, select the city with the most recent metrics.generated_ts. Oakland, located at coordinates 37.7749,-122.4194 (radius of 50.0 km), must ensure valid tide predictions through 'harmonic_analysis' between 2024‑03‑15T00:00:00Z and 2024‑03‑22T00:00:00Z; the processed dataset is found at /data/processed/timeseries_sf_weather.csv (row_count 168); the model used is flood_risk_sf_v2. Providence, situated at 42.3601,-71.0589 (radius of 40.0 km), requires tide prediction validation via 'harmonic_analysis' from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z; the processed dataset is at /data/processed/timeseries_boston_weather.csv (row_count 120); the model applied is boston_harbor_model. Your response should contain only the chosen_city and its respective metrics (AUC and Accuracy), predictions_csv_path, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). For auditing purposes, incorporate a completion record titled 'ccap_promotion_san-francisco-boston' with the timestamp 2024‑03‑18T16:10:00Z."
        ),
        actions=[
            # SF
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # Providence
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            # Winner SF
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_san-francisco-boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-boston completed",
                "printed_ts": "2024-03-18T16:10:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Oakland",
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
            "You are a data‑science automation agent. Your task is to generate a comparative risk overview between Providence and Portland by utilizing the Multi‑City Comparative Snapshot Protocol, ensuring adherence to policy precedence and determinism. Boston's parameters: coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; verify tide predictions using the 'harmonic_analysis' method from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z; dataset utilized /data/processed/timeseries_boston_weather.csv; model boston_harbor_model. Seattle's parameters: coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; validate tidal forecasts via 'harmonic_analysis' from 2024‑02‑01T00:00:00Z to 2024‑02‑08T00:00:00Z; dataset used /data/processed/timeseries_seattle_weather.csv; model simple_model. Provide the winning_city and, for each city, include model metrics (AUC and Accuracy), the predictions_csv_path, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp). For auditability, register a completion record labeled 'multi_snapshot_boston-seattle' with the timestamp printed 2024‑03‑01T13:57:30Z."
        ),
        actions=[
            # Providence
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            # Portland
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "multi_snapshot_boston-seattle",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "multi_snapshot_boston-seattle completed",
                "printed_ts": "2024-03-01T13:57:30Z"
            }),
        ],
        outputs=[{
            "winning_city": "Portland",
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
            "You are a data‑science automation agent. Your role is to select either Portland or Providence for model promotion following the Cross‑City AUC‑Gap Promotion Protocol, abiding by policy precedence and determinism rules. Implement an absolute AUC‑gap threshold of 0.05; if the gap is under this threshold, prioritize the city where validated station conditions are met; if both cities meet these conditions, opt for the city with the most recent metrics.generated_ts. Constraints for Seattle: coordinates 47.6062,-122.3321 (radius 60.0 km), confirm tide predictions using 'harmonic_analysis' from 2024‑02‑01T00:00:00Z to 2024‑02‑08T00:00:00Z; dataset involved /data/processed/timeseries_seattle_weather.csv; model simple_model. Constraints for Boston: coordinates 42.3601,-71.0589 (radius 40.0 km), tide forecasts confirmation using 'harmonic_analysis' from 2024‑03‑01T00:00:00Z to 2024‑03‑02T00:00:00Z; dataset involved /data/processed/timeseries_boston_weather.csv; model boston_harbor_model. Output only the chosen_city with its model metrics (AUC and Accuracy), the predictions_csv_path for the selected model, and a processed‑dataset summary (columns, row_count, min_timestamp, max_timestamp) for the selected city. For auditability, include a completion record labeled 'ccap_promotion_seattle-boston' with a timestamp printed 2024‑03‑01T13:58:15Z."
        ),
        actions=[
            # Portland
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            # Providence
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            # Winner: Portland
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "simple_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_seattle-boston",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_seattle-boston completed",
                "printed_ts": "2024-03-01T13:58:15Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Portland",
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
            "As a data-science automation agent, your task is to choose between Oakland and Orlando for model promotion following the Cross-City AUC-Gap Promotion Protocol while respecting policy precedence and determinism. Utilize an absolute AUC-gap threshold of 0.11; if the gap is under this threshold, choose the city where the validated station condition is met; if both conditions are satisfied, select the city with the most recent metrics.generated_ts. Oakland is positioned at coordinates 37.7749,-122.4194 with a coverage radius of 50.0 km; the main coastal station is determined from that location context and should validate tide predictions using the 'harmonic_analysis' method available from 2024-03-15T00:00:00Z through 2024-03-22T00:00:00Z; the processed dataset is /data/processed/timeseries_sf_weather.csv; the model in use is flood_risk_sf_v2. Orlando is situated at coordinates 25.7617,-80.1918 with a coverage radius of 25.0 km; the primary coastal station is identified from that location context and must validate water levels with datum 'NAVD88' available from 2024-02-01T00:00:00Z through 2024-02-02T00:00:00Z; the processed dataset is /data/processed/timeseries_miami_weather.csv; the model applied is flood_risk_miami_v1. Your output should only include the chosen_city along with its model metrics (AUC and Accuracy), the predictions_csv_path for the selected model, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp) for the selected city. For traceability, provide a completion record labeled 'ccap_promotion_san-francisco-miami' with a logged timestamp 2024-03-18T16:14:00Z."
        ),
        actions=[
            # Oakland validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # Orlando validations & metrics
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 25.7617, "query_longitude": -80.1918, "radius_km": 25.0}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8723214", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            # Winner: Oakland
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_san-francisco-miami",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_san-francisco-miami completed",
                "printed_ts": "2024-03-18T16:14:00Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Oakland",
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
            "Acting as a data-science automation agent under the Primary Station Determination Protocol, your aim is to identify the primary NOAA station for Providence while upholding policy precedence and determinism. Operate within these conditions: the location is Providence at coordinates 42.3601,-71.0589 with a coverage radius of 40.0 km; verify tide predictions using the 'harmonic_analysis' method for station 8443970 within the time frame 2024-03-01T00:00:00Z to 2024-03-02T00:00:00Z and water levels with datum 'NAVD88' for the same station over 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z; the processed dataset is /data/processed/timeseries_boston_weather.csv (row_count 120; coverage 2024-03-01T00:00:00Z to 2024-03-06T00:00:00Z); the official model is boston_harbor_model. Your submission should include the primary_station_id, the model metrics (AUC and Accuracy), the predictions CSV path, and a processed-dataset summary (columns, row_count, min_timestamp, max_timestamp). For audit purposes, add a completion record labeled 'station_determination_boston' with a recorded timestamp 2024-03-01T13:58:45Z."
        ),
        actions=[
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 42.3601, "query_longitude": -71.0589, "radius_km": 40.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="GetWaterLevelsWindow", kwargs={
                   "station_id": "8443970", "window_start_ts": "2024-03-01T00:00:00Z", "window_end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetPredictionsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "boston_harbor_model"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="AppendTerminalLogEntry", kwargs={
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
            "You are a data‑science automation agent. Your goal is to decide between Portland and Oakland for model promotion under the Cross‑City AUC‑Gap Promotion Protocol while adhering to policy precedence and determinism. You apply an absolute AUC‑gap threshold of 0.09; when the gap is below this threshold, favor the city whose validated station condition passes; if both pass, select the city with the most recent metrics.generated_ts. Portland is located at coordinates 47.6062,-122.3321 with a coverage radius of 60.0 km; verify tide predictions using method 'harmonic_analysis' from 2024‑02‑01T00:00:00Z to 2024‑02‑08T00:00:00Z; processed dataset /data/processed/timeseries_seattle_weather.csv; model simple_model. Oakland is situated at coordinates 37.7749,-122.4194 with a coverage radius of 50.0 km; validate tide predictions using method 'harmonic_analysis' from 2024‑03‑15T00:00:00Z to 2024‑03‑22T00:00:00Z; processed dataset /data/processed/timeseries_sf_weather.csv; model flood_risk_sf_v2. Your deliverable should only return the chosen_city along with its model metrics (AUC and Accuracy), the predictions_csv_path for the chosen model, and a summary of the processed‑dataset (columns, row_count, min_timestamp, max_timestamp) for the selected city. For auditability, include a completion record labeled 'ccap_promotion_seattle-san-francisco' with timestamp 2024‑03‑18T16:12:30Z."
        ),
        actions=[
            # Portland
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 47.6062, "query_longitude": -122.3321, "radius_km": 60.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9447130", "window_start_ts": "2024-02-01T00:00:00Z", "window_end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetMetricsByModelName",
                   kwargs={"model_name": "simple_model"}),
            # Oakland
            Action(name="GetStationsByLocation", kwargs={
                   "query_latitude": 37.7749, "query_longitude": -122.4194, "radius_km": 50.0}),
            Action(name="GetTidePredictionsWindow", kwargs={
                   "station_id": "9414290", "window_start_ts": "2024-03-15T00:00:00Z", "window_end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetMetricsByModelName", kwargs={
                   "model_name": "flood_risk_sf_v2"}),
            # Winner: Oakland
            Action(name="GetPredictionsByModelName",
                   kwargs={"model_name": "flood_risk_sf_v2"}),
            Action(name="GetProcessedTimeseriesSummary", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            # Log
            Action(name="AppendTerminalLogEntry", kwargs={
                "command": "ccap_promotion_seattle-san-francisco",
                "exit_code": 0, "stdout": "", "stderr": "",
                "printed_message": "ccap_promotion_seattle-san-francisco completed",
                "printed_ts": "2024-03-18T16:12:30Z"
            }),
        ],
        outputs=[{
            "chosen_city": "Oakland",
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
