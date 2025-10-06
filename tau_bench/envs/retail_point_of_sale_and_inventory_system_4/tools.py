import json
from typing import Any

from tau_bench.envs.tool import Tool


def _filter_db(db, filter_params):
    pass
    def match(row):
        pass
        for filter, value in filter_params.items():
            if not isinstance(value, list):
                value = [value]
            if row.get(filter) not in value:
                return False
        return True

    return [row for row in db if match(row)]


def _find_by_id(db, id_field, id_value):
    pass
    for i, row in enumerate(db):
        if row.get(id_field) == id_value:
            return i, row
    return None, None


#1. Clients
class EditCustomersDb(Tool):  #CREATE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        customer_id: str = None,
        name: str = None,
        email: str = None,
        address: str = None,
        phone_number: str = None,
        membership_level: str = None,
        loyalty_points: int = None,
        status: str = None,
        birthdate: str = None,
        opt_in_marketing: bool = None,
        current_time: str = None,
        delete: bool = False
    ) -> str:
        db = data.get("customers", [])
        if customer_id:
            idx, row = _find_by_id(db, "customer_id", customer_id)
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
                    if email is not None:
                        row["email"] = email
                    if address is not None:
                        row["address"] = address
                    if phone_number is not None:
                        row["phone_number"] = phone_number
                    if membership_level is not None:
                        row["membership_level"] = membership_level
                    if loyalty_points is not None:
                        row["loyalty_points"] = loyalty_points
                    if status is not None:
                        row["status"] = status
                    if birthdate is not None:
                        row["birthdate"] = birthdate
                    if opt_in_marketing is not None:
                        row["opt_in_marketing"] = opt_in_marketing
                    if current_time is not None:
                        row["updated_at"] = current_time
                    payload = {"result": row}
                    out = json.dumps(payload)
                    return out
            else:
                payload = {"error": f"Customer {customer_id} not found"}
                out = json.dumps(payload)
                return out
        else:
            #--- ADD ---
            if name is None or email is None or current_time is None:
                payload = {
                        "error": "Missing required field for creation (name, email, current_time)"
                    }
                out = json.dumps(
                    payload)
                return out
            new_row = {
                "name": name,
                "email": email,
                "created_at": current_time,
                "updated_at": current_time,
            }
            new_row["customer_id"] = (
                customer_id
                if customer_id is not None
                else "CUST-" + str(5000 + len(db) + 1)
            )
            new_row["birthdate"] = (
                birthdate if birthdate is not None else "No DOB given."
            )
            new_row["opt_in_marketing"] = (
                opt_in_marketing if opt_in_marketing is not None else True
            )
            new_row["address"] = address if address is not None else "No address given."
            new_row["phone_number"] = (
                phone_number if phone_number is not None else "No phone number given."
            )
            new_row["membership_level"] = (
                membership_level if membership_level is not None else "basic"
            )
            new_row["loyalty_points"] = (
                loyalty_points if loyalty_points is not None else 0
            )
            new_row["status"] = status if status is not None else "active"
            db.append(new_row)
            payload = {"result": new_row}
            out = json.dumps(payload)
            return out
        pass
        db = data.get("customers", [])
        if customer_id:
            idx, row = _find_by_id(db, "customer_id", customer_id)
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
                    if email is not None:
                        row["email"] = email
                    if address is not None:
                        row["address"] = address
                    if phone_number is not None:
                        row["phone_number"] = phone_number
                    if membership_level is not None:
                        row["membership_level"] = membership_level
                    if loyalty_points is not None:
                        row["loyalty_points"] = loyalty_points
                    if status is not None:
                        row["status"] = status
                    if birthdate is not None:
                        row["birthdate"] = birthdate
                    if opt_in_marketing is not None:
                        row["opt_in_marketing"] = opt_in_marketing
                    if current_time is not None:
                        row["updated_at"] = current_time
                    payload = {"result": row}
                    out = json.dumps(payload)
                    return out
            else:
                payload = {"error": f"Customer {customer_id} not found"}
                out = json.dumps(payload)
                return out
        else:
            #--- ADD ---
            if name is None or email is None or current_time is None:
                payload = {
                        "error": "Missing required field for creation (name, email, current_time)"
                    }
                out = json.dumps(
                    payload)
                return out
            new_row = {
                "name": name,
                "email": email,
                "created_at": current_time,
                "updated_at": current_time,
            }
            new_row["customer_id"] = (
                customer_id
                if customer_id is not None
                else "CUST-" + str(5000 + len(db) + 1)
            )
            new_row["birthdate"] = (
                birthdate if birthdate is not None else "No DOB given."
            )
            new_row["opt_in_marketing"] = (
                opt_in_marketing if opt_in_marketing is not None else True
            )
            new_row["address"] = address if address is not None else "No address given."
            new_row["phone_number"] = (
                phone_number if phone_number is not None else "No phone number given."
            )
            new_row["membership_level"] = (
                membership_level if membership_level is not None else "basic"
            )
            new_row["loyalty_points"] = (
                loyalty_points if loyalty_points is not None else 0
            )
            new_row["status"] = status if status is not None else "active"
            db.append(new_row)
            payload = {"result": new_row}
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EditCustomersDb",
                "description": "Create, update, or delete a customer row by customer_id. If delete is True, it deletes the row. If customer_id is given it will edit the row with the given information. If no customer_id is given, it will create a new row with the given info, as long as name, email and current_time are given.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "default": None,
                            "description": "The customer_id of the record if deleted or editing a record.",
                        },
                        "delete": {
                            "type": "boolean",
                            "default": False,
                            "description": "A boolean indicating whether the specified record should be deleted.",
                        },
                        "name": {
                            "type": "string",
                            "default": None,
                            "description": "The name of a customer to create or update a record with.",
                        },
                        "email": {
                            "type": "string",
                            "default": None,
                            "description": "The email of a customer to create or update a record with.",
                        },
                        "address": {
                            "type": "string",
                            "default": None,
                            "description": "The address of a customer to create or update a record with.",
                        },
                        "phone_number": {
                            "type": "string",
                            "default": None,
                            "description": "The phone number of a customer to create or update a record with.",
                        },
                        "membership_level": {
                            "type": "string",
                            "default": None,
                            "description": "The membership level of a customer to create or update a record with.",
                        },
                        "loyalty_points": {
                            "type": "integer",
                            "default": None,
                            "description": "The number of loyalty_points a customer has for creating or updating a record.",
                        },
                        "status": {
                            "type": "string",
                            "default": None,
                            "description": "The status of a customer to create or update a record with.",
                        },
                        "birthdate": {
                            "type": "string",
                            "default": None,
                            "description": "The birthdate of a customer to create or update a record with.",
                        },
                        "opt_in_marketing": {
                            "type": "boolean",
                            "default": None,
                            "description": "A boolean indicating if the customer opted into marketing, for creating or updating their record.",
                        },
                        "current_time": {
                            "type": "string",
                            "default": None,
                            "description": "The current time stamp to set the 'modified_at' time, and the 'created_at' time if creating a record.",
                        },
                    },
                    "required": [],
                },
            },
        }


class GetCustomersInfoByParam(Tool):  #VIEW
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filter_params: dict[str, Any],
        info_items: list[str] = None
    ) -> str:
        db = data.get("customers", [])
        filtered_db = _filter_db(db, filter_params)
        if not info_items:
            payload = filtered_db
            out = json.dumps(payload)
            return out
        payload = [
            {info_item: row.get(info_item) for info_item in info_items}
            for row in filtered_db
        ]
        out = json.dumps(payload)
        return out
        pass
        db = data.get("customers", [])
        filtered_db = _filter_db(db, filter_params)
        if not info_items:
            payload = filtered_db
            out = json.dumps(payload)
            return out
        payload = [
                {info_item: row.get(info_item) for info_item in info_items}
                for row in filtered_db
            ]
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomersInfoByParam",
                "description": "Filter customers by parameters and return specified fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary of ways to filter items in the database. To pass the filter an item must match one of the possible given values for all the filtering paramets",
                        },
                        "info_items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries.",
                        },
                    },
                    "required": ["filter_params"],
                },
            },
        }


class GetTopNCustomersByLoyaltyPoints(Tool):  #VIEW
    @staticmethod
    def invoke(data: dict[str, Any], n: int) -> str:
        customers = data["customers"]
        # Order by loyalty_points from highest to lowest
        sorted_customers = sorted(
            customers, key=lambda c: c["loyalty_points"], reverse=True
        )
        top_customers = sorted_customers[:n]
        payload = top_customers
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTopNCustomersByLoyaltyPoints",
                "description": "Get the top N customers sorted by loyalty points in descending order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "n": {
                            "type": "integer",
                            "description": "Number of top customers to return.",
                        }
                    },
                    "required": ["n"],
                },
            },
        }


class GetCustomersWithBirthdayToday(Tool):  #VIEW
    @staticmethod
    def invoke(data: dict[str, Any], current_day: str) -> str:
        db = data.get("customers", [])
        # current_day must follow the "MM-DD" format
        result = []
        for row in db:
            birthdate = row.get("birthdate", "")
            # Allow birthdate in either "YYYY-MM-DD" or "MM-DD"
            if len(birthdate) >= 5:
                birthdate = birthdate[-5:]
            if birthdate == current_day:
                result.append(row.get("customer_id"))
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomersWithBirthdayToday",
                "description": "Return a list of customer IDs who have a birthday on the given day (MM-DD).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_day": {
                            "type": "string",
                            "description": "The current day in MM-DD format (e.g., '04-23').",
                        }
                    },
                    "required": ["current_day"],
                },
            },
        }


#2. Staff


class EditEmployeesDb(Tool):  #CREATE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str = None,
        name: str = None,
        role: str = None,
        phone_number: str = None,
        email: str = None,
        store_id: str = None,
        hire_date: str = None,
        status: str = None,
        delete: bool = False
    ) -> str:
        _nameL = name or ''.lower()
        pass
        db = data.get("employees", [])
        if employee_id:
            idx, row = _find_by_id(db, "employee_id", employee_id)
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
                    if role is not None:
                        row["role"] = role
                    if phone_number is not None:
                        row["phone_number"] = phone_number
                    if email is not None:
                        row["email"] = email
                    if store_id is not None:
                        row["store_id"] = store_id
                    if hire_date is not None:
                        row["hire_date"] = hire_date
                    if status is not None:
                        row["status"] = status
                    payload = {"result": row}
                    out = json.dumps(payload)
                    return out
            else:
                payload = {"error": f"Employee {employee_id} not found"}
                out = json.dumps(payload)
                return out
        else:
            #--- ADD ---
            if name is None or role is None:
                payload = {"error": "Missing required field for creation (name, role)"}
                out = json.dumps(
                    payload)
                return out
            new_row = {
                "employee_id": (
                    employee_id
                    if employee_id is not None
                    else f"EMP-{1000 + len(db) + 1}"
                ),
                "name": name if name is not None else "Unknown",
                "role": role if role is not None else "Unknown",
                "phone_number": (
                    phone_number if phone_number is not None else "No phone"
                ),
                "email": (
                    email
                    if email is not None
                    else name.lower().replace(" ", ".") + "@retailpos.com"
                ),
                "store_id": store_id if store_id is not None else "Unknown",
                "hire_date": hire_date if hire_date is not None else "Unknown",
                "status": status if status is not None else "active",
            }
            db.append(new_row)
            payload = {"result": new_row}
            out = json.dumps(payload)
            return out
        _nameL = name or ''.lower()
        pass
        db = data.get("employees", [])
        if employee_id:
            idx, row = _find_by_id(db, "employee_id", employee_id)
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
                    if role is not None:
                        row["role"] = role
                    if phone_number is not None:
                        row["phone_number"] = phone_number
                    if email is not None:
                        row["email"] = email
                    if store_id is not None:
                        row["store_id"] = store_id
                    if hire_date is not None:
                        row["hire_date"] = hire_date
                    if status is not None:
                        row["status"] = status
                    payload = {"result": row}
                    out = json.dumps(payload)
                    return out
            else:
                payload = {"error": f"Employee {employee_id} not found"}
                out = json.dumps(payload)
                return out
        else:
            #--- ADD ---
            if name is None or role is None:
                payload = {"error": "Missing required field for creation (name, role)"}
                out = json.dumps(
                    payload)
                return out
            new_row = {
                "employee_id": (
                    employee_id
                    if employee_id is not None
                    else f"EMP-{1000 + len(db) + 1}"
                ),
                "name": name if name is not None else "Unknown",
                "role": role if role is not None else "Unknown",
                "phone_number": (
                    phone_number if phone_number is not None else "No phone"
                ),
                "email": (
                    email
                    if email is not None
                    else name.lower().replace(" ", ".") + "@retailpos.com"
                ),
                "store_id": store_id if store_id is not None else "Unknown",
                "hire_date": hire_date if hire_date is not None else "Unknown",
                "status": status if status is not None else "active",
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
                "name": "EditEmployeesDb",
                "description": "Create, update, or delete an employee row by employee_id. If delete is True, it deletes the row. If employee_id is given it will edit the row with the given information. If no employee_id is given, it will create a new row with the given info, as long as name, role and email are given.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "default": None,
                            "description": "The employee_id of the record to edit or delete. If not provided, a new id will be generated.",
                        },
                        "delete": {
                            "type": "boolean",
                            "default": False,
                            "description": "A boolean indicating whether the specified record should be deleted.",
                        },
                        "name": {
                            "type": "string",
                            "default": None,
                            "description": "The name of the employee to create or update a record with.",
                        },
                        "role": {
                            "type": "string",
                            "default": None,
                            "description": "The role of the employee to create or update a record with.",
                        },
                        "phone_number": {
                            "type": "string",
                            "default": None,
                            "description": "The phone number of the employee to create or update a record with.",
                        },
                        "email": {
                            "type": "string",
                            "default": None,
                            "description": "The email of the employee to create or update a record with.",
                        },
                        "store_id": {
                            "type": "string",
                            "default": None,
                            "description": "The store_id of the employee to create or update a record with.",
                        },
                        "hire_date": {
                            "type": "string",
                            "default": None,
                            "description": "The hire date of the employee to create or update a record with.",
                        },
                        "status": {
                            "type": "string",
                            "default": None,
                            "description": "The status of the employee to create or update a record with.",
                        },
                    },
                    "required": [],
                },
            },
        }


class GetEmployeesInfoByParam(Tool):  #VIEW
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filter_params: dict[str, Any],
        info_items: list[str] = None
    ) -> str:
        db = data.get("employees", [])
        filtered_db = _filter_db(db, filter_params)
        if not info_items:
            payload = filtered_db
            out = json.dumps(payload)
            return out
        payload = [
            {info_item: row.get(info_item) for info_item in info_items}
            for row in filtered_db
        ]
        out = json.dumps(payload)
        return out
        pass
        db = data.get("employees", [])
        filtered_db = _filter_db(db, filter_params)
        if not info_items:
            payload = filtered_db
            out = json.dumps(payload)
            return out
        payload = [
                {info_item: row.get(info_item) for info_item in info_items}
                for row in filtered_db
            ]
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeesInfoByParam",
                "description": "Filter employees by any combination of fields. Returns all fields by default, or only those specified in 'fields' parameter if given.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary of ways to filter items in the database. To pass the filter an item must match one of the possible given values for all the filtering paramets",
                        },
                        "info_items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries.",
                        },
                    },
                    "required": ["filter_params"],
                },
            },
        }


#3. Items
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
        db = data.get("products", [])
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


class GetProductsInfoByParam(Tool):  #VIEW
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filter_params: dict[str, Any],
        info_items: list[str] = None
    ) -> str:
        db = data.get("products", [])
        filtered_db = _filter_db(db, filter_params)
        if not info_items:
            payload = filtered_db
            out = json.dumps(payload)
            return out
        payload = [
            {info_item: row.get(info_item) for info_item in info_items}
            for row in filtered_db
        ]
        out = json.dumps(payload)
        return out
        pass
        db = data.get("products", [])
        filtered_db = _filter_db(db, filter_params)
        if not info_items:
            payload = filtered_db
            out = json.dumps(payload)
            return out
        payload = [
                {info_item: row.get(info_item) for info_item in info_items}
                for row in filtered_db
            ]
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductsInfoByParam",
                "description": "Filter products by parameters and return specified fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary of ways to filter items in the database. To pass the filter an item must match one of the possible given values for all the filtering paramets",
                        },
                        "info_items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries.",
                        },
                    },
                    "required": ["filter_params"],
                },
            },
        }


class GetTopNMostExpensiveProductsByStore(Tool):  #VIEW
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str, n: int) -> str:
        products = {p["sku"]: p["price"] for p in data.get("products", [])}
        inventory = {i["sku"]: i["store_id"] for i in data.get("inventory", [])}

        items = [
            {"sku": sku, "price": price}
            for sku, price in products.items()
            if inventory.get(sku) == store_id
        ]

        # Order by price from highest to lowest and select top x
        top_items = sorted(items, key=lambda i: i["price"], reverse=True)[:n]
        payload = top_items
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTopNMostExpensiveProductsByStore",
                "description": "Return the top n most expensive products available in a given store, based on product price.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "The unique ID of the store.",
                        },
                        "n": {
                            "type": "integer",
                            "description": "The number of top expensive products to return.",
                        },
                    },
                    "required": ["store_id", "n"],
                },
            },
        }


#4. Stock
class EditInventoryDb(Tool):  #CREATE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: str = None,
        sku: str = None,
        store_id: str = None,
        quantity: int = None,
        reserved_quantity: int = None,
        reorder_level: int = None,
        safety_stock: int = None,
        location: str = None,
        status: str = None,
        last_stock_count: str = None,
        current_time: str = None,
        delete: bool = False
    ) -> str:
        db = data.get("inventory", [])
        if id:
            idx, row = _find_by_id(db, "id", id)
            if row:
                if delete:
                    #--- REMOVE ---
                    del db[idx]
                    payload = {"result": "deleted"}
                    out = json.dumps(payload)
                    return out
                else:
                    #--- MODIFY ---
                    if sku is not None:
                        row["sku"] = sku
                    if store_id is not None:
                        row["store_id"] = store_id
                    if quantity is not None:
                        row["quantity"] = quantity
                    if reserved_quantity is not None:
                        row["reserved_quantity"] = reserved_quantity
                    if reorder_level is not None:
                        row["reorder_level"] = reorder_level
                    if safety_stock is not None:
                        row["safety_stock"] = safety_stock
                    if location is not None:
                        row["location"] = location
                    if status is not None:
                        row["status"] = status
                    if last_stock_count is not None:
                        row["last_stock_count"] = last_stock_count
                    if current_time is not None:
                        row["updated_at"] = current_time
                    payload = {"result": row}
                    out = json.dumps(payload)
                    return out
            else:
                payload = {"error": f"Inventory {id} not found"}
                out = json.dumps(payload)
                return out
        else:
            #--- ADD ---
            if (
                sku is None
                or store_id is None
                or quantity is None
                or current_time is None
            ):
                payload = {
                        "error": "Missing required field for creation (sku, store_id, quantity, current_time)"
                    }
                out = json.dumps(
                    payload)
                return out
            new_row = {
                "id": id if id is not None else f"INV-{1000 + len(db) + 5}",
                "sku": sku,
                "store_id": store_id,
                "quantity": quantity,
                "reserved_quantity": (
                    reserved_quantity if reserved_quantity is not None else 0
                ),
                "reorder_level": reorder_level if reorder_level is not None else 0,
                "safety_stock": safety_stock if safety_stock is not None else 0,
                "location": location if location is not None else "Unknown",
                "status": status if status is not None else "in_stock",
                "last_stock_count": (
                    last_stock_count if last_stock_count is not None else "Unknown"
                ),
                "created_at": current_time,
                "updated_at": current_time,
            }
            db.append(new_row)
            payload = {"result": new_row}
            out = json.dumps(payload)
            return out
        pass
        db = data.get("inventory", [])
        if id:
            idx, row = _find_by_id(db, "id", id)
            if row:
                if delete:
                    #--- REMOVE ---
                    del db[idx]
                    payload = {"result": "deleted"}
                    out = json.dumps(payload)
                    return out
                else:
                    #--- MODIFY ---
                    if sku is not None:
                        row["sku"] = sku
                    if store_id is not None:
                        row["store_id"] = store_id
                    if quantity is not None:
                        row["quantity"] = quantity
                    if reserved_quantity is not None:
                        row["reserved_quantity"] = reserved_quantity
                    if reorder_level is not None:
                        row["reorder_level"] = reorder_level
                    if safety_stock is not None:
                        row["safety_stock"] = safety_stock
                    if location is not None:
                        row["location"] = location
                    if status is not None:
                        row["status"] = status
                    if last_stock_count is not None:
                        row["last_stock_count"] = last_stock_count
                    if current_time is not None:
                        row["updated_at"] = current_time
                    payload = {"result": row}
                    out = json.dumps(payload)
                    return out
            else:
                payload = {"error": f"Inventory {id} not found"}
                out = json.dumps(payload)
                return out
        else:
            #--- ADD ---
            if (
                sku is None
                or store_id is None
                or quantity is None
                or current_time is None
            ):
                payload = {
                        "error": "Missing required field for creation (sku, store_id, quantity, current_time)"
                    }
                out = json.dumps(
                    payload)
                return out
            new_row = {
                "id": id if id is not None else f"INV-{1000 + len(db) + 5}",
                "sku": sku,
                "store_id": store_id,
                "quantity": quantity,
                "reserved_quantity": (
                    reserved_quantity if reserved_quantity is not None else 0
                ),
                "reorder_level": reorder_level if reorder_level is not None else 0,
                "safety_stock": safety_stock if safety_stock is not None else 0,
                "location": location if location is not None else "Unknown",
                "status": status if status is not None else "in_stock",
                "last_stock_count": (
                    last_stock_count if last_stock_count is not None else "Unknown"
                ),
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
                "name": "EditInventoryDb",
                "description": "Create, update, or delete an inventory row by id. If delete is True, deletes the row. If id is given it will edit the row with the given information. If no id is given, it will create a new row with the given info, as long as sku, store_id, quantity, location, and current_time are given.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "default": None,
                            "description": "The inventory id to edit or delete. If not provided, a new id will be generated.",
                        },
                        "delete": {
                            "type": "boolean",
                            "default": False,
                            "description": "Whether to delete the specified inventory record.",
                        },
                        "sku": {
                            "type": "string",
                            "default": None,
                            "description": "SKU of the product.",
                        },
                        "store_id": {
                            "type": "string",
                            "default": None,
                            "description": "Store ID.",
                        },
                        "quantity": {
                            "type": "integer",
                            "default": None,
                            "description": "Quantity in stock.",
                        },
                        "reserved_quantity": {
                            "type": "integer",
                            "default": None,
                            "description": "Reserved quantity.",
                        },
                        "reorder_level": {
                            "type": "integer",
                            "default": None,
                            "description": "Reorder level.",
                        },
                        "safety_stock": {
                            "type": "integer",
                            "default": None,
                            "description": "Safety stock.",
                        },
                        "location": {
                            "type": "string",
                            "default": None,
                            "description": "Location in store.",
                        },
                        "status": {
                            "type": "string",
                            "default": None,
                            "description": "Status of inventory.",
                        },
                        "last_stock_count": {
                            "type": "string",
                            "default": None,
                            "description": "Last stock count date.",
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


class GetInventoryInfoByParam(Tool):  #VIEW
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filter_params: dict[str, Any],
        info_items: list[str] = None
    ) -> str:
        db = data.get("inventory", [])
        filtered_db = _filter_db(db, filter_params)
        if not info_items:
            payload = filtered_db
            out = json.dumps(payload)
            return out
        payload = [
            {info_item: row.get(info_item) for info_item in info_items}
            for row in filtered_db
        ]
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryInfoByParam",
                "description": "Filter inventory by parameters and return specified fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary of ways to filter items in the database. To pass the filter an item must match one of the possible given values for all the filtering paramets",
                        },
                        "info_items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries.",
                        },
                    },
                    "required": ["filter_params"],
                },
            },
        }


class CheckLowStock(Tool):  #CREATE
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str, current_time: str) -> str:
        db = data.get("inventory", [])
        low_stock_skus = []
        for row in db:
            if row.get("store_id") == store_id:
                quantity = row.get("quantity", 0)
                reorder_level = row.get("reorder_level", 0)
                safety_stock = row.get("safety_stock", 0)
                if quantity <= reorder_level or row["status"] in [
                    "low_stock",
                    "critical",
                ]:
                    row["quantity"] += safety_stock
                    row["safety_stock"] = 0
                    row["updated_at"] = current_time
                    if row["status"] not in ["low_stock", "critical"]:
                        row["status"] = "low_stock"
                    low_stock_skus.append(row.get("sku"))
        payload = {"low_stock_skus": low_stock_skus}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckLowStock",
                "description": "Checks all inventory items for a given store_id. If quantity is below reorder_level, adds safety_stock to quantity, sets safety_stock to 0, and marks status as 'low_stock'. Returns a list of SKUs for items with 'low_stock' or 'critical' status for that store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "Store ID to check inventory for.",
                        },
                        "current_time": {
                            "type": "string",
                            "description": "Timestamp for updated_at.",
                        },
                    },
                    "required": ["store_id", "current_time"],
                },
            },
        }


class UpdateInventoryItem(Tool):  #CREATE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sku: str,
        store_id: str,
        quantity_change: int,
        current_time: str
    ) -> str:
        db = data.get("inventory", [])
        filtered_db = _filter_db(db, {"sku": sku, "store_id": store_id})
        if len(filtered_db) == 1:
            row = filtered_db[0]
            row["quantity"] = row.get("quantity", 0) + quantity_change
            row["updated_at"] = current_time
            payload = {"result": row}
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": f"Inventory item {sku} in store {store_id} not found"}
            out = json.dumps(payload)
            return out
        pass
        db = data.get("inventory", [])
        filtered_db = _filter_db(db, {"sku": sku, "store_id": store_id})
        if len(filtered_db) == 1:
            row = filtered_db[0]
            row["quantity"] = row.get("quantity", 0) + quantity_change
            row["updated_at"] = current_time
            payload = {"result": row}
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": f"Inventory item {sku} in store {store_id} not found"}
            out = json.dumps(
                payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryItem",
                "description": "Update the quantity and updated_at time of an inventory item by inventory_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "The inventory item's id to update.",
                        },
                        "quantity_change": {
                            "type": "integer",
                            "description": "The amount to change the quantity by (can be negative).",
                        },
                        "current_time": {
                            "type": "string",
                            "description": "Timestamp for updated_at.",
                        },
                    },
                    "required": ["inventory_id", "quantity_change", "current_time"],
                },
            },
        }


#5. Discounts
class EditPromotionsDb(Tool):  #CREATE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        promotion_id: str = None,
        name: str = None,
        type: str = None,
        discount_value: float = None,
        description: str = None,
        applicable_skus: list = None,
        start_date: str = None,
        end_date: str = None,
        status: str = None,
        usage_limit: int = None,
        times_used: int = None,
        delete: bool = False
    ) -> str:
        db = data.get("promotions", [])
        if promotion_id:
            idx, row = _find_by_id(db, "promotion_id", promotion_id)
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
                    if type is not None:
                        row["type"] = type
                    if discount_value is not None:
                        row["discount_value"] = discount_value
                    if description is not None:
                        row["description"] = description
                    if applicable_skus is not None:
                        row["applicable_skus"] = applicable_skus
                    if start_date is not None:
                        row["start_date"] = start_date
                    if end_date is not None:
                        row["end_date"] = end_date
                    if status is not None:
                        row["status"] = status
                    if usage_limit is not None:
                        row["usage_limit"] = usage_limit
                    if times_used is not None:
                        row["times_used"] = times_used
                    payload = {"result": row}
                    out = json.dumps(payload)
                    return out
            else:
                payload = {"error": f"Promotion {promotion_id} not found"}
                out = json.dumps(payload)
                return out
        else:
            #--- ADD ---
            if not promotion_id:
                promotion_id = f"PROMO-{1000 + len(db) + 1}"
            if (
                name is None
                or type is None
                or discount_value is None
                or applicable_skus is None
                or start_date is None
            ):
                payload = {
                        "error": "Missing required field for creation (name, type, discount_value, applicable_skus)"
                    }
                out = json.dumps(
                    payload)
                return out
            new_row = {
                "promotion_id": promotion_id,
                "name": name,
                "type": type,
                "discount_value": discount_value,
                "description": (
                    description if description is not None else "No description"
                ),
                "applicable_skus": applicable_skus,
                "start_date": start_date if len(start_date) < 10 else start_date[:10],
                "end_date": end_date if end_date is not None else "9999-12-31",
                "status": status if status is not None else "active",
                "usage_limit": usage_limit if usage_limit is not None else 0,
                "times_used": times_used if times_used is not None else 0,
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
                "name": "EditPromotionsDb",
                "description": "Create, update, or delete a promotion row by promotion_id. If delete is True, deletes the row. If promotion_id is given it will edit the row with the given information. If no promotion_id is given, it will create a new row with the given info, as long as name, type, discount_value, applicable_skus, start_date, end_date, and current_time are given.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "default": None,
                            "description": "The promotion id to edit or delete. If not provided, a new id will be generated.",
                        },
                        "delete": {
                            "type": "boolean",
                            "default": False,
                            "description": "Whether to delete the specified promotion.",
                        },
                        "name": {
                            "type": "string",
                            "default": None,
                            "description": "Name of the promotion.",
                        },
                        "type": {
                            "type": "string",
                            "default": None,
                            "description": "Type of promotion.",
                        },
                        "discount_value": {
                            "type": "number",
                            "default": None,
                            "description": "Discount value.",
                        },
                        "description": {
                            "type": "string",
                            "default": None,
                            "description": "Description of the promotion.",
                        },
                        "applicable_skus": {
                            "type": "array",
                            "items": {"type": "string"},
                            "default": None,
                            "description": "SKUs to which the promotion applies. If empty, applies to all products.",
                        },
                        "start_date": {
                            "type": "string",
                            "default": None,
                            "description": "Start date of the promotion.",
                        },
                        "end_date": {
                            "type": "string",
                            "default": None,
                            "description": "End date of the promotion.",
                        },
                        "status": {
                            "type": "string",
                            "default": None,
                            "description": "Status of the promotion.",
                        },
                        "usage_limit": {
                            "type": "integer",
                            "default": None,
                            "description": "Usage limit for the promotion.",
                        },
                        "times_used": {
                            "type": "integer",
                            "default": None,
                            "description": "Number of times the promotion has been used.",
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


class GetPromotionsInfoByParam(Tool):  #VIEW
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filter_params: dict[str, Any],
        info_items: list[str] = None
    ) -> str:
        db = data.get("promotions", [])
        filtered_db = _filter_db(db, filter_params)
        if not info_items:
            payload = filtered_db
            out = json.dumps(payload)
            return out
        payload = [
            {info_item: row.get(info_item) for info_item in info_items}
            for row in filtered_db
        ]
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPromotionsInfoByParam",
                "description": "Filter promotions by parameters and return specified fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary of ways to filter items in the database. To pass the filter an item must match one of the possible given values for all the filtering paramets",
                        },
                        "info_items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries.",
                        },
                    },
                    "required": ["filter_params"],
                },
            },
        }


#6. Sales
class EditTransactionsDb(Tool):  #CREATE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        transaction_id: str = None,
        store_id: str = None,
        employee_id: str = None,
        customer_id: str = None,
        line_items: list = None,
        total_amount: float = None,
        tax_amount: float = None,
        payment_method: str = None,
        tax_rate: float = None,
        discount_total: float = None,
        change_given: float = None,
        status: str = None,
        current_time: str = None,
        delete: bool = False
    ) -> str:
        db = data.get("transactions", [])
        if transaction_id:
            idx, row = _find_by_id(db, "transaction_id", transaction_id)
            if row:
                if delete:
                    #--- REMOVE ---
                    del db[idx]
                    payload = {"result": "deleted"}
                    out = json.dumps(payload)
                    return out
                else:
                    #--- MODIFY ---
                    if store_id is not None:
                        row["store_id"] = store_id
                    if employee_id is not None:
                        row["employee_id"] = employee_id
                    if current_time is not None:
                        row["timestamp"] = current_time
                    if customer_id is not None:
                        row["customer_id"] = customer_id
                    if line_items is not None:
                        row["line_items"] = line_items
                    if total_amount is not None:
                        row["total_amount"] = total_amount
                    if tax_amount is not None:
                        row["tax_amount"] = tax_amount
                    if payment_method is not None:
                        row["payment_method"] = payment_method
                    if tax_rate is not None:
                        row["tax_rate"] = tax_rate
                    if discount_total is not None:
                        row["discount_total"] = discount_total
                    if change_given is not None:
                        row["change_given"] = change_given
                    if status is not None:
                        row["status"] = status
                    payload = {"result": row}
                    out = json.dumps(payload)
                    return out
            else:
                payload = {"error": f"Transaction {transaction_id} not found"}
                out = json.dumps(payload)
                return out
        else:
            #--- ADD ---
            if not transaction_id:
                transaction_id = f"TXN-{1000 + len(db) + 1}"
            if (
                store_id is None
                or employee_id is None
                or current_time is None
                or customer_id is None
                or line_items is None
            ):
                payload = {
                        "error": "Missing required field for creation (store_id, employee_id, current_time, customer_id, line_items)"
                    }
                out = json.dumps(
                    payload)
                return out
            new_row = {
                "transaction_id": transaction_id,
                "store_id": store_id,
                "employee_id": employee_id,
                "timestamp": current_time,
                "customer_id": customer_id,
                "line_items": line_items,
                "total_amount": total_amount if total_amount is not None else 0.0,
                "tax_amount": tax_amount if tax_amount is not None else 0.0,
                "payment_method": (
                    payment_method if payment_method is not None else "Unknown"
                ),
                "tax_rate": tax_rate if tax_rate is not None else 0.0,
                "discount_total": discount_total if discount_total is not None else 0.0,
                "change_given": change_given if change_given is not None else 0.0,
                "status": status if status is not None else "completed",
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
                "name": "EditTransactionsDb",
                "description": "Create, update, or delete a transaction row by transaction_id. If delete is True, deletes the row. If transaction_id is given it will edit the row with the given information. If no transaction_id is given, it will create a new row with the given info, as long as store_id, employee_id, timestamp, customer_id, line_items, and current_time are given.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {
                            "type": "string",
                            "default": None,
                            "description": "The transaction id to edit or delete. If not provided, a new id will be generated.",
                        },
                        "delete": {
                            "type": "boolean",
                            "default": False,
                            "description": "Whether to delete the specified transaction.",
                        },
                        "store_id": {
                            "type": "string",
                            "default": None,
                            "description": "Store ID.",
                        },
                        "employee_id": {
                            "type": "string",
                            "default": None,
                            "description": "Employee ID.",
                        },
                        "timestamp": {
                            "type": "string",
                            "default": None,
                            "description": "Timestamp of transaction.",
                        },
                        "customer_id": {
                            "type": "string",
                            "default": None,
                            "description": "Customer ID.",
                        },
                        "line_items": {
                            "type": "array",
                            "items": {"type": "object"},
                            "default": None,
                            "description": "Line items for the transaction.",
                        },
                        "total_amount": {
                            "type": "number",
                            "default": None,
                            "description": "Total amount for the transaction.",
                        },
                        "tax_amount": {
                            "type": "number",
                            "default": None,
                            "description": "Tax amount for the transaction.",
                        },
                        "payment_method": {
                            "type": "string",
                            "default": None,
                            "description": "Payment method.",
                        },
                        "tax_rate": {
                            "type": "number",
                            "default": None,
                            "description": "Tax rate.",
                        },
                        "discount_total": {
                            "type": "number",
                            "default": None,
                            "description": "Total discount applied.",
                        },
                        "change_given": {
                            "type": "number",
                            "default": None,
                            "description": "Change given to customer.",
                        },
                        "status": {
                            "type": "string",
                            "default": None,
                            "description": "Status of transaction.",
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


class GetTransactionsInfoByParam(Tool):  #VIEW
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filter_params: dict[str, Any],
        info_items: list[str] = None
    ) -> str:
        pass
        db = data.get("transactions", [])
        # If sku exists in filter_params, filter transactions based on line_items that include that sku
        filter_params_no_sku = filter_params.copy()
        if "sku" in filter_params.keys():
            db = [
                transaction
                for transaction in db
                if any(
                    item["sku"] in filter_params["sku"]
                    for item in transaction.get("line_items", [])
                )
            ]
            del filter_params_no_sku["sku"]  # Eliminate sku from filter_params after it has been utilized

        filtered_db = _filter_db(db, filter_params_no_sku)
        if not info_items:
            payload = filtered_db
            out = json.dumps(payload)
            return out
        payload = [
            {info_item: row.get(info_item) for info_item in info_items}
            for row in filtered_db
        ]
        out = json.dumps(payload)
        return out
        pass
        db = data.get("transactions", [])
        #If sku exists in filter_params, filter transactions based on line_items that include that sku
        filter_params_no_sku = filter_params.copy()
        if "sku" in filter_params.keys():
            db = [
                transaction
                for transaction in db
                if any(
                    item["sku"] in filter_params["sku"]
                    for item in transaction.get("line_items", [])
                )
            ]
            del filter_params_no_sku["sku"]  #Eliminate sku from filter_params after it has been utilized

        filtered_db = _filter_db(db, filter_params_no_sku)
        if not info_items:
            payload = filtered_db
            out = json.dumps(payload)
            return out
        payload = [
                {info_item: row.get(info_item) for info_item in info_items}
                for row in filtered_db
            ]
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTransactionsInfoByParam",
                "description": "Filter transactions by parameters and return specified fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary of ways to filter items in the database. To pass the filter an item must match one of the possible given values for all the filtering paramets",
                        },
                        "info_items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries.",
                        },
                    },
                    "required": ["filter_params"],
                },
            },
        }


class CreatePurchaseTransaction(Tool):  #CREATE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        customer_id: str,
        employee_id: str,
        items: dict[str, int],
        store_id: str,
        current_time: str,
        payment_method: str
    ) -> str:
        products = {p["sku"]: p for p in data.get("products", [])}
        inventory = data.get("inventory", [])
        transactions = data.get("transactions", [])

        line_items = []
        total_amount = 0.0
        total_tax = 0.0
        discount_total = 0.0
        for sku, quantity in items.items():
            product = products.get(sku)
            if not product:
                payload = {"error": f"Product with SKU {sku} not found."}
                out = json.dumps(payload)
                return out

            # Verify stock availability in inventory
            inv_item = next(
                (i for i in inventory if i["sku"] == sku and i["store_id"] == store_id),
                None,
            )
            if not inv_item or inv_item.get("quantity", 0) < quantity:
                payload = {"error": f"Insufficient stock of SKU {sku} in store {store_id}."}
                out = json.dumps(payload)
                return out

            unit_price = product["price"]
            if product.get("is_discountable", True):
                discount_rate = product.get("discount_rate", 0.0)
                # assign 0 if the value is neither a float nor an integer
                if not isinstance(discount_rate, (float, int)):
                    discount_rate = 0.0
            else:
                discount_rate = 0.0
            discount = discount_rate * unit_price * quantity
            tax = unit_price * quantity * product["tax_rate"]
            line_items.append(
                {
                    "sku": sku,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "discount": discount,
                }
            )
            total_amount += (unit_price * quantity) - discount + tax
            total_tax += tax
            discount_total += discount

            # Reduce stock
            inv_item["quantity"] -= quantity

        transaction_id = f"TXN-{1000 + len(transactions) + 1}"
        transaction = {
            "transaction_id": transaction_id,
            "store_id": store_id,
            "employee_id": employee_id,
            "timestamp": current_time,
            "total_amount": round(total_amount, 2),
            "tax_amount": round(total_tax, 2),
            "payment_method": payment_method,
            "tax_rate": product["tax_rate"],
            "discount_total": round(discount_total, 2),
            "change_given": 0.0,
            "status": "completed",
            "customer_id": customer_id,
            "line_items": line_items,
        }
        transactions.append(transaction)
        payload = transaction
        out = json.dumps(payload)
        return out
        pass
        products = {p["sku"]: p for p in data.get("products", [])}
        inventory = data.get("inventory", [])
        transactions = data.get("transactions", [])

        line_items = []
        total_amount = 0.0
        total_tax = 0.0
        discount_total = 0.0
        for sku, quantity in items.items():
            product = products.get(sku)
            if not product:
                payload = {"error": f"Product with SKU {sku} not found."}
                out = json.dumps(payload)
                return out

            #Verify stock availability in inventory
            inv_item = next(
                (i for i in inventory if i["sku"] == sku and i["store_id"] == store_id),
                None,
            )
            if not inv_item or inv_item.get("quantity", 0) < quantity:
                payload = {"error": f"Insufficient stock of SKU {sku} in store {store_id}."}
                out = json.dumps(
                    payload)
                return out

            unit_price = product["price"]
            if product.get("is_discountable", True):
                discount_rate = product.get("discount_rate", 0.0)
                #assign 0 if the value is neither a float nor an integer
                if not isinstance(discount_rate, (float, int)):
                    discount_rate = 0.0
            else:
                discount_rate = 0.0
            discount = discount_rate * unit_price * quantity
            tax = unit_price * quantity * product["tax_rate"]
            line_items.append(
                {
                    "sku": sku,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "discount": discount,
                }
            )
            total_amount += (unit_price * quantity) - discount + tax
            total_tax += tax
            discount_total += discount

            #Reduce stock
            inv_item["quantity"] -= quantity

        transaction_id = f"TXN-{1000+ len(transactions) + 1}"
        transaction = {
            "transaction_id": transaction_id,
            "store_id": store_id,
            "employee_id": employee_id,
            "timestamp": current_time,
            "total_amount": round(total_amount, 2),
            "tax_amount": round(total_tax, 2),
            "payment_method": payment_method,
            "tax_rate": product["tax_rate"],
            "discount_total": round(discount_total, 2),
            "change_given": 0.0,
            "status": "completed",
            "customer_id": customer_id,
            "line_items": line_items,
        }
        transactions.append(transaction)
        payload = transaction
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePurchaseTransaction",
                "description": "Create a new purchase transaction for a customer, specifying items (SKU:quantity), employee, store, timestamp, and payment method. This checks the stock (but doesn't update it) and also calculates total amount, tax, and discounts. Returns the transaction details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The ID of the customer making the purchase.",
                        },
                        "employee_id": {
                            "type": "string",
                            "description": "The ID of the employee processing the transaction.",
                        },
                        "items": {
                            "type": "object",
                            "description": "Dictionary of SKU to quantity pairs for items being purchased.",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The ID of the store where the purchase is made.",
                        },
                        "current_time": {
                            "type": "string",
                            "format": "date-time",
                            "description": "Timestamp of the transaction (ISO format).",
                        },
                        "payment_method": {
                            "type": "string",
                            "description": "Payment method used for the transaction (e.g., 'credit_card', 'cash').",
                        },
                    },
                    "required": [
                        "customer_id",
                        "employee_id",
                        "items",
                        "store_id",
                        "timestamp",
                        "payment_method",
                    ],
                },
            },
        }


class CreateRefundTransaction(Tool):  #CREATE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sku: str,
        quantity: int,
        employee_id: str,
        current_time: str,
        original_transaction_id: str
    ) -> str:
        transactions = data["transactions"]
        for transaction in transactions:
            if transaction["transaction_id"] == original_transaction_id:
                original_transaction = transaction
                break

        refund_transaction = original_transaction.copy()
        refund_transaction["transaction_id"] = original_transaction_id + "REFUND" + sku
        refund_transaction["employee_id"] = employee_id
        refund_transaction["status"] = "refund"
        refund_transaction["timestamp"] = current_time

        item_info = {}
        for item in original_transaction["line_items"]:
            if item["sku"] == sku:
                item_info = item

        total_refund_amount = (
            item_info["unit_price"] * (1 + original_transaction["tax_rate"]) * quantity
            - item_info["discount"]
        )
        refund_transaction["total_amount"] = (
            total_refund_amount * -1
        )  # Use negative value for refunds

        total_tax = (
            item_info["unit_price"] * original_transaction["tax_rate"] * quantity
        )
        refund_transaction["tax_amount"] = total_tax
        refund_transaction["discount_total"] = 0.0
        refund_transaction["change_given"] = 0.0
        refund_transaction["status"] = "refund"
        item_info["quantity"] = quantity
        refund_transaction["line_items"] = [item_info]

        # Add entry to transactions table
        transactions.append(refund_transaction)
        payload = refund_transaction
        out = json.dumps(payload)
        return out
        pass
        transactions = data["transactions"]
        for transaction in transactions:
            if transaction["transaction_id"] == original_transaction_id:
                original_transaction = transaction
                break

        refund_transaction = original_transaction.copy()
        refund_transaction["transaction_id"] = original_transaction_id + "REFUND" + sku
        refund_transaction["employee_id"] = employee_id
        refund_transaction["status"] = "refund"
        refund_transaction["timestamp"] = current_time

        item_info = {}
        for item in original_transaction["line_items"]:
            if item["sku"] == sku:
                item_info = item

        total_refund_amount = (
            item_info["unit_price"] * (1 + original_transaction["tax_rate"]) * quantity
            - item_info["discount"]
        )
        refund_transaction["total_amount"] = (
            total_refund_amount * -1
        )  #Use negative value for refunds

        total_tax = (
            item_info["unit_price"] * original_transaction["tax_rate"] * quantity
        )
        refund_transaction["tax_amount"] = total_tax
        refund_transaction["discount_total"] = 0.0
        refund_transaction["change_given"] = 0.0
        refund_transaction["status"] = "refund"
        item_info["quantity"] = quantity
        refund_transaction["line_items"] = [item_info]

        #Add entry to transactions table
        transactions.append(refund_transaction)
        payload = refund_transaction
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRefundTransaction",
                "description": "Create a new refund transaction for a given product SKU and customer, using the original transaction's context.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the refunded product.",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "The quantity of items being refunded.",
                        },
                        "employee_id": {
                            "type": "string",
                            "description": "The employee issuing the refund.",
                        },
                        "current_time": {
                            "type": "string",
                            "format": "date-time",
                            "description": "The current time for the refund transaction.",
                        },
                        "original_transaction_id": {
                            "type": "string",
                            "description": "The ID of the original transaction being refunded.",
                        },
                    },
                    "required": [
                        "customer_id",
                        "sku",
                        "quantity",
                        "employee_id",
                        "origional_transaction_id",
                    ],
                },
            },
        }


class GetCustomerPurchaseCountsBySku(Tool):  #VIEW
    @staticmethod
    def invoke(data: dict[str, Any], sku: str) -> str:
        transactions = data["transactions"]
        purchase_counts = {}

        for transaction in transactions:
            customer_id = transaction.get("customer_id")
            for item in transaction.get("line_items", []):
                if item["sku"] == sku:
                    if customer_id:
                        purchase_counts[customer_id] = (
                            purchase_counts.get(customer_id, 0) + item["quantity"]
                        )
        payload = purchase_counts
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerPurchaseCountsBySku",
                "description": "Get a list of customer IDs and how many times they purchased a specific product SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to count purchases for.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }


class GetCustomersAboveXSpend(Tool):  #VIEW
    @staticmethod
    def invoke(data: dict[str, Any], transactions: list[dict[str, Any]] = None, amount: float = None) -> str:
        spend_by_customer = {}
        # Use transactions from data if not provided
        txn_list = transactions if transactions is not None else data.get("transactions", [])
        for txn in txn_list:
            customer_id = txn.get("customer_id")
            total_amount = txn.get("total_amount", 0.0)
            if customer_id:
                spend_by_customer[customer_id] = (
                    spend_by_customer.get(customer_id, 0.0) + total_amount
                )
        result = [cid for cid, spend in spend_by_customer.items() if spend > amount]
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomersAboveXSpend",
                "description": "Return a list of customer IDs who have spent more than the specified amount across all transactions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "amount": {
                            "type": "integer",
                            "description": "The minimum total spend threshold.",
                        }
                    },
                    "required": ["amount"],
                },
            },
        }


#VARIOUS FUNCTIONS


class FilterAndSortIdsByDate(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        ids_dates: dict[str, str],
        filter_start_date: str = None,
        filter_end_date: str = None,
        top_n: int = None,
        sort_order: str = "newest"
    ) -> str:
        # Transform dictionary into a list of tuples (id, date)
        items = list(ids_dates.items())

        def timestamp_to_value(ts: str) -> str:
            return int(
                ts.replace("-", "").replace(":", "").replace("T", "").replace("Z", "")
            )

        # Apply date range filter if specified
        if filter_start_date or filter_end_date:
            filtered = []
            for id_, date in items:
                date_value = timestamp_to_value(date)
                if filter_start_date and date_value < timestamp_to_value(
                    filter_start_date
                ):
                    continue
                if filter_end_date and date_value > timestamp_to_value(filter_end_date):
                    continue
                filtered.append((id_, date))
            result = dict(filtered)
        else:
            # Order by date
            reverse = (
                sort_order == "newest"
            )  # Newest indicates highest values first, which is in reverse order
            sorted_items = sorted(
                items, key=lambda x: timestamp_to_value(x[1]), reverse=reverse
            )
            if top_n is not None:
                sorted_items = sorted_items[:top_n]
            result = dict(sorted_items)
        payload = result
        out = json.dumps(payload)
        return out
        pass
        #Transform dictionary into a list of tuples (id, date)
        items = list(ids_dates.items())

        def timestamp_to_value(ts: str) -> str:
            pass
            return int(
                ts.replace("-", "").replace(":", "").replace("T", "").replace("Z", "")
            )

        #Apply date range filter if specified
        if filter_start_date or filter_end_date:
            filtered = []
            for id_, date in items:
                date_value = timestamp_to_value(date)
                if filter_start_date and date_value < timestamp_to_value(
                    filter_start_date
                ):
                    continue
                if filter_end_date and date_value > timestamp_to_value(filter_end_date):
                    continue
                filtered.append((id_, date))
            result = dict(filtered)
        else:
            #Order by date
            reverse = (
                sort_order == "newest"
            )  #Newest indicates highest values first, which is in reverse order
            sorted_items = sorted(
                items, key=lambda x: timestamp_to_value(x[1]), reverse=reverse
            )
            if top_n is not None:
                sorted_items = sorted_items[:top_n]
            result = dict(sorted_items)
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterAndSortIdsByDate",
                "description": "Filter a dictionary of IDs and dates by date range, or sort and return the top N newest/oldest entries.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ids_dates": {
                            "type": "object",
                            "description": "Dictionary mapping IDs to date strings (ISO format).",
                        },
                        "filter_start_date": {
                            "type": "string",
                            "default": None,
                            "description": "Start date (inclusive) for filtering (ISO format).",
                        },
                        "filter_end_date": {
                            "type": "string",
                            "default": None,
                            "description": "End date (inclusive) for filtering (ISO format).",
                        },
                        "top_n": {
                            "type": "integer",
                            "default": None,
                            "description": "Number of top entries to return after sorting.",
                        },
                        "sort_order": {
                            "type": "string",
                            "default": "desc",
                            "description": "Sort order: 'desc' for newest first, 'asc' for oldest first.",
                        },
                    },
                    "required": ["ids_dates"],
                },
            },
        }


#Enroll all tools
TOOLS = [
    EditCustomersDb(),
    GetCustomersInfoByParam(),
    GetTopNCustomersByLoyaltyPoints(),
    GetCustomersWithBirthdayToday(),
    EditEmployeesDb(),
    GetEmployeesInfoByParam(),
    EditProductsDb(),
    GetProductsInfoByParam(),
    GetTopNMostExpensiveProductsByStore(),
    EditInventoryDb(),
    GetInventoryInfoByParam(),
    CheckLowStock(),
    UpdateInventoryItem(),
    EditPromotionsDb(),
    GetPromotionsInfoByParam(),
    EditTransactionsDb(),
    GetTransactionsInfoByParam(),
    CreateRefundTransaction(),
    CreatePurchaseTransaction(),
    GetCustomerPurchaseCountsBySku(),
    GetCustomersAboveXSpend(),
    FilterAndSortIdsByDate(),
]
