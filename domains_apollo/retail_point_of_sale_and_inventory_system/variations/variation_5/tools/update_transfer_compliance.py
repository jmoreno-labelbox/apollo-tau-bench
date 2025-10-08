from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class UpdateTransferCompliance(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], transfer_id: str, status: str) -> str:
        entry = {"transfer_id": transfer_id, "status": status}
        data.setdefault("transfer_compliance", []).append(entry)
        payload = {"message": "Transfer compliance updated.", "entry": entry}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTransferCompliance",
                "parameters": {
                    "transfer_id": {"type": "string"},
                    "status": {"type": "string"},
                },
                "required": ["transfer_id", "status"],
            },
        }
