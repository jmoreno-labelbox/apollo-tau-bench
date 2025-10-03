import json
from typing import Any

from tau_bench.envs.tool import Tool

LAT = 55
LONG = 55


class SetProjectConfig(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], target_city: str = None, forecast_horizon_days: int = None, max_station_distance_km_nullable: float = None) -> str:
        target_city = target_city
        horizon = forecast_horizon_days
        max_radius = max_station_distance_km_nullable
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
        payload = {"config_id": "CONFIG_001", **config}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setProjectConfig",
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
    def invoke(data: dict[str, Any], city_name: str) -> str:
        results = data.get("geocoding_results", [])
        for result in results:
            if result.get("query_city") == city_name:
                payload = result
                out = json.dumps(payload)
                return out
        json_city_path = "_".join(city_name.split()).lower()
        result = {
            "geo_id": "GEO_001",
            "query_city": city_name,
            "latitude": LAT,
            "longitude": LONG,
            "raw_json_path_nullable": f"/data/raw/geocoding_{json_city_path}.json",
        }
        data.get("geocoding_results", []).append(result)
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setGeocodeCity",
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
    def invoke(data: dict[str, Any], files: list = None) -> str:
        pass
        # This is a mockup; in an actual setting, this would engage with a file system.
        files = files or []
        project_dir_id = "PROJ_DIR_001"
        file_dir = {
            "paths": files,
            "project_dir_id": project_dir_id,
        }
        data.get("file_directory", []).append(file_dir)
        payload = {"status": "success", "project_dir_id": project_dir_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setProjectDirectories",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class FindNoaaStation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], latitude: float = None, longitude: float = None) -> str:
        station_id = "NOAA_STATION_001"
        noaa_station_json = {
            "station_ids": station_id,
            "raw_json_path_nullable": f"/data/raw/noaa_station_{station_id}.json",
        }
        data.get("noaa_station_searches", []).append(noaa_station_json)
        payload = noaa_station_json
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findNoaaStation",
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
    def invoke(
        data: dict[str, Any],
        city: str = None,
        city_name: str = None,
        latitude: Any = None
    ) -> str:
        # Accept either city or city_name
        if city_name is not None:
            city = city_name
        id = "WEATHER_FORECAST_001"
        weather_forecast_json = {
            "forecast_id": id,
            "raw_json_path_nullable": f"/data/raw/weather_forecast_{id}.json",
        }
        data.get("weather_forecasts", []).append(weather_forecast_json)
        payload = weather_forecast_json
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setWeatherForecast",
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
    def invoke(data: dict[str, Any], station_id: str = None) -> str:
        pass
        # This is a mockup; in an actual setting, this would retrieve data from NOAA.

        water_level_data = {
            "station_id": station_id,
            "data_points": [
                {"timestamp": "2023-10-01T00:00:00Z", "water_level_meters": 1.2},
                {"timestamp": "2023-10-01T01:00:00Z", "water_level_meters": 1.3},
            ],
            "raw_json_path_nullable": f"/data/raw/water_levels_{station_id}.json",
        }
        data.get("water_level_data", []).append(water_level_data)
        payload = water_level_data
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setWaterLevels",
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
    def invoke(data: dict[str, Any], station_id: str = None) -> str:
        # This is a mockup; in an actual setting, this would retrieve data from NOAA.

        tide_prediction_data = {
            "station_id": station_id,
            "predictions": [
                {"timestamp": "2023-10-01T00:00:00Z", "predicted_tide_meters": 1.5},
                {"timestamp": "2023-10-01T01:00:00Z", "predicted_tide_meters": 1.6},
            ],
            "raw_json_path_nullable": f"/data/raw/tide_predictions_{station_id}.json",
        }
        data.get("tide_predictions", []).append(tide_prediction_data)
        payload = tide_prediction_data
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setTidePredictions",
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
    def invoke(data: dict[str, Any], station_id: str = None) -> str:
        # This is a mockup; in an actual setting, this would retrieve data from NOAA.

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
        payload = coastal_meteorology_data
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setCoastalMeteorology",
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
    def invoke(data: dict[str, Any], input_csv_path: str = None) -> str:
        if not input_csv_path:
            payload = {"error": "input_csv_path is a required argument."}
            out = json.dumps(payload)
            return out

        features_id = "FEATURES_001"
        new_features_path = "/processed_data/features_001.csv"

        feature_entry = {
            "features_id": features_id,
            "source_csv_path": input_csv_path,
            "features_csv_path": new_features_path,
            "feature_names": [
                "precip_24h_mm",
                "tide_anomaly_6h_max_m",
                "pressure_drop_6h_hpa",
            ],
        }

        data.setdefault("features", []).append(feature_entry)
        payload = feature_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createFeatures",
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
    def invoke(
        data: dict[str, Any], 
        classification_threshold_m: float = None, 
        precip_24h_threshold_mm: float = None, 
        test_split_fraction: float = None
    ) -> str:
        config_id = "MODEL_CONFIG_001"

        config_entry = {
            "config_id": config_id,
            "classification_threshold_m": classification_threshold_m,
            "precip_24h_threshold_mm": precip_24h_threshold_mm,
            "test_split_fraction": test_split_fraction,
            "config_json_path": f"/configs/model_config_{config_id}.json",
        }

        data.setdefault("model_config", []).append(config_entry)
        payload = config_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setModelConfig",
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
    def invoke(data: dict[str, Any], model_config_id: str = None, model_name: str = None, model_type: str = None, features_id: list[str] = None) -> str:
        model_id = f"MODEL_{model_name}"
        model_entry = {
            "model_id": model_id,
            "model_name": model_name,
            "config_id": model_config_id,
            "model_path": f"/models/{model_id}.joblib",
            "model_type": model_type,
            "feature_names": features_id,
            "train_metrics_json_path_nullable": f"/metrics/{model_id}_train_metrics.json",
        }
        data.setdefault("models", []).append(model_entry)
        payload = model_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createModel",
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
    def invoke(data: dict[str, Any], model_name: str = None, model_type: str = None, features_id: list[str] = None) -> str:
        model_id = f"MODEL_{model_name}"

        model_entry = {
            "model_id": model_id,
            "model_name": model_name,
            "model_path": f"/models/{model_id}.joblib",
            "model_type": model_type,
            "feature_names": features_id,
            "train_metrics_json_path_nullable": f"/metrics/{model_id}_train_metrics.json",
        }
        data.setdefault("models", []).append(model_entry)
        payload = model_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getModel",
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
    def invoke(data: dict[str, Any], features_id: str = None, test_fraction: float = None) -> str:
        split_id = "SPLIT_001"

        split_entry = {
            "split_id": split_id,
            "features_id": features_id,
            "method": "time_based",
            "test_fraction": test_fraction,
            "split_summary_json_path": f"/processed_data/split_summary_{split_id}.json",
        }

        data.setdefault("dataset_split.json", []).append(split_entry)
        payload = split_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createDatasetSplit",
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
    def invoke(
        data: dict[str, Any], 
        model_name: str = None, 
        model_type: str = None, 
        features_id: str = None, 
        config_id: str = None, 
        split_id: str = None
    ) -> str:
        model_id = f"MODEL_{model_name}"
        predictions_id = "PRED_001"

        model_entry = {
            "model_id": model_id,
            "model_name": model_name,
            "model_type": model_type,
            "features_id": features_id,
            "config_id": config_id,
            "split_id": split_id,
            "model_path": f"/models/{model_id}.joblib",
        }

        predictions_entry = {
            "predictions_id": predictions_id,
            "model_id": model_id,
            "predictions_csv_path": f"/predictions/PRED_{model_id}.csv",
        }

        data.setdefault("models.json", []).append(model_entry)
        data.setdefault("predictions.json", []).append(predictions_entry)
        payload = predictions_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "trainModel",
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
    def invoke(data: dict[str, Any], model_id: str = None, predictions_id: str = None) -> str:
        metrics_id = "METRICS_001"
        if not predictions_id:
            predictions_id = "PRED_001"
        metrics_entry = {
            "model_id": model_id,
            "metrics_id": metrics_id,
            "predictions_id": predictions_id,
            "auc": 0.87,
            "accuracy": 0.91,
            "metrics_json_path": f"/metrics/metrics_{metrics_id}.json",
        }

        data.setdefault("metrics.json", []).append(metrics_entry)
        payload = metrics_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "evaluateModel",
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
    def invoke(data: dict[str, Any], predictions_id: str = None, metrics_id: str = None) -> str:
        pass
        output_id = "STAKEHOLDER_OUTPUT_001"

        # In a genuine situation, this would transfer files to a designated 'deliverables' location.
        # At this point, we simply generate the record.
        output_entry = {
            "stakeholder_output_id": output_id,
            "final_predictions_id": predictions_id,
            "final_metrics_id": metrics_id,
            "status": "ready",
            "predictions_csv_path": f"/deliverables/final_predictions_{output_id}.csv",
            "metrics_json_path": f"/deliverables/final_metrics_{output_id}.json",
        }

        data.setdefault("stakeholder_outputs.json", []).append(output_entry)
        payload = output_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "prepareStakeholderOutputs",
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
    def invoke(data: dict[str, Any], predictions_id: str = None, model_id: str = None) -> str:
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
        payload = qc_figure_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createSummaryPlots",
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
    def invoke(
        data: dict[str, Any],
        to: list[str] = None,
        cc: list[str] = None,
        bcc: list[str] = None,
        subject: str = None,
        body_text: str = "",
        body: str = None,
        body_html_nullable: str = None,
        attachments_paths: list[str] = None
    ) -> str:
        # Accept either body or body_text
        if body is not None:
            body_text = body
        """Generates a Gmail-like JSON draft (without sending email). Helpful for compiling evaluation results and deliverables into an email artifact."""
        to = to if to is not None else []
        cc = cc if cc is not None else []
        bcc = bcc if bcc is not None else []
        attachments_paths = attachments_paths if attachments_paths is not None else []

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
        payload = {"message_id": message_id, "json_path": json_path}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createGmailJson",
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
    def invoke(
        data: dict[str, Any],
        title: str = None,
        parent_database_id_nullable: str = None,
        parent_page_id_nullable: str = None,
        icon_emoji_nullable: str = None,
        cover_image_url_nullable: str = None,
        tags: list = None,
        status_nullable: str = None,
        properties: dict = None,
        blocks: list = None,
        attachments_paths: list = None
    ) -> str:
        """Generates a Notion-like page JSON (including metadata and block structure). Does NOT interact with Notion; solely documents a consistent JSON artifact."""
        if not title:
            payload = {"error": "title is required"}
            out = json.dumps(payload)
            return out

        page_id = "NOTION_PAGE_001"  # consistent for evaluations
        slug = "_".join(title.lower().split())
        json_path = f"/notion/pages/{page_id}.json"

        page_entry = {
            "page_id": page_id,
            "title": title,
            "parent_database_id_nullable": parent_database_id_nullable,
            "parent_page_id_nullable": parent_page_id_nullable,
            "icon_emoji_nullable": icon_emoji_nullable,
            "cover_image_url_nullable": cover_image_url_nullable,
            "tags": tags or [],
            "status_nullable": status_nullable,
            "properties": properties or {},  # for example, {"Model":"SF_V1","AUC":0.87}
            "blocks": blocks or [],  # for instance, [{"type":"heading_2","text":"Overview"}, ...]
            "attachments_paths": attachments_paths or [],
            "json_path": json_path,
            "slug": slug,
        }

        data.setdefault("notion_pages.json", []).append(page_entry)
        payload = {"page_id": page_id, "json_path": json_path}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createNotionPageJson",
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
    def invoke(data: dict[str, Any], page_id: str = None, model_id: str = None) -> str:
        zotero_id = "ZOTERO_001"
        entry = {
            "page_id": page_id,
            "model_id": model_id,
            "zotero_id": zotero_id,
        }

        data.setdefault("zotero_metadata", []).append(entry)
        payload = entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "enrichNotion",
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
    def invoke(
        data: dict[str, Any],
        log_type: str = None,
        message: str = None,
        type: Any = None
    ) -> str:
        logs = data.setdefault("terminal_log", [])
        if log_type == "completed":
            entry = {"event_id": "APPEND_002", "message": message}
        else:
            entry = {"event_id": "APPEND_001", "message": message}
        logs.append(entry)
        payload = entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "appendTerminalLog",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }


class StartEtlRun(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], weather_raw_path: str = None, tides_raw_path: str = None, water_levels_raw_path: str = None, city_name: str = None) -> str:
        pass
        weather = weather_raw_path
        tides = tides_raw_path
        water = water_levels_raw_path
        city_name  # This line seems to be unused, but kept for consistency

        #consistently generate processed path
        elt_id = "ETL_001"
        processed_path = f"/data/processed/timeseries_{elt_id}.csv"

        etl_entry = {
            "etl_run_id": elt_id,
            "inputs": {"weather": weather, "tides": tides, "water_levels": water},
            "status": "completed",
            "processed_path": processed_path,
        }
        data.setdefault("etl_runs", []).append(etl_entry)
        payload = {"status": "completed", **etl_entry}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "startEtlRun",
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
    def invoke(data: dict[str, Any], processed_csv_path: str = None) -> str:
        entry = {"processed_csv_path": processed_csv_path}
        data.setdefault("processed_timeseries.json", []).append(entry)
        payload = {**entry, "status": "completed"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "registerProcessedTimeseries",
                "parameters": {
                    "type": "object",
                    "properties": {"processed_csv_path": {"type": "string"}},
                    "required": ["processed_csv_path"],
                },
            },
        }


class CreateQCFigures(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        figure_type: str = "overview",
        processed_csv_path: str = None
    ) -> str:
        qc_fig_id = "QC_FIG_001"
        figures = {
            "qc_figure_id": qc_fig_id,
            "source": processed_csv_path,
            "figure_paths": [f"/figures/qc_{figure_type}.png", "/figures/qc_gaps.png"],
        }
        data.setdefault("qc_figures.json", []).append(figures)
        payload = figures
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createQcfigures",
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
