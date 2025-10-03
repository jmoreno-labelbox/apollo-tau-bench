import json
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool


def _get_next_inventory_id(inventory_list: list[dict[str, Any]]) -> str:
    pass
    max_inv_num = 0
    for inv in inventory_list:
        if inv["id"].startswith("INV-"):
            try:
                num = int(inv["id"].split("-")[1])
                if num > max_inv_num:
                    max_inv_num = num
            except ValueError:
                pass
    return f"INV-{max_inv_num + 1:04d}"


#Helper Functions
def _get_next_transaction_id(transactions_list: list[dict[str, Any]]) -> str:
    pass
    max_txn_num = 0
    for txn in transactions_list:
        if txn["transaction_id"].startswith("TXN-"):
            try:
                num = int(txn["transaction_id"].split("-")[1])
                if num > max_txn_num:
                    max_txn_num = num
            except ValueError:
                pass
    return f"TXN-{max_txn_num + 1:04d}"


class SearchProducts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], query: str, category: str | None = None) -> str:
        _queryL = query or ''.lower()
        _categoryL = category or ''.lower()
        pass
        products = data.get("products", [])
        results = []

        for product in products:
            if query.lower() in product.get("name", "").lower():
                if category and product.get("category", "").lower() != category.lower():
                    continue
                results.append(product)
        payload = {"products": results, "count": len(results)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchProducts",
                "description": "Search for products by name and optional category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query for product name.",
                        },
                        "category": {
                            "type": "string",
                            "description": "Optional: Filter by product category.",
                        },
                    },
                    "required": ["query"],
                },
            },
        }


class GetCustomerDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str) -> str:
        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                payload = customer
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Customer with ID {customer_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerDetails",
                "description": "Get detailed information about a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        }
                    },
                    "required": ["customer_id"],
                },
            },
        }


class GetProductDetailsBySKU(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str) -> str:
        products = data.get("products", [])
        for product in products:
            if product.get("sku") == sku:
                payload = product
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Product with SKU {sku} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductDetailsBySku",
                "description": "Get detailed information about a product by its SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Stock Keeping Unit (SKU) of the product.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }


class ListAllProducts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], limit: int | None = None) -> str:
        products = data.get("products", [])
        if limit:
            products = products[:limit]
        payload = {"products": products, "count": len(products)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAllProducts",
                "description": "List all products with optional limit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "limit": {
                            "type": "integer",
                            "description": "Optional: Maximum number of products to return.",
                        }
                    },
                    "required": [],
                },
            },
        }


class ListProductsByCategory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], category: str) -> str:
        _categoryL = category or ''.lower()
        pass
        products = data.get("products", [])
        category_products = [
            p for p in products if p.get("category", "").lower() == category.lower()
        ]
        payload = {
                "products": category_products,
                "count": len(category_products),
                "category": category,
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
                "name": "ListProductsByCategory",
                "description": "List all products in a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "Product category to filter by.",
                        }
                    },
                    "required": ["category"],
                },
            },
        }


class GetTransactionDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], transaction_id: str) -> str:
        transactions = data.get("transactions", [])
        for transaction in transactions:
            if transaction.get("transaction_id") == transaction_id:
                payload = transaction
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Transaction with ID {transaction_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTransactionDetails",
                "description": "Get detailed information about a specific transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {
                            "type": "string",
                            "description": "Unique identifier of the transaction.",
                        }
                    },
                    "required": ["transaction_id"],
                },
            },
        }


class ListTransactionsByCustomer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str) -> str:
        transactions = data.get("transactions", [])
        customer_transactions = [
            t for t in transactions if t.get("customer_id") == customer_id
        ]
        payload = {
            "transactions": customer_transactions,
            "count": len(customer_transactions),
            "customer_id": customer_id,
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
                "name": "ListTransactionsByCustomer",
                "description": "List all transactions for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        }
                    },
                    "required": ["customer_id"],
                },
            },
        }


class GetInventoryLevel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str) -> str:
        inventory = data.get("inventory", [])
        products = data.get("products", [])

        product = next((p for p in products if p.get("sku") == sku), None)
        if not product:
            payload = {"error": f"Product with SKU {sku} not found."}
            out = json.dumps(payload)
            return out

        inventory_records = [inv for inv in inventory if inv.get("sku") == sku]

        if not inventory_records:
            payload = {"error": f"No inventory records found for SKU {sku}"}
            out = json.dumps(payload)
            return out

        total_quantity = sum(inv.get("quantity", 0) for inv in inventory_records)
        total_reserved = sum(
            inv.get("reserved_quantity", 0) for inv in inventory_records
        )
        total_available = total_quantity - total_reserved

        inventory_info = {
            "sku": sku,
            "name": product.get("name"),
            "total_quantity": total_quantity,
            "total_reserved_quantity": total_reserved,
            "total_available_quantity": total_available,
            "inventory_records": inventory_records,
        }
        payload = inventory_info
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryLevel",
                "description": "Get current inventory level for a specific product SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Stock Keeping Unit (SKU) of the product.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }


class ListLowStockProducts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inventory: list = None, products: list = None, threshold: int = 10) -> str:
        inventory = inventory if inventory is not None else data.get("inventory", [])
        products = products if products is not None else data.get("products", [])
        low_stock_products = []

        for inv_record in inventory:
            quantity = inv_record.get("quantity", 0)
            if quantity <= threshold:
                product = next(
                    (p for p in products if p.get("sku") == inv_record.get("sku")), None
                )

                low_stock_info = {
                    "sku": inv_record.get("sku"),
                    "name": product.get("name") if product else "Unknown",
                    "store_id": inv_record.get("store_id"),
                    "current_stock": quantity,
                    "threshold": threshold,
                    "category": product.get("category") if product else "Unknown",
                }
                low_stock_products.append(low_stock_info)
        payload = {
                "low_stock_products": low_stock_products,
                "count": len(low_stock_products),
                "threshold": threshold,
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
                "name": "ListLowStockProducts",
                "description": "List products with stock levels below the specified threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "threshold": {
                            "type": "integer",
                            "description": "Stock level threshold. Default is 10.",
                        }
                    },
                    "required": [],
                },
            },
        }


class GetTotalSalesByDate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], date: str) -> str:
        transactions = data.get("transactions", [])
        total_sales = 0.0
        transaction_count = 0

        for transaction in transactions:
            if transaction.get("timestamp", "").startswith(date):
                total_sales += transaction.get("total_amount", 0.0)
                transaction_count += 1

        sales_info = {
            "date": date,
            "total_sales": total_sales,
            "transaction_count": transaction_count,
        }
        payload = sales_info
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTotalSalesByDate",
                "description": "Get total sales amount for a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format.",
                        }
                    },
                    "required": ["date"],
                },
            },
        }


class GetCustomerLoyaltyPoints(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str) -> str:
        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                loyalty_info = {
                    "customer_id": customer_id,
                    "name": customer.get("name"),
                    "loyalty_points": customer.get("loyalty_points", 0),
                    "membership_level": customer.get("membership_level", "bronze"),
                }
                payload = loyalty_info
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Customer with ID {customer_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerLoyaltyPoints",
                "description": "Get loyalty points balance for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        }
                    },
                    "required": ["customer_id"],
                },
            },
        }


class GetEmployeeDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        employees = data.get("employees", [])
        for employee in employees:
            if employee.get("employee_id") == employee_id:
                payload = employee
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Employee with ID {employee_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeDetails",
                "description": "Get detailed information about a specific employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Unique identifier of the employee.",
                        }
                    },
                    "required": ["employee_id"],
                },
            },
        }


class ListAllEmployees(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employees: list = None) -> str:
        employees = employees if employees is not None else data.get("employees", [])
        payload = {"employees": employees, "count": len(employees)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAllEmployees",
                "description": "List all employees.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class RecordSale(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        customer_id: str,
        items: list[dict[str, Any]],
        payment_method: str
    ) -> str:
        customers = data.get("customers", [])
        customer = next(
            (c for c in customers if c.get("customer_id") == customer_id), None
        )
        if not customer:
            payload = {"error": f"Customer with ID {customer_id} not found."}
            out = json.dumps(payload)
            return out

        products = data.get("products", [])
        inventory = data.get("inventory", [])
        total_amount = 0.0
        validated_items = []

        for item in items:
            sku = item.get("sku")
            quantity = item.get("quantity", 1)

            product = next((p for p in products if p.get("sku") == sku), None)
            if not product:
                payload = {"error": f"Product with SKU {sku} not found."}
                out = json.dumps(payload)
                return out

            # Verify stock availability
            total_available = 0
            for inv in inventory:
                if inv.get("sku") == sku:
                    total_available += inv.get("quantity", 0) - inv.get(
                        "reserved_quantity", 0
                    )

            if total_available < quantity:
                payload = {
                    "error": f"Insufficient stock for product {sku}. Available: {total_available}, Requested: {quantity}"
                }
                out = json.dumps(payload)
                return out

            # Revise stock levels
            remaining_quantity = quantity
            for inv in inventory:
                if inv.get("sku") == sku and remaining_quantity > 0:
                    available = inv.get("quantity", 0) - inv.get("reserved_quantity", 0)
                    if available > 0:
                        deduct = min(available, remaining_quantity)
                        inv["quantity"] = inv.get("quantity", 0) - deduct
                        remaining_quantity -= deduct

            unit_price = product.get("price", 0.0)
            item_total = unit_price * quantity
            total_amount += item_total

            validated_items.append(
                {
                    "sku": sku,
                    "name": product.get("name"),
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "total_price": item_total,
                }
            )

        transactions = data.get("transactions", [])
        transaction_id = _get_next_transaction_id(transactions)

        # Calculate tax amount (assuming 8.25% tax rate)
        tax_rate = 0.0825
        tax_amount = total_amount * tax_rate
        final_total = total_amount + tax_amount

        # Convert validated_items to line_items format
        line_items = []
        for item in validated_items:
            line_items.append({
                "sku": item["sku"],
                "quantity": item["quantity"],
                "unit_price": item["unit_price"],
                "discount": 0.0  # No discount applied in RecordSale
            })

        # Create transaction with proper structure matching data file
        transaction = {
            "transaction_id": transaction_id,
            "store_id": "STORE-001",  # Default store
            "employee_id": "EMP-1002",  # Default employee
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "total_amount": final_total,
            "tax_amount": tax_amount,
            "payment_method": payment_method,
            "tax_rate": tax_rate,
            "discount_total": 0.0,
            "change_given": 0.0,
            "status": "completed",
            "customer_id": customer_id,
            "line_items": line_items,
        }

        transactions.append(transaction)
        data["transactions"] = transactions
        payload = transaction
        out = json.dumps(payload, indent=2)
        return out
        pass
        customers = data.get("customers", [])
        customer = next(
            (c for c in customers if c.get("customer_id") == customer_id), None
        )
        if not customer:
            payload = {"error": f"Customer with ID {customer_id} not found."}
            out = json.dumps(payload)
            return out

        products = data.get("products", [])
        inventory = data.get("inventory", [])
        total_amount = 0.0
        validated_items = []

        for item in items:
            sku = item.get("sku")
            quantity = item.get("quantity", 1)

            product = next((p for p in products if p.get("sku") == sku), None)
            if not product:
                payload = {"error": f"Product with SKU {sku} not found."}
                out = json.dumps(payload)
                return out

            #Verify stock availability
            total_available = 0
            for inv in inventory:
                if inv.get("sku") == sku:
                    total_available += inv.get("quantity", 0) - inv.get(
                        "reserved_quantity", 0
                    )

            if total_available < quantity:
                payload = {
                        "error": f"Insufficient stock for product {sku}. Available: {total_available}, Requested: {quantity}"
                    }
                out = json.dumps(
                    payload)
                return out

            #Revise stock levels
            remaining_quantity = quantity
            for inv in inventory:
                if inv.get("sku") == sku and remaining_quantity > 0:
                    available = inv.get("quantity", 0) - inv.get("reserved_quantity", 0)
                    if available > 0:
                        deduct = min(available, remaining_quantity)
                        inv["quantity"] = inv.get("quantity", 0) - deduct
                        remaining_quantity -= deduct

            unit_price = product.get("price", 0.0)
            item_total = unit_price * quantity
            total_amount += item_total

            validated_items.append(
                {
                    "sku": sku,
                    "name": product.get("name"),
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "total_price": item_total,
                }
            )

        transactions = data.get("transactions", [])
        transaction_id = _get_next_transaction_id(transactions)

        # Calculate tax amount (assuming 8.25% tax rate)
        tax_rate = 0.0825
        tax_amount = total_amount * tax_rate
        final_total = total_amount + tax_amount

        # Convert validated_items to line_items format
        line_items = []
        for item in validated_items:
            line_items.append({
                "sku": item["sku"],
                "quantity": item["quantity"],
                "unit_price": item["unit_price"],
                "discount": 0.0  # No discount applied in RecordSale
            })

        # Create transaction with proper structure matching data file
        transaction = {
            "transaction_id": transaction_id,
            "store_id": "STORE-001",  # Default store
            "employee_id": "EMP-1002",  # Default employee
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "total_amount": final_total,
            "tax_amount": tax_amount,
            "payment_method": payment_method,
            "tax_rate": tax_rate,
            "discount_total": 0.0,
            "change_given": 0.0,
            "status": "completed",
            "customer_id": customer_id,
            "line_items": line_items,
        }

        transactions.append(transaction)
        data["transactions"] = transactions
        payload = transaction
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordSale",
                "description": "Record a new sale transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        },
                        "items": {
                            "type": "array",
                            "description": "List of items being purchased.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {
                                        "type": "string",
                                        "description": "Product SKU.",
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "description": "Quantity being purchased.",
                                    },
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "payment_method": {
                            "type": "string",
                            "description": "Payment method used.",
                        },
                    },
                    "required": ["customer_id", "items", "payment_method"],
                },
            },
        }


class AddNewProduct(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        name: str,
        description: str,
        category: str,
        price: float,
        stock_quantity: int
    ) -> str:
        products = data.get("products", [])
        category_prefix = category[:4].upper()
        product_num = (
            len(
                [
                    p
                    for p in products
                    if p.get("category", "").upper() == category.upper()
                ]
            )
            + 1
        )
        sku = f"{category_prefix}-{product_num:04d}"

        new_product = {
            "sku": sku,
            "name": name,
            "description": description,
            "category": category,
            "price": price,
        }

        products.append(new_product)
        data["products"] = products
        payload = new_product
        out = json.dumps(payload, indent=2)
        return out
        pass
        products = data.get("products", [])
        category_prefix = category[:4].upper()
        product_num = (
            len(
                [
                    p
                    for p in products
                    if p.get("category", "").upper() == category.upper()
                ]
            )
            + 1
        )
        sku = f"{category_prefix}-{product_num:04d}"

        new_product = {
            "sku": sku,
            "name": name,
            "description": description,
            "category": category,
            "price": price,
        }

        products.append(new_product)
        data["products"] = products
        payload = new_product
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddNewProduct",
                "description": "Add a new product to the inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Product name."},
                        "description": {
                            "type": "string",
                            "description": "Product description.",
                        },
                        "category": {
                            "type": "string",
                            "description": "Product category.",
                        },
                        "price": {"type": "number", "description": "Product price."},
                        "stock_quantity": {
                            "type": "integer",
                            "description": "Initial stock quantity.",
                        },
                    },
                    "required": [
                        "name",
                        "description",
                        "category",
                        "price",
                        "stock_quantity",
                    ],
                },
            },
        }


class UpdateProductPrice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str, new_price: float) -> str:
        products = data.get("products", [])
        for i, product in enumerate(products):
            if product.get("sku") == sku:
                products[i]["price"] = new_price
                data["products"] = products
                payload = products[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Product with SKU {sku} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProductPrice",
                "description": "Update the price for a specific product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Product SKU to update.",
                        },
                        "new_price": {
                            "type": "number",
                            "description": "New product price.",
                        },
                    },
                    "required": ["sku", "new_price"],
                },
            },
        }


class AddNewCustomer(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], name: str, email: str, phone_number: str, address: str
    ) -> str:
        customers = data.get("customers", [])

        if any(c.get("email") == email for c in customers):
            payload = {"error": f"Customer with email {email} already exists."}
            out = json.dumps(payload)
            return out

        customer_id = f"CUST-{len(customers) + 5001:04d}"

        new_customer = {
            "customer_id": customer_id,
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "address": address,
            "loyalty_points": 0,
            "membership_level": "bronze",
        }

        customers.append(new_customer)
        data["customers"] = customers
        payload = new_customer
        out = json.dumps(payload, indent=2)
        return out
        pass
        customers = data.get("customers", [])

        if any(c.get("email") == email for c in customers):
            payload = {"error": f"Customer with email {email} already exists."}
            out = json.dumps(payload)
            return out

        customer_id = f"CUST-{len(customers) + 5001:04d}"

        new_customer = {
            "customer_id": customer_id,
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "address": address,
            "loyalty_points": 0,
            "membership_level": "bronze",
        }

        customers.append(new_customer)
        data["customers"] = customers
        payload = new_customer
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddNewCustomer",
                "description": "Add a new customer to the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Customer's full name.",
                        },
                        "email": {
                            "type": "string",
                            "description": "Customer's email address.",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "Customer's phone number.",
                        },
                        "address": {
                            "type": "string",
                            "description": "Customer's address.",
                        },
                    },
                    "required": ["name", "email", "phone_number", "address"],
                },
            },
        }


class UpdateCustomerLoyaltyPoints(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str, points_to_add: int) -> str:
        customers = data.get("customers", [])
        for i, customer in enumerate(customers):
            if customer.get("customer_id") == customer_id:
                current_points = customer.get("loyalty_points", 0)
                customers[i]["loyalty_points"] = current_points + points_to_add
                data["customers"] = customers
                payload = customers[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Customer with ID {customer_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomerLoyaltyPoints",
                "description": "Update loyalty points for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        },
                        "points_to_add": {
                            "type": "integer",
                            "description": "Number of points to add.",
                        },
                    },
                    "required": ["customer_id", "points_to_add"],
                },
            },
        }


class UpdateCustomerMembershipLevel(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], customer_id: str, new_membership_level: str
    ) -> str:
        _new_membership_levelL = new_membership_level or ''.lower()
        pass
        customers = data.get("customers", [])
        valid_levels = ["bronze", "silver", "gold", "platinum", "vip"]

        if new_membership_level.lower() not in valid_levels:
            payload = {
                    "error": f"Invalid membership level. Valid levels are: {', '.join(valid_levels)}"
                }
            out = json.dumps(
                payload)
            return out

        for i, customer in enumerate(customers):
            if customer.get("customer_id") == customer_id:
                customers[i]["membership_level"] = new_membership_level.lower()
                data["customers"] = customers
                payload = customers[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Customer with ID {customer_id} not found."}
        out = json.dumps(payload)
        return out
        _new_membership_levelL = new_membership_level or ''.lower()
        pass
        customers = data.get("customers", [])
        valid_levels = ["bronze", "silver", "gold", "platinum", "vip"]

        if new_membership_level.lower() not in valid_levels:
            payload = {
                    "error": f"Invalid membership level. Valid levels are: {', '.join(valid_levels)}"
                }
            out = json.dumps(
                payload)
            return out

        for i, customer in enumerate(customers):
            if customer.get("customer_id") == customer_id:
                customers[i]["membership_level"] = new_membership_level.lower()
                data["customers"] = customers
                payload = customers[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Customer with ID {customer_id} not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomerMembershipLevel",
                "description": "Update membership level for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        },
                        "new_membership_level": {
                            "type": "string",
                            "description": "New membership level.",
                        },
                    },
                    "required": ["customer_id", "new_membership_level"],
                },
            },
        }


class ProcessReturn(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        original_transaction_id: str,
        items_to_return: list[dict[str, Any]],
        reason: str
    ) -> str:
        transactions = data.get("transactions", [])
        original_txn = next(
            (
                t
                for t in transactions
                if t.get("transaction_id") == original_transaction_id
            ),
            None,
        )
        if not original_txn:
            payload = {"error": f"Original transaction {original_transaction_id} not found."}
            out = json.dumps(payload)
            return out

        inventory = data.get("inventory", [])
        return_amount = 0.0
        validated_returns = []

        for return_item in items_to_return:
            sku = return_item.get("sku")
            return_quantity = return_item.get("quantity", 1)

            original_item = next(
                (
                    item
                    for item in original_txn.get("line_items", [])
                    if item.get("sku") == sku
                ),
                None,
            )
            if not original_item:
                payload = {
                    "error": f"Product {sku} was not in original transaction {original_transaction_id}."
                }
                out = json.dumps(payload)
                return out

            if return_quantity > original_item.get("quantity", 0):
                payload = {
                    "error": f"Cannot return {return_quantity} of {sku}. Original quantity was {original_item.get('quantity', 0)}."
                }
                out = json.dumps(payload)
                return out

            # Revise stock levels (reintroduce returned products)
            any_store_inventory = next(
                (inv for inv in inventory if inv.get("sku") == sku), None
            )
            if any_store_inventory:
                any_store_inventory["quantity"] = (
                    any_store_inventory.get("quantity", 0) + return_quantity
                )

            unit_price = original_item.get("unit_price", 0.0)
            item_return_amount = unit_price * return_quantity
            return_amount += item_return_amount

            validated_returns.append(
                {
                    "sku": sku,
                    "name": original_item.get("name"),
                    "quantity": return_quantity,
                    "unit_price": unit_price,
                    "return_amount": item_return_amount,
                }
            )

        return_transaction_id = f"RTN-{len(transactions) + 1:04d}"

        return_transaction = {
            "transaction_id": return_transaction_id,
            "type": "return",
            "original_transaction_id": original_transaction_id,
            "customer_id": original_txn.get("customer_id"),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "items": validated_returns,
            "total_amount": -return_amount,
            "reason": reason,
            "status": "completed",
        }

        transactions.append(return_transaction)
        data["transactions"] = transactions
        payload = return_transaction
        out = json.dumps(payload, indent=2)
        return out
        pass
        transactions = data.get("transactions", [])
        original_txn = next(
            (
                t
                for t in transactions
                if t.get("transaction_id") == original_transaction_id
            ),
            None,
        )
        if not original_txn:
            payload = {"error": f"Original transaction {original_transaction_id} not found."}
            out = json.dumps(
                payload)
            return out

        inventory = data.get("inventory", [])
        return_amount = 0.0
        validated_returns = []

        for return_item in items_to_return:
            sku = return_item.get("sku")
            return_quantity = return_item.get("quantity", 1)

            original_item = next(
                (
                    item
                    for item in original_txn.get("line_items", [])
                    if item.get("sku") == sku
                ),
                None,
            )
            if not original_item:
                payload = {
                        "error": f"Product {sku} was not in original transaction {original_transaction_id}."
                    }
                out = json.dumps(
                    payload)
                return out

            if return_quantity > original_item.get("quantity", 0):
                payload = {
                        "error": f"Cannot return {return_quantity} of {sku}. Original quantity was {original_item.get('quantity', 0)}."
                    }
                out = json.dumps(
                    payload)
                return out

            #Revise stock levels (reintroduce returned products)
            any_store_inventory = next(
                (inv for inv in inventory if inv.get("sku") == sku), None
            )
            if any_store_inventory:
                any_store_inventory["quantity"] = (
                    any_store_inventory.get("quantity", 0) + return_quantity
                )

            unit_price = original_item.get("unit_price", 0.0)
            item_return_amount = unit_price * return_quantity
            return_amount += item_return_amount

            validated_returns.append(
                {
                    "sku": sku,
                    "name": original_item.get("name"),
                    "quantity": return_quantity,
                    "unit_price": unit_price,
                    "return_amount": item_return_amount,
                }
            )

        return_transaction_id = f"RTN-{len(transactions) + 1:04d}"

        return_transaction = {
            "transaction_id": return_transaction_id,
            "type": "return",
            "original_transaction_id": original_transaction_id,
            "customer_id": original_txn.get("customer_id"),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "items": validated_returns,
            "total_amount": -return_amount,
            "reason": reason,
            "status": "completed",
        }

        transactions.append(return_transaction)
        data["transactions"] = transactions
        payload = return_transaction
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessReturn",
                "description": "Process a return for items from a previous transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "original_transaction_id": {
                            "type": "string",
                            "description": "ID of the original transaction.",
                        },
                        "items_to_return": {
                            "type": "array",
                            "description": "List of items being returned.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {
                                        "type": "string",
                                        "description": "Product SKU.",
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "description": "Quantity being returned.",
                                    },
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "reason": {
                            "type": "string",
                            "description": "Reason for the return.",
                        },
                    },
                    "required": [
                        "original_transaction_id",
                        "items_to_return",
                        "reason",
                    ],
                },
            },
        }


class UpdateTransactionStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], transaction_id: str, new_status: str) -> str:
        transactions = data.get("transactions", [])
        valid_statuses = ["pending", "completed", "cancelled", "refunded"]

        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        for i, transaction in enumerate(transactions):
            if transaction.get("transaction_id") == transaction_id:
                transactions[i]["status"] = new_status
                data["transactions"] = transactions
                payload = transactions[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Transaction with ID {transaction_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTransactionStatus",
                "description": "Update the status of an existing transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {
                            "type": "string",
                            "description": "Unique identifier of the transaction.",
                        },
                        "new_status": {"type": "string", "description": "New status."},
                    },
                    "required": ["transaction_id", "new_status"],
                },
            },
        }


class UpdateCustomerEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str, new_email: str) -> str:
        customers = data.get("customers", [])

        for customer in customers:
            if (
                customer.get("email") == new_email
                and customer.get("customer_id") != customer_id
            ):
                payload = {
                    "error": f"Email {new_email} is already in use by another customer."
                }
                out = json.dumps(payload)
                return out

        for i, customer in enumerate(customers):
            if customer.get("customer_id") == customer_id:
                customers[i]["email"] = new_email
                data["customers"] = customers
                payload = customers[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Customer with ID {customer_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomerEmail",
                "description": "Update the email address for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        },
                        "new_email": {
                            "type": "string",
                            "description": "New email address for the customer.",
                        },
                    },
                    "required": ["customer_id", "new_email"],
                },
            },
        }


class AddEmployee(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        name: str,
        role: str,
        store_id: str,
        email: str,
        phone_number: str
    ) -> str:
        employees = data.get("employees", [])

        if any(e.get("email") == email for e in employees):
            payload = {"error": f"Employee with email {email} already exists."}
            out = json.dumps(payload)
            return out

        employee_id = f"EMP-{len(employees) + 1001:04d}"

        new_employee = {
            "employee_id": employee_id,
            "name": name,
            "role": role,
            "store_id": store_id,
            "email": email,
            "phone_number": phone_number,
            "hire_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "active",
        }

        employees.append(new_employee)
        data["employees"] = employees
        payload = new_employee
        out = json.dumps(payload, indent=2)
        return out
        pass
        employees = data.get("employees", [])

        if any(e.get("email") == email for e in employees):
            payload = {"error": f"Employee with email {email} already exists."}
            out = json.dumps(payload)
            return out

        employee_id = f"EMP-{len(employees) + 1001:04d}"

        new_employee = {
            "employee_id": employee_id,
            "name": name,
            "role": role,
            "store_id": store_id,
            "email": email,
            "phone_number": phone_number,
            "hire_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "active",
        }

        employees.append(new_employee)
        data["employees"] = employees
        payload = new_employee
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddEmployee",
                "description": "Add a new employee to the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Full name of the employee.",
                        },
                        "role": {
                            "type": "string",
                            "description": "Job role of the employee.",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "Store ID where the employee works.",
                        },
                        "email": {
                            "type": "string",
                            "description": "Email address of the employee.",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "Phone number of the employee.",
                        },
                    },
                    "required": ["name", "role", "store_id", "email", "phone_number"],
                },
            },
        }


class RemoveEmployee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        employees = data.get("employees", [])
        original_len = len(employees)
        employees[:] = [e for e in employees if e.get("employee_id") != employee_id]

        if len(employees) == original_len:
            payload = {"error": f"Employee with ID {employee_id} not found."}
            out = json.dumps(payload)
            return out

        data["employees"] = employees
        payload = {"success": f"Employee {employee_id} removed successfully."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveEmployee",
                "description": "Remove an employee from the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Unique identifier of the employee to remove.",
                        }
                    },
                    "required": ["employee_id"],
                },
            },
        }


class UpdateEmployeeStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str, new_status: str) -> str:
        employees = data.get("employees", [])

        for i, employee in enumerate(employees):
            if employee.get("employee_id") == employee_id:
                employees[i]["status"] = new_status
                data["employees"] = employees
                payload = employees[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Employee with ID {employee_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmployeeStatus",
                "description": "Update the status of an existing employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Unique identifier of the employee.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status for the employee.",
                        },
                    },
                    "required": ["employee_id", "new_status"],
                },
            },
        }


class UpdateProductStock(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str, new_stock_quantity: int) -> str:
        products = data.get("products", [])

        for i, product in enumerate(products):
            if product.get("sku") == sku:
                products[i]["stock_quantity"] = new_stock_quantity
                data["products"] = products
                payload = products[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Product with SKU {sku} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProductStock",
                "description": "Update the stock quantity of an existing product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Product SKU to update.",
                        },
                        "new_stock_quantity": {
                            "type": "integer",
                            "description": "New stock quantity for the product.",
                        },
                    },
                    "required": ["sku", "new_stock_quantity"],
                },
            },
        }


class UpdateCustomerAddress(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str, new_address: str) -> str:
        customers = data.get("customers", [])

        for i, customer in enumerate(customers):
            if customer.get("customer_id") == customer_id:
                customers[i]["address"] = new_address
                data["customers"] = customers
                payload = customers[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Customer with ID {customer_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomerAddress",
                "description": "Update the address of an existing customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        },
                        "new_address": {
                            "type": "string",
                            "description": "New address for the customer.",
                        },
                    },
                    "required": ["customer_id", "new_address"],
                },
            },
        }


class UpdateCustomerPhoneNumber(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str, new_phone_number: str) -> str:
        customers = data.get("customers", [])

        for i, customer in enumerate(customers):
            if customer.get("customer_id") == customer_id:
                customers[i]["phone_number"] = new_phone_number
                data["customers"] = customers
                payload = customers[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Customer with ID {customer_id} not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomerPhoneNumber",
                "description": "Update the phone number of an existing customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer.",
                        },
                        "new_phone_number": {
                            "type": "string",
                            "description": "New phone number for the customer.",
                        },
                    },
                    "required": ["customer_id", "new_phone_number"],
                },
            },
        }


class AddPromotion(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        promotion_id: str,
        name: str,
        description: str,
        discount_type: str,
        value: float,
        start_date: str,
        end_date: str
    ) -> str:
        promotions = data.get("promotions", [])

        if any(p.get("promotion_id") == promotion_id for p in promotions):
            payload = {"error": f"Promotion with ID {promotion_id} already exists."}
            out = json.dumps(payload)
            return out

        new_promotion = {
            "promotion_id": promotion_id,
            "name": name,
            "description": description,
            "discount_type": discount_type,
            "value": value,
            "start_date": start_date,
            "end_date": end_date,
            "status": "active",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        promotions.append(new_promotion)
        data["promotions"] = promotions
        payload = new_promotion
        out = json.dumps(payload, indent=2)
        return out
        pass
        promotions = data.get("promotions", [])

        if any(p.get("promotion_id") == promotion_id for p in promotions):
            payload = {"error": f"Promotion with ID {promotion_id} already exists."}
            out = json.dumps(
                payload)
            return out

        new_promotion = {
            "promotion_id": promotion_id,
            "name": name,
            "description": description,
            "discount_type": discount_type,
            "value": value,
            "start_date": start_date,
            "end_date": end_date,
            "status": "active",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        promotions.append(new_promotion)
        data["promotions"] = promotions
        payload = new_promotion
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addPromotion",
                "description": "Add a new promotion to the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "Unique identifier for the promotion.",
                        },
                        "name": {
                            "type": "string",
                            "description": "Name of the promotion.",
                        },
                        "description": {
                            "type": "string",
                            "description": "Description of the promotion.",
                        },
                        "discount_type": {
                            "type": "string",
                            "description": "Type of discount (percentage or fixed).",
                        },
                        "value": {"type": "number", "description": "Discount value."},
                        "start_date": {
                            "type": "string",
                            "description": "Start date of the promotion (YYYY-MM-DD).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date of the promotion (YYYY-MM-DD).",
                        },
                    },
                    "required": [
                        "promotion_id",
                        "name",
                        "description",
                        "discount_type",
                        "value",
                        "start_date",
                        "end_date",
                    ],
                },
            },
        }


class UpdateInventoryQuantity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str, new_quantity: int) -> str:
        inventory = data.get("inventory", [])

        for i, inv_record in enumerate(inventory):
            if inv_record.get("id") == inventory_id:
                inventory[i]["quantity"] = new_quantity
                inventory[i]["updated_at"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                data["inventory"] = inventory
                payload = inventory[i]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Inventory record with ID {inventory_id} not found."}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateInventoryQuantity",
                "description": "Update the quantity of an inventory record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "Unique identifier of the inventory record.",
                        },
                        "new_quantity": {
                            "type": "integer",
                            "description": "New quantity for the inventory record.",
                        },
                    },
                    "required": ["inventory_id", "new_quantity"],
                },
            },
        }


class GetInventoryAnalytics(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str | None = None) -> str:
        inventory = data.get("inventory", [])
        products = data.get("products", [])

        if store_id:
            inventory = [inv for inv in inventory if inv.get("store_id") == store_id]

        total_items = len(inventory)
        total_quantity = sum(inv.get("quantity", 0) for inv in inventory)
        total_value = 0.0

        for inv_record in inventory:
            product = next(
                (p for p in products if p.get("sku") == inv_record.get("sku")), None
            )
            if product:
                total_value += inv_record.get("quantity", 0) * product.get("price", 0)

        low_stock_items = len(
            [inv for inv in inventory if inv.get("quantity", 0) <= 10]
        )

        analytics = {
            "store_id": store_id,
            "total_items": total_items,
            "total_quantity": total_quantity,
            "total_value": round(total_value, 2),
            "low_stock_items": low_stock_items,
            "average_quantity": (
                round(total_quantity / total_items, 2) if total_items > 0 else 0
            ),
        }
        payload = analytics
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getInventoryAnalytics",
                "description": "Get inventory analytics for a store or all stores.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "Optional: Store ID to filter analytics.",
                        }
                    },
                    "required": [],
                },
            },
        }


class AddInventoryRecord(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sku: str,
        store_id: str,
        quantity: int,
        location: str,
        reorder_level: int,
        safety_stock: int
    ) -> str:
        inventory = data.get("inventory", [])
        products = data.get("products", [])

        # Verify the existence of the product
        product = next((p for p in products if p.get("sku") == sku), None)
        if not product:
            payload = {"error": f"Product with SKU {sku} not found."}
            out = json.dumps(payload)
            return out

        # Determine if an inventory entry is present for this SKU and location
        existing_record = next(
            (
                inv
                for inv in inventory
                if inv.get("sku") == sku and inv.get("store_id") == store_id
            ),
            None,
        )
        if existing_record:
            payload = {
                "error": f"Inventory record for SKU {sku} in store {store_id} already exists."
            }
            out = json.dumps(payload)
            return out

        inventory_id = _get_next_inventory_id(inventory)

        new_inventory_record = {
            "id": inventory_id,
            "sku": sku,
            "store_id": store_id,
            "quantity": quantity,
            "location": location,
            "reorder_level": reorder_level,
            "safety_stock": safety_stock,
            "reserved_quantity": 0,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        inventory.append(new_inventory_record)
        data["inventory"] = inventory
        payload = new_inventory_record
        out = json.dumps(payload, indent=2)
        return out
        pass
        inventory = data.get("inventory", [])
        products = data.get("products", [])

        #Verify the existence of the product
        product = next((p for p in products if p.get("sku") == sku), None)
        if not product:
            payload = {"error": f"Product with SKU {sku} not found."}
            out = json.dumps(payload)
            return out

        #Determine if an inventory entry is present for this SKU and location
        existing_record = next(
            (
                inv
                for inv in inventory
                if inv.get("sku") == sku and inv.get("store_id") == store_id
            ),
            None,
        )
        if existing_record:
            payload = {
                    "error": f"Inventory record for SKU {sku} in store {store_id} already exists."
                }
            out = json.dumps(
                payload)
            return out

        inventory_id = _get_next_inventory_id(inventory)

        new_inventory_record = {
            "id": inventory_id,
            "sku": sku,
            "store_id": store_id,
            "quantity": quantity,
            "location": location,
            "reorder_level": reorder_level,
            "safety_stock": safety_stock,
            "reserved_quantity": 0,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        inventory.append(new_inventory_record)
        data["inventory"] = inventory
        payload = new_inventory_record
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addInventoryRecord",
                "description": "Add a new inventory record for a product in a store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "SKU of the product."},
                        "store_id": {
                            "type": "string",
                            "description": "Store ID where the inventory is located.",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "Initial quantity in stock.",
                        },
                        "location": {
                            "type": "string",
                            "description": "Physical location within the store.",
                        },
                        "reorder_level": {
                            "type": "integer",
                            "description": "Reorder level threshold.",
                        },
                        "safety_stock": {
                            "type": "integer",
                            "description": "Safety stock level.",
                        },
                    },
                    "required": [
                        "sku",
                        "store_id",
                        "quantity",
                        "location",
                        "reorder_level",
                        "safety_stock",
                    ],
                },
            },
        }


class RemovePromotion(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_id: str) -> str:
        promotions = data.get("promotions", [])
        original_len = len(promotions)
        promotions[:] = [p for p in promotions if p.get("promotion_id") != promotion_id]

        if len(promotions) == original_len:
            payload = {"error": f"Promotion with ID {promotion_id} not found."}
            out = json.dumps(payload)
            return out

        data["promotions"] = promotions
        payload = {"success": f"Promotion {promotion_id} removed successfully."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removePromotion",
                "description": "Remove a promotion from the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "Unique identifier of the promotion to remove.",
                        }
                    },
                    "required": ["promotion_id"],
                },
            },
        }


#LIST OF TOOLS
TOOLS = [
    SearchProducts(),
    GetCustomerDetails(),
    GetProductDetailsBySKU(),
    ListAllProducts(),
    ListProductsByCategory(),
    GetTransactionDetails(),
    ListTransactionsByCustomer(),
    GetInventoryLevel(),
    ListLowStockProducts(),
    GetTotalSalesByDate(),
    GetCustomerLoyaltyPoints(),
    GetEmployeeDetails(),
    ListAllEmployees(),
    RecordSale(),
    AddNewProduct(),
    UpdateProductStock(),
    UpdateProductPrice(),
    AddNewCustomer(),
    UpdateCustomerLoyaltyPoints(),
    UpdateCustomerMembershipLevel(),
    ProcessReturn(),
    UpdateTransactionStatus(),
    UpdateCustomerAddress(),
    UpdateCustomerEmail(),
    UpdateCustomerPhoneNumber(),
    AddEmployee(),
    RemoveEmployee(),
    UpdateEmployeeStatus(),
    AddPromotion(),
    UpdateInventoryQuantity(),
    GetInventoryAnalytics(),
    AddInventoryRecord(),
    RemovePromotion(),
]
