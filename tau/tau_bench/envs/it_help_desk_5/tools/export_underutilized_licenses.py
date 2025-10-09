from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ExportUnderutilizedLicenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], output_data: Any = None) -> str:
        csv_data = output_data
        if csv_data is None:
            payload = {"status": "error", "description": "The data field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        csv_path = "reports/underutilized_licenses.csv"
        payload = {"path": csv_path, "licenses": csv_data}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "exportUnderutilizedLicenses",
                "description": "Exports a CSV underutilized licenses",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "output_data": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "The data to be written to a CSV.",
                        },
                    },
                    "required": ["output_data"],
                },
            },
        }
