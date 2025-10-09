from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSiemAlertDetailsTool(Tool):
    """Get information about a SIEM alert."""

    @staticmethod
    def invoke(data: dict[str, Any], alert_id: str, severity_in: Any = None) -> str:
        aid = alert_id
        for a in data.get("siem_alerts", {}).values():
            if a["alert_id"] == aid:
                payload = a
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"SIEM alert {aid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSiemAlertDetails",
                "description": "Get detailed information for a specific SIEM alert",
                "parameters": {
                    "type": "object",
                    "properties": {"alert_id": {"type": "string"}},
                    "required": ["alert_id"],
                },
            },
        }
