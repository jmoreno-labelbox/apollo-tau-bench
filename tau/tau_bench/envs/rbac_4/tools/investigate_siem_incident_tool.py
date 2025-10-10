# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InvestigateSiemIncidentTool(Tool):
    """Record an investigation result for a SIEM alert."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("alert_id")
        analyst = kwargs.get("analyst_id")
        notes = kwargs.get("notes")
        investigated_on = kwargs.get("investigated_on")

        investigations = data.get("siem_investigations", [])
        new_id = f"INV-{len(investigations) + 1:03d}"
        investigations.append({
            "investigation_id": new_id,
            "alert_id": aid,
            "analyst_id": analyst,
            "notes": notes,
            "investigated_on": investigated_on
        })
        return json.dumps({"success": f"Investigation {new_id} recorded"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "investigate_siem_incident",
                "description": "Create a record of SIEM incident investigation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {"type": "string"},
                        "analyst_id": {"type": "string"},
                        "notes": {"type": "string"},
                        "investigated_on": {"type": "string"}
                    },
                    "required": ["alert_id", "analyst_id", "notes", "investigated_on"]
                }
            }
        }
