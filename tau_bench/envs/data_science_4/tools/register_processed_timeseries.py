from tau_bench.envs.tool import Tool
import json
from typing import Any

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
