# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogTransfer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        entry = {
            "from_store": kwargs["from_store"],
            "to_store": kwargs["to_store"],
            "sku": kwargs["sku"],
            "quantity": kwargs["quantity"]
        }
        data.setdefault("transfer_logs", []).append(entry)
        return json.dumps({"message": "Transfer logged.", "entry": entry}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
