import json
from pathlib import Path
from typing import List, Dict, Any
import copy

from domains.base import BaseDomain
from domains.dto import Tool


class DataScienceSystem(BaseDomain):
    def __init__(self, tools: List[Tool]):
        super().__init__(tools)
        self.master_database = self._load_data()
        self.database = copy.deepcopy(self.master_database)

    def reset_database(self):
        self.database = copy.deepcopy(self.master_database)
        return True

    def _load_data(self) -> Dict[str, Any]:
        db = {}
        data_path = Path(__file__).parent / "data"

        table_files = [
            "coastal_meteorology",
            "dataset_split",
            "environment",
            "etl_runs",
            "features",
            "file_directory",
            "file_store",
            "geocoding_results",
            "gmail_messages",
            "mcp_tool_calls",
            "metrics",
            "model_config",
            "models",
            "noaa_station_searches",
            "notion_pages",
            "predictions",
            "processed_timeseries",
            "project_config",
            "qc_figures",
            "stakeholder_outputs",
            "terminal_log",
            "tide_predictions",
            "water_levels",
            "weather_forecasts",
            "zotero_fulltexts",
            "zotero_metadata",
            "zotero_searches",
        ]

        for table_name in table_files:
            file_path = data_path / f"{table_name}.json"
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if content:
                        db[table_name] = json.loads(content)
                    else:
                        db[table_name] = []
            except FileNotFoundError:
                raise FileNotFoundError(f"Core data file not found: {file_path}")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from {file_path}: {e}")
                db[table_name] = []

        return db
