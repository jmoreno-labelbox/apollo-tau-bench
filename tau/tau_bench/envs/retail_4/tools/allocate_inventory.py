# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AllocateInventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], item_id: str = None, item_ids: List[str] = None, quantity: int = 1) -> str:
        """
        Allocate inventory for order fulfillment with availability validation
        Supports both single item and batch processing with multiple items
        """
        # Check the validity of input parameters.
        if not item_id and not item_ids:
            return json.dumps({
                "error": "Either item_id or item_ids must be provided",
                "status": "failed"
            })

        if item_id and item_ids:
            return json.dumps({
                "error": "Cannot specify both item_id and item_ids. Use one or the other.",
                "status": "failed"
            })

        # Create a collection of items for processing.
        items_to_process = []
        if item_id:
            items_to_process.append(item_id)
        if item_ids:
            items_to_process.extend(item_ids)

        # Eliminate duplicates while maintaining the sequence.
        items_to_process = list(dict.fromkeys(items_to_process))

        if not items_to_process:
            return json.dumps({
                "error": "No valid item IDs provided",
                "status": "failed"
            })

        if quantity <= 0:
            return json.dumps({
                "error": "Quantity must be greater than 0",
                "status": "failed"
            })

        # Validation: Ensure item_id is present in product variants prior to adding to orders.
        products = list(data.get("products", {}).values())
        allocation_results = []
        successful_allocations = []
        failed_allocations = []
        total_allocation_value = 0.0

        for current_item_id in items_to_process:
            product_found = None
            variant_found = None

            for product in products:
                variants = product.get("variants", {})
                if current_item_id in variants:
                    product_found = product
                    variant_found = variants[current_item_id]
                    break

            if not variant_found:
                failed_allocations.append({
                    "item_id": current_item_id,
                    "error": f"Item {current_item_id} not found in product catalog",
                    "status": "failed"
                })
                continue

            # Policy: Verify product availability prior to allocation - do not allocate items that are not in stock.
            is_available = variant_found.get("available", False)
            if not is_available:
                failed_allocations.append({
                    "item_id": current_item_id,
                    "error": f"Item {current_item_id} is not available for allocation",
                    "status": "failed"
                })
                continue

            # Guideline: Implement precise variant pricing from the product catalog - avoid any unauthorized alterations to prices.
            unit_price = variant_found.get("price", 0)
            total_price = unit_price * quantity

            allocation_result = {
                "item_id": current_item_id,
                "product_name": product_found.get("name"),
                "product_id": product_found.get("product_id"),
                "quantity_allocated": quantity,
                "unit_price": unit_price,
                "total_price": total_price,
                "variant_options": variant_found.get("options", {}),
                "status": "success"
            }

            allocation_results.append(allocation_result)
            successful_allocations.append(allocation_result)
            total_allocation_value += total_price

        # Assess overall condition
        overall_status = "success" if successful_allocations else "failed"
        if successful_allocations and failed_allocations:
            overall_status = "partial_success"

        result = {
            "status": overall_status,
            "batch_processing": len(items_to_process) > 1,
            "allocation_summary": {
                "total_items_processed": len(items_to_process),
                "successful_allocations": len(successful_allocations),
                "failed_allocations": len(failed_allocations),
                "total_allocation_value": round(total_allocation_value, 2),
                "quantity_per_item": quantity
            },
            "successful_allocations": successful_allocations,
            "failed_allocations": failed_allocations,
            "allocation_details": allocation_results
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "allocate_inventory",
                "description": "Allocate inventory items for order fulfillment with availability checking. Supports both single item and batch processing with multiple items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "string",
                            "description": "Single product variant identifier (cannot be used with item_ids)"
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Array of product variant identifiers for batch processing (cannot be used with item_id)"
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "Quantity to allocate for each item (applies to all items in batch processing)",
                            "default": 1
                        }
                    }
                }
            }
        }
