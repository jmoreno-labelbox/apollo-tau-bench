# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _ensure_list(d: Dict[str, Any], key: str) -> List[Any]:
    if key not in d or not isinstance(d[key], list):
        d[key] = []
    return d[key]

class InsertAccessCheck(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, note_nullable, status, system_name, checked_ts = NOW_TS) -> str:
        rows = _ensure_list(data, "access_checks")
        payload = {"candidate_id": candidate_id, "system_name": system_name,
                   "status": status, "note_nullable": note_nullable,
                   "checked_ts": checked_ts}
        rows.append(payload)
        return json.dumps({"inserted": payload}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "insert_access_check", "description": "Append a pass/fail access check.",
                             "parameters": {"type": "object", "properties": {"candidate_id": {"type": "string"},
                                                                             "system_name": {"type": "string"},
                                                                             "status": {"type": "string"},
                                                                             "note_nullable": {"type": "string"}},
                                            "required": ["candidate_id", "system_name", "status"]}}}