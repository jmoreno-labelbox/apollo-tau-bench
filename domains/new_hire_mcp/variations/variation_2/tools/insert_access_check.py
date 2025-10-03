from tau_bench.envs.tool import Tool
import json
from typing import Any

class InsertAccessCheck(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, system_name: str = None, status: str = None, note_nullable: str = None, checked_ts: str = NOW_TS) -> str:
        rows = _ensure_list(data, "access_checks")
        payload = {
            "candidate_id": candidate_id,
            "system_name": system_name,
            "status": status,
            "note_nullable": note_nullable,
            "checked_ts": checked_ts,
        }
        rows.append(payload)
        payload = {"inserted": payload}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertAccessCheck",
                "description": "Append a pass/fail access check.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "system_name": {"type": "string"},
                        "status": {"type": "string"},
                        "note_nullable": {"type": "string"},
                    },
                    "required": ["candidate_id", "system_name", "status"],
                },
            },
        }
