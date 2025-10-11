# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PlaceGroceryOrderTool(Tool):
    """
    A tool to create a formal order from a grocery list for a specific store.
    """

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Gets the tool's JSON schema."""
        return {
            "type": "function",
            "function": {
                "name": "place_grocery_order",
                "description": "Places a grocery order from a list for a store, creating order and order_item records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": { "type": "integer", "description": "The unique ID for the household placing the order." },
                        "store_id": { "type": "integer", "description": "The unique ID of the store to order from." },
                        "list_id": { "type": "integer", "description": "The unique ID of the grocery list to use." },
                        "user_id": { "type": "integer", "description": "The ID of the user placing the order." },
                        "substitutions": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "Optional list of substitutions for out-of-stock items."
                        }
                    },
                    "required": ["household_id", "store_id", "list_id", "user_id"],
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], household_id, list_id, store_id, user_id, substitutions = []) -> Dict[str, Any]:
        """
        Executes the logic to create order and order_item records.

        Args:
            data: The main in-memory dictionary containing all datasets.
            **kwargs: Keyword arguments passed to the tool.

        Returns:
            A dictionary following the standard response format. On success,
            the 'data' key contains the newly created and calculated order object.
        """
        # 1. Check Input Validity
        param_definitions = {
            "household_id": {"type": int, "required": True}, "store_id": {"type": int, "required": True},
            "list_id": {"type": int, "required": True}, "user_id": {"type": int, "required": True},
            "substitutions": {"type": list, "required": False},
        }
        validation_error = _validate_inputs(kwargs, param_definitions)
        if validation_error:
            return _build_error_response(validation_error["error_code"], validation_error["details"])

        list_record = next((g for g in data.get("grocery_lists", []) if g.get("list_id") == list_id), None)
        if not list_record:
            return _build_error_response("NOT_FOUND", {"entity": "GroceryList", "entity_id": list_id})
        if list_record.get("status_enum") == "ordered":
            return _build_error_response("UNSUPPORTED_OPERATION", {"operation": "Place Order", "entity": f"GroceryList {list_id} has already been ordered."})

        # 3. Main Functionality
        # 3a. Generate the primary Order entry.
        orders_table = data.setdefault("orders", [])
        max_order_id = max((o.get("order_id", 0) for o in orders_table), default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["orders"])
        new_order_id = max_order_id + 1

        timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
        # Streamlined scheduling: the following day from 6 to 8 PM.
        delivery_start = (datetime.now(timezone.utc) + timedelta(days=1)).replace(hour=18, minute=0, second=0, microsecond=0).isoformat().replace('+00:00', 'Z')
        delivery_end = (datetime.now(timezone.utc) + timedelta(days=1)).replace(hour=20, minute=0, second=0, microsecond=0).isoformat().replace('+00:00', 'Z')

        new_order_record = {
            "order_id": new_order_id, "household_id": household_id, "store_id": store_id,
            "list_id": list_id, "status_enum": "placed", "subtotal_cents": 0, "total_cents": 0,
            "placed_ts": timestamp, "scheduled_slot_start_ts": delivery_start, "scheduled_slot_end_ts": delivery_end
        }

        # 3b. Generate Order Items and compute subtotal
        sub_map = {s["original_ingredient_id"]: s["substitute_product_id"] for s in substitutions}
        list_items = [item for item in data.get("grocery_list_items", []) if item.get("list_id") == list_id]
        oi_table = data.setdefault("order_items", [])
        max_oi_id = max((oi.get("order_item_id", 0) for oi in oi_table), default=DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["order_items"])

        subtotal_cents = 0
        for item in list_items:
            ingredient_id = item["ingredient_id"]
            product_id_to_add = sub_map.get(ingredient_id)
            substitute_product_id_for_log = None

            if product_id_to_add:
                 substitute_product_id_for_log = product_id_to_add
            else:
                # Identify the top available product when no alternatives are offered.
                candidate_products = [p for p in data.get("store_products", []) if p.get("store_id") == store_id and p.get("ingredient_id") == ingredient_id and p.get("stock_status_enum") in ("in_stock", "low")]
                if not candidate_products: continue # Ignore the item if it's unavailable and has no substitute.
                product_id_to_add = min(candidate_products, key=lambda p: p.get("price_cents", float('inf')))["product_id"]

            product_record = next((p for p in data.get("store_products", []) if p.get("product_id") == product_id_to_add), None)
            if not product_record: continue

            max_oi_id += 1
            oi_table.append({
                "order_item_id": max_oi_id, "order_id": new_order_id, "product_id": product_id_to_add,
                "requested_qty": 1, "fulfilled_qty": 1, "substitute_product_id": substitute_product_id_for_log
            })
            subtotal_cents += product_record.get("price_cents", 0)

        # 3c. Complete total calculations and refresh status information.
        new_order_record["subtotal_cents"] = subtotal_cents
        new_order_record["total_cents"] = subtotal_cents + DEFAULT_BUSINESS_RULES["DEFAULT_ORDER_FEE_CENTS"]
        orders_table.append(new_order_record)
        list_record["status_enum"] = "ordered"

        # 4. Review and verification
        _log_audit_event(
            data, household_id=household_id, user_id=user_id, entity_type="orders",
            entity_id=new_order_id, action_enum="create", payload_json={"list_id": list_id, "store_id": store_id}
        )

        # 5. Reply
        return _build_success_response(new_order_record)
