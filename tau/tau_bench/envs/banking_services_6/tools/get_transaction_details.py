from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetTransactionDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], transaction_id: str = None) -> str:
        transaction = next((t for t in data.get('transactions', {}).values() if t['transaction_id'] == transaction_id), None)
        if transaction:
            return json.dumps(transaction)
        return json.dumps({"error": "Transaction not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetTransactionDetails",
                        "description": "Retrieves the full details of a single transaction.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "transaction_id": {"type": "string", "description": "The unique ID of the transaction."}
                                },
                                "required": ["transaction_id"]
                        }
                }
        }
