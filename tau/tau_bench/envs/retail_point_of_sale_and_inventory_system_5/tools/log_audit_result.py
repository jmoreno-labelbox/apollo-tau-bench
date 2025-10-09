from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class LogAuditResult(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str, sku: str, auditor_id: str, result: str = "discrepancy_logged",
        timestamp: Any = None,
        photo: Any = None,
        digital_signature: str = None
    ) -> str:
        entry = {
            "store_id": store_id,
            "sku": sku,
            "auditor_id": auditor_id,
            "result": result,
        }
        data.setdefault("audit_logs", []).append(entry)
        payload = {"message": "Audit result logged.", "entry": entry}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogAuditResult",
                "parameters": {
                    "store_id": {"type": "string"},
                    "sku": {"type": "string"},
                    "auditor_id": {"type": "string"},
                    "result": {"type": "string"},
                },
                "required": ["store_id", "sku", "auditor_id"],
            },
        }
