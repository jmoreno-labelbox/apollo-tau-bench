# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


ERROR_MESSAGES = {
    "REQUIRED_PARAMETER": "Required parameter '{param}' is missing.",
    "INVALID_PARAMETER_TYPE": "Parameter '{param}' must be of type {expected_type}.",
    "NOT_FOUND": "{entity} with ID {entity_id} not found.",
    "OPERATION_FAILED": "Operation failed: {reason}",
}










def _validate_inputs(
    args: Dict[str, Any],
    param_definitions: Dict[str, Dict[str, Any]]
) -> Optional[Dict[str, Any]]:
    """
    Validates tool arguments against a set of definitions.

    This helper checks for the presence of required parameters and validates the
    data type for all provided parameters against the definitions. It's designed
    to be the first call within any tool's `invoke` method to act as a
    protective guard clause.

    Args:
        args: The dictionary of arguments passed to the tool (e.g., kwargs).
        param_definitions: A dictionary where each key is a parameter name and
            the value is another dictionary defining its rules, such as
            'type' (e.g., int, str) and 'required' (bool).

    Returns:
        None if all validations pass.
        A dictionary containing the 'error_code' and 'details' for the
        first validation failure, ready to be passed to _build_error_response().
    """
    for param, definition in param_definitions.items():
        is_required = definition.get("required", False)
        expected_type = definition.get("type")

        if is_required and param not in args:
            return {
                "error_code": "REQUIRED_PARAMETER",
                "details": {"param": param}
            }

        if param in args and expected_type is not None:
            value = args[param]
            if not isinstance(value, expected_type):
                return {
                    "error_code": "INVALID_PARAMETER_TYPE",
                    "details": {
                        "param": param,
                        "expected_type": expected_type.__name__
                    }
                }

    return None

def _log_audit_event(data: Dict[str, Any], household_id, user_id, entity_type, entity_id, action_enum = "custom_action", payload_json = {}) -> None:
    """
    Logs an action to the audit trail.

    This helper constructs and appends a new audit log entry to the in-memory
    'audit_logs' dataset. It automatically generates a new unique 'audit_id'
    and a UTC timestamp for the 'created_at' field. This function modifies
    the 'data' dictionary in place.

    Args:
        data: The main in-memory dictionary containing all datasets, which
              will be mutated by this function.
        **kwargs: Keyword arguments that map to the audit log schema. Expected
            keys include 'household_id', 'user_id', 'entity_type',
            'entity_id', 'action_enum', and 'payload_json'.
    """
    audit_logs_table = data.setdefault("audit_logs", [])

    # 1. Generate a new unique ID based on the last entry or the default start value
    base_id = DEFAULT_BUSINESS_RULES["INITIAL_ID_DEFAULTS"]["audit_logs"]
    max_id = base_id
    if audit_logs_table:
        max_id = max(int(log.get("audit_id", 0)) for log in audit_logs_table)
    next_id = max_id + 1

    # 2. Get the current timestamp in ISO 8601 format (UTC)
    timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

    # 3. Construct the new log entry from kwargs
    new_log_entry = {
        "audit_id": next_id,
        "household_id": household_id,
        "user_id": user_id,
        "entity_type": entity_type,
        "entity_id": entity_id,
        "action_enum": action_enum,
        "payload_json": payload_json,
        "created_at": timestamp
    }

    # 4. Append the new entry to the table
    audit_logs_table.append(new_log_entry)

def _build_success_response(data: Any) -> str:
    """
    Builds a standardized success response envelope as a JSON string.

    Args:
        data: The payload to be included in the response.

    Returns:
        A JSON string representing the successful response.
    """
    response_dict = {
        "success": True,
        "data": data
    }
    return json.dumps(response_dict, indent=2)

def _build_error_response(error_code: str, details: Optional[Dict[str, Any]] = None) -> str:
    """
    Builds a standardized error response envelope as a JSON string.

    Args:
        error_code: The error code, corresponding to a key in ERROR_MESSAGES.
        details: A dictionary with specific details to format the error message.

    Returns:
        A JSON string representing the failed response.
    """
    details = details or {}
    message_template = ERROR_MESSAGES.get(error_code, "An unknown error occurred.")

    try:
        message = message_template.format(**details)
    except KeyError:
        message = message_template

    response_dict = {
        "success": False,
        "error": {
            "code": error_code,
            "message": message,
            "details": details
        }
    }
    return json.dumps(response_dict, indent=2)

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
        validation_error = _validate_inputs({"household_id": household_id, "list_id": list_id, "store_id": store_id, "user_id": user_id, "substitutions": substitutions}, param_definitions)
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