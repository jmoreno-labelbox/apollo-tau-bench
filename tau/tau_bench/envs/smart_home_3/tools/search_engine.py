from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchEngine(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], search_term: str = "", search_type: str = "all") -> str:
        search_term = search_term.lower()

        if not search_term:
            payload = {"error": "search_term required"}
            out = json.dumps(payload, indent=2)
            return out

        results = {}

        if search_type in ["all", "devices"]:
            devices = data.get("devices", {}).values()
            results["devices"] = [d for d in devices.values() if search_term in str(d).lower()]

        if search_type in ["all", "scenes"]:
            scenes = data.get("scenes", {}).values()
            results["scenes"] = [s for s in scenes.values() if search_term in str(s).lower()]

        if search_type in ["all", "lists"]:
            lists = data.get("custom_lists", {}).values()
            results["lists"] = [l for l in lists.values() if search_term in str(l).lower()]

        if search_type in ["all", "reminders"]:
            reminders = data.get("reminders", {}).values()
            results["reminders"] = [
                r for r in reminders.values() if search_term in str(r).lower()
            ]

        if search_type in ["all", "members"]:
            members = data.get("members", {}).values()
            results["members"] = [m for m in members.values() if search_term in str(m).lower()]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchEngine",
                "description": "Search across all smart home entities",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "search_term": {
                            "type": "string",
                            "description": "Term to search for",
                        },
                        "search_type": {
                            "type": "string",
                            "enum": [
                                "all",
                                "devices",
                                "scenes",
                                "lists",
                                "reminders",
                                "members",
                            ],
                            "description": "Type of entities to search",
                        },
                    },
                    "required": ["search_term"],
                    "additionalProperties": False,
                },
            },
        }
