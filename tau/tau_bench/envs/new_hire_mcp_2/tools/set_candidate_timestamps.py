# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetCandidateTimestamps(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        fields = kwargs.get("fields", {})
        rows = _ensure_list(data, "candidates")
        row = _find_by_key(rows, "candidate_id", candidate_id)
        if row:
            for k, v in fields.items():
                row[k] = v if v is not None else NOW_TS
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"candidate_id": candidate_id, "updated": True, "fields": fields}, indent=2)
        return json.dumps({"candidate_id": candidate_id, "updated": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_candidate_timestamps",
                                                 "description": "Set timestamp fields on candidate to provided values or NOW_TS.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"candidate_id": {"type": "string"},
                                                                               "fields": {"type": "object"}},
                                                                "required": ["candidate_id", "fields"]}}}
