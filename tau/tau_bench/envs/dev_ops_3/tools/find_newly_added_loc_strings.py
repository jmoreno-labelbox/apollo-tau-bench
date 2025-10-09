from tau_bench.envs.tool import Tool
import json
from typing import Any

class find_newly_added_loc_strings(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str, hours_ago: int) -> str:
        pass
        from datetime import datetime, timedelta

        loc_strings = data.get("loc_strings", [])
        now = datetime.fromisoformat(FIXED_TIMESTAMP.replace("Z", "+00:00"))
        time_threshold = now - timedelta(hours=hours_ago)

        new_strings = []
        for s in loc_strings:
            if s.get("project_id") == project_id:
                try:
                    created_at_dt = datetime.fromisoformat(
                        s["created_at"].replace("Z", "+00:00")
                    )
                    if created_at_dt >= time_threshold:
                        new_strings.append(s)
                except (ValueError, TypeError, KeyError):
                    continue
        payload = {"count": len(new_strings), "results": new_strings}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findNewlyAddedLocStrings",
                "description": "Finds all localization strings for a given project that were created within a specified time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "hours_ago": {"type": "integer"},
                    },
                    "required": ["project_id", "hours_ago"],
                },
            },
        }
