import json
from typing import Any, Dict
from domains.dto import Tool

LAT = 55
LONG = 55


class SetProjectConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        target_city = kwargs.get("target_city")
        horizon = kwargs.get("forecast_horizon_days")
        max_radius = kwargs.get("max_station_distance_km_nullable")
        configs = data.get("project_config", [])

        timezone = "America/New_York"
        for config in configs:
            if config.get("target_city") == target_city:
                timezone = config.get("timezone_default")
                break
        config = {
            "config_id": "CONFIG_001",
            "target_city": target_city,
            "timezone_default": timezone,
            "forecast_horizon_days": horizon,
            "max_station_distance_km_nullable": max_radius,
        }
        data.get("project_config", []).append(config)
        return json.dumps({"config_id": "CONFIG_001", **config})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetProjectConfig",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_city": {
                            "type": "string",
                            "description": "The name of the city to look up.",
                        }
                    },
                    "required": ["target_city"],
                },
            },
        }


class SetGeocodeCity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city_name = kwargs.get("city_name")

        results = data.get("geocoding_results", [])
        for result in results:
            if result.get("query_city") == city_name:
                return json.dumps(result)
        json_city_path = "_".join(city_name.split()).lower()
        result = {
            "geo_id": "GEO_001",
            "query_city": city_name,
            "latitude": LAT,
            "longitude": LONG,
            "raw_json_path_nullable": f"/data/raw/geocoding_{json_city_path}.json",
        }
        data.get("geocoding_results", []).append(result)
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetGeocodeCity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_name": {
                            "type": "string",
                            "description": "The name of the city.",
                        }
                    },
                    "required": ["city_name"],
                },
            },
        }


class SetProjectDirectories(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # This is a simulation; in a real environment, this would interact with a file system.
        files = kwargs.get("files", [])
        project_dir_id = "PROJ_DIR_001"
        file_dir = {
            "paths": files,
            "project_dir_id": project_dir_id,
        }
        data.get("file_directory", []).append(file_dir)
        return json.dumps({"status": "success", "project_dir_id": project_dir_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetProjectDirectories",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class FindNoaaStation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        lat = kwargs.get("latitude")
        lon = kwargs.get("longitude")

        station_id = "NOAA_STATION_001"
        noaa_station_json = {
            "station_ids": station_id,
            "raw_json_path_nullable": f"/data/raw/noaa_station_{station_id}.json",
        }
        data.get("noaa_station_searches", []).append(noaa_station_json)
        return json.dumps(noaa_station_json)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindNoaaStation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "latitude": {
                            "type": "number",
                            "description": "The latitude of the search area.",
                        },
                        "longitude": {
                            "type": "number",
                            "description": "The longitude of the search area.",
                        },
                        "radius_km": {
                            "type": "number",
                            "description": "The search radius in kilometers.",
                        },
                    },
                    "required": ["latitude", "longitude"],
                },
            },
        }


class SetWeatherForecast(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city = kwargs.get("city")
        id = "WEATHER_FORECAST_001"
        weather_forecast_json = {
            "forecast_id": id,
            "raw_json_path_nullable": f"/data/raw/weather_forecast_{id}.json",
        }
        data.get("weather_forecasts", []).append(weather_forecast_json)
        return json.dumps(weather_forecast_json)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetWeatherForecast",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "latitude": {
                            "type": "number",
                            "description": "The latitude of the forecast location.",
                        },
                        "longitude": {
                            "type": "number",
                            "description": "The longitude of the forecast location.",
                        },
                        "horizon_days": {
                            "type": "integer",
                            "description": "The number of days to forecast.",
                        },
                    },
                    "required": ["latitude", "longitude"],
                },
            },
        }


class SetWaterLevels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        station_id = kwargs.get("station_id")
        # This is a simulation; in a real environment, this would fetch data from NOAA.

        water_level_data = {
            "station_id": station_id,
            "data_points": [
                {"timestamp": "2023-10-01T00:00:00Z", "water_level_meters": 1.2},
                {"timestamp": "2023-10-01T01:00:00Z", "water_level_meters": 1.3},
            ],
            "raw_json_path_nullable": f"/data/raw/water_levels_{station_id}.json",
        }
        data.get("water_level_data", []).append(water_level_data)
        return json.dumps(water_level_data)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetWaterLevels",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {
                            "type": "string",
                            "description": "The ID of the NOAA station.",
                        }
                    },
                    "required": ["station_id"],
                },
            },
        }


class SetTidePredictions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        station_id = kwargs.get("station_id")
        # This is a simulation; in a real environment, this would fetch data from NOAA.

        tide_prediction_data = {
            "station_id": station_id,
            "predictions": [
                {"timestamp": "2023-10-01T00:00:00Z", "predicted_tide_meters": 1.5},
                {"timestamp": "2023-10-01T01:00:00Z", "predicted_tide_meters": 1.6},
            ],
            "raw_json_path_nullable": f"/data/raw/tide_predictions_{station_id}.json",
        }
        data.get("tide_predictions", []).append(tide_prediction_data)
        return json.dumps(tide_prediction_data)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetTidePredictions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {
                            "type": "string",
                            "description": "The ID of the NOAA station.",
                        }
                    },
                    "required": ["station_id"],
                },
            },
        }


class SetCoastalMeteorology(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        station_id = kwargs.get("station_id")
        # This is a simulation; in a real environment, this would fetch data from NOAA.

        coastal_meteorology_data = {
            "station_id": station_id,
            "data_points": [
                {
                    "timestamp": "2023-10-01T00:00:00Z",
                    "wind_speed_m_s": 5.0,
                    "pressure_hPa": 1013,
                },
                {
                    "timestamp": "2023-10-01T01:00:00Z",
                    "wind_speed_m_s": 5.5,
                    "pressure_hPa": 1012,
                },
            ],
            "raw_json_path_nullable": f"/data/raw/coastal_meteorology_{station_id}.json",
        }
        data.get("coastal_meteorology_data", []).append(coastal_meteorology_data)
        return json.dumps(coastal_meteorology_data)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetCoastalMeteorology",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {
                            "type": "string",
                            "description": "The ID of the NOAA station.",
                        }
                    },
                    "required": ["station_id"],
                },
            },
        }


class CreateFeatures(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        input_path = kwargs.get("input_csv_path")
        if not input_path:
            return json.dumps({"error": "input_csv_path is a required argument."})

        features_id = "FEATURES_001"
        new_features_path = "/processed_data/features_001.csv"

        feature_entry = {
            "features_id": features_id,
            "source_csv_path": input_path,
            "features_csv_path": new_features_path,
            "feature_names": [
                "precip_24h_mm",
                "tide_anomaly_6h_max_m",
                "pressure_drop_6h_hpa",
            ],
        }

        data.setdefault("features", []).append(feature_entry)
        return json.dumps(feature_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFeatures",
                "description": "Takes a path to a processed timeseries CSV and engineers a standard set of features required for modeling.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "input_csv_path": {
                            "type": "string",
                            "description": "The file path to the processed timeseries data.",
                        }
                    },
                    "required": ["input_csv_path"],
                },
            },
        }


class SetModelConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        config_id = "MODEL_CONFIG_001"

        config_entry = {
            "config_id": config_id,
            "classification_threshold_m": kwargs.get("classification_threshold_m"),
            "precip_24h_threshold_mm": kwargs.get("precip_24h_threshold_mm"),
            "test_split_fraction": kwargs.get("test_split_fraction"),
            "config_json_path": f"/configs/model_config_{config_id}.json",
        }

        data.setdefault("model_config", []).append(config_entry)
        return json.dumps(config_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetModelConfig",
                "description": "Creates a configuration record for the modeling process with specified parameters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "classification_threshold_m": {
                            "type": "number",
                            "description": "The threshold in meters for classifying high-risk events.",
                        },
                        "precip_24h_threshold_mm": {
                            "type": "number",
                            "description": "The precipitation threshold in millimeters.",
                        },
                        "test_split_fraction": {
                            "type": "number",
                            "description": "The fraction of data for the test set.",
                        },
                    },
                    "required": [],
                },
            },
        }


class CreateModel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        config_id = kwargs.get("model_config_id")
        model_name = kwargs.get("model_name")
        model_id = f"MODEL_{model_name}"
        model_entry = {
            "model_id": model_id,
            "model_name": model_name,
            "config_id": config_id,
            "model_path": f"/models/{model_id}.joblib",
            "model_type": kwargs.get("model_type"),
            "feature_names": kwargs.get("features_id"),
            "train_metrics_json_path_nullable": f"/metrics/{model_id}_train_metrics.json",
        }
        data.setdefault("models", []).append(model_entry)
        return json.dumps(model_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateModel",
                "description": "Creates a model entry, linking a configuration, model type, and feature set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_config_id": {
                            "type": "string",
                            "description": "The ID of the model configuration.",
                        },
                        "model_type": {
                            "type": "string",
                            "description": "The type of model to train, e.g., 'logistic_regression'.",
                        },
                        "features_id": {
                            "type": "string",
                            "description": "The ID of the feature set to be used by the model.",
                        },
                    },
                    "required": ["model_config_id", "model_type", "features_id"],
                },
            },
        }


class GetModel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:

        model_name = kwargs.get("model_name")
        model_id = f"MODEL_{model_name}"

        model_entry = {
            "model_id": model_id,
            "model_name": model_name,
            "model_path": f"/models/{model_id}.joblib",
            "model_type": kwargs.get("model_type"),
            "feature_names": kwargs.get("features_id"),
            "train_metrics_json_path_nullable": f"/metrics/{model_id}_train_metrics.json",
        }
        data.setdefault("models", []).append(model_entry)
        return json.dumps(model_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetModel",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_config_id": {
                            "type": "string",
                            "description": "The ID of the model configuration.",
                        },
                        "model_type": {
                            "type": "string",
                            "description": "The type of model to train, e.g., 'logistic_regression'.",
                        },
                        "features_id": {
                            "type": "string",
                            "description": "The ID of the feature set to be used by the model.",
                        },
                    },
                    "required": [],
                },
            },
        }


class CreateDatasetSplit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        split_id = "SPLIT_001"

        split_entry = {
            "split_id": split_id,
            "features_id": kwargs.get("features_id"),
            "method": "time_based",
            "test_fraction": kwargs.get("test_fraction"),
            "split_summary_json_path": f"/processed_data/split_summary_{split_id}.json",
        }

        data.setdefault("dataset_split.json", []).append(split_entry)
        return json.dumps(split_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDatasetSplit",
                "description": "Creates a train/test split from the feature set based on the specified method.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "features_id": {
                            "type": "string",
                            "description": "The ID of the feature set to use.",
                        },
                        "test_fraction": {
                            "type": "number",
                            "description": "The fraction of data for the test set.",
                        },
                    },
                    "required": ["features_id", "test_fraction"],
                },
            },
        }


class TrainModel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        model_name = kwargs.get("model_name")
        model_id = f"MODEL_{model_name}"
        predictions_id = "PRED_001"

        model_entry = {
            "model_id": model_id,
            "model_name": model_name,
            "model_type": kwargs.get("model_type"),
            "features_id": kwargs.get("features_id"),
            "config_id": kwargs.get("config_id"),
            "split_id": kwargs.get("split_id"),
            "model_path": f"/models/{model_id}.joblib",
        }

        predictions_entry = {
            "predictions_id": predictions_id,
            "model_id": model_id,
            "predictions_csv_path": f"/predictions/PRED_{model_id}.csv",
        }

        data.setdefault("models.json", []).append(model_entry)
        data.setdefault("predictions.json", []).append(predictions_entry)

        return json.dumps(predictions_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TrainModel",
                "description": "Trains a simple logistic regression model using the specified features, configuration, and data split.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {
                            "type": "string",
                            "description": "A descriptive name for the model.",
                        },
                        "features_id": {
                            "type": "string",
                            "description": "The ID of the feature set.",
                        },
                        "config_id": {
                            "type": "string",
                            "description": "The ID of the model configuration.",
                        },
                        "split_id": {
                            "type": "string",
                            "description": "The ID of the dataset split.",
                        },
                    },
                    "required": ["model_name", "features_id", "config_id", "split_id"],
                },
            },
        }


class EvaluateModel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        metrics_id = "METRICS_001"
        predictions_id = kwargs.get("predictions_id")
        if not predictions_id:
            predictions_id = "PRED_001"
        metrics_entry = {
            "model_id": kwargs.get("model_id"),
            "metrics_id": metrics_id,
            "predictions_id": predictions_id,
            "auc": 0.87,
            "accuracy": 0.91,
            "metrics_json_path": f"/metrics/metrics_{metrics_id}.json",
        }

        data.setdefault("metrics.json", []).append(metrics_entry)
        return json.dumps(metrics_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EvaluateModel",
                "description": "Calculates performance metrics (AUC and accuracy) for a trained model based on its predictions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "predictions_id": {
                            "type": "string",
                            "description": "The ID of the predictions to evaluate.",
                        }
                    },
                    "required": ["predictions_id"],
                },
            },
        }


class PrepareStakeholderOutputs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        output_id = "STAKEHOLDER_OUTPUT_001"

        # In a real scenario, this would copy files to a final 'deliverables' location.
        # Here we just create the record.
        output_entry = {
            "stakeholder_output_id": output_id,
            "final_predictions_id": kwargs.get("predictions_id"),
            "final_metrics_id": kwargs.get("metrics_id"),
            "status": "ready",
            "predictions_csv_path": f"/deliverables/final_predictions_{output_id}.csv",
            "metrics_json_path": f"/deliverables/final_metrics_{output_id}.json",
        }

        data.setdefault("stakeholder_outputs.json", []).append(output_entry)
        return json.dumps(output_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PrepareStakeholderOutputs",
                "description": "Finalizes the modeling run by creating a record pointing to the definitive prediction and metrics files.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "predictions_id": {
                            "type": "string",
                            "description": "The ID of the final predictions.",
                        },
                        "metrics_id": {
                            "type": "string",
                            "description": "The ID of the final metrics.",
                        },
                    },
                    "required": ["predictions_id", "metrics_id"],
                },
            },
        }


class CreateSummaryPlots(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        predictions_id = kwargs.get("predictions_id")
        model_id = kwargs.get("model_id")

        figure_id = "FIGURE_001"
        figure_path = f"/figures/risk_timeseries_{model_id}.png"

        qc_figure_entry = {
            "figure_id": figure_id,
            "figure_paths": [figure_path, f"/figures/summary_{model_id}.png"],
            "descriptions": [
                f"Time series summary plot showing predicted flood risk probability vs key drivers for model '{model_id}'."
            ],
            "predictions_id": predictions_id,
        }

        data.setdefault("qc_figures.json", []).append(qc_figure_entry)

        return json.dumps(qc_figure_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSummaryPlots",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "predictions_id": {
                            "type": "string",
                            "description": "The ID of the final predictions.",
                        },
                        "metrics_id": {
                            "type": "string",
                            "description": "The ID of the final metrics.",
                        },
                    },
                    "required": [],
                },
            },
        }


class CreateGmailJson(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Creates a Gmail-style JSON draft (not sending email). Useful for packaging
        evaluation results and deliverables into an email artifact.
        """
        to = kwargs.get("to", [])
        cc = kwargs.get("cc", [])
        bcc = kwargs.get("bcc", [])
        subject = kwargs.get("subject")
        body_text = kwargs.get("body_text", "")
        body_html_nullable = kwargs.get("body_html_nullable")
        attachments_paths = kwargs.get("attachments_paths", [])

        message_id = "GMAIL_MSG_001"
        json_path = f"/gmail/outbox/{message_id}.json"

        msg_entry = {
            "message_id": message_id,
            "to": to if isinstance(to, list) else [to],
            "cc": cc if isinstance(cc, list) else ([cc] if cc else []),
            "bcc": bcc if isinstance(bcc, list) else ([bcc] if bcc else []),
            "subject": subject,
            "body_text": body_text,
            "body_html_path_nullable": body_html_nullable,
            "attachments_paths": attachments_paths,
            "json_path": json_path,
            "status": "draft",
        }

        data.setdefault("gmail_outbox.json", []).append(msg_entry)
        return json.dumps({"message_id": message_id, "json_path": json_path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateGmailJson",
                "description": "Creates a Gmail-style JSON draft with recipients, subject, body, and attachments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "to": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Recipient emails",
                        },
                        "cc": {"type": "array", "items": {"type": "string"}},
                        "bcc": {"type": "array", "items": {"type": "string"}},
                        "subject": {"type": "string"},
                        "body_text": {"type": "string"},
                        "body_html_nullable": {
                            "type": "string",
                            "description": "Optional path to HTML body",
                        },
                        "attachments_paths": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "File paths to attach",
                        },
                    },
                    "required": ["to"],
                },
            },
        }


class CreateNotionPageJson(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Creates a Notion-style page JSON (metadata + block structure).
        Does NOT call Notion; only records a deterministic JSON artifact.
        """
        title = kwargs.get("title")
        if not title:
            return json.dumps({"error": "title is required"})

        page_id = "NOTION_PAGE_001"  # deterministic for evals
        slug = "_".join(title.lower().split())
        json_path = f"/notion/pages/{page_id}.json"

        page_entry = {
            "page_id": page_id,
            "title": title,
            "parent_database_id_nullable": kwargs.get("parent_database_id_nullable"),
            "parent_page_id_nullable": kwargs.get("parent_page_id_nullable"),
            "icon_emoji_nullable": kwargs.get("icon_emoji_nullable"),
            "cover_image_url_nullable": kwargs.get("cover_image_url_nullable"),
            "tags": kwargs.get("tags", []),
            "status_nullable": kwargs.get("status_nullable"),
            "properties": kwargs.get(
                "properties", {}
            ),  # e.g., {"Model":"SF_V1","AUC":0.87}
            "blocks": kwargs.get(
                "blocks", []
            ),  # e.g., [{"type":"heading_2","text":"Overview"}, ...]
            "attachments_paths": kwargs.get("attachments_paths", []),
            "json_path": json_path,
            "slug": slug,
        }

        data.setdefault("notion_pages.json", []).append(page_entry)
        return json.dumps({"page_id": page_id, "json_path": json_path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNotionPageJson",
                "description": "Creates a Notion-style page JSON (metadata + block structure + attachments).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "parent_database_id_nullable": {"type": "string"},
                        "parent_page_id_nullable": {"type": "string"},
                        "icon_emoji_nullable": {"type": "string"},
                        "cover_image_url_nullable": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "status_nullable": {"type": "string"},
                        "properties": {"type": "object"},
                        "blocks": {"type": "array", "items": {"type": "object"}},
                        "attachments_paths": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["title"],
                },
            },
        }


class EnrichNotion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        page_id = kwargs.get("page_id")
        model_id = kwargs.get("model_id")

        zotero_id = "ZOTERO_001"
        entry = {
            "page_id": page_id,
            "model_id": model_id,
            "zotero_id": zotero_id,
        }

        data.setdefault("zotero_metadata", []).append(entry)

        return json.dumps(entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnrichNotion",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "predictions_id": {
                            "type": "string",
                            "description": "The ID of the final predictions.",
                        },
                        "metrics_id": {
                            "type": "string",
                            "description": "The ID of the final metrics.",
                        },
                    },
                    "required": [],
                },
            },
        }


class AppendTerminalLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        msg = kwargs.get("message")
        log_type = kwargs.get("type")
        logs = data.setdefault("terminal_log", [])
        if log_type == "completed":
            entry = {"event_id": f"APPEND_002", "message": msg}
        else:
            entry = {"event_id": f"APPEND_001", "message": msg}
        logs.append(entry)
        return json.dumps(entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendTerminalLog",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }


class StartEtlRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        weather = kwargs.get("weather_raw_path")
        tides = kwargs.get("tides_raw_path")
        water = kwargs.get("water_levels_raw_path")
        city = kwargs.get("city_name")

        # deterministically produce processed path
        elt_id = "ETL_001"
        processed_path = f"/data/processed/timeseries_{elt_id}.csv"

        etl_entry = {
            "etl_run_id": elt_id,
            "inputs": {"weather": weather, "tides": tides, "water_levels": water},
            "status": "completed",
            "processed_path": processed_path,
        }
        data.setdefault("etl_runs", []).append(etl_entry)
        return json.dumps({"status": "completed", **etl_entry})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StartEtlRun",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_name": {"type": "string"},
                        "weather_raw_path": {"type": "string"},
                        "tides_raw_path": {"type": "string"},
                        "water_levels_raw_path": {"type": "string"},
                    },
                    "required": [
                        "city_name",
                        "weather_raw_path",
                        "tides_raw_path",
                        "water_levels_raw_path",
                    ],
                },
            },
        }


class RegisterProcessedTimeseries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        path = kwargs.get("processed_csv_path")
        entry = {"processed_csv_path": path}
        data.setdefault("processed_timeseries.json", []).append(entry)
        return json.dumps({**entry, "status": "completed"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterProcessedTimeseries",
                "parameters": {
                    "type": "object",
                    "properties": {"processed_csv_path": {"type": "string"}},
                    "required": ["processed_csv_path"],
                },
            },
        }


class CreateQCFigures(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        processed_csv_path = kwargs.get("processed_csv_path")
        figure_type = kwargs.get("figure_type", "overview")
        qc_fig_id = "QC_FIG_001"
        figures = {
            "qc_figure_id": qc_fig_id,
            "source": processed_csv_path,
            "figure_paths": [f"/figures/qc_{figure_type}.png", "/figures/qc_gaps.png"],
        }
        data.setdefault("qc_figures.json", []).append(figures)
        return json.dumps(figures)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateQCFigures",
                "parameters": {
                    "type": "object",
                    "properties": {"processed_csv_path": {"type": "string"}},
                    "required": ["processed_csv_path"],
                },
            },
        }


TOOLS = [
    SetProjectConfig(),
    SetGeocodeCity(),
    SetProjectDirectories(),
    FindNoaaStation(),
    SetWeatherForecast(),
    SetWaterLevels(),
    SetTidePredictions(),
    SetCoastalMeteorology(),
    CreateFeatures(),
    SetModelConfig(),
    CreateDatasetSplit(),
    TrainModel(),
    EvaluateModel(),
    PrepareStakeholderOutputs(),
    CreateModel(),
    GetModel(),
    CreateSummaryPlots(),
    CreateGmailJson(),
    CreateNotionPageJson(),
    EnrichNotion(),
    AppendTerminalLog(),
    StartEtlRun(),
    RegisterProcessedTimeseries(),
    CreateQCFigures(),
]
