# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_transaction(Tool):
    """
    Searches for and returns a transaction. If the transaction_id is known, it will return that exact row. If the other parameters are sent, then it will search for and return all transactions matching those parameters
    """

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id, date, employee_id, status, store_id, transaction_id) -> str:

        transactions = list(data.get("transactions", {}).values())

        matches = []
        for transaction in transactions:
            # Use transaction_id if provided, prioritizing it over other parameters.
            if (transaction_id is not None) and (
                transaction["transaction_id"] == transaction_id
            ):
                return transaction

            # If any search parameters match, include them in the list of matches.
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

                # Check if the row is a match.
                # It must fulfill all specified criteria.
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

        return json.dumps(matches)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_transaction",
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
