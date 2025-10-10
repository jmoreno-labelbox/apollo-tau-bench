# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrderStatusTool(Tool):
    """
    A tool to retrieve the status and details of a grocery order.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "get_order_status",
                "description": "Retrieves the full details of a grocery order, including its status and all line items enriched with product names.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "integer",
                            "description": "The unique identifier for the order to retrieve."
                        }
                    },
                    "required": ["order_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """
        Executes the logic to find and return the details of an order.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool. Expects 'order_id'.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the fully detailed and hydrated order object.
        """
        # 1. Verify Input Data
        param_definitions = {
            "order_id": {"type": int, "required": True}
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        order_id = kwargs["order_id"]

        # 2. Data Extraction
        order_record = next((o for o in list(data.get("orders", {}).values()) if o.get("order_id") == order_id), None)

        if not order_record:
            return _build_error_response("NOT_FOUND", {"entity": "Order", "entity_id": order_id})

        # 3. Data Enhancement (Hydration)
        order_items = [item for item in data.get("order_items", []) if item.get("order_id") == order_id]
        all_products = data.get("store_products", [])

        enriched_items = []
        for item in order_items:
            enriched_item = item.copy()

            # Augment with the primary product name.
            product_info = next((p for p in all_products if p.get("product_id") == item.get("product_id")), None)
            enriched_item["product_name"] = product_info.get("product_name") if product_info else "Unknown Product"

            # Add the alternative product name if relevant.
            sub_id = item.get("substitute_product_id")
            if sub_id:
                sub_info = next((p for p in all_products if p.get("product_id") == sub_id), None)
                enriched_item["substitute_product_name"] = sub_info.get("product_name") if sub_info else "Unknown Substitute"

            enriched_items.append(enriched_item)

        # 4. Construct the completed response object.
        detailed_order = order_record.copy()
        detailed_order["items"] = enriched_items

        # 5. Return the uniform success response.
        return _build_success_response(detailed_order)
