from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
        db = _convert_db_to_list(data.get("employees", {}).values()
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
        db = _convert_db_to_list(data.get("employees", {}).values()
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
