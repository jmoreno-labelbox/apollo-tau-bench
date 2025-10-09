from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateDataArchiveEntry(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, system: str = None, 
               retention_label: str = None, location_uri: str = None) -> str:
        archives = data.setdefault("data_archives", [])
        archive_id = _get_next_id(archives, "archive_id", "arch")
        new_archive = {
            "archive_id": archive_id,
            "employee_id": employee_id,
            "system": system,
            "location_uri": location_uri,
            "retention_label": retention_label,
            "created_at": FIXED_NOW,
        }
        data["archives"][archive_id] = new_archive
        payload = new_archive
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createDataArchiveEntry",
                "description": "Creates an entry in the data archives table, typically after a mailbox export.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "system": {"type": "string"},
                        "retention_label": {"type": "string"},
                        "location_uri": {"type": "string"},
                    },
                    "required": [
                        "employee_id",
                        "system",
                        "retention_label",
                        "location_uri",
                    ],
                },
            },
        }
