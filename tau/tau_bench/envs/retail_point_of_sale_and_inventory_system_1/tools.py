import json
from typing import Dict, Any
import re
from datetime import datetime

from domains.dto import Tool

class GetProductSkuByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_name = kwargs.get('product_name')
        products = data.get("products", [])
        for product in products:
            if product.get("name") == product_name:
                return json.dumps({"sku": product.get("sku")})
        return json.dumps({"sku": None})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_sku_by_name",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get('sku')
        store_id = kwargs.get('store_id')
        inventory_items = data.get("inventory", [])
        for item in inventory_items:
            if item.get("sku") == sku and item.get("store_id") == store_id:
                return json.dumps(item)
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_item_by_sku_and_store",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        promotion_name = kwargs.get('promotion_name')
        query_date_str = kwargs.get('query_date')
        promotions = data.get("promotions", [])

        if not query_date_str:
            return json.dumps({})

        try:
            query_date = datetime.strptime(query_date_str, "%Y-%m-%d").date()
        except ValueError:
            return json.dumps({"error": "Invalid date format for query_date. Use YYYY-MM-DD."})

        for promo in promotions:
            if promo.get("name") == promotion_name:
                start_date_str = promo.get("start_date", "").split("T")[0]
                end_date_str = promo.get("end_date", "").split("T")[0]

                if promo.get("status") == "active" and start_date_str and end_date_str:
                    try:
                        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
                        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

                        if start_date <= query_date <= end_date:
                            return json.dumps(promo)
                    except ValueError:
                        continue
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_promotion_by_name_and_date",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_name = kwargs.get('customer_name')
        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("name") == customer_name:
                return json.dumps({"customer_id": customer.get("customer_id")})
        return json.dumps({"customer_id": None})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_id_by_name",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get('name')
        membership_level = kwargs.get('membership_level')
        opt_in_marketing = kwargs.get('opt_in_marketing')
        loyalty_points = kwargs.get('loyalty_points')

        customers = data.get("customers", [])

        max_customer_id_num = 0
        for customer in customers:
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
            "status": "active"
        }

        customers.append(new_customer)
        data["customers"] = customers

        return json.dumps({"customer_id": new_customer_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_customer",
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
                        }
                    },
                    "required": ["name", "membership_level", "opt_in_marketing", "loyalty_points"],
                },
            },
        }

class UpdateInventorySale(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_id = kwargs.get('inventory_id')
        quantity_sold = kwargs.get('quantity_sold')
        last_stock_count_date = kwargs.get('last_stock_count_date')
        inventory_items = data.get("inventory", [])
        updated_item = None
        for item in inventory_items:
            if item.get("id") == inventory_id:
                item["quantity"] = item.get("quantity", 0) - quantity_sold
                item["reserved_quantity"] = max(0, item.get("reserved_quantity", 0) - quantity_sold)
                item["last_stock_count"] = last_stock_count_date
                updated_item = item
                break
        return json.dumps({"updated_inventory_item": updated_item})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_sale",
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
                    "required": ["inventory_id", "quantity_sold", "last_stock_count_date"],
                },
            },
        }

class CreateTransaction(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs.get('store_id')
        employee_id = kwargs.get('employee_id')
        total_amount = kwargs.get('total_amount', 0.0)
        tax_amount = kwargs.get('tax_amount', 0.0)
        payment_method = kwargs.get('payment_method')
        discount_total = kwargs.get('discount_total', 0.0)
        customer_id = kwargs.get('customer_id')
        line_items = kwargs.get('line_items', [])

        transactions = data.get("transactions", [])

        max_transaction_id_num = 0
        for transaction in transactions:
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

        transactions.append(new_transaction)
        data["transactions"] = transactions

        return json.dumps({"transaction_id": new_transaction_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_transaction",
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
                                "required": ["sku", "quantity", "unit_price", "discount"],
                            },
                        },
                    },
                    "required": ["store_id", "employee_id", "total_amount", "tax_amount", "payment_method", "discount_total", "customer_id", "line_items"],
                },
            },
        }

class GetEmployeeIdByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_name = kwargs.get("employee_name")
        employees = data.get("employees", [])

        for employee in employees:
            if employee.get("name") == employee_name:
                return json.dumps({"employee_id": employee.get("employee_id")})

        return json.dumps({"employee_id": None})


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_id_by_name",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        promotion_id = kwargs.get('promotion_id')
        promotions = data.get("promotions", [])
        for promo in promotions:
            if promo.get("promotion_id") == promotion_id:
                promo["status"] = "active"
                return json.dumps({"promotion_id": promotion_id, "status": "active"})
        return json.dumps({"promotion_id": promotion_id, "status": "not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "activate_promotion",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        promotion_id = kwargs.get('promotion_id')
        promotions = data.get("promotions", [])
        for promo in promotions:
            if promo.get("promotion_id") == promotion_id:
                promo["status"] = "inactive"
                return json.dumps({"promotion_id": promotion_id, "status": "inactive"})
        return json.dumps({"promotion_id": promotion_id, "status": "not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deactivate_promotion",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        promotion_id = kwargs.get('promotion_id')
        promotions = data.get("promotions", [])
        updated_promo = None
        for promo in promotions:
            if promo.get("promotion_id") == promotion_id:
                for key, value in kwargs.items():
                    if key != 'promotion_id':
                        promo[key] = value
                updated_promo = promo
                break
        return json.dumps({"updated_promotion": updated_promo})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_promotion_details",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get('status')
        promotions = data.get("promotions", [])
        results = [promo for promo in promotions if promo.get("status") == status]
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_promotions_by_status",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get('sku')
        products = data.get("products", [])
        for product in products:
            if product.get("sku") == sku:
                return json.dumps(product)
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_details_by_sku",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get('sku')
        products = data.get("products", [])
        updated_product = None
        for product in products:
            if product.get("sku") == sku:
                for key, value in kwargs.items():
                    if key != 'sku':
                        product[key] = value
                updated_product = product
                break
        return json.dumps({"updated_product": updated_product})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_product_details",
                "description": "Updates various details of an existing product by SKU. Can update 'status', 'is_discountable', 'price', etc.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to update.",
                        },
                        "name": {"type": "string", "description": "The new name of the product."},
                        "category": {"type": "string", "description": "The new category of the product."},
                        "price": {"type": "number", "format": "float", "description": "The new price of the product."},
                        "is_discountable": {"type": "boolean", "description": "New discountability status."},
                        "description": {"type": "string", "description": "A new description for the product."},
                        "supplier_id": {"type": "string", "description": "The new supplier ID."},
                        "weight_kg": {"type": "number", "format": "float", "description": "The new weight in kg."},
                        "dimensions_cm": {"type": "string", "description": "The new dimensions (LxWxH)."},
                        "brand": {"type": "string", "description": "The new brand of the product."},
                        "cost": {"type": "number", "format": "float", "description": "The new cost of the product."},
                        "barcode": {"type": "string", "description": "The new barcode."},
                        "tax_rate": {"type": "number", "format": "float", "description": "The new tax rate."},
                        "discount_rate": {"type": "number", "format": "float", "description": "The new default discount rate."},
                        "status": {"type": "string", "description": "The new status of the product (e.g., 'active', 'discontinued', 'clearance', 'limited_availability')."},
                        "expiry_date": {"type": ["string", "null"], "format": "date", "description": "The new expiry date (YYYY-MM-DD), or null."}                    },
                    "required": ["sku"],
                },
            },
        }

class UpdateCustomerLoyaltyPoints(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        points_to_add = kwargs.get('points_to_add')
        customers = data.get("customers", [])
        updated_customer = None
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                customer["loyalty_points"] = customer.get("loyalty_points", 0) + points_to_add
                updated_customer = customer
                break
        return json.dumps({"updated_customer": updated_customer})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customer_loyalty_points",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_id = kwargs.get('inventory_id')
        change_amount = kwargs.get('change_amount')
        inventory_items = data.get("inventory", [])
        updated_item = None
        for item in inventory_items:
            if item.get("id") == inventory_id:
                item["reserved_quantity"] = item.get("reserved_quantity", 0) + change_amount
                updated_item = item
                break
        return json.dumps({"updated_inventory_item": updated_item})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_reserved_quantity",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        promotion_id = kwargs.get('promotion_id')
        promotions = data.get("promotions", [])
        for promo in promotions:
            if promo.get("promotion_id") == promotion_id:
                return json.dumps(promo)
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_promotion_by_id",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get('name')
        promotion_type = kwargs.get('type')
        discount_value = kwargs.get('discount_value')
        description = kwargs.get('description')
        applicable_skus = kwargs.get('applicable_skus')
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')
        status = kwargs.get('status')
        usage_limit = kwargs.get('usage_limit')
        times_used = kwargs.get('times_used')

        promotions = data.get("promotions", [])  # Mudei para lista []

        max_promotion_id_num = 0
        for promo in promotions:  # Itera direto na lista
            if isinstance(promo.get("promotion_id"), str):
                match = re.match(r"PROMO-(\d+)", promo["promotion_id"])
                if match:
                    num = int(match.group(1))
                    if num > max_promotion_id_num:
                        max_promotion_id_num = num

        next_promotion_id_num = max_promotion_id_num + 1
        new_promotion_id = f"PROMO-{next_promotion_id_num:03d}"  # Garante 3 dígitos com zeros à esquerda

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
            "times_used": times_used
        }

        promotions.append(new_promotion)  # Adiciona à lista
        data["promotions"] = promotions
        return json.dumps({"promotion_id": new_promotion_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_promotion",
                "description": "Creates a new promotion record with specified details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "The name of the new promotion."},
                        "type": {"type": "string", "description": "The type of the promotion (e.g., 'percentage', 'fixed_bundle', 'bogo_percentage', 'tax_free')."},
                        "discount_value": {"type": "number", "description": "The discount value (e.g., 10.0 for 10% or $10)."},
                        "description": {"type": "string", "description": "A brief description of the promotion."},
                        "applicable_skus": {"type": "array", "items": {"type": "string"}, "description": "A list of SKUs the promotion applies to."},
                        "start_date": {"type": "string", "format": "date", "description": "The start date of the promotion (YYYY-MM-DD)."},
                        "end_date": {"type": "string", "format": "date", "description": "The end date of the promotion (YYYY-MM-DD)."},
                        "status": {"type": "string", "description": "The initial status of the promotion (e.g., 'active', 'scheduled', 'planned')."},
                        "usage_limit": {"type": ["integer", "null"], "description": "The maximum number of times this promotion can be used, or null if unlimited."},
                        "times_used": {"type": "integer", "description": "The initial count of how many times the promotion has been used."},
                    },
                    "required": ["name", "type", "discount_value", "description", "applicable_skus", "start_date", "end_date", "status", "times_used"],
                },
            },
        }

class GetProductByStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get('status')
        products = data.get("products", [])  # Lista []
        results = [product for product in products if product.get("status") == status]
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_by_status",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        customers = data.get("customers", [])  # Lista []
        updated_customer = None
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                for key, value in kwargs.items():
                    if key != 'customer_id':
                        customer[key] = value
                customer["updated_at"] = "2025-07-28T16:38:15Z"  # Current time
                updated_customer = customer
                break
        return json.dumps({"updated_customer": updated_customer})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customer_details",
                "description": "Updates various details of an existing customer record by ID. Can update 'membership_level', 'email', 'phone_number', 'address', etc.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The ID of the customer to update.",
                        },
                        "name": {"type": "string", "description": "The new full name of the customer."},
                        "phone_number": {"type": "string", "description": "The new contact phone number."},
                        "email": {"type": "string", "description": "The new company email address."},
                        "address": {"type": "string", "description": "The new physical address."},
                        "membership_level": {"type": "string", "description": "The new membership level (e.g., 'basic', 'silver', 'gold', 'platinum', 'diamond')."},
                        "birthdate": {"type": "string", "format": "date", "description": "The new birthdate (YYYY-MM-DD)."},
                        "opt_in_marketing": {"type": "boolean", "description": "New marketing opt-in status."},
                        "status": {"type": "string", "description": "The new employment status (e.g. 'active', 'inactive', 'terminated')."},
                    },
                    "required": ["customer_id"],
                },
            },
        }

class UpdateInventoryStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_id = kwargs.get('inventory_id')
        status = kwargs.get('status')
        inventory_items = data.get("inventory", [])  # Lista []
        updated_item = None
        for item in inventory_items:
            if item.get("id") == inventory_id:
                item["status"] = status
                updated_item = item
                break
        return json.dumps({"updated_inventory_item": updated_item})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_status",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        customers = data.get("customers", [])  # Lista []
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                return json.dumps(customer)
        return json.dumps({})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_details_by_id",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        sku = kwargs.get('sku')
        transactions = data.get("transactions", [])  # Lista []
        for txn in transactions:
            if txn.get("customer_id") == customer_id:
                for item in txn.get("line_items", []):
                    if item.get("sku") == sku:
                        return json.dumps({
                            "transaction_id": txn.get("transaction_id"),  # Supondo que id esteja no objeto
                            "unit_price": item.get("unit_price")
                        })
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_transaction_by_customer_and_sku",
                "description": "Finds a past transaction for a customer containing a specific SKU and returns its ID and the item's unit price.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "The customer's unique ID."},
                        "sku": {"type": "string", "description": "The SKU of the product to find."},
                    },
                    "required": ["customer_id", "sku"],
                },
            },
        }

class ProcessItemReturn(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        transaction_id = kwargs.get('transaction_id')
        sku = kwargs.get('sku')
        quantity_returned = kwargs.get('quantity_returned')
        unit_price = kwargs.get('unit_price')

        transactions = data.get("transactions", [])  # Lista []
        inventory = data.get("inventory", [])  # Lista []

        for txn in transactions:
            if txn.get("transaction_id") == transaction_id:
                txn['status'] = 'returned'
                break

        for item in inventory:
            if item.get("sku") == sku:
                item["quantity"] += quantity_returned
                break

        credit_amount = unit_price * quantity_returned
        return json.dumps({"status": "success", "credit_amount": credit_amount})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_item_return",
                "description": "Processes an item return and calculates the credit amount based on the original unit price.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {"type": "string", "description": "The ID of the transaction for the return."},
                        "sku": {"type": "string", "description": "The SKU of the item being returned."},
                        "quantity_returned": {"type": "integer", "description": "The quantity of the item being returned."},
                        "unit_price": {"type": "number", "description": "The original unit price of the item for credit calculation."},
                    },
                    "required": ["transaction_id", "sku", "quantity_returned", "unit_price"],
                },
            },
        }

class GetProductsByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get('category')
        products = data.get("products", [])  # Lista []
        results = [product for product in products if product.get("category") == category]
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_products_by_category",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get('sku')
        quantity = kwargs.get('quantity')
        from_store_id = kwargs.get('from_store_id')
        to_store_id = kwargs.get('to_store_id')

        inventory = data.get("inventory", [])  # Corrigido para lista
        from_item = None
        to_item = None

        for item in inventory:
            if item['store_id'] == from_store_id and item['sku'] == sku:
                from_item = item
            if item['store_id'] == to_store_id and item['sku'] == sku:
                to_item = item

        if from_item and to_item:
            from_item['quantity'] -= quantity
            to_item['quantity'] += quantity
            return json.dumps({
                "status": "success",
                "sku": sku,
                "quantity": quantity,
                "from_store": from_store_id,
                "to_store": to_store_id
            })

        return json.dumps({"status": "failed", "reason": "Inventory item not found in one or both stores."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "execute_inventory_transfer",
                "description": "Executes a stock transfer of a specific SKU from one store to another.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "The SKU of the product to transfer."},
                        "quantity": {"type": "integer", "description": "The quantity of stock to transfer."},
                        "from_store_id": {"type": "string", "description": "The ID of the origin store."},
                        "to_store_id": {"type": "string", "description": "The ID of the destination store."},
                    },
                    "required": ["sku", "quantity", "from_store_id", "to_store_id"],
                },
            },
        }

class CreateInventoryRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get('sku')
        store_id = kwargs.get('store_id')
        location = kwargs.get('location')

        inventory_list = data.get("inventory", [])  # Corrigido para lista

        for item in inventory_list:
            if item.get("sku") == sku and item.get("store_id") == store_id:
                return json.dumps({"status": "exists", "inventory_id": item.get("id")})

        max_inv_id_num = 0
        for item in inventory_list:
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
            "last_stock_count": "2025-07-28"
        }

        inventory_list.append(new_record)  # Corrigido para append
        data["inventory"] = inventory_list

        return json.dumps({"status": "created", "inventory_id": new_inv_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_inventory_record",
                "description": "Creates a new inventory record for a product at a specific store, if one does not already exist.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "The SKU of the product."},
                        "store_id": {"type": "string", "description": "The ID of the store."},
                        "location": {"type": "string", "description": "A placeholder location for the new inventory record."},
                    },
                    "required": ["sku", "store_id", "location"],
                },
            },
        }

class CalculateTransactionTotals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        line_items = kwargs.get('line_items', [])
        promotion_ids = kwargs.get('promotion_ids', [])
        credit_amount = kwargs.get('credit_amount', 0.0)

        products = data.get("products", [])  # Corrigido para lista
        promotions = data.get("promotions", [])  # Corrigido para lista

        subtotal = 0.0
        total_discount = 0.0
        final_line_items = []

        for item in line_items:
            sku = item.get('sku')
            quantity = item.get('quantity')
            product_details = next((p for p in products if p['sku'] == sku), None)

            if not product_details:
                continue

            price = product_details.get('price', 0.0)
            item_subtotal = price * quantity
            subtotal += item_subtotal

            item_discount_value = 0.0

            for promo_id in promotion_ids:
                promo = next((p for p in promotions if p['promotion_id'] == promo_id), None)
                if promo and sku in promo.get('applicable_skus', []):
                    if promo.get('type') == 'percentage':
                        item_discount_value = item_subtotal * (promo.get('discount_value', 0.0) / 100.0)

            total_discount += item_discount_value
            final_line_items.append({
                "sku": sku,
                "quantity": quantity,
                "unit_price": price,
                "discount": round(item_discount_value / quantity, 2) if quantity > 0 else 0.0
            })

        subtotal_after_discount = subtotal - total_discount
        final_subtotal = subtotal_after_discount - credit_amount

        tax_rate = 0.0825
        total_tax = final_subtotal * tax_rate
        final_total = final_subtotal + total_tax

        return json.dumps({
            "calculated_total_amount": round(final_total, 2),
            "calculated_tax_amount": round(total_tax, 2),
            "calculated_discount_total": round(total_discount, 2),
            "calculated_line_items": final_line_items
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_transaction_totals",
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
                                    "quantity": {"type": "integer"}
                                },
                                "required": ["sku", "quantity"]
                            }
                        },
                        "promotion_ids": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "credit_amount": {"type": "number"}
                    },
                    "required": ["line_items"],
                },
            },
        }

class UpdateStockLevel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_id = kwargs.get('inventory_id')
        quantity_to_add = kwargs.get('quantity_to_add')
        inventory = data.get("inventory", [])  # Corrigido para lista

        found_item = None
        for item in inventory:
            if item.get("id") == inventory_id:
                found_item = item
                break

        if found_item:
            found_item['quantity'] += quantity_to_add
            if found_item['quantity'] > found_item.get('reorder_level', 0):
                found_item['status'] = 'in_stock'
            elif found_item['quantity'] > 0:
                found_item['status'] = 'low_stock'
            else:
                found_item['status'] = 'out_of_stock'

            return json.dumps({
                "status": "success",
                "inventory_id": inventory_id,
                "new_quantity": found_item['quantity']
            })

        return json.dumps({"status": "error", "reason": "Inventory ID not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_stock_level",
                "description": "Updates the stock level for an inventory item, e.g., when receiving a shipment or correcting a count.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {"type": "string", "description": "The unique ID of the inventory item."},
                        "quantity_to_add": {"type": "integer", "description": "The number of units to add to the current quantity (can be negative)."},
                    },
                    "required": ["inventory_id", "quantity_to_add"],
                },
            },
        }

class FindCustomersByCriteria(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        membership_levels = kwargs.get('membership_levels', [])
        purchase_history_skus = kwargs.get('purchase_history_skus', [])

        customers = data.get("customers", [])  # Corrigido para lista
        transactions = data.get("transactions", [])  # Corrigido para lista

        qualified_customers = []

        for customer in customers:
            if customer.get("membership_level") in membership_levels:
                customer_id = customer.get("customer_id")
                for txn in transactions:
                    if txn.get("customer_id") == customer_id:
                        for item in txn.get("line_items", []):
                            if item.get("sku") in purchase_history_skus:
                                qualified_customers.append(customer)
                                break
                        break

        return json.dumps(qualified_customers)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_customers_by_criteria",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_ids = kwargs.get('customer_ids', [])
        promotion_id = kwargs.get('promotion_id')

        if "promo_codes" not in data:
            data["promo_codes"] = {}

        generated_assignments = []
        for cid in customer_ids:
            unique_code = f"VIP-{promotion_id}-{cid[-4:]}"
            assignment = {
                "code": unique_code,
                "promotion_id": promotion_id,
                "customer_id": cid,
                "is_used": False
            }
            data["promo_codes"][unique_code] = assignment
            generated_assignments.append(assignment)

        return json.dumps(generated_assignments)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_and_assign_promo_codes",
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
GenerateAndAssignPromoCodes()
]
