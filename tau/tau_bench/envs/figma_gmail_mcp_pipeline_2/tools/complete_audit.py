from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any

class CompleteAudit(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, report_asset_id: str = None) -> str:
        required = ["audit_id", "report_asset_id"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        audits: list[dict[str, Any]] = data.get("audits", [])
        for row in audits:
            if row.get("audit_id") == audit_id:
                row["status"] = "COMPLETED"
                row["report_asset_id_nullable"] = report_asset_id
                payload = row
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No audit with id '{audit_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "completeAudit",
                "description": "Mark an audit as COMPLETED and link the generated report asset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "report_asset_id": {"type": "string"},
                    },
                    "required": ["audit_id", "report_asset_id"],
                },
            },
        }
