from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

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
        db = _convert_db_to_list(data.get("customers", {}))
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
        db = _convert_db_to_list(data.get("customers", {}))
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
