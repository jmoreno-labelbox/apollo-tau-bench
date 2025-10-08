from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateCandidateEmailPointers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, message_field: str = None, message_id: str = None) -> str:
        rows = _ensure_list(data, "candidates")
        row = _find_by_key(rows, "candidate_id", candidate_id)
        if row:
            row[message_field] = message_id
            row.setdefault("updated_ts", NOW_TS)
            payload = {
                "candidate_id": candidate_id,
                "field": message_field,
                "value": message_id,
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {
            "candidate_id": candidate_id,
            "field": message_field,
            "value": message_id,
            "updated": False,
            "reason": "not_found",
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateCandidateEmailPointers",
                "description": "Set a candidate message pointer field to a message_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "message_field": {"type": "string"},
                        "message_id": {"type": "string"},
                    },
                    "required": ["candidate_id", "message_field", "message_id"],
                },
            },
        }
