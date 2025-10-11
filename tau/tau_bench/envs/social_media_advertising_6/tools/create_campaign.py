# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCampaign(Tool):
    """Create a campaign with explicit created_date and status."""

    @staticmethod
    def invoke(data: Dict[str, Any], created_date, name, objective, status) -> str:
        err = _require(kwargs, ["name", "objective", "created_date", "status"])
        if err: return _fail(err)
        rows = _assert_table(data, "campaigns")
        if any(r.get("name") == name for r in rows):
            return _fail("name_exists")
        new_id = _next_numeric_id(rows, "campaign_id")
        rec = {"campaign_id": new_id, "name": name, "objective": objective,
               "created_date": created_date, "status": status}
        rows.append(rec)
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_campaign",
                                                 "description": "Create a campaign (deterministic; explicit created_date).",
                                                 "parameters": {"type": "object",
                                                                "properties": {"name": {"type": "string"},
                                                                               "objective": {"type": "string"},
                                                                               "created_date": {"type": "string"},
                                                                               "status": {"type": "string"}},
                                                                "required": ["name", "objective", "created_date",
                                                                             "status"]}}}
