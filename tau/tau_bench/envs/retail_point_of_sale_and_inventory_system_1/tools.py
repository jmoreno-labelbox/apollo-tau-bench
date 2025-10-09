import json
import re
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class GetProductSkuByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_name: str = None) -> str:
        products = data.get("products", {}).values()
        for product in products.values():
            if product.get("name") == product_name:
                payload = {"sku": product.get("sku")}
                out = json.dumps(payload)
                return out
        payload = {"sku": None}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductSkuByName",
                "description": "Retrieves the SKU (Stock Keeping Unit) for a given product name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_name": {
                            "type": "string",
                            "description": "The full name of the product.",
                        },
                    },
                    "required": ["product_name"],
                },
            },
        }


class GetInventoryItemBySkuAndStore(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, store_id: str = None) -> str:
        inventory_items = data.get("inventory", {}).values()
        for item in inventory_items.values():
            if item.get("sku") == sku and item.get("store_id") == store_id:
                payload = item
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryItemBySkuAndStore",
                "description": "Retrieves detailed information for a specific inventory item by its SKU and store ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The ID of the store where the inventory is located.",
                        },
                    },
                    "required": ["sku", "store_id"],
                },
            },
        }


class GetPromotionByNameAndDate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_name: str = None, query_date: str = None) -> str:
        promotions = data.get("promotions", {}).values()

        if not query_date:
            payload = {}
            out = json.dumps(payload)
            return out

        try:
            query_date_obj = datetime.strptime(query_date, "%Y-%m-%d").date()
        except ValueError:
            payload = {"error": "Invalid date format for query_date. Use YYYY-MM-DD."}
            out = json.dumps(payload)
            return out

        for promo in promotions.values():
            if promo.get("name") == promotion_name:
                start_date_str = promo.get("start_date", "").split("T")[0]
                end_date_str = promo.get("end_date", "").split("T")[0]

                if promo.get("status") == "active" and start_date_str and end_date_str:
                    try:
                        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
                        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

                        if start_date <= query_date_obj <= end_date:
                            payload = promo
                            out = json.dumps(payload)
                            return out
                    except ValueError:
                        continue
        payload = {}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPromotionByNameAndDate",
                "description": "Retrieves details of a promotion by its name, only if it is active on the specified query date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_name": {
                            "type": "string",
                            "description": "The name of the promotion.",
                        },
                        "query_date": {
                            "type": "string",
                            "format": "date",
                            "description": "The date to check for promotion activity (YYYY-MM-DD).",
                        },
                    },
                    "required": ["promotion_name", "query_date"],
                },
            },
        }


class GetCustomerIdByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_name: str = None) -> str:
        customers = data.get("customers", {}).values()
        for customer in customers.values():
            if customer.get("name") == customer_name:
                payload = {"customer_id": customer.get("customer_id")}
                out = json.dumps(payload)
                return out
        payload = {"customer_id": None}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerIdByName",
                "description": "Retrieves the customer ID for a given customer name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_name": {
                            "type": "string",
                            "description": "The full name of the customer.",
                        },
                    },
                    "required": ["customer_name"],
                },
            },
        }


class CreateCustomer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, membership_level: str = None, 
               opt_in_marketing: bool = None, loyalty_points: int = None) -> str:
        customers = data.get("customers", {}).values()

        max_customer_id_num = 0
        for customer in customers.values():
            if isinstance(customer.get("customer_id"), str):
                match = re.match(r"CUST-(\d+)", customer["customer_id"])
                if match:
                    num = int(match.group(1))
                    max_customer_id_num = max(max_customer_id_num, num)

        next_customer_id_num = max_customer_id_num + 1
        new_customer_id = f"CUST-{next_customer_id_num}"

        new_customer = {
            "customer_id": new_customer_id,
            "name": name,
            "phone_number": None,
            "loyalty_points": loyalty_points,
            "email": f"{str(name).replace(' ', '.').lower()}@example.com",
            "address": None,
            "membership_level": membership_level,
            "birthdate": None,
            "opt_in_marketing": opt_in_marketing,
            "status": "active",
        }

        data["customers"][customer_id] = new_customer
        data["customers"] = customers
        payload = {"customer_id": new_customer_id}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCustomer",
                "description": "Creates a new customer record with specified details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The full name of the new customer.",
                        },
                        "membership_level": {
                            "type": "string",
                            "description": "The membership level for the new customer (e.g., 'basic', 'silver', 'gold', 'platinum').",
                        },
                        "opt_in_marketing": {
                            "type": "boolean",
                            "description": "Indicates if the customer has opted into marketing communications.",
                        },
                        "loyalty_points": {
                            "type": "integer",
                            "description": "The initial loyalty points for the customer.",
                        },
                    },
                    "required": [
                        "name",
                        "membership_level",
                        "opt_in_marketing",
                        "loyalty_points",
                    ],
                },
            },
        }


class UpdateInventorySale(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None, quantity_sold: int = None, last_stock_count_date: str = None) -> str:
        inventory_items = data.get("inventory", {}).values()
        updated_item = None
        for item in inventory_items.values():
            if item.get("id") == inventory_id:
                item["quantity"] = item.get("quantity", 0) - quantity_sold
                item["reserved_quantity"] = max(
                    0, item.get("reserved_quantity", 0) - quantity_sold
                )
                item["last_stock_count"] = last_stock_count_date
                updated_item = item
                break
        payload = {"updated_inventory_item": updated_item}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventorySale",
                "description": "Updates inventory quantities and last stock count date after a sale.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "Unique identifier of the inventory item to update.",
                        },
                        "quantity_sold": {
                            "type": "integer",
                            "description": "The number of units sold.",
                        },
                        "last_stock_count_date": {
                            "type": "string",
                            "format": "date",
                            "description": "The date of the last stock count (YYYY-MM-DD).",
                        },
                    },
                    "required": [
                        "inventory_id",
                        "quantity_sold",
                        "last_stock_count_date",
                    ],
                },
            },
        }


class CreateTransaction(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        store_id: str = None,
        employee_id: str = None,
        total_amount: float = 0.0,
        tax_amount: float = 0.0,
        payment_method: str = None,
        discount_total: float = 0.0,
        customer_id: str = None,
        line_items: list = []
,
    status: Any = None,
    ) -> str:
        transactions = data.get("transactions", {}).values()

        max_transaction_id_num = 0
        for transaction in transactions.values():
            txn_id = transaction.get("transaction_id")
            if isinstance(txn_id, str):
                match = re.match(r"TXN-(\d+)", txn_id)
                if match:
                    num = int(match.group(1))
                    max_transaction_id_num = max(max_transaction_id_num, num)

        next_transaction_id_num = max_transaction_id_num + 1
        new_transaction_id = f"TXN-{next_transaction_id_num:04d}"

        new_transaction = {
            "transaction_id": new_transaction_id,
            "store_id": store_id,
            "employee_id": employee_id,
            "total_amount": total_amount,
            "tax_amount": tax_amount,
            "payment_method": payment_method,
            "tax_rate": 0.0825,
            "discount_total": discount_total,
            "change_given": 0.0,
            "status": "completed",
            "customer_id": customer_id,
            "line_items": line_items,
        }

        data["transactions"][transaction_id] = new_transaction
        data["transactions"] = transactions
        payload = {"transaction_id": new_transaction_id}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTransaction",
                "description": "Creates a new transaction record for a completed sale.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "The ID of the store where the transaction occurred.",
                        },
                        "employee_id": {
                            "type": "string",
                            "description": "The ID of the employee who processed the transaction.",
                        },
                        "total_amount": {
                            "type": "number",
                            "format": "float",
                            "description": "The total amount of the transaction.",
                        },
                        "tax_amount": {
                            "type": "number",
                            "format": "float",
                            "description": "The total tax amount applied to the transaction.",
                        },
                        "payment_method": {
                            "type": "string",
                            "description": "The method of payment used for the transaction (e.g., 'credit_card', 'cash', 'mobile_wallet').",
                        },
                        "discount_total": {
                            "type": "number",
                            "format": "float",
                            "description": "The total discount applied to the transaction.",
                        },
                        "customer_id": {
                            "type": "string",
                            "description": "The ID of the customer associated with the transaction.",
                        },
                        "line_items": {
                            "type": "array",
                            "description": "A list of items included in the transaction.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                    "unit_price": {"type": "number", "format": "float"},
                                    "discount": {"type": "number", "format": "float"},
                                },
                                "required": [
                                    "sku",
                                    "quantity",
                                    "unit_price",
                                    "discount",
                                ],
                            },
                        },
                    },
                    "required": [
                        "store_id",
                        "employee_id",
                        "total_amount",
                        "tax_amount",
                        "payment_method",
                        "discount_total",
                        "customer_id",
                        "line_items",
                    ],
                },
            },
        }


class GetEmployeeIdByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_name: str = None) -> str:
        employees = data.get("employees", {}).values()

        for employee in employees.values():
            if employee.get("name") == employee_name:
                payload = {"employee_id": employee.get("employee_id")}
                out = json.dumps(payload)
                return out
        payload = {"employee_id": None}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeIdByName",
                "description": "Retrieves the employee ID for a given employee's full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_name": {
                            "type": "string",
                            "description": "The full name of the employee.",
                        },
                    },
                    "required": ["employee_name"],
                },
            },
        }


class ActivatePromotion(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_id: str = None) -> str:
        promotions = data.get("promotions", {}).values()
        for promo in promotions.values():
            if promo.get("promotion_id") == promotion_id:
                promo["status"] = "active"
                payload = {"promotion_id": promotion_id, "status": "active"}
                out = json.dumps(payload)
                return out
        payload = {"promotion_id": promotion_id, "status": "not_found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ActivatePromotion",
                "description": "Activates a promotion by setting its status to 'active'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "The ID of the promotion to activate.",
                        },
                    },
                    "required": ["promotion_id"],
                },
            },
        }


class DeactivatePromotion(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_id: str = None) -> str:
        promotions = data.get("promotions", {}).values()
        for promo in promotions.values():
            if promo.get("promotion_id") == promotion_id:
                promo["status"] = "inactive"
                payload = {"promotion_id": promotion_id, "status": "inactive"}
                out = json.dumps(payload)
                return out
        payload = {"promotion_id": promotion_id, "status": "not_found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeactivatePromotion",
                "description": "Deactivates a promotion by setting its status to 'inactive'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "The ID of the promotion to deactivate.",
                        },
                    },
                    "required": ["promotion_id"],
                },
            },
        }


class UpdatePromotionDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_id: str, key: str = None, value: Any = None,
    usage_limit: Any = None,
    times_used: Any = None,
    name: Any = None,
    description: Any = None,
    applicable_skus: Any = None,
    status: Any = None,
    end_date: Any = None,
    discount_value: Any = None,
    start_date: Any = None,
    requires_code: Any = None,
    type: Any = None,
    ) -> str:
        promotions = data.get("promotions", {}).values()
        updated_promo = None
        for promo in promotions.values():
            if promo.get("promotion_id") == promotion_id:
                if key is not None and value is not None:
                    promo[key] = value
                updated_promo = promo
                break
        payload = {"updated_promotion": updated_promo}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdatePromotionDetails",
                "description": "Updates various details of an existing promotion.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "The ID of the promotion to update.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The new name of the promotion.",
                        },
                        "type": {
                            "type": "string",
                            "description": "The new type of the promotion (e.g., 'percentage', 'fixed_bundle').",
                        },
                        "discount_value": {
                            "type": "number",
                            "description": "The new discount value.",
                        },
                        "description": {
                            "type": "string",
                            "description": "A new description for the promotion.",
                        },
                        "applicable_skus": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of SKUs the promotion applies to.",
                        },
                        "start_date": {
                            "type": "string",
                            "format": "date",
                            "description": "The new start date of the promotion (YYYY-MM-DD).",
                        },
                        "end_date": {
                            "type": "string",
                            "format": "date",
                            "description": "The new end date of the promotion (YYYY-MM-DD).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status of the promotion (e.g., 'active', 'scheduled', 'planned', 'inactive').",
                        },
                        "usage_limit": {
                            "type": "integer",
                            "description": "The new usage limit for the promotion.",
                        },
                        "times_used": {
                            "type": "integer",
                            "description": "The new number of times the promotion has been used.",
                        },
                    },
                    "required": ["promotion_id"],
                },
            },
        }


class GetPromotionsByStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], status: str = None) -> str:
        promotions = data.get("promotions", {}).values()
        results = [promo for promo in promotions.values() if promo.get("status") == status]
        payload = results
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPromotionsByStatus",
                "description": "Retrieves all promotions with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status of the promotions to retrieve (e.g., 'active', 'scheduled', 'planned', 'inactive').",
                        },
                    },
                    "required": ["status"],
                },
            },
        }


class GetProductDetailsBySKU(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None) -> str:
        products = data.get("products", {}).values()
        for product in products.values():
            if product.get("sku") == sku:
                payload = product
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductDetailsBySku",
                "description": "Retrieves all details for a product given its SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                    },
                    "required": ["sku"],
                },
            },
        }


class UpdateProductDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str, name: str = None, price: float = None, description: str = None,
    is_discountable: Any = None,
    category: Any = None,
    status: Any = None,
    ) -> str:
        products = data.get("products", {}).values()
        updated_product = None
        for product in products.values():
            if product.get("sku") == sku:
                if name is not None:
                    product["name"] = name
                if price is not None:
                    product["price"] = price
                if description is not None:
                    product["description"] = description
                updated_product = product
                break
        payload = {"updated_product": updated_product}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProductDetails",
                "description": "Updates various details of an existing product by SKU. Can update 'status', 'is_discountable', 'price', etc.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to update.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The new name of the product.",
                        },
                        "category": {
                            "type": "string",
                            "description": "The new category of the product.",
                        },
                        "price": {
                            "type": "number",
                            "format": "float",
                            "description": "The new price of the product.",
                        },
                        "is_discountable": {
                            "type": "boolean",
                            "description": "New discountability status.",
                        },
                        "description": {
                            "type": "string",
                            "description": "A new description for the product.",
                        },
                        "supplier_id": {
                            "type": "string",
                            "description": "The new supplier ID.",
                        },
                        "weight_kg": {
                            "type": "number",
                            "format": "float",
                            "description": "The new weight in kg.",
                        },
                        "dimensions_cm": {
                            "type": "string",
                            "description": "The new dimensions (LxWxH).",
                        },
                        "brand": {
                            "type": "string",
                            "description": "The new brand of the product.",
                        },
                        "cost": {
                            "type": "number",
                            "format": "float",
                            "description": "The new cost of the product.",
                        },
                        "barcode": {
                            "type": "string",
                            "description": "The new barcode.",
                        },
                        "tax_rate": {
                            "type": "number",
                            "format": "float",
                            "description": "The new tax rate.",
                        },
                        "discount_rate": {
                            "type": "number",
                            "format": "float",
                            "description": "The new default discount rate.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status of the product (e.g., 'active', 'discontinued', 'clearance', 'limited_availability').",
                        },
                        "expiry_date": {
                            "type": ["string", "null"],
                            "format": "date",
                            "description": "The new expiry date (YYYY-MM-DD), or null.",
                        },
                    },
                    "required": ["sku"],
                },
            },
        }


class UpdateCustomerLoyaltyPoints(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str = None, points_to_add: int = None) -> str:
        customers = data.get("customers", {}).values()
        updated_customer = None
        for customer in customers.values():
            if customer.get("customer_id") == customer_id:
                customer["loyalty_points"] = (
                    customer.get("loyalty_points", 0) + points_to_add
                )
                updated_customer = customer
                break
        payload = {"updated_customer": updated_customer}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomerLoyaltyPoints",
                "description": "Adds loyalty points to a customer's record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The ID of the customer to update.",
                        },
                        "points_to_add": {
                            "type": "integer",
                            "description": "The number of loyalty points to add.",
                        },
                    },
                    "required": ["customer_id", "points_to_add"],
                },
            },
        }


class UpdateInventoryReservedQuantity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None, change_amount: int = None) -> str:
        inventory_items = data.get("inventory", {}).values()
        updated_item = None
        for item in inventory_items.values():
            if item.get("id") == inventory_id:
                item["reserved_quantity"] = (
                    item.get("reserved_quantity", 0) + change_amount
                )
                updated_item = item
                break
        payload = {"updated_inventory_item": updated_item}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryReservedQuantity",
                "description": "Updates the reserved quantity for an inventory item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "Unique identifier of the inventory item to update.",
                        },
                        "change_amount": {
                            "type": "integer",
                            "description": "The amount to change the reserved quantity by (positive for add, negative for remove).",
                        },
                    },
                    "required": ["inventory_id", "change_amount"],
                },
            },
        }


class GetPromotionById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_id: str = None) -> str:
        promotions = data.get("promotions", {}).values()
        for promo in promotions.values():
            if promo.get("promotion_id") == promotion_id:
                payload = promo
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPromotionById",
                "description": "Retrieves details of a promotion by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "The unique ID of the promotion.",
                        },
                    },
                    "required": ["promotion_id"],
                },
            },
        }


class CreatePromotion(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        name: str = None,
        promotion_type: str = None,
        discount_value: float = None,
        description: str = None,
        applicable_skus: list[str] = None,
        start_date: str = None,
        end_date: str = None,
        status: str = None,
        usage_limit: int = None,
        times_used: int = None
,
    type: Any = None,
    ) -> str:
        promotions = data.get("promotions", {}).values()

        max_promotion_id_num = 0
        for promo in promotions.values():
            if isinstance(promo.get("promotion_id"), str):
                match = re.match(r"PROMO-(\d+)", promo["promotion_id"])
                if match:
                    num = int(match.group(1))
                    if num > max_promotion_id_num:
                        max_promotion_id_num = num

        next_promotion_id_num = max_promotion_id_num + 1
        new_promotion_id = f"PROMO-{next_promotion_id_num:03d}"

        new_promotion = {
            "promotion_id": new_promotion_id,
            "name": name,
            "type": promotion_type,
            "discount_value": discount_value,
            "description": description,
            "applicable_skus": applicable_skus,
            "start_date": start_date,
            "end_date": end_date,
            "status": status,
            "usage_limit": usage_limit,
            "times_used": times_used,
        }

        data["promotions"][promotion_id] = new_promotion
        data["promotions"] = promotions
        payload = {"promotion_id": new_promotion_id}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePromotion",
                "description": "Creates a new promotion record with specified details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of the new promotion.",
                        },
                        "type": {
                            "type": "string",
                            "description": "The type of the promotion (e.g., 'percentage', 'fixed_bundle', 'bogo_percentage', 'tax_free').",
                        },
                        "discount_value": {
                            "type": "number",
                            "description": "The discount value (e.g., 10.0 for 10% or $10).",
                        },
                        "description": {
                            "type": "string",
                            "description": "A brief description of the promotion.",
                        },
                        "applicable_skus": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of SKUs the promotion applies to.",
                        },
                        "start_date": {
                            "type": "string",
                            "format": "date",
                            "description": "The start date of the promotion (YYYY-MM-DD).",
                        },
                        "end_date": {
                            "type": "string",
                            "format": "date",
                            "description": "The end date of the promotion (YYYY-MM-DD).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The initial status of the promotion (e.g., 'active', 'scheduled', 'planned').",
                        },
                        "usage_limit": {
                            "type": ["integer", "null"],
                            "description": "The maximum number of times this promotion can be used, or null if unlimited.",
                        },
                        "times_used": {
                            "type": "integer",
                            "description": "The initial count of how many times the promotion has been used.",
                        },
                    },
                    "required": [
                        "name",
                        "type",
                        "discount_value",
                        "description",
                        "applicable_skus",
                        "start_date",
                        "end_date",
                        "status",
                        "times_used",
                    ],
                },
            },
        }


class GetProductByStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], status: str = None) -> str:
        products = data.get("products", {}).values()
        results = [product for product in products.values() if product.get("status") == status]
        payload = results
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getProductByStatus",
                "description": "Retrieves products with a specific status (e.g., 'active', 'discontinued', 'clearance', 'limited_availability').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status of the products to retrieve.",
                        },
                    },
                    "required": ["status"],
                },
            },
        }


class UpdateCustomerDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str, name: str = None, email: str = None, phone: str = None,
        address: Any = None,
        opt_in_marketing: Any = None,
        membership_level: Any = None,
        status: Any = None,
        phone_number: Any = None,
    ) -> str:
        customers = data.get("customers", {}).values()
        updated_customer = None
        for customer in customers.values():
            if customer.get("customer_id") == customer_id:
                if name is not None:
                    customer["name"] = name
                if email is not None:
                    customer["email"] = email
                if phone is not None:
                    customer["phone"] = phone
                customer["updated_at"] = "2025-07-28T16:38:15Z"
                updated_customer = customer
                break
        payload = {"updated_customer": updated_customer}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomerDetails",
                "description": "Updates various details of an existing customer record by ID. Can update 'membership_level', 'email', 'phone_number', 'address', etc.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The ID of the customer to update.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The new full name of the customer.",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "The new contact phone number.",
                        },
                        "email": {
                            "type": "string",
                            "description": "The new company email address.",
                        },
                        "address": {
                            "type": "string",
                            "description": "The new physical address.",
                        },
                        "membership_level": {
                            "type": "string",
                            "description": "The new membership level (e.g., 'basic', 'silver', 'gold', 'platinum', 'diamond').",
                        },
                        "birthdate": {
                            "type": "string",
                            "format": "date",
                            "description": "The new birthdate (YYYY-MM-DD).",
                        },
                        "opt_in_marketing": {
                            "type": "boolean",
                            "description": "New marketing opt-in status.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new employment status (e.g. 'active', 'inactive', 'terminated').",
                        },
                    },
                    "required": ["customer_id"],
                },
            },
        }


class UpdateInventoryStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None, status: str = None) -> str:
        inventory_items = data.get("inventory", {}).values()
        updated_item = None
        for item in inventory_items.values():
            if item.get("id") == inventory_id:
                item["status"] = status
                updated_item = item
                break
        payload = {"updated_inventory_item": updated_item}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryStatus",
                "description": "Updates the status of an inventory item (e.g., 'in_stock', 'low_stock', 'out_of_stock', 'critical').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "Unique identifier of the inventory item to update.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status of the inventory item.",
                        },
                    },
                    "required": ["inventory_id", "status"],
                },
            },
        }


class GetCustomerDetailsById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str = None) -> str:
        customers = data.get("customers", {}).values()
        for customer in customers.values():
            if customer.get("customer_id") == customer_id:
                payload = customer
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerDetailsById",
                "description": "Retrieves all details for a customer given their ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The ID of the customer.",
                        },
                    },
                    "required": ["customer_id"],
                },
            },
        }


class FindTransactionByCustomerAndSku(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str = None, sku: str = None) -> str:
        transactions = data.get("transactions", {}).values()
        for txn in transactions.values():
            if txn.get("customer_id") == customer_id:
                for item in txn.get("line_items", []):
                    if item.get("sku") == sku:
                        payload = {
                            "transaction_id": txn.get("transaction_id"),
                            "unit_price": item.get("unit_price"),
                        }
                        out = json.dumps(payload)
                        return out
        payload = {}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindTransactionByCustomerAndSku",
                "description": "Finds a past transaction for a customer containing a specific SKU and returns its ID and the item's unit price.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The customer's unique ID.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to find.",
                        },
                    },
                    "required": ["customer_id", "sku"],
                },
            },
        }


class ProcessItemReturn(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], transaction_id: str = None, sku: str = None, quantity_returned: int = None, unit_price: float = None) -> str:
        transactions = data.get("transactions", {}).values()
        inventory = data.get("inventory", {}).values()

        for txn in transactions.values():
            if txn.get("transaction_id") == transaction_id:
                txn["status"] = "returned"
                break

        for item in inventory.values():
            if item.get("sku") == sku:
                item["quantity"] += quantity_returned
                break

        credit_amount = unit_price * quantity_returned
        payload = {"status": "success", "credit_amount": credit_amount}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessItemReturn",
                "description": "Processes an item return and calculates the credit amount based on the original unit price.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {
                            "type": "string",
                            "description": "The ID of the transaction for the return.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the item being returned.",
                        },
                        "quantity_returned": {
                            "type": "integer",
                            "description": "The quantity of the item being returned.",
                        },
                        "unit_price": {
                            "type": "number",
                            "description": "The original unit price of the item for credit calculation.",
                        },
                    },
                    "required": [
                        "transaction_id",
                        "sku",
                        "quantity_returned",
                        "unit_price",
                    ],
                },
            },
        }


class GetProductsByCategory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], category: str = None) -> str:
        products = data.get("products", {}).values()
        results = [
            product for product in products.values() if product.get("category") == category
        ]
        payload = results
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductsByCategory",
                "description": "Retrieves all products that belong to a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The category of the products to retrieve.",
                        },
                    },
                    "required": ["category"],
                },
            },
        }


class ExecuteInventoryTransfer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, quantity: int = None, from_store_id: int = None, to_store_id: int = None) -> str:
        inventory = data.get("inventory", {}).values()
        from_item = None
        to_item = None

        for item in inventory.values():
            if item["store_id"] == from_store_id and item["sku"] == sku:
                from_item = item
            if item["store_id"] == to_store_id and item["sku"] == sku:
                to_item = item

        if from_item and to_item:
            from_item["quantity"] -= quantity
            to_item["quantity"] += quantity
            payload = {
                "status": "success",
                "sku": sku,
                "quantity": quantity,
                "from_store": from_store_id,
                "to_store": to_store_id,
            }
            out = json.dumps(payload)
            return out
        payload = {
            "status": "failed",
            "reason": "Inventory item not found in one or both stores.",
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExecuteInventoryTransfer",
                "description": "Executes a stock transfer of a specific SKU from one store to another.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to transfer.",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "The quantity of stock to transfer.",
                        },
                        "from_store_id": {
                            "type": "string",
                            "description": "The ID of the origin store.",
                        },
                        "to_store_id": {
                            "type": "string",
                            "description": "The ID of the destination store.",
                        },
                    },
                    "required": ["sku", "quantity", "from_store_id", "to_store_id"],
                },
            },
        }


class CreateInventoryRecord(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, store_id: str = None, location: str = None) -> str:
        inventory_list = data.get("inventory", {}).values()

        for item in inventory_list.values():
            if item.get("sku") == sku and item.get("store_id") == store_id:
                payload = {"status": "exists", "inventory_id": item.get("id")}
                out = json.dumps(payload)
                return out

        max_inv_id_num = 0
        for item in inventory_list.values():
            inv_id = item.get("id")
            if isinstance(inv_id, str):
                match = re.match(r"INV-(\d+)", inv_id)
                if match:
                    num = int(match.group(1))
                    if num > max_inv_id_num:
                        max_inv_id_num = num

        next_inv_id_num = max_inv_id_num + 1
        new_inv_id = f"INV-{next_inv_id_num:04d}"

        new_record = {
            "id": new_inv_id,
            "sku": sku,
            "store_id": store_id,
            "quantity": 0,
            "reserved_quantity": 0,
            "reorder_level": 10,
            "safety_stock": 5,
            "location": location,
            "status": "out_of_stock",
            "last_stock_count": "2025-07-28",
        }

        data["inventory"][inventory_id] = new_record
        data["inventory"] = inventory_list
        payload = {"status": "created", "inventory_id": new_inv_id}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInventoryRecord",
                "description": "Creates a new inventory record for a product at a specific store, if one does not already exist.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The ID of the store.",
                        },
                        "location": {
                            "type": "string",
                            "description": "A placeholder location for the new inventory record.",
                        },
                    },
                    "required": ["sku", "store_id", "location"],
                },
            },
        }


class CalculateTransactionTotals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], line_items: list = None, promotion_ids: list = None, credit_amount: float = 0.0) -> str:
        if line_items is None:
            line_items = []
        if promotion_ids is None:
            promotion_ids = []

        products = data.get("products", {}).values()
        promotions = data.get("promotions", {}).values()

        subtotal = 0.0
        total_discount = 0.0
        final_line_items = []

        for item in line_items:
            sku = item.get("sku")
            quantity = item.get("quantity")
            product_details = next((p for p in products.values() if p["sku"] == sku), None)

            if not product_details:
                continue

            price = product_details.get("price", 0.0)
            item_subtotal = price * quantity
            subtotal += item_subtotal

            item_discount_value = 0.0

            for promo_id in promotion_ids:
                promo = next(
                    (p for p in promotions.values() if p["promotion_id"] == promo_id), None
                )
                if promo and sku in promo.get("applicable_skus", []):
                    if promo.get("type") == "percentage":
                        item_discount_value = item_subtotal * (
                            promo.get("discount_value", 0.0) / 100.0
                        )

            total_discount += item_discount_value
            final_line_items.append(
                {
                    "sku": sku,
                    "quantity": quantity,
                    "unit_price": price,
                    "discount": (
                        round(item_discount_value / quantity, 2)
                        if quantity > 0
                        else 0.0
                    ),
                }
            )

        subtotal_after_discount = subtotal - total_discount
        final_subtotal = subtotal_after_discount - credit_amount

        tax_rate = 0.0825
        total_tax = final_subtotal * tax_rate
        final_total = final_subtotal + total_tax
        payload = {
            "calculated_total_amount": round(final_total, 2),
            "calculated_tax_amount": round(total_tax, 2),
            "calculated_discount_total": round(total_discount, 2),
            "calculated_line_items": final_line_items,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTransactionTotals",
                "description": "Calculates the final total, tax, and discount for a transaction based on items, promotions, and credits.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "line_items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "promotion_ids": {"type": "array", "items": {"type": "string"}},
                        "credit_amount": {"type": "number"},
                    },
                    "required": ["line_items"],
                },
            },
        }


class UpdateStockLevel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None, quantity_to_add: int = None) -> str:
        inventory = data.get("inventory", {}).values()

        found_item = None
        for item in inventory.values():
            if item.get("id") == inventory_id:
                found_item = item
                break

        if found_item:
            found_item["quantity"] += quantity_to_add
            if found_item["quantity"] > found_item.get("reorder_level", 0):
                found_item["status"] = "in_stock"
            elif found_item["quantity"] > 0:
                found_item["status"] = "low_stock"
            else:
                found_item["status"] = "out_of_stock"
            payload = {
                "status": "success",
                "inventory_id": inventory_id,
                "new_quantity": found_item["quantity"],
            }
            out = json.dumps(payload)
            return out
        payload = {"status": "error", "reason": "Inventory ID not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateStockLevel",
                "description": "Updates the stock level for an inventory item, e.g., when receiving a shipment or correcting a count.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "The unique ID of the inventory item.",
                        },
                        "quantity_to_add": {
                            "type": "integer",
                            "description": "The number of units to add to the current quantity (can be negative).",
                        },
                    },
                    "required": ["inventory_id", "quantity_to_add"],
                },
            },
        }


class FindCustomersByCriteria(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], membership_levels: list = None, purchase_history_skus: list = None) -> str:
        if membership_levels is None:
            membership_levels = []
        if purchase_history_skus is None:
            purchase_history_skus = []

        customers = data.get("customers", {}).values()
        transactions = data.get("transactions", {}).values()

        qualified_customers = []

        for customer in customers.values():
            if customer.get("membership_level") in membership_levels:
                customer_id = customer.get("customer_id")
                for txn in transactions.values():
                    if txn.get("customer_id") == customer_id:
                        for item in txn.get("line_items", []):
                            if item.get("sku") in purchase_history_skus:
                                qualified_data["customers"][customer_id] = customer
                                break
                        break
        payload = qualified_customers
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCustomersByCriteria",
                "description": "Finds customers based on multiple criteria like membership level and purchase history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "membership_levels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of membership levels to filter by (e.g., ['gold', 'platinum']).",
                        },
                        "purchase_history_skus": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of product SKUs to check for in the customers' purchase history.",
                        },
                    },
                    "required": ["membership_levels"],
                },
            },
        }


class GenerateAndAssignPromoCodes(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_ids: list[str] = None, promotion_id: str = None) -> str:
        if customer_ids is None:
            customer_ids = []

        if "promo_codes" not in data:
            data["promo_codes"] = {}

        generated_assignments = []
        for cid in customer_ids:
            unique_code = f"VIP-{promotion_id}-{cid[-4:]}"
            assignment = {
                "code": unique_code,
                "promotion_id": promotion_id,
                "customer_id": cid,
                "is_used": False,
            }
            data["promo_codes"][unique_code] = assignment
            generated_assignments.append(assignment)
        payload = generated_assignments
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateAndAssignPromoCodes",
                "description": "Generates unique, single-use promotion codes and assigns them to a list of customers for a specific promotion.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of customer IDs to receive the unique codes.",
                        },
                        "promotion_id": {
                            "type": "string",
                            "description": "The ID of the promotion to associate the codes with.",
                        },
                    },
                    "required": ["customer_ids", "promotion_id"],
                },
            },
        }


TOOLS = [
    GetProductSkuByName(),
    GetInventoryItemBySkuAndStore(),
    GetPromotionByNameAndDate(),
    GetCustomerIdByName(),
    CreateCustomer(),
    UpdateInventorySale(),
    CreateTransaction(),
    GetEmployeeIdByName(),
    ActivatePromotion(),
    DeactivatePromotion(),
    UpdatePromotionDetails(),
    GetPromotionsByStatus(),
    GetProductDetailsBySKU(),
    UpdateProductDetails(),
    UpdateCustomerLoyaltyPoints(),
    UpdateInventoryReservedQuantity(),
    GetPromotionById(),
    CreatePromotion(),
    GetProductByStatus(),
    UpdateCustomerDetails(),
    UpdateInventoryStatus(),
    GetCustomerDetailsById(),
    FindTransactionByCustomerAndSku(),
    ProcessItemReturn(),
    GetProductsByCategory(),
    ExecuteInventoryTransfer(),
    CreateInventoryRecord(),
    CalculateTransactionTotals(),
    UpdateStockLevel(),
    FindCustomersByCriteria(),
    GenerateAndAssignPromoCodes(),
]