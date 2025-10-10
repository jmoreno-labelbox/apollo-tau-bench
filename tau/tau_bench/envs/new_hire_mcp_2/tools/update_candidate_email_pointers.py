# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCandidateEmailPointers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, message_field, message_id) -> str:
        rows = _ensure_list(data, "candidates")
        row = _find_by_key(rows, "candidate_id", candidate_id)
        if row:
            row[message_field] = message_id
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"candidate_id": candidate_id, "field": message_field, "value": message_id}, indent=2)
        return json.dumps({"candidate_id": candidate_id, "field": message_field, "value": message_id, "updated": False,
                           "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_candidate_email_pointers",
                                                 "description": "Set a candidate message pointer field to a message_id.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"candidate_id": {"type": "string"},
                                                                               "message_field": {"type": "string"},
                                                                               "message_id": {"type": "string"}},
                                                                "required": ["candidate_id", "message_field",
                                                                             "message_id"]}}}
