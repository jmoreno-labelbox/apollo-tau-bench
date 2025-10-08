from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class CreateAuditSessionTool(Tool):
    """Generate/upsert an audit session for an artifact (deterministic audit_id)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str = None,
        audit_type: str = "COMBINED_DS_A11Y",
        created_ts: str = None
    ) -> str:
        artifact_id = _require_str(artifact_id, "artifact_id")
        created_ts = _require_str(created_ts, "created_ts")
        if not (artifact_id and created_ts):
            payload = {"error": "artifact_id and created_ts required"}
            out = json.dumps(payload)
            return out

        audit_id = _det_id("audit", [artifact_id, created_ts, audit_type])
        audits = _safe_table(data, "audits")
        idx = _index_by(audits, "audit_id")
        row = {
            "audit_id": audit_id,
            "artifact_id": artifact_id,
            "audit_type": audit_type,
            "status": "IN_PROGRESS",
            "created_ts": created_ts,
        }
        if audit_id in idx:
            audits[idx[audit_id]] = row
        else:
            audits.append(row)
        payload = {"success": True, "audit_id": audit_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditSession",
                "description": "Create/update an audit session (deterministic id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "audit_type": {"type": "string"},
                    },
                    "required": ["artifact_id", "created_ts"],
                },
            },
        }
