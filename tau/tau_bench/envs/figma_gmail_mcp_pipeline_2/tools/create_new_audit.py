from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any

class CreateNewAudit(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None, audit_type: str = None) -> str:
        required = ["artifact_id", "audit_type"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        audits: list[dict[str, Any]] = data.get("audits", [])
        audit_id = get_next_audit_id(data)
        created_ts = get_now_timestamp()

        new_audit = {
            "audit_id": audit_id,
            "artifact_id": artifact_id,
            "audit_type": audit_type,
            "created_ts": created_ts,
            "status": "RUNNING",
            "report_asset_id_nullable": None,
        }

        audits.append(new_audit)
        data["audits"] = audits
        payload = new_audit
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createNewAudit",
                "description": "Initialize a new audit session for a Figma artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "audit_type": {
                            "type": "string",
                            "enum": ["DS_MAPPING", "A11Y", "COMBINED_DS_A11Y"],
                        },
                    },
                    "required": ["artifact_id", "audit_type"],
                },
            },
        }
