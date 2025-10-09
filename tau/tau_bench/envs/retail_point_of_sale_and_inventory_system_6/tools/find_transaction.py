from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class find_transaction(Tool):
    """Searches for and retrieves a transaction. If the transaction_id is known, it returns that specific row. If other parameters are provided, it searches for and returns all transactions that match those parameters."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        transaction_id: str = None,
        store_id: str = None,
        employee_id: str = None,
        customer_id: str = None,
        status: str = None,
        date: str = None
    ) -> str:
        transactions = data.get("transactions", [])

        matches = []
        for transaction in transactions:
            # Utilize transaction_id if provided, prioritizing it over other parameters
            if (transaction_id is not None) and (
                transaction["transaction_id"] == transaction_id
            ):
                return transaction

            # If not, include in the matches list if any search parameters align
            else:
                # Retrieve matches
                store_id_match = (store_id is not None) and (
                    transaction["store_id"] == store_id
                )
                employee_id_match = (employee_id is not None) and (
                    transaction["employee_id"] == employee_id
                )
                customer_id_match = (customer_id is not None) and (
                    transaction["customer_id"] == customer_id
                )
                status_match = (status is not None) and (
                    transaction["status"] == status
                )
                date_match = (date is not None) and (
                    transaction["timestamp"][:10] == date
                )

                # Assess if the row is a match
                # It must satisfy all provided criteria
                is_match = all(
                    [
                        bool_out
                        for key, bool_out in zip(
                            [store_id, employee_id, customer_id, status, date],
                            [
                                store_id_match,
                                employee_id_match,
                                customer_id_match,
                                status_match,
                                date_match,
                            ],
                        )
                        if key is not None
                    ]
                )

                if is_match:
                    matches.append(json.dumps(transaction))
        payload = matches
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindTransaction",
                "description": "Finds a transaction. Will return 1 row if transaction_id is sent, otherwise it will return rows that match the other parameters",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {
                            "type": "string",
                            "description": "The exact id of the transaction if it is known",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The id of the store where the transaction took place",
                        },
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee that processed the order",
                        },
                        "customer_id": {
                            "type": "string",
                            "description": "The id of the customer that made the transaction",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the order",
                        },
                        "date": {
                            "type": "string",
                            "description": "The date of the order. YYYY-MM-DD",
                        },
                    },
                },
            },
        }
