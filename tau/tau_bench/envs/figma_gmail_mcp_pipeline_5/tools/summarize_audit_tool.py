from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SummarizeAuditTool(Tool):
    """Summarize counts of DS and A11y findings for an audit."""

    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None) -> str:
        audit_id = _require_str(audit_id, "audit_id")
        if not audit_id:
            payload = {"error": "audit_id is required"}
            out = json.dumps(payload)
            return out

        ds = data.get("audit_findings_ds", {}).values()
        a11y = data.get("audit_findings_a11y", {}).values()
        ds_count = sum(1 for r in ds.values() if r.get("audit_id") == audit_id)
        a11y_count = sum(1 for r in a11y.values() if r.get("audit_id") == audit_id)
        payload = {
                "audit_id": audit_id,
                "ds_findings": ds_count,
                "a11y_findings": a11y_count,
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
                "name": "SummarizeAudit",
                "description": "Return simple counts of design-system and accessibility findings for an audit.",
                "parameters": {
                    "type": "object",
                    "properties": {"audit_id": {"type": "string"}},
                    "required": ["audit_id"],
                },
            },
        }
