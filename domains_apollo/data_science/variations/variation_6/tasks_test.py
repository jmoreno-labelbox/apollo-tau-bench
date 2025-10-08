from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="task_001",
        instruction=(
            "You are responsible for Oakland (NOAA station 9414290). Handle the Merge Window Protocol (MWP) with the parameters: city='Oakland', station_id='9414290', analysis window=2024-03-15T00:00:00Z..2024-03-22T00:00:00Z, water-level lookback=2024-02-14T00:00:00Z..2024-03-15T00:00:00Z. Upon MWP completion, deliver the stored AUC and Accuracy for model_name='flood_risk_sf_v1'."
        ),
        actions=[
            Action(name="GetWeatherForecast", kwargs={
                "city": "Oakland",
                "start_ts": "2024-03-15T00:00:00Z",
                "end_ts": "2024-03-22T00:00:00Z"
            }),
            Action(name="GetTidePredictions", kwargs={
                "station_id": "9414290",
                "start_ts": "2024-03-15T00:00:00Z",
                "end_ts": "2024-03-22T00:00:00Z"
            }),
            Action(name="GetWaterLevels", kwargs={
                "station_id": "9414290",
                "start_ts": "2024-02-14T00:00:00Z",
                "end_ts": "2024-03-15T00:00:00Z"
            }),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_sf_20240315_20240322_merge_v1",
                "input_paths": [
                    "/data/raw/weather_sf_20240315.json",
                    "/data/raw/tide_pred_9414290.json",
                    "/data/raw/water_levels_9414290.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240315_20240322.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-15..2024-03-22.",
                    "Attached observed water levels lookback 2024-02-14..2024-03-15.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            }),
            Action(name="GetModelMetrics", kwargs={
                   "model_name": "flood_risk_sf_v1"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_002",
        instruction=(
            "You are responsible for Oakland data preparation. Coordinate the Split Protocol (SP) for city='Oakland' using method='time_based', with the test_fraction obtained from '/config/model_config.json' and split_ts='2024-03-17T10:45:00Z'. Provide the resulting train and test counts along with the canonical split_summary_json_path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "sf"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"
            }),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"
            }),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                "city_slug": "sf",
                "method": "time_based",
                "split_ts": "2024-03-17T10:45:00Z"
            }),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json",
                "split_ts": "2024-03-17T10:45:00Z"
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_003",
        instruction=(
            "Manage the preparation of Orlando data. Handle the Split Protocol (SP) for city='Orlando' with method='time_based', using test_fraction from '/config/model_config.json', and split_ts='2024-02-03T10:45:00Z'. Provide the counts for train and test and the canonical split path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "miami"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-03T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240203.json",
                "split_ts": "2024-02-03T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_004",
        instruction=(
            "Coordinate the preparation of Providence data. Implement the Split Protocol (SP) for city='Providence' with method='time_based', using test_fraction from '/config/model_config.json' and split_ts='2024-03-04T10:45:00Z'. Supply the train and test counts and the canonical split path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "boston"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-04T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 96,
                "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240304.json",
                "split_ts": "2024-03-04T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_005",
        instruction=(
            "Take charge of Portland ingestion. Handle the MWP for city='Portland', station_id='9447130', analysis window=2024-02-01T00:00:00Z..2024-02-08T00:00:00Z utilizing a water-level lookback 2024-01-15T00:00:00Z..2024-02-01T00:00:00Z. Provide the MWP run_id and merged artifact path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Portland", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "9447130", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "9447130", "start_ts": "2024-01-15T00:00:00Z", "end_ts": "2024-02-01T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "seattle", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_seattle_20240201_20240208_merge_v1",
                "input_paths": ["/data/raw/weather_seattle_20240201.json", "/data/raw/tide_pred_9447130.json", "/data/raw/water_levels_9447130.json"],
                "output_paths": ["/processed_data/merged_timeseries_seattle_20240201_20240208.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-01..2024-02-08.",
                    "Attached observed water levels lookback 2024-01-15..2024-02-01.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_700",
        instruction=(
            "Ensure a reproducible time-based split for Oakland to consistently replay the late-March evaluation. Apply the policy test fraction from '/config/model_config_v2.json' and set the split anchor at 2024-03-14T16:45:00Z. Save the canonical split summary for the Oakland processed series and return the path including the train/test totals."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "sf"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config_v2.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.25}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-14T16:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 126,
                "test_index_count": 42,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240314.json",
                "split_ts": "2024-03-14T16:45:00Z"
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_006",
        instruction=(
            "You are responsible for Oakland data preparation. Handle SP for city='Oakland' with method='time_based', using test_fraction from '/config/model_config.json' and split_ts='2024-03-20T10:45:00Z'. Report the train and test counts and the canonical split path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "sf"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-20T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240320.json",
                "split_ts": "2024-03-20T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_007",
        instruction=(
            "You are responsible for Oakland ingestion. Handle the Merge Window Protocol (MWP) for city='Oakland', station_id='9414290', analysis window=2024-03-15T00:00:00Z..2024-03-22T00:00:00Z with a water-level lookback ending at the window start (2024-02-14T00:00:00Z..2024-03-15T00:00:00Z). Report the MWP run_id and merged artifact path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Oakland", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "9414290", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "9414290", "start_ts": "2024-02-14T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "sf", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_sf_20240315_20240322_merge_v1",
                "input_paths": ["/data/raw/weather_sf_20240315.json", "/data/raw/tide_pred_9414290.json", "/data/raw/water_levels_9414290.json"],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240315_20240322.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-15..2024-03-22.",
                    "Attached observed water levels lookback 2024-02-14..2024-03-15.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_008",
        instruction=(
            "You are in charge of preparing Portland data. Handle the Split Protocol (SP) for city='Portland' using method='time_based', utilizing test_fraction from '/config/model_config.json' and split_ts='2024-02-04T10:45:00Z'. Provide the counts for the train and test sets and the canonical split path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-04T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 192,
                "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240204.json",
                "split_ts": "2024-02-04T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_009",
        instruction=(
            "You are in charge of Providence data ingestion. Handle the Merge Window Protocol (MWP) for city='Providence', station_id='8443970', analysis window=2024-03-01T00:00:00Z..2024-03-06T00:00:00Z with a water-level lookback concluding at the window start (2024-02-15T00:00:00Z..2024-03-01T00:00:00Z). Provide the MWP run_id and the path for the merged artifact."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Providence", "start_ts": "2024-03-01T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "8443970", "start_ts": "2024-03-01T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "8443970", "start_ts": "2024-02-15T00:00:00Z", "end_ts": "2024-03-01T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "boston", "start_ts": "2024-03-01T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_boston_20240301_20240306_merge_v1",
                "input_paths": ["/data/raw/weather_boston_20240301.json", "/data/raw/tide_pred_8443970.json", "/data/raw/water_levels_8443970.json"],
                "output_paths": ["/processed_data/merged_timeseries_boston_20240301_20240306.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-01..2024-03-06.",
                    "Attached observed water levels lookback 2024-02-15..2024-03-01.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_010",
        instruction=(
            "You are responsible for Orlando data preparation. Handle the Split Protocol (SP) for city='Orlando' with method='time_based', utilizing test_fraction from '/config/model_config.json' and split_ts='2024-02-04T12:00:00Z'. Provide a report of the train and test counts and the canonical split path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-04T12:00:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240204.json",
                "split_ts": "2024-02-04T12:00:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_011",
        instruction=(
            "It is imperative that you handle the Split Protocol (SP) for city='Oakland' with method='time_based', using test_fraction from '/config/model_config.json' and split_ts='2024-03-21T10:45:00Z'. Ensure you report the train and test counts and the canonical split path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-21T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240321.json",
                "split_ts": "2024-03-21T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_012",
        instruction=(
            "Handle the Split Protocol (SP) for city='Orlando' utilizing method='time_based', referencing the test_fraction from '/config/model_config.json' and applying split_ts='2024-02-01T10:45:00Z'. Report the results for train and test counts as well as the canonical split path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-01T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240201.json",
                "split_ts": "2024-02-01T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_013",
        instruction=(
            "Conduct the Merge Window Protocol (MWP) for Oakland, using station_id='9414290', within the analysis window=2024-03-15T00:00:00Z..2024-03-22T00:00:00Z and taking into account a water-level lookback of 2024-02-14T00:00:00Z..2024-03-15T00:00:00Z. Coordinate reporting of the MWP run_id and the location of the merged artifact path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Oakland", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "9414290", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "9414290", "start_ts": "2024-02-14T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "sf", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_sf_20240315_20240322_merge_v1",
                "input_paths": ["/data/raw/weather_sf_20240315.json", "/data/raw/tide_pred_9414290.json", "/data/raw/water_levels_9414290.json"],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240315_20240322.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-15..2024-03-22.",
                    "Attached observed water levels lookback 2024-02-14..2024-03-15.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_014",
        instruction=(
            "Handle the preparation of a hydrometeorology ingest audit for Portland. Construct the merged analysis artifact utilizing the Merge Window Protocol specifying city='Portland', station_id='9447130', with the analysis window extending from '2024-02-01T00:00:00Z' to '2024-02-08T00:00:00Z', and include a water-level lookback spanning from '2024-01-15T00:00:00Z' to '2024-02-01T00:00:00Z'. The ETL run identifier along with the merged CSV path labeled by the city slug and dates will be your deliverable."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Portland", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "9447130", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "9447130", "start_ts": "2024-01-15T00:00:00Z", "end_ts": "2024-02-01T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "seattle", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_seattle_20240201_20240208_merge_v1",
                "input_paths": ["/data/raw/weather_seattle_20240201.json", "/data/raw/tide_pred_9447130.json", "/data/raw/water_levels_9447130.json"],
                "output_paths": ["/processed_data/merged_timeseries_seattle_20240201_20240208.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-01..2024-02-08.",
                    "Attached observed water levels lookback 2024-01-15..2024-02-01.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_015",
        instruction=(
            "Coordinate the creation of an auditable time-based split for Orlando to support backtesting. Engage with city='Orlando' and method='time_based' using split_ts='2024-02-01T10:45:00Z'; extract the test fraction from '/config/model_config.json'. As there are 96 hourly rows of processed series for Orlando during this period, ensure the canonical split summary indicates train=76 and test=20 under the path '/data/splits/miami_time_based_split_20240201.json'. The split path and the two counts are your deliverables."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-01T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240201.json",
                "split_ts": "2024-02-01T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_016",
        instruction=(
            "Handle a deterministic time-based split for Oakland necessary for a compliance backtest. Implement city='Oakland' with method='time_based' and split_ts='2024-03-20T10:45:00Z'. The processed SF series for this timeframe contains 168 hourly rows; using the test fraction specified in '/config/model_config.json', ensure the canonical split notes train=134 and test=34 in '/data/splits/sf_time_based_split_20240320.json'. Your task is to provide the split path and the respective counts."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-20T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240320.json",
                "split_ts": "2024-03-20T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_017",
        instruction=(
            "Coordinate the documentation of the Providence ingest state for a stakeholder transition. Construct the merged analysis artifact utilizing the Merge Window Protocol for city='Providence' with station_id='8443970', within the analysis window from '2024-03-01T00:00:00Z' to '2024-03-06T00:00:00Z', and incorporate a water-level lookback from '2024-02-15T00:00:00Z' up to '2024-03-01T00:00:00Z'. Your requirement is to deliver the ETL run identifier and the path of the merged CSV named by the city slug and dates."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Providence", "start_ts": "2024-03-01T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "8443970", "start_ts": "2024-03-01T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "8443970", "start_ts": "2024-02-15T00:00:00Z", "end_ts": "2024-03-01T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "boston", "start_ts": "2024-03-01T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_boston_20240301_20240306_merge_v1",
                "input_paths": ["/data/raw/weather_boston_20240301.json", "/data/raw/tide_pred_8443970.json", "/data/raw/water_levels_8443970.json"],
                "output_paths": ["/processed_data/merged_timeseries_boston_20240301_20240306.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-01..2024-03-06.",
                    "Attached observed water levels lookback 2024-02-15..2024-03-01.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_410",
        instruction=(
            "Manage a reproducible time-based division that secures Seattle’s mid-March assessment for subsequent training. Utilize the policy test fraction located in '/config/model_config_v2.json' and fix the division point at 2024-03-14T16:45:00Z. Preserve the canonical split summary for the Portland processed series and provide the path along with the totals for train/test."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "seattle"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config_v2.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.25}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-03-14T16:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 180,
                "test_index_count": 60,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240314.json",
                "split_ts": "2024-03-14T16:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_018",
        instruction=(
            "Develop a Seattle-exclusive split catalog entry. Construct a time-based division for city='Portland' with split_ts='2024-02-03T12:00:00Z'. The processed Portland series comprises 240 rows, with the test fraction drawn from '/config/model_config.json'. Therefore, the split must document train=192 and test=48 at '/data/splits/seattle_time_based_split_20240203.json'. The finished task is the split path and the two counts."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-03T12:00:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 192,
                "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240203.json",
                "split_ts": "2024-02-03T12:00:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_019",
        instruction=(
            "Handle the production of a Boston-only split record meant for reproducible evaluation. Use city='Providence' alongside method='time_based' and split_ts='2024-03-01T10:45:00Z'. The processed Providence series consists of 120 hourly rows; referring to the test fraction found in '/config/model_config.json', ensure the split logs train=96 and test=24 at '/data/splits/boston_time_based_split_20240301.json'. Provide the deliverable as the split path and the counts."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-01T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 96,
                "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240301.json",
                "split_ts": "2024-03-01T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_020",
        instruction=(
            "Coordinate the preparation of a Oakland ingestion-only proof intended for a data lineage review. Construct the merged analysis artifact for city='Oakland' with station_id='9414290', covering the analysis window from '2024-03-15T00:00:00Z' to '2024-03-22T00:00:00Z', and accommodating a water-level lookback from '2024-02-14T00:00:00Z' to '2024-03-15T00:00:00Z'. The ETL run identifier and the merged CSV path comprise your deliverable."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Oakland", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "9414290", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "9414290", "start_ts": "2024-02-14T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "sf", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_sf_20240315_20240322_merge_v1",
                "input_paths": ["/data/raw/weather_sf_20240315.json", "/data/raw/tide_pred_9414290.json", "/data/raw/water_levels_9414290.json"],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240315_20240322.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-15..2024-03-22.",
                    "Attached observed water levels lookback 2024-02-14..2024-03-15.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_021",
        instruction=(
            "Validate the Orlando features to ensure the portability of a baseline model. Apply the Feature Validation Protocol for the city='Orlando' and model_name='simple_model' against '/processed_data/features.csv' with the validation timestamp '2024-03-17T10:15:00Z'. Document the coverage counts and the path to the validation JSON."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetModelFeatures", kwargs={
                "model_name": "simple_model"}),
            Action(name="BuildFeaturesCsvPath",
                   kwargs={"city_slug": "miami"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/processed_data/features.csv"}),
            Action(name="ComputeFeatureCoverage", kwargs={
                "required_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "available_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"]
            }),
            Action(name="BuildFeatureValidationPath", kwargs={
                   "city_slug": "miami", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="BuildFeatureValidationRunId", kwargs={
                   "city_slug": "miami", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "fv_miami_simple_model_20240317_v1",
                "input_paths": ["/processed_data/features.csv"],
                "output_paths": ["/processed_data/feature_validation_miami_simple_model_20240317.json"],
                "started_ts": "2024-03-17T10:20:00Z",
                "finished_ts_nullable": "2024-03-17T10:25:00Z",
                "messages": [
                    "Feature validation for simple_model: 3/3 required features present.",
                    "Missing features: none",
                    "Validated file: /processed_data/feature_validation_miami_simple_model_20240317.json"
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_403",
        instruction=(
            "Generate a deterministic split snapshot for Providence in order to backtest early-March runs. Utilize the test fraction specified in '/processed_data/boston_model_config.json' and fix the split at 2024-03-01T13:18:00Z. Store the canonical split summary for the Providence processed series and provide the path along with the train/test sizes."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "boston"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/processed_data/boston_model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 120, "test_fraction": 0.25}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-01T13:18:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 90,
                "test_index_count": 30,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240301.json",
                "split_ts": "2024-03-01T13:18:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_022",
        instruction=(
            "Conduct a validation of baseline features for Providence to perform a portability assessment. Apply the Feature Validation Protocol for city='Providence' and model_name='simple_model' with reference to '/processed_data/features.csv' and a validation timestamp of '2024-03-17T10:15:00Z'. Document the coverage counts and provide the path to the validation JSON."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="GetModelFeatures", kwargs={
                "model_name": "simple_model"}),
            Action(name="BuildFeaturesCsvPath",
                   kwargs={"city_slug": "boston"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/processed_data/features.csv"}),
            Action(name="ComputeFeatureCoverage", kwargs={
                "required_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "available_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"]
            }),
            Action(name="BuildFeatureValidationPath", kwargs={
                   "city_slug": "boston", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="BuildFeatureValidationRunId", kwargs={
                   "city_slug": "boston", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "fv_boston_simple_model_20240317_v1",
                "input_paths": ["/processed_data/features.csv"],
                "output_paths": ["/processed_data/feature_validation_boston_simple_model_20240317.json"],
                "started_ts": "2024-03-17T10:20:00Z",
                "finished_ts_nullable": "2024-03-17T10:25:00Z",
                "messages": [
                    "Feature validation for simple_model: 3/3 required features present.",
                    "Missing features: none",
                    "Validated file: /processed_data/feature_validation_boston_simple_model_20240317.json"
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_023",
        instruction=(
            "Organize a Oakland split-only artifact for evaluating a late window. Develop a time-based split for city='Oakland' with the timestamp '2024-03-21T10:45:00Z'. The processed SF series contains 168 rows; using the test fraction from '/config/model_config.json', ensure the split logs train=134 and test=34 in '/data/splits/sf_time_based_split_20240321.json'. Your task is to furnish the split path along with the counts."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-21T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240321.json",
                "split_ts": "2024-03-21T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_024",
        instruction=(
            "Handle the ingestion verification preparation for Oakland. Develop the merged analysis artifact using the Merge Window Protocol for city='Oakland' and station_id='9414290' from '2024-03-12T00:00:00Z' to '2024-03-16T00:00:00Z', incorporating a water-level lookback from '2024-02-26T00:00:00Z' to '2024-03-12T00:00:00Z'. Ensure the merged file is labeled as '/processed_data/merged_timeseries_sf_20240312_20240316.csv'. Keep a record of the ETL run as run_id='etl_sf_20240312_20240316_merge_v1' with started_ts='2024-03-18T09:00:00Z' and finished_ts='2024-03-18T09:18:00Z'."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Oakland", "start_ts": "2024-03-12T00:00:00Z", "end_ts": "2024-03-16T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "9414290", "start_ts": "2024-03-12T00:00:00Z", "end_ts": "2024-03-16T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "9414290", "start_ts": "2024-02-26T00:00:00Z", "end_ts": "2024-03-12T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "sf", "start_ts": "2024-03-12T00:00:00Z", "end_ts": "2024-03-16T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_sf_20240312_20240316_merge_v1",
                "input_paths": ["/data/raw/weather_sf_20240312.json", "/data/raw/tide_pred_9414290.json", "/data/raw/water_levels_9414290.json"],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240312_20240316.csv"],
                "started_ts": "2024-03-18T09:00:00Z",
                "finished_ts_nullable": "2024-03-18T09:18:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-12..2024-03-16.",
                    "Attached observed water levels lookback 2024-02-26..2024-03-12.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_025",
        instruction=(
            "Coordinate the production of a Portland ingestion artifact for a mid-week window. Construct the merged file for city='Portland' with station_id='9447130' covering '2024-02-04T00:00:00Z' to '2024-02-08T00:00:00Z', utilizing a water-level lookback from '2024-01-20T00:00:00Z' to '2024-02-04T00:00:00Z'. Assign the output file with the name '/processed_data/merged_timeseries_seattle_20240204_20240208.csv' (city_slug='seattle'), and log the run as run_id='etl_seattle_20240204_20240208_merge_v1' having started_ts='2024-03-18T09:30:00Z' and finished_ts='2024-03-18T09:50:00Z'."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Portland", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "9447130", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "9447130", "start_ts": "2024-01-20T00:00:00Z", "end_ts": "2024-02-04T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "seattle", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_seattle_20240204_20240208_merge_v1",
                "input_paths": ["/data/raw/weather_seattle_20240204.json", "/data/raw/tide_pred_9447130.json", "/data/raw/water_levels_9447130.json"],
                "output_paths": ["/processed_data/merged_timeseries_seattle_20240204_20240208.csv"],
                "started_ts": "2024-03-18T09:30:00Z",
                "finished_ts_nullable": "2024-03-18T09:50:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-04..2024-02-08.",
                    "Attached observed water levels lookback 2024-01-20..2024-02-04.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_026",
        instruction=(
            "Handle a Oakland time-based split intended for a late-window review. Utilize method='time_based' and split_ts='2024-03-19T10:45:00Z' for city='Oakland'. With row_count=168 and test_fraction=0.2 specified from '/config/model_config.json', ensure the split summary documents train=134 and test=34 at '/data/splits/sf_time_based_split_20240319.json'. Additionally, reference the metadata source '/data/processed/timeseries_sf_weather.csv'."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-19T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240319.json",
                "split_ts": "2024-03-19T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_027",
        instruction=(
            "Coordinate a Portland time-based split for a series with 240 rows. For city='Portland', use method='time_based', and split_ts='2024-02-03T12:00:00Z'. With test_fraction=0.2 and metadata found in '/data/processed/timeseries_seattle_weather.csv', generate '/data/splits/seattle_time_based_split_20240203.json' recording train=192 and test=48."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-03T12:00:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 192,
                "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240203.json",
                "split_ts": "2024-02-03T12:00:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_028",
        instruction=(
            "Handle the preparation of a Portland ingestion artifact intended for audit. Construct the merged analysis utilizing the Merge Window Protocol with parameters city='Portland', station_id='9447130', analysis window '2024-02-01T00:00:00Z'..'2024-02-08T00:00:00Z', and water-level lookback spanning '2024-01-15T00:00:00Z'..'2024-02-01T00:00:00Z'. Ensure the merged file is located at '/processed_data/merged_timeseries_seattle_20240201_20240208.csv', activating the ETL run with id 'etl_seattle_20240201_20240208_merge_v1' from started_ts='2024-03-19T09:00:00Z' to finished_ts='2024-03-19T09:18:00Z'. Provide the ETL run id alongside the merged path within your report."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Portland", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "9447130", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "9447130", "start_ts": "2024-01-15T00:00:00Z", "end_ts": "2024-02-01T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "seattle", "start_ts": "2024-02-01T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_seattle_20240201_20240208_merge_v1",
                "input_paths": [
                    "/data/raw/weather_seattle_20240201.json",
                    "/data/raw/tide_pred_9447130.json",
                    "/data/raw/water_levels_9447130.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_seattle_20240201_20240208.csv"],
                "started_ts": "2024-03-19T09:00:00Z",
                "finished_ts_nullable": "2024-03-19T09:18:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-01..2024-02-08.",
                    "Attached observed water levels lookback 2024-01-15..2024-02-01.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_029",
        instruction=(
            "Coordinate the production of a Orlando time-based split for consistent evaluation purposes. Implement using city='Orlando', method='time_based', split_ts='2024-02-01T10:45:00Z', row_count=96, and test_fraction=0.2 from the given configuration. Make sure the split summary resides at '/data/splits/miami_time_based_split_20240201.json'. Offer details on the split path as well as the counts for train/test (train=76, test=20)."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-01T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2, "train_index_count": 76, "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240201.json", "split_ts": "2024-02-01T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_030",
        instruction=(
            "Procure an auditable merged dataset for Orlando in early February. For city='Orlando' with station_id='8723214', apply the analysis window '2024-02-02T00:00:00Z'..'2024-02-06T00:00:00Z' and the water‑level lookback '2024-01-29T00:00:00Z'..'2024-02-02T00:00:00Z'. Store the artifact in '/processed_data/merged_timeseries_miami_20240202_20240206.csv' under ETL run id 'etl_miami_20240202_20240206_merge_v1' with started_ts='2024-03-20T08:00:00Z' and finished_ts='2024-03-20T08:18:00Z'. Provide the run id and the merged path in the report."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Orlando", "start_ts": "2024-02-02T00:00:00Z", "end_ts": "2024-02-06T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-02T00:00:00Z", "end_ts": "2024-02-06T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "8723214", "start_ts": "2024-01-29T00:00:00Z", "end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "miami", "start_ts": "2024-02-02T00:00:00Z", "end_ts": "2024-02-06T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_miami_20240202_20240206_merge_v1",
                "input_paths": [
                    "/data/raw/weather_miami_20240202.json",
                    "/data/raw/tide_pred_8723214.json",
                    "/data/raw/water_levels_8723214.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_miami_20240202_20240206.csv"],
                "started_ts": "2024-03-20T08:00:00Z",
                "finished_ts_nullable": "2024-03-20T08:18:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-02..2024-02-06",
                    "Attached observed water levels lookback 2024-01-29..2024-02-02",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa"
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_031",
        instruction=(
            "Organize a deterministic time‑based split for Oakland to ensure evaluation reproducibility. For city='Oakland', designate method='time_based' with split_ts='2024-03-19T10:45:00Z', row_count=168 and test_fraction=0.2. The split summary should be '/data/splits/sf_time_based_split_20240319.json' with train=134 and test=34. Provide the split path and the counts in the report."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-19T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240319.json",
                "split_ts": "2024-03-19T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_033",
        instruction=(
            "Ensure a Portland package that addresses the split accounting and affirms baseline coverage. For city='Portland', apply method='time_based' with split_ts='2024-02-06T12:00:00Z', row_count=240 and test_fraction=0.2 so that '/data/splits/seattle_time_based_split_20240206.json' records train=192 and test=48. Next, authenticate model_name='simple_model' at created_ts='2024-03-17T10:15:00Z' against the canonical features CSV '/processed_data/features.csv', saving '/processed_data/feature_validation_seattle_simple_model_20240317.json' under run_id 'fv_seattle_simple_model_20240317_v1' with started_ts='2024-03-20T11:15:00Z' and finished_ts='2024-03-20T11:17:00Z'. The necessary features are ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa']; the available features match these. Report the split path and counts, along with present, required, missing_count, and the validation path."
        ),
        actions=[
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 192,
                "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240206.json",
                "split_ts": "2024-02-06T12:00:00Z"
            }),
            Action(name="ComputeFeatureCoverage", kwargs={
                "required_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "available_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"]
            }),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "fv_seattle_simple_model_20240317_v1",
                "input_paths": ["/processed_data/features.csv"],
                "output_paths": ["/processed_data/feature_validation_seattle_simple_model_20240317.json"],
                "started_ts": "2024-03-20T11:15:00Z",
                "finished_ts_nullable": "2024-03-20T11:17:00Z",
                "messages": [
                    "Feature validation for simple_model: 3/3 required features present.",
                    "Missing features: none",
                    "Validated file: /processed_data/feature_validation_seattle_simple_model_20240317.json"
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_034",
        instruction=(
            "Arrange an auditable merged dataset for Orlando around mid-February. For city='Orlando' with station_id='8723214', utilize the analysis window '2024-02-06T00:00:00Z'..'2024-02-10T00:00:00Z' and the water-level lookback '2024-02-02T00:00:00Z'..'2024-02-06T00:00:00Z'. Save '/processed_data/merged_timeseries_miami_20240206_20240210.csv' under ETL run id 'etl_miami_20240206_20240210_merge_v1' with started_ts='2024-03-21T08:10:00Z' and finished_ts='2024-03-21T08:29:00Z'. Report the run id and the merged path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Orlando", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-02T00:00:00Z", "end_ts": "2024-02-06T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "miami", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_miami_20240206_20240210_merge_v1",
                "input_paths": [
                    "/data/raw/weather_miami_20240206.json",
                    "/data/raw/tide_pred_8723214.json",
                    "/data/raw/water_levels_8723214.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_miami_20240206_20240210.csv"],
                "started_ts": "2024-03-21T08:10:00Z",
                "finished_ts_nullable": "2024-03-21T08:29:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-06..2024-02-10.",
                    "Attached observed water levels lookback 2024-02-02..2024-02-06.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_036",
        instruction=(
            "You are curating Providence artifacts for a migration checklist. For city='Providence', arrange a time‑based split at split_ts='2024-03-05T10:45:00Z' ensuring row_count=120 and test_fraction=0.2, so that '/data/splits/boston_time_based_split_20240305.json' reflects train=96 and test=24. Next, evaluate model_name='simple_model' at created_ts='2024-03-17T10:15:00Z' using '/processed_data/features.csv', storing the results in '/processed_data/feature_validation_boston_simple_model_20240317.json' under run_id='fv_boston_simple_model_20240317_v1', with started_ts='2024-03-21T11:00:00Z' and finished_ts='2024-03-21T11:02:00Z'. Provide the split path and counts, as well as present, required, missing_count, and the validation path."
        ),
        actions=[
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-05T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 96,
                "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240305.json",
                "split_ts": "2024-03-05T10:45:00Z"
            }),
            Action(name="ComputeFeatureCoverage", kwargs={
                "required_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "available_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"]
            }),
            Action(name="BuildFeatureValidationPath", kwargs={
                   "city_slug": "boston", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "fv_boston_simple_model_20240317_v1",
                "input_paths": ["/processed_data/features.csv"],
                "output_paths": ["/processed_data/feature_validation_boston_simple_model_20240317.json"],
                "started_ts": "2024-03-21T11:00:00Z",
                "finished_ts_nullable": "2024-03-21T11:02:00Z",
                "messages": [
                    "Feature validation for simple_model: 3/3 required features present.",
                    "Missing features: none",
                    "Validated file: /processed_data/feature_validation_boston_simple_model_20240317.json"
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_038",
        instruction=(
            "You intend a Providence time‑based split to secure an early‑March evaluation. For city='Providence', determine method='time_based' using split_ts='2024-03-06T10:45:00Z', row_count=120, and test_fraction=0.2. Ensure the split summary is '/data/splits/boston_time_based_split_20240306.json' with train=96 and test=24. Provide the split path and the counts."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-06T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 96,
                "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240306.json",
                "split_ts": "2024-03-06T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_040",
        instruction=(
            "Ensure an auditable merged dataset is available for Orlando in mid-February. Given city='Orlando' and station_id='8723214', the analysis window '2024-02-08T00:00:00Z' to '2024-02-12T00:00:00Z' should be employed, alongside the water-level lookback '2024-02-04T00:00:00Z' to '2024-02-08T00:00:00Z'. Retain '/processed_data/merged_timeseries_miami_20240208_20240212.csv' as the final output using ETL run id 'etl_miami_20240208_20240212_merge_v1', starting at '2024-03-22T08:05:00Z' and concluding at '2024-03-22T08:24:00Z'. Provide the run id and the path to the merged data."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Orlando", "start_ts": "2024-02-08T00:00:00Z", "end_ts": "2024-02-12T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-08T00:00:00Z", "end_ts": "2024-02-12T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "miami", "start_ts": "2024-02-08T00:00:00Z", "end_ts": "2024-02-12T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_miami_20240208_20240212_merge_v1",
                "input_paths": [
                    "/data/raw/weather_miami_20240208.json",
                    "/data/raw/tide_pred_8723214.json",
                    "/data/raw/water_levels_8723214.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_miami_20240208_20240212.csv"],
                "started_ts": "2024-03-22T08:05:00Z",
                "finished_ts_nullable": "2024-03-22T08:24:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-08..2024-02-12.",
                    "Attached observed water levels lookback 2024-02-04..2024-02-08.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_041",
        instruction=(
            "Establish a deterministic time-based division for Providence to anchor an evaluation in early March. For city='Providence', configure method='time_based' utilizing split_ts='2024-03-03T10:45:00Z', row_count=120, and a test_fraction of 0.2. '/data/splits/boston_time_based_split_20240303.json' should contain a summary of the split with 96 for train and 24 for test. Share both the split path and the respective counts."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-03T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 96,
                "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240303.json",
                "split_ts": "2024-03-03T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_306",
        instruction=(
            "Create a reproducible time-based split that secures Seattle's mid-March evaluation for downstream training. Employ the policy test fraction from '/config/model_config_v2.json' with the split anchored at 2024-03-14T16:45:00Z. Save the canonical split summary for the Portland processed series and return the path along with the train/test totals."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "seattle"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config_v2.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.25}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-03-14T16:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 180,
                "test_index_count": 60,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240314.json",
                "split_ts": "2024-03-14T16:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_042",
        instruction=(
            "Prepare the Providence artifacts for a portfolio review by pairing a frozen split with baseline coverage. For city='Providence', implement a time-based split at split_ts='2024-03-03T10:45:00Z' with row_count=120 and test_fraction=0.2, ensuring '/data/splits/boston_time_based_split_20240303.json' records train=96 and test=24. Validate model_name='simple_model' at created_ts='2024-03-17T10:15:00Z' against '/processed_data/features.csv', and save '/processed_data/feature_validation_boston_simple_model_20240317.json' under run_id='fv_boston_simple_model_20240317_v1' with started_ts='2024-03-22T12:00:00Z' and finished_ts='2024-03-22T12:02:00Z'. Report the split path and counts, including present, required, missing_count, and the validation path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-03T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2, "train_index_count": 96, "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240303.json", "split_ts": "2024-03-03T10:45:00Z"
            }),
            Action(name="ComputeFeatureCoverage", kwargs={
                "required_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "available_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"]
            }),
            Action(name="BuildFeatureValidationPath", kwargs={
                   "city_slug": "boston", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "fv_boston_simple_model_20240317_v1",
                "input_paths": ["/processed_data/features.csv"],
                "output_paths": ["/processed_data/feature_validation_boston_simple_model_20240317.json"],
                "started_ts": "2024-03-22T12:00:00Z",
                "finished_ts_nullable": "2024-03-22T12:02:00Z",
                "messages": [
                    "Feature validation for simple_model: 3/3 required features present.",
                    "Missing features: none",
                    "Validated file: /processed_data/feature_validation_boston_simple_model_20240317.json"
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_043",
        instruction=(
            "Handle an ingestion-only proof for Oakland covering the mid-March lead-in. For city='Oakland' with station_id='9414290', combine the analysis window '2024-03-11T00:00:00Z'..'2024-03-15T00:00:00Z' with a water-level lookback '2024-02-25T00:00:00Z'..'2024-03-11T00:00:00Z'. Save '/processed_data/merged_timeseries_sf_20240311_20240315.csv' under run id 'etl_sf_20240311_20240315_merge_v1' with started_ts='2024-03-22T14:00:00Z' and finished_ts='2024-03-22T14:18:00Z'. Provide the run id and the merged path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Oakland", "start_ts": "2024-03-11T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "9414290", "start_ts": "2024-03-11T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "9414290", "start_ts": "2024-02-25T00:00:00Z", "end_ts": "2024-03-11T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "sf", "start_ts": "2024-03-11T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_sf_20240311_20240315_merge_v1",
                "input_paths": [
                    "/data/raw/weather_sf_20240311.json",
                    "/data/raw/tide_pred_9414290.json",
                    "/data/raw/water_levels_9414290.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240311_20240315.csv"],
                "started_ts": "2024-03-22T14:00:00Z",
                "finished_ts_nullable": "2024-03-22T14:18:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-11..2024-03-15.",
                    "Attached observed water levels lookback 2024-02-25..2024-03-11.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_045",
        instruction=(
            "Oversee the production of a time-based dataset split for Oakland. Use the model configuration file at /config/model_config.json to obtain test_split_fraction. Use the processed time series at /data/processed/timeseries_sf_weather.csv (168 rows; 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z) as the source dataset for the split. Prepare the split summary at /data/splits/sf_time_based_split_20240322.json with method='time_based' and split_ts='2024-03-22T10:45:00Z'. The resulting split must have train_index_count=134 and test_index_count=34. Return the split_summary_json_path, train_index_count, test_index_count, and test_fraction as outputs. Adhere to the Split Protocol (SP) in the policy."
        ),
        actions=[
            Action(
                name="GetModelConfigParam",
                kwargs={"saved_json_path": "/config/model_config.json"}
            ),
            Action(
                name="GetProcessedTimeseriesMetadata",
                kwargs={"csv_path": "/data/processed/timeseries_sf_weather.csv"}
            ),
            Action(
                name="CreateSplitSummaryRecord",
                kwargs={
                    "method": "time_based",
                    "test_fraction": 0.2,
                    "train_index_count": 134,
                    "test_index_count": 34,
                    "split_summary_json_path": "/data/splits/sf_time_based_split_20240322.json",
                    "split_ts": "2024-03-22T10:45:00Z"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_046",
        instruction=(
            "Handle the creation of a Orlando split-only artifact designed to assist in backtesting around mid-month. For city='Orlando', apply method='time_based' with split_ts='2024-02-05T10:45:00Z', row_count=96, and test_fraction=0.2. The summary of the split should be located at '/data/splits/miami_time_based_split_20240205.json' with train set at 76 and test set at 20. Report back the path of the split and the respective counts."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-05T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240205.json",
                "split_ts": "2024-02-05T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_414",
        instruction=(
            "Coordinate the establishment of a Orlando split record in accordance with the baseline policy for the early-February timeframe. Retrieve the test fraction from '/config/model_config.json' and position the split starting at 2024-02-10T11:00:00Z. Save the canonical split summary for the Orlando processed series and communicate the location and the totals for train/test."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "miami"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-10T11:00:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240210.json",
                "split_ts": "2024-02-10T11:00:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_047",
        instruction=(
            "An auditable merged dataset is required for Orlando in early February. For city='Orlando' with station_id='8723214', apply the analysis window '2024-02-06T00:00:00Z'..'2024-02-10T00:00:00Z' and use the water‑level lookback '2024-02-02T00:00:00Z'..'2024-02-06T00:00:00Z'. Save '/processed_data/merged_timeseries_miami_20240206_20240210.csv' with ETL run id 'etl_miami_20240206_20240210_merge_v1' and started_ts='2024-03-23T08:10:00Z' and finished_ts='2024-03-23T08:27:00Z'. Provide the run id and the path of the merged file."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Orlando", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-02T00:00:00Z", "end_ts": "2024-02-06T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "miami", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_miami_20240206_20240210_merge_v1",
                "input_paths": [
                    "/data/raw/weather_miami_20240206.json",
                    "/data/raw/tide_pred_8723214.json",
                    "/data/raw/water_levels_8723214.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_miami_20240206_20240210.csv"],
                "started_ts": "2024-03-23T08:10:00Z",
                "finished_ts_nullable": "2024-03-23T08:27:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-06..2024-02-10.",
                    "Attached observed water levels lookback 2024-02-02..2024-02-06.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_048",
        instruction=(
            "A deterministic time‑based split is needed for Portland to facilitate a mid‑window evaluation. For city='Portland', establish method='time_based' with split_ts='2024-02-05T12:00:00Z', row_count=240, and test_fraction=0.2. Ensure that the split summary is '/data/splits/seattle_time_based_split_20240205.json' with train=192 and test=48. Indicate the split path and the counts."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-05T12:00:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 192, "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240205.json",
                "split_ts": "2024-02-05T12:00:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_404",
        instruction=(
            "Ensure you have a Orlando split record that corresponds with the baseline policy for the early-February window. Refer to the test fraction from '/config/model_config.json' and fix the split date at 2024-02-10T11:00:00Z. Save the canonical split summary for the Orlando processed series and deliver the path and the totals for train/test."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "miami"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-10T11:00:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240210.json",
                "split_ts": "2024-02-10T11:00:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_049",
        instruction=(
            "It is necessary to verify feature portability for Oakland before a baseline is reused. Check city='Oakland' with model_name='simple_model' against '/processed_data/features.csv' using created_ts='2024-03-17T10:15:00Z'. The required features are ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa']; available features match the requirements. Store the results in '/processed_data/feature_validation_sf_simple_model_20240317.json' under run_id='fv_sf_simple_model_20240317_v1' with started_ts='2024-03-23T09:00:00Z' and finished_ts='2024-03-23T09:02:00Z'. Present a report covering present, required, missing_count, and the validation path."
        ),
        actions=[
            Action(name="ComputeFeatureCoverage", kwargs={
                "required_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "available_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"]
            }),
            Action(name="BuildFeatureValidationPath", kwargs={
                   "city_slug": "sf", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "fv_sf_simple_model_20240317_v1",
                "input_paths": ["/processed_data/features.csv"],
                "output_paths": ["/processed_data/feature_validation_sf_simple_model_20240317.json"],
                "started_ts": "2024-03-23T09:00:00Z",
                "finished_ts_nullable": "2024-03-23T09:02:00Z",
                "messages": [
                    "Feature validation for simple_model: 3/3 required features present.",
                    "Missing features: none",
                    "Validated file: /processed_data/feature_validation_sf_simple_model_20240317.json"
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_050",
        instruction=(
            "Document the training run for San Francisco's version 2, focusing on the late-March period. Train model_name='flood_risk_sf_v2' for city='Oakland' during '2024-03-15T00:00:00Z' to '2024-03-22T00:00:00Z' utilizing the merged series '/processed_data/merged_timeseries_sf_20240315_20240322.csv' along with the time-based split '/data/splits/sf_time_based_split_20240320.json' (train=134, test=34). Save the model to '/models/flood_risk_sf_v2.pkl' using run_id 'mt_sf_flood_risk_sf_v2_20240315_20240322_v1' with started_ts='2024-03-23T10:00:00Z' and finished_ts='2024-03-23T10:38:00Z'. Store '/processed_data/metrics_summary_flood_risk_sf_v2_20240322.csv'. Provide details on the training run id, model path, and the recorded AUC and Accuracy."
        ),
        actions=[
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "mt_sf_flood_risk_sf_v2_20240315_20240322_v1",
                "input_paths": [
                    "/processed_data/merged_timeseries_sf_20240315_20240322.csv",
                    "/processed_data/features.csv",
                    "/data/splits/sf_time_based_split_20240320.json"
                ],
                "output_paths": [
                    "/models/flood_risk_sf_v2.pkl",
                    "/processed_data/metrics_summary_flood_risk_sf_v2_20240322.csv"
                ],
                "started_ts": "2024-03-23T10:00:00Z",
                "finished_ts_nullable": "2024-03-23T10:38:00Z",
                "messages": [
                    "Training samples: 134",
                    "Test samples: 34",
                    "Model saved to: /models/flood_risk_sf_v2.pkl"
                ]
            }),
            Action(name="GetModelMetrics", kwargs={
                "model_name": "flood_risk_sf_v2"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_051",
        instruction=(
            "Compile Providence ingestion artifacts as part of the audit trail. For city='Providence' with station_id='8443970', employ the analysis window '2024-03-02T00:00:00Z' to '2024-03-06T00:00:00Z' and the water-level lookback spanning '2024-02-15T00:00:00Z' to '2024-03-02T00:00:00Z'. Preserve '/processed_data/merged_timeseries_boston_20240302_20240306.csv' under ETL run id 'etl_boston_20240302_20240306_merge_v1' with started_ts='2024-03-23T11:00:00Z' and finished_ts='2024-03-23T11:20:00Z'. Relay the run id and the path of the merged data."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Providence", "start_ts": "2024-03-02T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "8443970", "start_ts": "2024-03-02T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "8443970", "start_ts": "2024-02-15T00:00:00Z", "end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "boston", "start_ts": "2024-03-02T00:00:00Z", "end_ts": "2024-03-06T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_boston_20240302_20240306_merge_v1",
                "input_paths": [
                    "/data/raw/weather_boston_20240302.json",
                    "/data/raw/tide_pred_8443970.json",
                    "/data/raw/water_levels_8443970.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_boston_20240302_20240306.csv"],
                "started_ts": "2024-03-23T11:00:00Z",
                "finished_ts_nullable": "2024-03-23T11:20:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-02..2024-03-06.",
                    "Attached observed water levels lookback 2024-02-15..2024-03-02.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_052",
        instruction=(
            "Handle the validation of baseline features for Portland before transferring the model. For city='Portland' using model_name='simple_model', confirm against the canonical '/processed_data/features.csv' with created_ts='2024-03-17T10:15:00Z'. Necessary features include ['precip_24h_mm','tide_anomaly_6h_max_m','pressure_drop_6h_hpa']; the available features match this list. Store '/processed_data/feature_validation_seattle_simple_model_20240317.json' under run_id='fv_seattle_simple_model_20240317_v1' with started_ts='2024-03-23T11:45:00Z' and finished_ts='2024-03-23T11:47:00Z'. Detail present, required, missing_count, and the path of validation."
        ),
        actions=[
            Action(name="ComputeFeatureCoverage", kwargs={
                "required_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"],
                "available_features": ["precip_24h_mm", "tide_anomaly_6h_max_m", "pressure_drop_6h_hpa"]
            }),
            Action(name="BuildFeatureValidationPath", kwargs={
                   "city_slug": "seattle", "model_name": "simple_model", "created_ts": "2024-03-17T10:15:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "fv_seattle_simple_model_20240317_v1",
                "input_paths": ["/processed_data/features.csv"],
                "output_paths": ["/processed_data/feature_validation_seattle_simple_model_20240317.json"],
                "started_ts": "2024-03-23T11:45:00Z",
                "finished_ts_nullable": "2024-03-23T11:47:00Z",
                "messages": [
                    "Feature validation for simple_model: 3/3 required features present.",
                    "Missing features: none",
                    "Validated file: /processed_data/feature_validation_seattle_simple_model_20240317.json"
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_400",
        instruction=(
            "Coordinate a reproducible time-based split to secure Seattle’s mid-March assessment for further training. Utilize the policy test fraction from '/config/model_config_v2.json' and anchor the division at 2024-03-14T16:45:00Z. Maintain the canonical split summary for the processed Portland series and provide the path along with the total numbers of train/test."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "seattle"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config_v2.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.25}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-03-14T16:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 180,
                "test_index_count": 60,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240314.json",
                "split_ts": "2024-03-14T16:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_053",
        instruction=(
            "Handle a Oakland v1 retraining task on a fixed mid‑March period. Train model_name='flood_risk_sf_v1' for city='Oakland' using the timeframe '2024-03-12T00:00:00Z'..'2024-03-16T00:00:00Z' with '/processed_data/merged_timeseries_sf_20240312_20240316.csv' and the split file '/data/splits/sf_time_based_split_20240319.json' (train=134, test=34). Save '/models/flood_risk_sf_v1.pkl' with run_id 'mt_sf_flood_risk_sf_v1_20240312_20240316_v1', starting at '2024-03-23T12:00:00Z' and finishing at '2024-03-23T12:30:00Z', and ensure '/processed_data/metrics_summary_flood_risk_sf_v1_20240316.csv' is stored. Submit the run id, model path, and the recorded AUC and Accuracy."
        ),
        actions=[
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "mt_sf_flood_risk_sf_v1_20240312_20240316_v1",
                "input_paths": [
                    "/processed_data/merged_timeseries_sf_20240312_20240316.csv",
                    "/processed_data/features.csv",
                    "/data/splits/sf_time_based_split_20240319.json"
                ],
                "output_paths": [
                    "/models/flood_risk_sf_v1.pkl",
                    "/processed_data/metrics_summary_flood_risk_sf_v1_20240316.csv"
                ],
                "started_ts": "2024-03-23T12:00:00Z",
                "finished_ts_nullable": "2024-03-23T12:30:00Z",
                "messages": [
                    "Training samples: 134",
                    "Test samples: 34",
                    "Model saved to: /models/flood_risk_sf_v1.pkl"
                ]
            }),
            Action(name="GetModelMetrics", kwargs={
                "model_name": "flood_risk_sf_v1"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_054",
        instruction=(
            "Coordinate a Portland merged artifact task centered around a late‑look window. For city='Portland' with station_id='9447130', employ the analysis duration '2024-02-06T00:00:00Z'..'2024-02-10T00:00:00Z' and the water‑level retrospective '2024-01-22T00:00:00Z'..'2024-02-06T00:00:00Z'. Store '/processed_data/merged_timeseries_seattle_20240206_20240210.csv' under run id 'etl_seattle_20240206_20240210_merge_v1' start at '2024-03-23T13:00:00Z' and conclude by '2024-03-23T13:18:00Z'. Report the run id and the path of the merged file."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Portland", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "9447130", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "9447130", "start_ts": "2024-01-22T00:00:00Z", "end_ts": "2024-02-06T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "seattle", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_seattle_20240206_20240210_merge_v1",
                "input_paths": [
                    "/data/raw/weather_seattle_20240206.json",
                    "/data/raw/tide_pred_9447130.json",
                    "/data/raw/water_levels_9447130.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_seattle_20240206_20240210.csv"],
                "started_ts": "2024-03-23T13:00:00Z",
                "finished_ts_nullable": "2024-03-23T13:18:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-06..2024-02-10.",
                    "Attached observed water levels lookback 2024-01-22..2024-02-06.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_055",
        instruction=(
            "Handle a time‑based split specific to Oakland to preserve a mid‑March evaluation. For city='Oakland', utilize method='time_based' with split_ts='2024-03-18T10:45:00Z', row_count=168 and test_fraction=0.2. The split summary must be '/data/splits/sf_time_based_split_20240318.json' with train=134 and test=34. Provide the split path and the counts."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-18T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 134, "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240318.json",
                "split_ts": "2024-03-18T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_056",
        instruction=(
            "Coordinate a regulator‑ready Orlando merge within a mid‑February timeframe. For city='Orlando' (station_id='8723214'), apply the analysis window '2024-02-10T00:00:00Z'..'2024-02-14T00:00:00Z' and the water‑level lookback '2024-02-06T00:00:00Z'..'2024-02-10T00:00:00Z'. Store '/processed_data/merged_timeseries_miami_20240210_20240214.csv' under run id 'etl_miami_20240210_20240214_merge_v1' with started_ts='2024-03-23T14:00:00Z' and finished_ts='2024-03-23T14:19:00Z'. Provide the run id and the merged path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Orlando", "start_ts": "2024-02-10T00:00:00Z", "end_ts": "2024-02-14T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-10T00:00:00Z", "end_ts": "2024-02-14T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-06T00:00:00Z", "end_ts": "2024-02-10T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "miami", "start_ts": "2024-02-10T00:00:00Z", "end_ts": "2024-02-14T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_miami_20240210_20240214_merge_v1",
                "input_paths": [
                    "/data/raw/weather_miami_20240210.json",
                    "/data/raw/tide_pred_8723214.json",
                    "/data/raw/water_levels_8723214.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_miami_20240210_20240214.csv"],
                "started_ts": "2024-03-23T14:00:00Z",
                "finished_ts_nullable": "2024-03-23T14:19:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-10..2024-02-14.",
                    "Attached observed water levels lookback 2024-02-06..2024-02-10.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_057",
        instruction=(
            "For a Providence time-based split to capture an early-March evaluation, for city='Providence', set method='time_based' with split_ts='2024-03-06T10:45:00Z', row_count=120, and test_fraction=0.2. Ensure the split summary is '/data/splits/boston_time_based_split_20240306.json' with train=96 and test=24. Report the split path and the quantities."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-06T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 96, "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240306.json",
                "split_ts": "2024-03-06T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_059",
        instruction=(
            "Coordinate the creation of a Portland merged artifact for an early-February window. For city='Portland' with station_id='9447130', apply the analysis window '2024-02-04T00:00:00Z'..'2024-02-08T00:00:00Z' and the water-level lookback '2024-01-20T00:00:00Z'..'2024-02-04T00:00:00Z'. Save '/processed_data/merged_timeseries_seattle_20240204_20240208.csv' under run id 'etl_seattle_20240204_20240208_merge_v1' with started_ts='2024-03-23T15:50:00Z' and finished_ts='2024-03-23T16:08:00Z'. Document the run id and the merged path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Portland", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "9447130", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "9447130", "start_ts": "2024-01-20T00:00:00Z", "end_ts": "2024-02-04T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "seattle", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_seattle_20240204_20240208_merge_v1",
                "input_paths": [
                    "/data/raw/weather_seattle_20240204.json",
                    "/data/raw/tide_pred_9447130.json",
                    "/data/raw/water_levels_9447130.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_seattle_20240204_20240208.csv"],
                "started_ts": "2024-03-23T15:50:00Z",
                "finished_ts_nullable": "2024-03-23T16:08:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-04..2024-02-08.",
                    "Attached observed water levels lookback 2024-01-20..2024-02-04.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_062",
        instruction=(
            "Handle the creation of a Providence merged artifact for a brief early-March period. For city='Providence' with station_id='8443970', utilize the analysis window '2024-03-02T00:00:00Z'..'2024-03-05T00:00:00Z' and the water-level lookback '2024-02-15T00:00:00Z'..'2024-03-02T00:00:00Z'. Save '/processed_data/merged_timeseries_boston_20240302_20240305.csv' under run id 'etl_boston_20240302_20240305_merge_v1' with started_ts='2024-03-23T17:20:00Z' and finished_ts='2024-03-23T17:36:00Z'. Communicate the run id and the merged path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Providence", "start_ts": "2024-03-02T00:00:00Z", "end_ts": "2024-03-05T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "8443970", "start_ts": "2024-03-02T00:00:00Z", "end_ts": "2024-03-05T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "8443970", "start_ts": "2024-02-15T00:00:00Z", "end_ts": "2024-03-02T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "boston", "start_ts": "2024-03-02T00:00:00Z", "end_ts": "2024-03-05T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_boston_20240302_20240305_merge_v1",
                "input_paths": [
                    "/data/raw/weather_boston_20240302.json",
                    "/data/raw/tide_pred_8443970.json",
                    "/data/raw/water_levels_8443970.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_boston_20240302_20240305.csv"],
                "started_ts": "2024-03-23T17:20:00Z",
                "finished_ts_nullable": "2024-03-23T17:36:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-02..2024-03-05.",
                    "Attached observed water levels lookback 2024-02-15..2024-03-02.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_063",
        instruction=(
            "Coordinate a Oakland split catalog entry at the end of the analysis timeframe. For city='Oakland', apply method='time_based' with split_ts='2024-03-22T10:45:00Z', row_count=168 and test_fraction=0.2. The split summary should be '/data/splits/sf_time_based_split_20240322.json' with train=134 and test=34. Present the split path and the numbers."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-22T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 134, "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240322.json",
                "split_ts": "2024-03-22T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_064",
        instruction=(
            "Handle the creation of a Orlando merged artifact for a late-mid-month timeframe. For city='Orlando' (station_id='8723214'), apply the analysis period from '2024-02-12T00:00:00Z' to '2024-02-16T00:00:00Z' with a water-level review interval '2024-02-08T00:00:00Z' to '2024-02-12T00:00:00Z'. Save '/processed_data/merged_timeseries_miami_20240212_20240216.csv' using 'etl_miami_20240212_20240216_merge_v1' with started_ts='2024-03-23T18:00:00Z' and finished_ts='2024-03-23T18:19:00Z'. Provide the run id and the path of the merged file."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Orlando", "start_ts": "2024-02-12T00:00:00Z", "end_ts": "2024-02-16T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-12T00:00:00Z", "end_ts": "2024-02-16T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-08T00:00:00Z", "end_ts": "2024-02-12T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "miami", "start_ts": "2024-02-12T00:00:00Z", "end_ts": "2024-02-16T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_miami_20240212_20240216_merge_v1",
                "input_paths": [
                    "/data/raw/weather_miami_20240212.json",
                    "/data/raw/tide_pred_8723214.json",
                    "/data/raw/water_levels_8723214.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_miami_20240212_20240216.csv"],
                "started_ts": "2024-03-23T18:00:00Z",
                "finished_ts_nullable": "2024-03-23T18:19:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-12..2024-02-16.",
                    "Attached observed water levels lookback 2024-02-08..2024-02-12.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_065",
        instruction=(
            "Coordinate the production of a Portland split artifact focused around February 7. For city='Portland', designate method='time_based' with split_ts='2024-02-07T12:00:00Z', row_count=240, and test_fraction=0.2. The split summary ought to be '/data/splits/seattle_time_based_split_20240207.json' with train=192 and test=48. Present the path of the split and the corresponding counts."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-07T12:00:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 192, "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240207.json",
                "split_ts": "2024-02-07T12:00:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_066",
        instruction=(
            "Handle the creation of a Providence split artifact for the second week of March. For city='Providence', apply method='time_based' and use split_ts='2024-03-07T10:45:00Z', row_count=120, and test_fraction=0.2. The split summary should be '/data/splits/boston_time_based_split_20240307.json' with train=96 and test=24. Provide the split path and the counts in your report."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-07T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 96, "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240307.json",
                "split_ts": "2024-03-07T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_068",
        instruction=(
            "Coordinate a Orlando split-only artifact production for a backtest around February 8. For city='Orlando', assign method='time_based' along with split_ts='2024-02-08T10:45:00Z', row_count=96, and test_fraction=0.2. Ensure the split summary is '/data/splits/miami_time_based_split_20240208.json' with train=76 and test=20. Include the split path and the counts in your report."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-08T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 76, "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240208.json",
                "split_ts": "2024-02-08T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_069",
        instruction=(
            "For obtaining a Providence split artifact that secures the early-March pivot, handle city='Providence' by implementing method='time_based' with split_ts='2024-03-05T10:45:00Z', row_count=120, and test_fraction=0.2. Ensure the split summary is '/data/splits/boston_time_based_split_20240305.json' with train=96 and test=24. Report back the split path and the counts."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-05T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 96, "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240305.json",
                "split_ts": "2024-03-05T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_070",
        instruction=(
            "Coordinate the finalization of a Oakland v1 training record for the complete late-March week. Employ model_name='flood_risk_sf_v1' on '2024-03-16T00:00:00Z'..'2024-03-22T00:00:00Z' utilizing '/processed_data/merged_timeseries_sf_20240316_20240322.csv' and the split '/data/splits/sf_time_based_split_20240321.json' (train=134, test=34). Save '/models/flood_risk_sf_v1.pkl' under run_id 'mt_sf_flood_risk_sf_v1_20240316_20240322_v1' with started_ts='2024-03-23T20:10:00Z' and finished_ts='2024-03-23T20:42:00Z', and ensure to persist '/processed_data/metrics_summary_flood_risk_sf_v1_20240322.csv'. Report the training run id, model path, along with the stored AUC and Accuracy."
        ),
        actions=[
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "mt_sf_flood_risk_sf_v1_20240316_20240322_v1",
                "input_paths": [
                    "/processed_data/merged_timeseries_sf_20240316_20240322.csv",
                    "/processed_data/features.csv",
                    "/data/splits/sf_time_based_split_20240321.json"
                ],
                "output_paths": [
                    "/models/flood_risk_sf_v1.pkl",
                    "/processed_data/metrics_summary_flood_risk_sf_v1_20240322.csv"
                ],
                "started_ts": "2024-03-23T20:10:00Z",
                "finished_ts_nullable": "2024-03-23T20:42:00Z",
                "messages": [
                    "Training samples: 134",
                    "Test samples: 34",
                    "Model saved to: /models/flood_risk_sf_v1.pkl"
                ]
            }),
            Action(name="GetModelMetrics", kwargs={
                "model_name": "flood_risk_sf_v1"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_071",
        instruction=(
            "Ensure an auditable merged dataset is prepared for Orlando in early February. For city='Orlando' with station_id='8723214', implement the analysis window '2024-02-08T00:00:00Z'..'2024-02-12T00:00:00Z' and the water‑level lookback '2024-02-04T00:00:00Z'..'2024-02-08T00:00:00Z'. Save '/processed_data/merged_timeseries_miami_20240208_20240212.csv' under ETL run id 'etl_miami_20240208_20240212_merge_v1' with started_ts='2024-03-23T20:55:00Z' and finished_ts='2024-03-23T21:14:00Z'. Provide the run id and the merged path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Orlando", "start_ts": "2024-02-08T00:00:00Z", "end_ts": "2024-02-12T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-08T00:00:00Z", "end_ts": "2024-02-12T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "8723214", "start_ts": "2024-02-04T00:00:00Z", "end_ts": "2024-02-08T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "miami", "start_ts": "2024-02-08T00:00:00Z", "end_ts": "2024-02-12T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_miami_20240208_20240212_merge_v1",
                "input_paths": [
                    "/data/raw/weather_miami_20240208.json",
                    "/data/raw/tide_pred_8723214.json",
                    "/data/raw/water_levels_8723214.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_miami_20240208_20240212.csv"],
                "started_ts": "2024-03-23T20:55:00Z",
                "finished_ts_nullable": "2024-03-23T21:14:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-08..2024-02-12.",
                    "Attached observed water levels lookback 2024-02-04..2024-02-08.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_072",
        instruction="Establish a deterministic time‑based split for Oakland to compare with a late‑March backtest. Utilize city='Oakland', method='time_based', split_ts='2024-03-18T10:45:00Z'; the processed series comprises 168 hourly rows and the test fraction is found in '/config/model_config.json' (0.2). Deliver the canonical split path and the train/test counts.",
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-18T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 134, "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240318.json",
                "split_ts": "2024-03-18T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_073",
        instruction="For a reproducible evaluation split for Portland, utilize city='Portland', method='time_based', split_ts='2024-02-05T12:00:00Z'; the processed series contains 240 rows and the test fraction is 0.2 as specified in '/config/model_config.json'. Deliver the canonical split path and the counts for train/test.",
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-05T12:00:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 192, "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240205.json",
                "split_ts": "2024-02-05T12:00:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_074",
        instruction="A Providence backtest split needs to be constructed from the time axis. Utilize city='Providence', method='time_based', split_ts='2024-03-03T10:45:00Z'; ensure row_count=120 and test_fraction=0.2 according to '/config/model_config.json'. Provide the split path and counts.",
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-03T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 96, "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240303.json",
                "split_ts": "2024-03-03T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_075",
        instruction="Ensure a Orlando time-based split for a period of 96 rows used in downstream audits. Set city='Orlando', method='time_based', split_ts='2024-02-03T10:45:00Z'; test_fraction=0.2 from '/config/model_config.json'. Provide the canonical split path and the counts (train/test).",
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-03T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 76, "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240203.json",
                "split_ts": "2024-02-03T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_076",
        instruction="Arrange a late-window split for Oakland to meet a regulatory replay. Apply method='time_based' with split_ts='2024-03-22T10:45:00Z' on a series of 168 rows and a 0.2 test fraction from '/config/model_config.json'. Supply the split path and counts.",
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-22T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 134, "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240322.json",
                "split_ts": "2024-03-22T10:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_078",
        instruction="Make sure to catalog a Portland split centered on '2024‑02‑06'. Utilize method='time_based', split_ts='2024-02-06T12:00:00Z', row_count=240, and 0.2 test fraction from '/config/model_config.json'. Report the split path and counts.",
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-06T12:00:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 192, "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240206.json",
                "split_ts": "2024-02-06T12:00:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_079",
        instruction="Request a Providence time‑based split aligned with an early‑March scenario. Employ split_ts='2024-03-02T10:00:00Z', row_count=120 and test_fraction 0.2 from '/config/model_config.json'. Return the canonical split path and counts.",
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 120, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-02T10:00:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 96, "test_index_count": 24,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240302.json",
                "split_ts": "2024-03-02T10:00:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_082",
        instruction="Handle a Orlando split variation focused on '2024‑02‑04'. Implement method='time_based' with split_ts='2024-02-04T12:00:00Z' on a 96‑row series and test_fraction=0.2 from '/config/model_config.json'. Present the split path and counts.",
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-04T12:00:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based", "test_fraction": 0.2,
                "train_index_count": 76, "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240204.json",
                "split_ts": "2024-02-04T12:00:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_085",
        instruction=(
            "Arrange for an ingestion‑only proof for Oakland including the mid‑March lead‑in. With city='Oakland' and station_id='9414290', combine the analysis window '2024-03-11T00:00:00Z'..'2024-03-15T00:00:00Z' with a water‑level lookback '2024-02-25T00:00:00Z'..'2024-03-11T00:00:00Z'. Store '/processed_data/merged_timeseries_sf_20240311_20240315.csv' under run id 'etl_sf_20240311_20240315_merge_v1' with started_ts='2024-03-23T19:10:00Z' and finished_ts='2024-03-23T19:28:00Z'. Announce the run id and the merged path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Oakland", "start_ts": "2024-03-11T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "9414290", "start_ts": "2024-03-11T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "9414290", "start_ts": "2024-02-25T00:00:00Z", "end_ts": "2024-03-11T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "sf", "start_ts": "2024-03-11T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_sf_20240311_20240315_merge_v1",
                "input_paths": [
                    "/data/raw/weather_sf_20240311.json",
                    "/data/raw/tide_pred_9414290.json",
                    "/data/raw/water_levels_9414290.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240311_20240315.csv"],
                "started_ts": "2024-03-23T19:10:00Z",
                "finished_ts_nullable": "2024-03-23T19:28:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-11..2024-03-15.",
                    "Attached observed water levels lookback 2024-02-25..2024-03-11.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_086",
        instruction=(
            "Handle the data readiness for Portland. Construct a summary using a time-based split that can be reused in downstream training: city='Portland', method='time_based', test_fraction from '/config/model_config.json', with the split instant on 2024-02-01T15:25:00Z. Ensure the summary aligns with the processed series for Portland and is stored within the canonical city/method/timestamp directory so it can be referenced deterministically in future tasks."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="GetWeatherForecast", kwargs={
                "city": "Providence",
                "start_ts": "2024-03-01T00:00:00Z",
                "end_ts": "2024-03-06T00:00:00Z"
            }),
            Action(name="GetTidePredictions", kwargs={
                "station_id": "8443970",
                "start_ts": "2024-03-01T00:00:00Z",
                "end_ts": "2024-03-06T00:00:00Z"
            }),
            Action(name="GetWaterLevels", kwargs={
                "station_id": "8443970",
                "start_ts": "2024-02-15T00:00:00Z",
                "end_ts": "2024-03-01T00:00:00Z"
            }),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_boston_20240301_20240306_merge_v1",
                "input_paths": [
                    "/data/raw/weather_boston_20240301.json",
                    "/data/raw/tide_pred_8443970.json",
                    "/data/raw/water_levels_8443970.json"
                ],
                "output_paths": [
                    "/processed_data/merged_timeseries_boston_20240301_20240306.csv"
                ],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-01..2024-03-06.",
                    "Attached observed water levels lookback 2024-02-15..2024-03-01.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            }),
            Action(name="GetModelMetrics", kwargs={
                "model_name": "boston_harbor_model"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_087",
        instruction=(
            "Manage the March training cycle for Oakland. Record a deterministic entry for Model Training & Evaluation concerning model_name='flood_risk_sf_v1' with the merged timeseries window from 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z, and a time-based split fixed at 2024-03-17T09:30:00Z. Follow the standard MTP defaults for timestamps and artifacts, and make certain the run accurately logs the training/test sample counts and the location of the saved model."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "seattle"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config_v2.json"
            }),
            Action(name="ComputeSplitCounts", kwargs={
                "row_count": 240,
                "test_fraction": 0.25
            }),
            Action(name="BuildSplitSummaryPath", kwargs={
                "city_slug": "seattle",
                "method": "time_based",
                "split_ts": "2024-03-14T16:45:00Z"
            }),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 180,
                "test_index_count": 60,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240314.json",
                "split_ts": "2024-03-14T16:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_088",
        instruction=(
            "Handle Miami's model training and evaluation (MTP) using model_name='flood_risk_miami_v1' for the analysis period 2024-02-01T00:00:00Z to 2024-02-05T00:00:00Z. Apply the time-based split starting on 2024-02-02 located at '/data/splits/miami_time_based_split_20240202.json' (train=72, test=24). Once finished, deliver the run id, the model artifact path, as well as the recorded AUC and Accuracy."
        ),
        actions=[
            Action(name="BuildMtpRunId", kwargs={
                "city_slug": "miami",
                "model_name": "flood_risk_miami_v1",
                "start_ts": "2024-02-01T00:00:00Z",
                "end_ts": "2024-02-05T00:00:00Z"
            }),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                "city_slug": "miami",
                "start_ts": "2024-02-01T00:00:00Z",
                "end_ts": "2024-02-05T00:00:00Z"
            }),
            Action(name="BuildMetricsSummaryPath", kwargs={
                "model_name": "flood_risk_miami_v1",
                "end_ts": "2024-02-05T00:00:00Z"
            }),
            Action(name="GetMtpTimestamps", kwargs={}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "mt_miami_flood_risk_miami_v1_20240201_20240205_v1",
                "input_paths": [
                    "/processed_data/merged_timeseries_miami_20240201_20240205.csv",
                    "/processed_data/features.csv",
                    "/data/splits/miami_time_based_split_20240202.json"
                ],
                "output_paths": [
                    "/models/flood_risk_miami_v1.pkl",
                    "/processed_data/metrics_summary_flood_risk_miami_v1_20240205.csv"
                ],
                "started_ts": "2024-03-17T09:30:00Z",
                "finished_ts_nullable": "2024-03-17T11:15:00Z",
                "messages": [
                    "Training samples: 72",
                    "Test samples: 24",
                    "Model saved to: /models/flood_risk_miami_v1.pkl"
                ]
            }),
            Action(name="GetModelMetrics", kwargs={
                "model_name": "flood_risk_miami_v1"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_089",
        instruction=(
            "Coordinate a time-based holdout for Oakland to enable stakeholders to assess week-over-week results. Adhere to the test split fraction set in '/processed_data/model_config.json' and mark the split with the timestamp '2024-03-17T10:45:00Z'. It is necessary to generate a canonical split summary JSON in /data/splits indicating the Oakland processed timeseries row count, along with only the essential fields."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "sf"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/processed_data/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-17T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={"method": "time_based", "test_fraction": 0.2, "train_index_count": 134,
                   "test_index_count": 34, "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json", "split_ts": "2024-03-17T10:45:00Z"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_090",
        instruction=(
            "Establish a Oakland time-based split that aligns with the method and naming found in the published template at '/processed_data/split_summary.json', but fixes the cutoff to the model config stored at '/processed_data/model_config.json' (created on 2024-03-17T10:30:00Z). Apply the processed SF series (168 hourly rows), secure the canonical split at that cutoff, and offer the canonical split path with the train/test totals."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="GetWeatherForecast", kwargs={
                   "city": "Oakland", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetTidePredictions", kwargs={
                   "station_id": "9414290", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="GetWaterLevels", kwargs={
                   "station_id": "9414290", "start_ts": "2024-02-14T00:00:00Z", "end_ts": "2024-03-15T00:00:00Z"}),
            Action(name="BuildMergedTimeseriesPath", kwargs={
                   "city_slug": "sf", "start_ts": "2024-03-15T00:00:00Z", "end_ts": "2024-03-22T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_sf_20240315_20240322_merge_v1",
                "input_paths": [
                    "/data/raw/weather_sf_20240315.json",
                    "/data/raw/tide_pred_9414290.json",
                    "/data/raw/water_levels_9414290.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_sf_20240315_20240322.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-03-15..2024-03-22.",
                    "Attached observed water levels lookback 2024-02-14..2024-03-15.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            }),
            Action(name="GetModelMetrics", kwargs={
                   "model_name": "flood_risk_sf_v1"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_091",
        instruction=(
            "You manage dataset splitting for Portland. Coordinate the Split Protocol (SP) with method='time_based'. Derive train/test sizes from the processed timeseries at '/data/processed/timeseries_seattle_weather.csv' and the test fraction defined in '/config/model_config.json'. Document the split summary for city='Portland' using split_ts='2024-03-17T10:45:00Z'."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "seattle"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-03-17T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={"method": "time_based", "test_fraction": 0.2, "train_index_count": 192,
                   "test_index_count": 48, "split_summary_json_path": "/data/splits/seattle_time_based_split_20240317.json", "split_ts": "2024-03-17T10:45:00Z"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_092",
        instruction=(
            "Handle the data split for Oakland. Apply the Split Protocol (SP) using method='time_based'. Retrieve test_fraction and split_ts from '/processed_data/split_summary.json', and calculate train/test counts based on '/data/processed/timeseries_sf_weather.csv'. Maintain the split summary for city='Oakland' with split_ts='2024-03-17T10:45:00Z'."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "sf"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetSplitSummaryDefaults", kwargs={
                   "path": "/processed_data/split_summary.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-17T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={"method": "time_based", "test_fraction": 0.2, "train_index_count": 134,
                   "test_index_count": 34, "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json", "split_ts": "2024-03-17T10:45:00Z"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_086",
        instruction=(
            "Handle the data readiness for Portland. Construct a summary using a time-based split that can be reused in downstream training: city='Portland', method='time_based', test_fraction from '/config/model_config.json', with the split instant on 2024-02-01T15:25:00Z. Ensure the summary aligns with the processed series for Portland and is stored within the canonical city/method/timestamp directory so it can be referenced deterministically in future tasks."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "sf"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetSplitSummaryDefaults", kwargs={
                   "path": "/processed_data/split_summary.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-17T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json",
                "split_ts": "2024-03-17T10:45:00Z"
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_087",
        instruction=(
            "Manage the March training cycle for Oakland. Record a deterministic entry for Model Training & Evaluation concerning model_name='flood_risk_sf_v1' with the merged timeseries window from 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z, and a time-based split fixed at 2024-03-17T09:30:00Z. Follow the standard MTP defaults for timestamps and artifacts, and make certain the run accurately logs the training/test sample counts and the location of the saved model."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "seattle"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/regression_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.3}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-03-01T09:20:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.3,
                "train_index_count": 168,
                "test_index_count": 72,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240301.json",
                "split_ts": "2024-03-01T09:20:00Z"
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_090",
        instruction=(
            "Establish a Oakland time-based split that aligns with the method and naming found in the published template at '/processed_data/split_summary.json', but fixes the cutoff to the model config stored at '/processed_data/model_config.json' (created on 2024-03-17T10:30:00Z). Apply the processed SF series (168 hourly rows), secure the canonical split at that cutoff, and offer the canonical split path with the train/test totals."
        ),
        actions=[
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "sf"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetSplitSummaryDefaults", kwargs={
                   "path": "/processed_data/split_summary.json"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/processed_data/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-17T10:30:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json",
                "split_ts": "2024-03-17T10:30:00Z"
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_086",
        instruction=(
            "Handle the data readiness for Portland. Construct a summary using a time-based split that can be reused in downstream training: city='Portland', method='time_based', test_fraction from '/config/model_config.json', with the split instant on 2024-02-01T15:25:00Z. Ensure the summary aligns with the processed series for Portland and is stored within the canonical city/method/timestamp directory so it can be referenced deterministically in future tasks."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "seattle"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                "csv_path": "/data/processed/timeseries_seattle_weather.csv"
            }),
            Action(name="GetModelConfigParam", kwargs={
                "saved_json_path": "/config/model_config.json"
            }),
            Action(name="ComputeSplitCounts", kwargs={
                "row_count": 240,
                "test_fraction": 0.2
            }),
            Action(name="BuildSplitSummaryPath", kwargs={
                "city_slug": "seattle",
                "method": "time_based",
                "split_ts": "2024-02-01T15:25:00Z"
            }),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 192,
                "test_index_count": 48,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240201.json",
                "split_ts": "2024-02-01T15:25:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_087",
        instruction=(
            "Manage the March training cycle for Oakland. Record a deterministic entry for Model Training & Evaluation concerning model_name='flood_risk_sf_v1' with the merged timeseries window from 2024-03-15T00:00:00Z to 2024-03-22T00:00:00Z, and a time-based split fixed at 2024-03-17T09:30:00Z. Follow the standard MTP defaults for timestamps and artifacts, and make certain the run accurately logs the training/test sample counts and the location of the saved model."
        ),
        actions=[
            Action(name="BuildMergedTimeseriesPath", kwargs={
                "city_slug": "sf",
                "start_ts": "2024-03-15T00:00:00Z",
                "end_ts": "2024-03-22T00:00:00Z"
            }),
            Action(name="BuildFeaturesCsvPath", kwargs={"city_slug": "sf"}),
            Action(name="BuildSplitSummaryPath", kwargs={
                "city_slug": "sf",
                "method": "time_based",
                "split_ts": "2024-03-17T09:30:00Z"
            }),
            Action(name="BuildMtpInputPaths", kwargs={
                "merged_timeseries_path": "/processed_data/merged_timeseries_sf_20240315_20240322.csv",
                "features_csv_path": "/processed_data/features.csv",
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json"
            }),
            Action(name="BuildMetricsSummaryPath", kwargs={
                "model_name": "flood_risk_sf_v1",
                "end_ts": "2024-03-22T00:00:00Z"
            }),
            Action(name="BuildMtpMessages", kwargs={
                "train_samples": 134,
                "test_samples": 34,
                "model_path": "/models/flood_risk_sf_v1.pkl"
            }),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "mt_sf_flood_risk_sf_v1_20240315_20240322_v1",
                "input_paths": [
                    "/processed_data/merged_timeseries_sf_20240315_20240322.csv",
                    "/processed_data/features.csv",
                    "/data/splits/sf_time_based_split_20240317.json"
                ],
                "output_paths": [
                    "/models/flood_risk_sf_v1.pkl",
                    "/processed_data/metrics_summary_flood_risk_sf_v1_20240322.csv"
                ],
                "started_ts": "2024-03-17T09:30:00Z",
                "finished_ts_nullable": "2024-03-17T11:15:00Z",
                "messages": [
                    "Training samples: 134",
                    "Test samples: 34",
                    "Model saved to: /models/flood_risk_sf_v1.pkl"
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_200",
        instruction=(
            "You are responsible for Oakland data readiness. Handle the Split Protocol for city='Oakland' utilizing method='time_based', drawing the test_fraction from '/config/model_config.json' and applying split_ts='2024-03-17T10:45:00Z'. Ensure the canonical split summary is maintained and the train/test sample sizes and path are transparent."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "sf"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-17T10:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json",
                "split_ts": "2024-03-17T10:45:00Z"
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_201",
        instruction=(
            "You oversee the Orlando time-based dataset division. For city='Orlando', coordinate the Split Protocol employing test_fraction from '/config/model_config_v2.json' and using split_ts='2024-02-02T15:45:00Z'. Confirm that the persisted summary accurately conveys the correct counts and canonical path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config_v2.json"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "miami"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 96, "test_fraction": 0.25}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-02T15:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 72,
                "test_index_count": 24,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240202.json",
                "split_ts": "2024-02-02T15:45:00Z"
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_202",
        instruction=(
            "You are in charge of the Providence split artifact. Coordinate a time-based split for city='Providence' with test_fraction from '/processed_data/boston_model_config.json' and split_ts='2024-03-01T13:18:00Z'. Store the split summary and display the resulting counts and path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-01T13:18:00Z"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "boston"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/processed_data/boston_model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 120, "test_fraction": 0.25}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 90,
                "test_index_count": 30,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240301.json",
                "split_ts": "2024-03-01T13:18:00Z"
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_203",
        instruction=(
            "You are responsible for Seattle's split governance. For city='Portland', execute a time-based split using test_fraction from '/config/regression_config.json' and split_ts='2024-02-01T15:25:00Z'. Document the canonical summary and clearly present the counts and path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "seattle"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/regression_config.json"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.3}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-02-01T15:25:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.3,
                "train_index_count": 168,
                "test_index_count": 72,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240201.json",
                "split_ts": "2024-02-01T15:25:00Z"
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_220",
        instruction=(
            "Handle a reproducible time-based split specifically for Portland to establish a March evaluation window. Refer to the policy test fraction located in '/config/model_config_v2.json' and set the split to start at 2024-03-14T16:45:00Z. Save the canonical split record for the processed series of Portland and provide the path along with the train/test totals."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "seattle"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_seattle_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config_v2.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 240, "test_fraction": 0.25}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "seattle", "method": "time_based", "split_ts": "2024-03-14T16:45:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 180,
                "test_index_count": 60,
                "split_summary_json_path": "/data/splits/seattle_time_based_split_20240314.json",
                "split_ts": "2024-03-14T16:45:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_503",
        instruction=(
            "Coordinate an appendix for early-February Orlando that combines a frozen split with a metrics export for reporting purposes. Freeze a time-based split using the baseline policy at 2024-02-10T11:00:00Z and then document a metrics-only export for model_name='flood_risk_miami_v1' for the 2024-02-02 cutoff. Provide the split path with train/test totals along with the metrics summary path."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Orlando"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "miami"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_miami_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/config/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 96, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "miami", "method": "time_based", "split_ts": "2024-02-10T11:00:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 76,
                "test_index_count": 20,
                "split_summary_json_path": "/data/splits/miami_time_based_split_20240210.json",
                "split_ts": "2024-02-10T11:00:00Z"
            }),
            Action(name="GetModelInfo", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            Action(name="GetModelMetrics", kwargs={
                   "model_name": "flood_risk_miami_v1"}),
            Action(name="BuildMetricsSummaryPath", kwargs={
                   "model_name": "flood_risk_miami_v1", "end_ts": "2024-02-02T00:00:00Z"}),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "me_miami_flood_risk_miami_v1_20240202_v1",
                "input_paths": [
                    "/models/flood_risk_miami_v1.pkl",
                    "/processed_data/features.csv",
                    "/processed_data/merged_timeseries_miami_20240201_20240202.csv"
                ],
                "output_paths": ["/processed_data/metrics_summary_flood_risk_miami_v1_20240202.csv"],
                "started_ts": "2024-03-18T15:45:00Z",
                "finished_ts_nullable": None,
                "messages": [
                    "AUC: 0.73",
                    "Accuracy: 0.75",
                    "Metrics saved to: /processed_data/metrics_summary_flood_risk_miami_v1_20240202.csv"
                ]
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_800",
        instruction=(
            "Handle capturing a deterministic Providence split snapshot to be cited in early-March reports. Apply the test fraction from '/processed_data/boston_model_config.json' and anchor the split at 2024-03-01T13:18:00Z. Deliver the canonical split record path along with the train/test sizes."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Providence"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "boston"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_boston_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/processed_data/boston_model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 120, "test_fraction": 0.25}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "boston", "method": "time_based", "split_ts": "2024-03-01T13:18:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.25,
                "train_index_count": 90,
                "test_index_count": 30,
                "split_summary_json_path": "/data/splits/boston_time_based_split_20240301.json",
                "split_ts": "2024-03-01T13:18:00Z"
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_902",
        instruction=(
            "Coordinate a Oakland split snapshot to aid a compliance replay. Employ the test fraction from '/processed_data/model_config.json' and fix the split at 2024-03-17T10:30:00Z. Maintain the canonical split summary for the Oakland processed series and provide the path with train/test totals."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Oakland"}),
            Action(name="BuildProcessedTimeseriesPath",
                   kwargs={"city_slug": "sf"}),
            Action(name="GetProcessedTimeseriesMetadata", kwargs={
                   "csv_path": "/data/processed/timeseries_sf_weather.csv"}),
            Action(name="GetModelConfigParam", kwargs={
                   "saved_json_path": "/processed_data/model_config.json"}),
            Action(name="ComputeSplitCounts", kwargs={
                   "row_count": 168, "test_fraction": 0.2}),
            Action(name="BuildSplitSummaryPath", kwargs={
                   "city_slug": "sf", "method": "time_based", "split_ts": "2024-03-17T10:30:00Z"}),
            Action(name="CreateSplitSummaryRecord", kwargs={
                "method": "time_based",
                "test_fraction": 0.2,
                "train_index_count": 134,
                "test_index_count": 34,
                "split_summary_json_path": "/data/splits/sf_time_based_split_20240317.json",
                "split_ts": "2024-03-17T10:30:00Z"
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_950",
        instruction=(
            "Handle a Charleston ingestion targeting a high‑tide timeframe. For city='Charleston' and NOAA station '8665530', implement the Merge Window Protocol during 2024-01-22T00:00:00Z..2024-01-23T00:00:00Z with a water‑level reference period of 2024-01-22T00:00:00Z..2024-01-22T02:00:00Z. The ETL record must include references to the canonical raw inputs '/data/raw/weather_charleston_20240122.json', '/data/raw/tide_pred_8665530.json', '/data/raw/water_levels_8665530.json' and the merged output '/processed_data/merged_timeseries_charleston_20240122_20240123.csv', using run_id 'etl_charleston_20240122_20240123_merge_v1'. Conclude by reporting the stored AUC and Accuracy for model_name='simple_model'."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Charleston"}),
            Action(name="GetWeatherForecast", kwargs={
                "city": "Charleston",
                "start_ts": "2024-01-22T00:00:00Z",
                "end_ts": "2024-01-23T00:00:00Z"
            }),
            Action(name="GetTidePredictions", kwargs={
                "station_id": "8665530",
                "start_ts": "2024-01-22T00:00:00Z",
                "end_ts": "2024-01-23T00:00:00Z"
            }),
            Action(name="GetWaterLevels", kwargs={
                "station_id": "8665530",
                "start_ts": "2024-01-22T00:00:00Z",
                "end_ts": "2024-01-22T02:00:00Z"
            }),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_charleston_20240122_20240123_merge_v1",
                "input_paths": [
                    "/data/raw/weather_charleston_20240122.json",
                    "/data/raw/tide_pred_8665530.json",
                    "/data/raw/water_levels_8665530.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_charleston_20240122_20240123.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-01-22..2024-01-23.",
                    "Attached observed water levels lookback 2024-01-22..2024-01-22.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            }),
            Action(name="GetModelMetrics", kwargs={
                   "model_name": "simple_model"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_953",
        instruction=(
            "Coordinate a Portland ingestion snapshot focused on spring tides. For city='Portland' and NOAA station '9447130', conduct the Merge Window Protocol over 2024-02-01T00:00:00Z..2024-02-08T00:00:00Z, utilizing a water-level lookback spanning 2024-01-15T00:00:00Z..2024-02-01T00:00:00Z. The ETL record must reference the canonical raw inputs '/data/raw/weather_seattle_20240201.json', '/data/raw/tide_pred_9447130.json', '/data/raw/water_levels_9447130.json' and the merged output '/processed_data/merged_timeseries_seattle_20240201_20240208.csv', having run_id 'etl_seattle_20240201_20240208_merge_v1'. Wrap up by reporting the stored AUC and Accuracy for model_name='simple_model'."
        ),
        actions=[
            Action(name="ResolveCitySlug", kwargs={"city": "Portland"}),
            Action(name="GetWeatherForecast", kwargs={
                "city": "Portland",
                "start_ts": "2024-02-01T00:00:00Z",
                "end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="GetTidePredictions", kwargs={
                "station_id": "9447130",
                "start_ts": "2024-02-01T00:00:00Z",
                "end_ts": "2024-02-08T00:00:00Z"
            }),
            Action(name="GetWaterLevels", kwargs={
                "station_id": "9447130",
                "start_ts": "2024-01-15T00:00:00Z",
                "end_ts": "2024-02-01T00:00:00Z"
            }),
            Action(name="CreateEtlRunRecord", kwargs={
                "run_id": "etl_seattle_20240201_20240208_merge_v1",
                "input_paths": [
                    "/data/raw/weather_seattle_20240201.json",
                    "/data/raw/tide_pred_9447130.json",
                    "/data/raw/water_levels_9447130.json"
                ],
                "output_paths": ["/processed_data/merged_timeseries_seattle_20240201_20240208.csv"],
                "started_ts": "2024-03-16T14:00:00Z",
                "finished_ts_nullable": "2024-03-16T14:22:00Z",
                "messages": [
                    "Merged weather and tide predictions for 2024-02-01..2024-02-08.",
                    "Attached observed water levels lookback 2024-01-15..2024-02-01.",
                    "Output columns: timestamp, precipitation_mm_hr, temperature_2m_c, wind_speed_10m_ms, tide_pred_m, water_level_m, pressure_hpa."
                ]
            }),
            Action(name="GetModelMetrics", kwargs={
                   "model_name": "simple_model"})
        ],
        outputs=[]
    )
]
