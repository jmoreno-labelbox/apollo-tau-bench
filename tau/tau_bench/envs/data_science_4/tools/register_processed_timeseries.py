# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RegisterProcessedTimeseries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], processed_csv_path) -> str:
        path = processed_csv_path
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
