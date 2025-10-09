from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class StatusMonitor(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], report_type: str = "summary", category: str = None) -> str:
        status = {}

        if report_type == "summary" or not category:
            status["devices"] = {
                "total": len(data.get("devices", [])),
                "by_type": {},
                "by_location": {},
                "powered_on": 0,
            }

            for device in data.get("devices", []):
                device_type = device.get("type", "unknown")
                location = device.get("location", "unknown")
                status["devices"]["by_type"][device_type] = (
                    status["devices"]["by_type"].get(device_type, 0) + 1
                )
                status["devices"]["by_location"][location] = (
                    status["devices"]["by_location"].get(location, 0) + 1
                )
                if device.get("state", {}).get("power") == "on":
                    status["devices"]["powered_on"] += 1

            status["scenes"] = {"total": len(data.get("scenes", []))}
            status["lists"] = {"total": len(data.get("custom_lists", []))}
            status["reminders"] = {
                "total": len(data.get("reminders", [])),
                "active": len(
                    [
                        r
                        for r in data.get("reminders", [])
                        if r.get("status") == "active"
                    ]
                ),
            }
            status["members"] = {
                "total": len(data.get("members", [])),
                "residents": len(
                    [
                        m
                        for m in data.get("members", [])
                        if m.get("residence", {}).get("lives_in_house")
                    ]
                ),
            }

        if category == "devices" or report_type == "detailed":
            devices = data.get("devices", [])
            status["device_details"] = [
                {
                    "id": d["id"],
                    "type": d["type"],
                    "location": d["location"],
                    "power": d.get("state", {}).get("power", "unknown"),
                    "last_updated": d.get("state", {}).get("last_updated"),
                }
                for d in devices
            ]
        payload = status
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StatusMonitor",
                "description": "Get system status and analytics",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_type": {
                            "type": "string",
                            "enum": ["summary", "detailed"],
                            "description": "Type of report",
                        },
                        "category": {
                            "type": "string",
                            "enum": [
                                "devices",
                                "scenes",
                                "lists",
                                "reminders",
                                "members",
                            ],
                            "description": "Focus on specific category",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
