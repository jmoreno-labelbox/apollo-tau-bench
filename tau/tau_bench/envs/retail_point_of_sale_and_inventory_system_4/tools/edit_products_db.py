from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class EditProductsDb(Tool):  #CREATE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sku: str = None,
        name: str = None,
        category: str = None,
        price: float = None,
        is_discountable: bool = None,
        description: str = None,
        supplier_id: str = None,
        weight_kg: float = None,
        dimensions_cm: str = None,
        brand: str = None,
        cost: float = None,
        barcode: str = None,
        tax_rate: float = None,
        discount_rate: float = None,
        status: str = None,
        expiry_date: str = None,
        current_time: str = None,
        delete: bool = False
    ) -> str:
        db = _convert_db_to_list(data.get("products", {}).values()
        if sku:
            idx, row = _find_by_id(db, "sku", sku)
            if row:
                if delete:
                    #--- REMOVE ---
                    del db[idx]
                    payload = {"result": "deleted"}
                    out = json.dumps(payload)
                    return out
                else:
                    #--- MODIFY ---
                    if name is not None:
                        row["name"] = name
                    if category is not None:
                        row["category"] = category
                    if price is not None:
                        row["price"] = price
                    if is_discountable is not None:
                        row["is_discountable"] = is_discountable
                    if description is not None:
                        row["description"] = description
                    if supplier_id is not None:
                        row["supplier_id"] = supplier_id
                    if weight_kg is not None:
                        row["weight_kg"] = weight_kg
                    if dimensions_cm is not None:
                        row["dimensions_cm"] = dimensions_cm
                    if brand is not None:
                        row["brand"] = brand
                    if cost is not None:
                        row["cost"] = cost
                    if barcode is not None:
                        row["barcode"] = barcode
                    if tax_rate is not None:
                        row["tax_rate"] = tax_rate
                    if discount_rate is not None:
                        row["discount_rate"] = discount_rate
                    if status is not None:
                        row["status"] = status
                    if expiry_date is not None:
                        row["expiry_date"] = expiry_date
                    if current_time is not None:
                        row["updated_at"] = current_time
                    payload = {"result": row}
                    out = json.dumps(payload)
                    return out
            else:
                payload = {"error": f"Product {sku} not found"}
                out = json.dumps(payload)
                return out
        else:
            #--- ADD ---
            if name is None or price is None or current_time is None:
                payload = {
                        "error": "Missing required field for creation (name, price, current_time)"
                    }
                out = json.dumps(
                    payload)
                return out
            new_row = {
                "sku": sku if sku is not None else f"SKU-{1000 + len(db) + 1}",
                "name": name,
                "category": category if category is not None else "Uncategorized",
                "price": price,
                "is_discountable": (
                    is_discountable if is_discountable is not None else True
                ),
                "description": (
                    description if description is not None else "No description"
                ),
                "supplier_id": supplier_id if supplier_id is not None else "Unknown",
                "weight_kg": weight_kg if weight_kg is not None else 0.0,
                "dimensions_cm": (
                    dimensions_cm if dimensions_cm is not None else "Unknown"
                ),
                "brand": brand if brand is not None else "Unknown",
                "cost": cost if cost is not None else 0.0,
                "barcode": barcode if barcode is not None else "Unknown",
                "tax_rate": tax_rate if tax_rate is not None else 0.0825,
                "discount_rate": discount_rate if discount_rate is not None else 0.0,
                "status": status if status is not None else "active",
                "expiry_date": expiry_date if expiry_date is not None else "None",
                "created_at": current_time,
                "updated_at": current_time,
            }
            db.append(new_row)
            payload = {"result": new_row}
            out = json.dumps(payload)
            return out
        pass
        db = _convert_db_to_list(data.get("products", {}).values()
        if sku:
            idx, row = _find_by_id(db, "sku", sku)
            if row:
                if delete:
                    #--- REMOVE ---
                    del db[idx]
                    payload = {"result": "deleted"}
                    out = json.dumps(payload)
                    return out
                else:
                    #--- MODIFY ---
                    if name is not None:
                        row["name"] = name
                    if category is not None:
                        row["category"] = category
                    if price is not None:
                        row["price"] = price
                    if is_discountable is not None:
                        row["is_discountable"] = is_discountable
                    if description is not None:
                        row["description"] = description
                    if supplier_id is not None:
                        row["supplier_id"] = supplier_id
                    if weight_kg is not None:
                        row["weight_kg"] = weight_kg
                    if dimensions_cm is not None:
                        row["dimensions_cm"] = dimensions_cm
                    if brand is not None:
                        row["brand"] = brand
                    if cost is not None:
                        row["cost"] = cost
                    if barcode is not None:
                        row["barcode"] = barcode
                    if tax_rate is not None:
                        row["tax_rate"] = tax_rate
                    if discount_rate is not None:
                        row["discount_rate"] = discount_rate
                    if status is not None:
                        row["status"] = status
                    if expiry_date is not None:
                        row["expiry_date"] = expiry_date
                    if current_time is not None:
                        row["updated_at"] = current_time
                    payload = {"result": row}
                    out = json.dumps(payload)
                    return out
            else:
                payload = {"error": f"Product {sku} not found"}
                out = json.dumps(payload)
                return out
        else:
            #--- ADD ---
            if name is None or price is None or current_time is None:
                payload = {
                        "error": "Missing required field for creation (name, price, current_time)"
                    }
                out = json.dumps(
                    payload)
                return out
            new_row = {
                "sku": sku if sku is not None else f"SKU-{1000 + len(db) + 1}",
                "name": name,
                "category": category if category is not None else "Uncategorized",
                "price": price,
                "is_discountable": (
                    is_discountable if is_discountable is not None else True
                ),
                "description": (
                    description if description is not None else "No description"
                ),
                "supplier_id": supplier_id if supplier_id is not None else "Unknown",
                "weight_kg": weight_kg if weight_kg is not None else 0.0,
                "dimensions_cm": (
                    dimensions_cm if dimensions_cm is not None else "Unknown"
                ),
                "brand": brand if brand is not None else "Unknown",
                "cost": cost if cost is not None else 0.0,
                "barcode": barcode if barcode is not None else "Unknown",
                "tax_rate": tax_rate if tax_rate is not None else 0.0825,
                "discount_rate": discount_rate if discount_rate is not None else 0.0,
                "status": status if status is not None else "active",
                "expiry_date": expiry_date if expiry_date is not None else "None",
                "created_at": current_time,
                "updated_at": current_time,
            }
            db.append(new_row)
            payload = {"result": new_row}
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EditProductsDb",
                "description": "Create, update, or delete a product row by sku. If delete is True, deletes the row. If sku is given it will edit the row with the given information. If no sku is given, it will create a new row with the given info, as long as name, category, price, and current_time are given.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "default": None,
                            "description": "The SKU of the product to edit or delete. If not provided, a new SKU will be generated.",
                        },
                        "delete": {
                            "type": "boolean",
                            "default": False,
                            "description": "Whether to delete the specified product.",
                        },
                        "name": {
                            "type": "string",
                            "default": None,
                            "description": "Name of the product.",
                        },
                        "category": {
                            "type": "string",
                            "default": None,
                            "description": "Category of the product.",
                        },
                        "price": {
                            "type": "number",
                            "default": None,
                            "description": "Price of the product.",
                        },
                        "is_discountable": {
                            "type": "boolean",
                            "default": None,
                            "description": "Whether the product is discountable.",
                        },
                        "description": {
                            "type": "string",
                            "default": None,
                            "description": "Description of the product.",
                        },
                        "supplier_id": {
                            "type": "string",
                            "default": None,
                            "description": "Supplier ID for the product.",
                        },
                        "weight_kg": {
                            "type": "number",
                            "default": None,
                            "description": "Weight in kg.",
                        },
                        "dimensions_cm": {
                            "type": "string",
                            "default": None,
                            "description": "Dimensions in cm.",
                        },
                        "brand": {
                            "type": "string",
                            "default": None,
                            "description": "Brand of the product.",
                        },
                        "cost": {
                            "type": "number",
                            "default": None,
                            "description": "Cost of the product.",
                        },
                        "barcode": {
                            "type": "string",
                            "default": None,
                            "description": "Barcode of the product.",
                        },
                        "tax_rate": {
                            "type": "number",
                            "default": None,
                            "description": "Tax rate for the product.",
                        },
                        "discount_rate": {
                            "type": "number",
                            "default": None,
                            "description": "Discount rate for the product.",
                        },
                        "status": {
                            "type": "string",
                            "default": None,
                            "description": "Status of the product.",
                        },
                        "expiry_date": {
                            "type": "string",
                            "default": None,
                            "description": "Expiry date of the product.",
                        },
                        "current_time": {
                            "type": "string",
                            "default": None,
                            "description": "Current timestamp for created_at/updated_at.",
                        },
                    },
                    "required": [],
                },
            },
        }
