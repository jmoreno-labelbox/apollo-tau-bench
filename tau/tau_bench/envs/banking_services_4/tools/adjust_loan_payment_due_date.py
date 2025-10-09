from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class AdjustLoanPaymentDueDate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_id: str = None, new_due_date: str = None) -> str:
        if not loan_id or not new_due_date:
            return json.dumps({'error': 'loan_id and new_due_date are required'})
        loans = load_json('loans.json')
        loan = next((l for l in loans.values() if l['loan_id'] == loan_id), None)
        if not loan or 'maturity_date' not in loan:
            return json.dumps({'error': 'Loan not found or maturity_date not present.'})
        loan['maturity_date'] = new_due_date
        return json.dumps({'success': True, 'loan_id': loan_id, 'new_due_date': new_due_date})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'adjustLoanPaymentDueDate',
                'description': 'Modifies the due date of a loan repayment (policy-checked, only if maturity_date exists).',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'loan_id': {'type': 'string', 'description': 'Loan ID'},
                        'new_due_date': {'type': 'string', 'description': 'New due date (YYYY-MM-DD)'}
                    },
                    'required': ['loan_id', 'new_due_date']
                }
            }
        }
