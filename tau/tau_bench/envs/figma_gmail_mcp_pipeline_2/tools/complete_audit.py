# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CompleteAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], audit_id, report_asset_id) -> str:
        required = ["audit_id", "report_asset_id"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        audits: List[Dict[str, Any]] = list(data.get("audits", {}).values())
        for row in audits:
            if row.get("audit_id") == audit_id:
                row["status"] = "COMPLETED"
                row["report_asset_id_nullable"] = report_asset_id
                return json.dumps(row, indent=2)

        return json.dumps({"error": f"No audit with id '{audit_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "complete_audit",
                "description": "Mark an audit as COMPLETED and link the generated report asset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "report_asset_id": {"type": "string"}
                    },
                    "required": ["audit_id", "report_asset_id"]
                }
            }
        }
