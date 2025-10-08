from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class RecordAccessChecks(Tool):
    @staticmethod
    def invoke(data, candidate_id: str, checks: list = None) -> str:
        checks = checks or []
        rows = data.setdefault("access_checks", [])
        ids = []
        for i, chk in enumerate(checks):
            payload = {
                "access_check_id": _next_seq(rows, "access_check_id", "acc"),
                "candidate_id": candidate_id,
                "system_name": chk["system_name"],
                "status": chk["status"],
                "note_nullable": chk.get("note"),
                "checked_ts": _fixed_ts(chk.get("checked_ts")),
            }
            rows.append(payload)
            ids.append(payload["access_check_id"])
        payload = {"inserted": len(ids), "access_check_ids": ids}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordAccessChecks",
                "description": "Bulk insert access checks for candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "checks": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "system_name": {"type": "string"},
                                    "status": {"type": "string"},
                                    "note": {"type": "string"},
                                    "checked_ts": {"type": "string"},
                                },
                                "required": ["system_name", "status"],
                            },
                        },
                    },
                    "required": ["candidate_id", "checks"],
                },
            },
        }
