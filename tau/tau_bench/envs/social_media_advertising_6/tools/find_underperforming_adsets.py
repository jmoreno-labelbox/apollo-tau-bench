# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool










def _require(kwargs: Dict[str, Any], names: List[str]) -> Optional[str]:
    for n in names:
        if n not in kwargs:
            return f"missing_arg:{n}"
    return None

def _index(rows: List[Dict[str, Any]], key: str) -> Dict[str, Dict[str, Any]]:
    return {str(r.get(key)): r for r in rows}

def _fail(msg: str) -> str:
    return json.dumps({"error": msg})

def _assert_table(data: Dict[str, Any], key: str) -> List[Dict[str, Any]]:
    if key not in data:
        raise ValueError(f"missing_table:{key}")
    tbl = data[key]
    if not isinstance(tbl, list):
        raise ValueError(f"invalid_table:{key}")
    return tbl

class FindUnderperformingAdsets(Tool):
    """Find adsets below a ROAS threshold for a given day (joins f_insights with adsets)."""

    @staticmethod
    def invoke(data: Dict[str, Any], date, min_roas) -> str:
        req = ["date", "min_roas"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        ins = _assert_table(data, "f_insights")
        adsets = _index(_assert_table(data, "adsets"), "adset_id")
        th = float(min_roas)
        out = []
        for r in ins:
            if r.get("date") != date:
                continue
            aid = str(r.get("adset_id"))
            spend = float(r.get("spend", 0.0));
            rev = float(r.get("revenue", 0.0))
            roas = (rev / spend) if spend > 0 else 0.0
            if roas < th:
                a = adsets.get(aid, {})
                out.append({"adset_id": aid, "roas": roas, "spend": spend, "revenue": rev, "status": a.get("status")})
        return json.dumps(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_underperforming_adsets",
                                                 "description": "Find adsets with ROAS below threshold on a date.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"date": {"type": "string"},
                                                                               "min_roas": {"type": "number"}},
                                                                "required": ["date", "min_roas"]}}}