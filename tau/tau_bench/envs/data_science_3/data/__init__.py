import json
import os
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> dict[str, Any]:
    db: dict[str, Any] = {}
    # auto-generated from files present in data/
    tables = ['coastal_meteorology', 'dataset_split', 'environment', 'etl_runs', 'features', 'file_directory', 'file_store', 'geocoding_results', 'gmail_messages', 'mcp_tool_calls', 'metrics', 'model_config', 'models', 'noaa_station_searches', 'notion_pages', 'predictions', 'processed_timeseries', 'project_config', 'qc_figures', 'stakeholder_outputs', 'terminal_log', 'tide_predictions', 'water_levels', 'weather_forecasts', 'zotero_fulltexts', 'zotero_metadata', 'zotero_searches']
    for name in tables:
        path = os.path.join(FOLDER_PATH, f"{name}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                db[name] = json.loads(content) if content else []
        except FileNotFoundError:
            db[name] = []
    return db

