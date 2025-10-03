from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class ListAuditsTool(Tool):
    """Enumerate audit sessions filtered by artifact or status."""

    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None, status: str = None) -> str:
        audits = data.get("audits", [])
        out = []
        for a in audits:
            if artifact_id and a.get("artifact_id") != artifact_id:
                continue
            if status and a.get("status") != status:
                continue
            out.append(
                _small_fields(
                    a, ["audit_id", "artifact_id", "audit_type", "status", "created_ts"]
                )
            )
        out.sort(key=lambda r: r.get("audit_id", ""))
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAudits",
                "description": "List audits filtered by artifact_id and/or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                },
            },
        }
