from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class InvestigateSiemIncidentTool(Tool):
    """Document the outcome of an investigation for a SIEM alert."""

    @staticmethod
    def invoke(data: dict[str, Any], alert_id: str = None, analyst_id: str = None, notes: str = None, investigated_on: str = None, created_on: Any = None) -> str:
        investigations = data.get("siem_investigations", {}).values()
        new_id = f"INV-{len(investigations) + 1:03d}"
        investigations.append(
            {
                "investigation_id": new_id,
                "alert_id": alert_id,
                "analyst_id": analyst_id,
                "notes": notes,
                "investigated_on": investigated_on,
            }
        )
        payload = {"success": f"Investigation {new_id} recorded"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InvestigateSiemIncident",
                "description": "Create a record of SIEM incident investigation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {"type": "string"},
                        "analyst_id": {"type": "string"},
                        "notes": {"type": "string"},
                        "investigated_on": {"type": "string"},
                    },
                    "required": ["alert_id", "analyst_id", "notes", "investigated_on"],
                },
            },
        }
