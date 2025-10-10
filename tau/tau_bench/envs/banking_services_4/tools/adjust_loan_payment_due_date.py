# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AdjustLoanPaymentDueDate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        loan_id = kwargs.get('loan_id')
        new_due_date = kwargs.get('new_due_date')
        if not loan_id or not new_due_date:
            return json.dumps({'error': 'loan_id and new_due_date are required'})
        loans = load_json('loans.json')
        loan = next((l for l in loans if l['loan_id'] == loan_id), None)
        if not loan or 'maturity_date' not in loan:
            return json.dumps({'error': 'Loan not found or maturity_date not present.'})
        loan['maturity_date'] = new_due_date
        return json.dumps({'success': True, 'loan_id': loan_id, 'new_due_date': new_due_date})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'adjust_loan_payment_due_date',
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
