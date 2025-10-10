# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertAccessCheck(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = _ensure_list(data, "access_checks")
        payload = {"candidate_id": kwargs.get("candidate_id"), "system_name": kwargs.get("system_name"),
                   "status": kwargs.get("status"), "note_nullable": kwargs.get("note_nullable"),
                   "checked_ts": kwargs.get("checked_ts", NOW_TS)}
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
