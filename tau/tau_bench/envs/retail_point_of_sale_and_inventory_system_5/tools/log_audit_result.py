# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogAuditResult(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        entry = {
            "store_id": kwargs["store_id"],
            "sku": kwargs["sku"],
            "auditor_id": kwargs["auditor_id"],
            "result": kwargs.get("result", "discrepancy_logged")
        }
        data.setdefault("audit_logs", []).append(entry)
        return json.dumps({"message": "Audit result logged.", "entry": entry})
    @staticmethod
    def get_info() -> Dict[str, Any]:
