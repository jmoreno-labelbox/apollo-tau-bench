from tau_bench.envs.tool import Tool
import collections
import json
from datetime import date, datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetOrderStatusTool(Tool):
    """
    A tool to retrieve the status and details of a grocery order.
    """

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Gets the tool's JSON schema."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetOrderStatus",
                "description": "Retrieves the full details of a grocery order, including its status and all line items enriched with product names.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "integer",
                            "description": "The unique identifier for the order to retrieve.",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], order_id: int) -> dict[str, Any]:
        """
        Executes the logic to find and return the details of an order.

        Args:
            data: The main in-memory dictionary containing all datasets.
            order_id: The ID of the order to retrieve.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the fully detailed and hydrated order object.
        """
        #1. Validate Inputs
        param_definitions = {"order_id": {"type": int, "required": True}}
        validation_error = _validate_inputs({"order_id": order_id}, param_definitions)
        if validation_error:
            return _build_error_response(
                validation_error["error_code"], validation_error["details"]
            )

        #2. Data Retrieval
        order_record = next(
            (o for o in data.get("orders", []) if o.get("order_id") == order_id), None
        )

        if not order_record:
            return _build_error_response(
                "NOT_FOUND", {"entity": "Order", "entity_id": order_id}
            )

        #3. Data Enrichment (Hydration)
        order_items = [
            item
            for item in data.get("order_items", [])
            if item.get("order_id") == order_id
        ]
        all_products = data.get("store_products", [])

        enriched_items = []
        for item in order_items:
            enriched_item = item.copy()

            #Enrich with the main product name
            product_info = next(
                (
                    p
                    for p in all_products
                    if p.get("product_id") == item.get("product_id")
                ),
                None,
            )
            enriched_item["product_name"] = (
                product_info.get("product_name") if product_info else "Unknown Product"
            )

            #Enrich with the substitute product name, if applicable
            sub_id = item.get("substitute_product_id")
            if sub_id:
                sub_info = next(
                    (p for p in all_products if p.get("product_id") == sub_id), None
                )
                enriched_item["substitute_product_name"] = (
                    sub_info.get("product_name") if sub_info else "Unknown Substitute"
                )

            enriched_items.append(enriched_item)

        #4. Build the final response object
        detailed_order = order_record.copy()
        detailed_order["items"] = enriched_items

        #5. Return the standardized success response
        return _build_success_response(detailed_order)
