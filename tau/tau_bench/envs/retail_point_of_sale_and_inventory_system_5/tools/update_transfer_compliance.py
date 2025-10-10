# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTransferCompliance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        entry = {
            "transfer_id": kwargs["transfer_id"],
            "status": kwargs["status"]
        }
        data.setdefault("transfer_compliance", []).append(entry)
        return json.dumps({"message": "Transfer compliance updated.", "entry": entry}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_transfer_compliance", "parameters": {"transfer_id": {"type": "string"}, "status": {"type": "string"}}, "required": ["transfer_id", "status"]}}
