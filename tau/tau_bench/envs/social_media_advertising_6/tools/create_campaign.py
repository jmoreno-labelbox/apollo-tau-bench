# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool










def _require(kwargs: Dict[str, Any], names: List[str]) -> Optional[str]:
    for n in names:
        if n not in kwargs:
            return f"missing_arg:{n}"
    return None

def _next_numeric_id(rows: List[Dict[str, Any]], key: str) -> str:
    mx = 0
    for r in rows:
        v = str(r.get(key))
        if v.isdigit():
            mx = max(mx, int(v))
    return str(mx + 1)

def _fail(msg: str) -> str:
    return json.dumps({"error": msg})

def _assert_table(data: Dict[str, Any], key: str) -> List[Dict[str, Any]]:
    if key not in data:
        raise ValueError(f"missing_table:{key}")
    tbl = data[key]
    if not isinstance(tbl, list):
        raise ValueError(f"invalid_table:{key}")
    return tbl

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