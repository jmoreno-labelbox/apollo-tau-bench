from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetSupplierDetails(Tool):
    """Retrieve supplier record using supplier_id."""

    @staticmethod
    def invoke(data, supplier_id: str = None) -> str:
        if not supplier_id:
            payload = {"error": "supplier_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        sup = next(
            (
                s
                for s in data.get("suppliers", [])
                if s.get("supplier_id") == supplier_id
            ),
            None,
        )
        payload = sup or {"error": f"supplier_id {supplier_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getSupplierDetails",
                "description": "Fetch supplier by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"supplier_id": {"type": "string"}},
                    "required": ["supplier_id"],
                },
            },
        }
