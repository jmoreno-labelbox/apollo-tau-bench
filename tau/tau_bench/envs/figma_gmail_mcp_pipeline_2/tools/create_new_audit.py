# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["artifact_id", "audit_type"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        audits: List[Dict[str, Any]] = data.get("audits", [])
        audit_id = get_next_audit_id(data)
        created_ts = get_now_timestamp()

        new_audit = {
            "audit_id": audit_id,
            "artifact_id": kwargs["artifact_id"],
            "audit_type": kwargs["audit_type"],
            "created_ts": created_ts,
            "status": "RUNNING",
            "report_asset_id_nullable": None
        }

        audits.append(new_audit)
        data["audits"] = audits
        return json.dumps(new_audit, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_audit",
                "description": "Initialize a new audit session for a Figma artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "audit_type": {"type": "string", "enum": ["DS_MAPPING", "A11Y", "COMBINED_DS_A11Y"]}
                    },
                    "required": ["artifact_id", "audit_type"]
                }
            }
        }
