from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCustomerLoansTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        loans = data.get('loans', [])

        customer_loans = []
        for loan in loans:
            if loan['customer_id'] == customer_id:
                customer_loans.append({
                    'loan_id': loan['loan_id'],
                    'loan_type': loan['loan_type'],
                    'original_amount': loan['principal_amount'],
                    'current_balance': loan['current_balance'],
                    'interest_rate': loan['interest_rate'],
                    'monthly_payment': loan['monthly_payment'],
                    'status': loan['status']
                })

        return json.dumps(customer_loans, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerLoans",
                "description": "Get all loans for a specific customer",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"}
                    },
                    "required": ["customer_id"]
                }
            }
        }
