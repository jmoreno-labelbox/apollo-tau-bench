# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInventoryStock(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, item_id: str = None, item_ids: List[str] = None, new_stock_level: int = None, new_stock_levels: List[int] = None, stock_action: str = "set", exclude_unavailable: bool = False) -> str:
        """
        Update inventory stock levels for supplier items (single item or batch update)
        Optionally excludes non-available items from processing

        Writes to: suppliers.json (updates item_stock levels)
        Data Sources: suppliers.json (supplier_id, item_stock), products.json (item availability)
        """
        # Ensure that at least one item ID is supplied.
        if not item_id and not item_ids:
            return json.dumps({
                "error": "Either item_id or item_ids must be provided",
                "status": "failed"
            })

        # Create the collection of items for processing.
        items_to_process = []
        if item_id:
            items_to_process.append(item_id)
        if item_ids:
            items_to_process.extend(item_ids)

        # Eliminate duplicates while maintaining sequence.
        items_to_process = list(dict.fromkeys(items_to_process))

        if not items_to_process:
            return json.dumps({
                "error": "No valid item IDs provided",
                "status": "failed"
            })

        # Manage inventory quantities - may be a single value or an array.
        stock_levels_list = []
        if new_stock_level is not None and new_stock_levels is not None:
            return json.dumps({
                "error": "Cannot specify both new_stock_level and new_stock_levels. Use one or the other.",
                "status": "failed"
            })
        elif new_stock_level is not None:
            if new_stock_level < 0:
                return json.dumps({"error": "Stock level cannot be negative", "status": "failed"})
            # Unified stock level for all products.
            stock_levels_list = [new_stock_level] * len(items_to_process)
        elif new_stock_levels is not None:
            if len(new_stock_levels) != len(items_to_process):
                return json.dumps({
                    "error": f"Number of stock levels ({len(new_stock_levels)}) must match number of items ({len(items_to_process)})",
                    "status": "failed"
                })
            # Ensure all inventory quantities are zero or greater.
            for i, level in enumerate(new_stock_levels):
                if level < 0:
                    return json.dumps({
                        "error": f"Stock level at index {i} cannot be negative: {level}",
                        "status": "failed"
                    })
            stock_levels_list = new_stock_levels
        else:
            return json.dumps({
                "error": "Either new_stock_level or new_stock_levels must be provided",
                "status": "failed"
            })

        valid_actions = ["set", "add", "subtract"]
        if stock_action not in valid_actions:
            return json.dumps({
                "error": f"Invalid stock action '{stock_action}'. Valid actions: {', '.join(valid_actions)}",
                "status": "failed"
            })

        suppliers = data.get("suppliers", [])
        supplier_to_update = None
        supplier_index = None

        # Locate the vendor.
        for i, supplier in enumerate(suppliers):
            if supplier.get("supplier_id") == supplier_id:
                supplier_to_update = supplier
                supplier_index = i
                break

        if not supplier_to_update:
            return json.dumps({"error": f"Supplier {supplier_id} not found", "status": "failed"})

        # Retrieve product availability data when exclude_unavailable is set to True.
        item_availability_map = {}
        if exclude_unavailable:
            products = list(data.get("products", {}).values())
            for product in products:
                variants = product.get("variants", {})
                for variant_id, variant_info in variants.items():
                    item_availability_map[variant_id] = variant_info.get("available", False)

        # Check that all items are in the supplier's inventory and apply availability filters if necessary.
        item_stock = supplier_to_update.get("item_stock", {})
        missing_items = []
        unavailable_items = []
        filtered_items = []

        for i, item in enumerate(items_to_process):
            if item not in item_stock:
                missing_items.append(item)
                continue

            # Verify availability when exclude_unavailable is set to True.
            if exclude_unavailable:
                is_available = item_availability_map.get(item, False)
                if not is_available:
                    unavailable_items.append(item)
                    continue

            # Item meets all filter criteria.
            filtered_items.append((item, stock_levels_list[i]))

        if missing_items:
            return json.dumps({
                "error": f"Items not found in supplier {supplier_id} inventory: {', '.join(missing_items)}",
                "status": "failed"
            })

        if not filtered_items:
            error_message = "No items to process"
            if exclude_unavailable and unavailable_items:
                error_message += f". All items are marked as unavailable: {', '.join(unavailable_items)}"
            return json.dumps({
                "error": error_message,
                "status": "failed",
                "unavailable_items": unavailable_items if exclude_unavailable else []
            })

        # UPDATE OPERATION: Modify inventory counts for selected items
        update_results = []
        for item, stock_level_to_apply in filtered_items:
            old_stock = item_stock[item]

            # Manage various stock conditions.
            if old_stock in ["discontinued", "out_of_stock"]:
                if stock_action in ["add", "subtract"]:
                    update_results.append({
                        "item_id": item,
                        "status": "error",
                        "message": f"Cannot modify stock for {old_stock} item",
                        "previous_stock": old_stock,
                        "new_stock": old_stock  # No modifications.
                    })
                    continue
                # Enable "set" to revert from discontinued/out_of_stock status.
                item_stock[item] = stock_level_to_apply
                new_stock_value = stock_level_to_apply
            else:
                # Quantitative inventory levels
                old_stock_num = int(old_stock) if isinstance(old_stock, (int, str)) and str(old_stock).isdigit() else 0

                if stock_action == "set":
                    item_stock[item] = stock_level_to_apply
                    new_stock_value = stock_level_to_apply
                elif stock_action == "add":
                    new_value = old_stock_num + stock_level_to_apply
                    item_stock[item] = new_value
                    new_stock_value = new_value
                elif stock_action == "subtract":
                    new_value = max(0, old_stock_num - stock_level_to_apply)
                    item_stock[item] = new_value if new_value > 0 else "out_of_stock"
                    new_stock_value = item_stock[item]

            update_results.append({
                "item_id": item,
                "status": "success",
                "previous_stock": old_stock,
                "new_stock": new_stock_value,
                "action_performed": stock_action,
                "action_value": stock_level_to_apply
            })

        supplier_to_update["item_stock"] = item_stock
        supplier_to_update["stock_updated"] = datetime.now().isoformat()

        # Modify the supplier in the data structure.
        data["suppliers"][supplier_index] = supplier_to_update

        # Compute overall statistics.
        successful_updates = [r for r in update_results if r["status"] == "success"]
        failed_updates = [r for r in update_results if r["status"] == "error"]

        result = {
            "status": "success",
            "supplier_id": supplier_id,
            "supplier_name": supplier_to_update.get("name"),
            "filtering_summary": {
                "exclude_unavailable": exclude_unavailable,
                "total_items_requested": len(items_to_process),
                "items_filtered_out": len(unavailable_items) if exclude_unavailable else 0,
                "unavailable_items": unavailable_items if exclude_unavailable else [],
                "items_processed": len(filtered_items)
            },
            "batch_update_summary": {
                "total_items_processed": len(filtered_items),
                "successful_updates": len(successful_updates),
                "failed_updates": len(failed_updates),
                "stock_action": stock_action
            },
            "update_details": update_results,
            "stock_updated": supplier_to_update["stock_updated"]
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_stock",
                "description": "Update inventory stock levels for supplier items (single item or batch update). Optionally excludes non-available items from processing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier identifier (e.g., '#SUP0001')"},
                        "item_id": {"type": "string", "description": "Single item identifier (optional if using item_ids)"},
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of item identifiers for batch update (optional if using item_id)"
                        },
                        "new_stock_level": {"type": "integer", "description": "New stock level for single item or all items (optional if using new_stock_levels)"},
                        "new_stock_levels": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "List of stock levels corresponding to each item in item_ids (optional if using new_stock_level)"
                        },
                        "stock_action": {"type": "string", "description": "Action: 'set', 'add', or 'subtract'", "default": "set"},
                        "exclude_unavailable": {
                            "type": "boolean",
                            "description": "Optional flag to exclude items marked as unavailable in the product catalog from stock updates",
                            "default": False
                        }
                    },
                    "required": ["supplier_id"]
                }
            }
        }
