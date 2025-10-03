from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateAuditSession(Tool):  #WRITE
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str, audit_type: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(artifact_id, str) or not artifact_id:
            raise ValueError("artifact_id must be a non-empty string")

        allowed_audit_types = ["DS_MAPPING", "A11Y", "COMBINED_DS_A11Y"]
        if audit_type not in allowed_audit_types:
            raise ValueError(f"audit_type must be one of: {allowed_audit_types}")

        audits = data.get("audits", [])

        #Create a new audit_id by incrementing from current audits
        next_num = len(audits) + 1
        audit_id = f"audit_{next_num:03d}"

        #Assign created_ts to a time following the latest audit (2024-08-23T14:00:00Z)
        #Select a random time thereafter, for example, 2024-08-24T09:15:00Z
        created_ts = "2024-08-24T09:15:00Z"

        new_audit = {
            "audit_id": audit_id,
            "artifact_id": artifact_id,
            "audit_type": audit_type,
            "created_ts": created_ts,
            "status": "RUNNING",
            "report_asset_id_nullable": None,
        }

        audits.append(new_audit)
        payload = {"new_audit": new_audit}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditSession",
                "description": "Create a new audit session for a Figma artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {
                            "type": "string",
                            "description": "The artifact ID to audit.",
                        },
                        "audit_type": {
                            "type": "string",
                            "description": "Type of audit (DS_MAPPING, A11Y, COMBINED_DS_A11Y).",
                        },
                    },
                    "required": ["artifact_id", "audit_type"],
                },
            },
        }
