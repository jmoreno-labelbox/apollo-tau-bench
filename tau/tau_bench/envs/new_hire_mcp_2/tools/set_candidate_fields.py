from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetCandidateFields(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, fields: dict = None) -> str:
        if fields is None:
            fields = {}
        rows = _ensure_list(data, "candidates")
        row = _find_by_key(rows, "candidate_id", candidate_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            row.setdefault("updated_ts", NOW_TS)
            payload = {"candidate_id": candidate_id, "updated": True, "fields": fields}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"candidate_id": candidate_id, "updated": False, "reason": "not_found"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetCandidateFields",
                "description": "Update fields on an existing candidate. No-op if not found.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "fields": {"type": "object"},
                    },
                    "required": ["candidate_id", "fields"],
                },
            },
        }
