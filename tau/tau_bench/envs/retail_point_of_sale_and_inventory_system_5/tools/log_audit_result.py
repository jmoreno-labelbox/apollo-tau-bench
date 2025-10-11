# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogAuditResult(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], auditor_id, sku, store_id, result = "discrepancy_logged") -> str:
        entry = {
            "store_id": store_id,
            "sku": sku,
            "auditor_id": auditor_id,
            "result": result
        }
        data.setdefault("audit_logs", []).append(entry)
        return json.dumps({"message": "Audit result logged.", "entry": entry})
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "log_audit_result",
                "description": "Tool function: log_audit_result",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
