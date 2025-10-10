# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PerformPhysicalCount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str, warehouse_id: str, **kwargs) -> str:
        inventory = list(data.get("inventory", {}).values())
        instruction_amount = kwargs.get("instruction_amount", 0)
        quantity_available_flag = kwargs.get("quantity_available_flag", False)

        inventory_item = next(
            (item for item in inventory
             if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id),
            None
        )

        if not inventory_item:
            return json.dumps({"error": f"Inventory not found for SKU {sku} in warehouse {warehouse_id}"})

        # Simulate physical count with slight variance
        system_count = inventory_item.get("quantity_on_hand", 0)
        if quantity_available_flag:
            system_count = inventory_item.get("quantity_available", 0)
        physical_count = system_count - int(system_count * 0.0075)  # 0.75% variance
        if instruction_amount:
            physical_count = instruction_amount

        count_record = {
            "count_id": f"CNT-{sku}-{warehouse_id}",
            "sku": sku,
            "warehouse_id": warehouse_id,
            "system_count": system_count,
            "physical_count": physical_count,
            "count_date": get_current_timestamp(),
            "counter_id": "EMP-CYCLE-001",
            "variance": physical_count - system_count
        }

        if "cycle_counts" not in data:
            data["cycle_counts"] = []
        data["cycle_counts"].append(count_record)

        return json.dumps({
            "count_id": count_record["count_id"],
            "system_count": system_count,
            "physical_count": physical_count,
            "variance": count_record["variance"]
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "perform_physical_count",
                "description": "Perform physical inventory count for a specific SKU",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "Product SKU"},
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"},
                        "instruction_amount": {"type": "integer", "description": "Amount to adjust"},
                        "quantity_available_flag": {"type": "boolean", "description": "Use quantity available instead of quantity on hand"}
                    },
                    "required": ["sku", "warehouse_id"]
                }
            }
        }
