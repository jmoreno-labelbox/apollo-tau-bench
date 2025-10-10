# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetCandidateFields(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        fields = kwargs.get("fields", {})
        rows = _ensure_list(data, "candidates")
        row = _find_by_key(rows, "candidate_id", candidate_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"candidate_id": candidate_id, "updated": True, "fields": fields}, indent=2)
        return json.dumps({"candidate_id": candidate_id, "updated": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_candidate_fields",
                                                 "description": "Update fields on an existing candidate. No-op if not found.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"candidate_id": {"type": "string"},
                                                                               "fields": {"type": "object"}},
                                                                "required": ["candidate_id", "fields"]}}}
