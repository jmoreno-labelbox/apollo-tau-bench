from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ProcessBulkProductUpdate(Tool):
    """Handle mass updates to the product catalog with validation checks."""

    @staticmethod
    def invoke(
        data: dict[str, Any], update_type: Any, product_ids: Any, update_data: Any = {}
    ) -> str:
        update_type = f"{update_type}"
        product_ids = [_idstr(x) for x in (product_ids or [])]
        update_data = update_data or {}

        if not update_type or not product_ids:
            return _error("update_type and product_ids are required.")

        products = data.get("products", {}).values()
        bulk_updates = data.setdefault("bulk_updates", [])
        updated_count = 0

        for pid in product_ids:
            product = _find_one(list(products.values()), "product_id", pid)
            if product:
                if update_type == "price" and "list_price" in update_data:
                    product["list_price"] = update_data["list_price"]
                product["last_modified"] = FIXED_NOW
                updated_count += 1

        update_id = f"UPD_{len(bulk_updates) + 1:03d}"
        bulk_updates.append(
            {
                "update_id": update_id,
                "update_type": update_type,
                "product_ids": list(product_ids),
                "update_data": update_data,
                "processed_at": FIXED_NOW,
            }
        )

        _append_audit(
            data,
            "bulk_product_update",
            update_id,
            {"updated_count": updated_count, "update_type": update_type},
        )
        payload = {
                "update_type": update_type,
                "total_products": len(product_ids),
                "updated_count": updated_count,
                "update_id": update_id,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        update_type = f"{update_type}"
        product_ids = [_idstr(x) for x in (product_ids or [])]
        update_data = update_data or {}

        if not update_type or not product_ids:
            return _error("update_type and product_ids are required.")

        products = data.get("products", {}).values()
        bulk_updates = data.setdefault("bulk_updates", [])
        updated_count = 0

        for pid in product_ids:
            product = _find_one(list(products.values()), "product_id", pid)
            if product:
                if update_type == "price" and "list_price" in update_data:
                    product["list_price"] = update_data["list_price"]
                product["last_modified"] = FIXED_NOW
                updated_count += 1

        update_id = f"UPD_{len(bulk_updates) + 1:03d}"
        bulk_updates.append(
            {
                "update_id": update_id,
                "update_type": update_type,
                "product_ids": list(product_ids),
                "update_data": update_data,
                "processed_at": FIXED_NOW,
            }
        )

        _append_audit(
            data,
            "bulk_product_update",
            update_id,
            {"updated_count": updated_count, "update_type": update_type},
        )
        payload = {
                "update_type": update_type,
                "total_products": len(product_ids),
                "updated_count": updated_count,
                "update_id": update_id,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessBulkProductUpdate",
                "description": "Process bulk updates to product catalog with validation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "update_type": {"type": "string"},
                        "product_ids": {"type": "array", "items": {"type": "string"}},
                        "update_data": {"type": "object"},
                    },
                    "required": ["update_type", "product_ids"],
                },
            },
        }
