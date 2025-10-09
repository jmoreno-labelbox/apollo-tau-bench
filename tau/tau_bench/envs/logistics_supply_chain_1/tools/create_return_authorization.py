from tau_bench.envs.tool import Tool
import json
import random
from typing import Any

class CreateReturnAuthorization(Tool):
    """Generates a Return Merchandise Authorization (RMA) record for a customer return."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, line_items: list = None, reason: str = None) -> str:
        if not all([order_id, line_items, reason]):
            payload = {"error": "order_id, line_items, and reason are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if "rma_authorizations" not in data:
            data["rma_authorizations"] = []

        max_rma_num = max(
            (
                int(r.get("rma_id", "RMA-1000").split("-")[1])
                for r in data["rma_authorizations"]
            ),
            default=1000,
        )
        new_rma_id = f"RMA-{max_rma_num + 1}"

        rma_record = {
            "rma_id": new_rma_id,
            "order_id": order_id,
            "line_items_to_return": line_items,
            "reason": reason,
            "status": "Authorized",
        }
        data["rma_authorizations"].append(rma_record)
        payload = {"rma_id": new_rma_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReturnAuthorization",
                "description": "Creates a Return Merchandise Authorization (RMA) to formally approve a customer's return request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The original order ID the return is associated with.",
                        },
                        "line_items": {
                            "type": "array",
                            "description": "A list of products being returned.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the return provided by the customer.",
                        },
                    },
                    "required": ["order_id", "line_items", "reason"],
                },
            },
        }
