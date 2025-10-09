from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

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
        db = _convert_db_to_list(data.get("transactions", {}))
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
        pass
        db = _convert_db_to_list(data.get("transactions", {}))
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
