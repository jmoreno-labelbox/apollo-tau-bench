from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class CreateCampaign(Tool):
    """Generate a campaign with specified created_date and status."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str, objective: str, created_date: str, status: str) -> str:
        err = _require({"name": name, "objective": objective, "created_date": created_date, "status": status}, ["name", "objective", "created_date", "status"])
        if err:
            return _fail(err)
        rows = _assert_table(data, "campaigns")
        if any(r.get("name") == name for r in rows):
            return _fail("name_exists")
        new_id = _next_numeric_id(rows, "campaign_id")
        rec = {
            "campaign_id": new_id,
            "name": name,
            "objective": objective,
            "created_date": created_date,
            "status": status,
        }
        rows.append(rec)
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createCampaign",
                "description": "Create a campaign (deterministic; explicit created_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "objective": {"type": "string"},
                        "created_date": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["name", "objective", "created_date", "status"],
                },
            },
        }
