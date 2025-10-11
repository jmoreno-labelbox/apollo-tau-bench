from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os
from . import load_json
def _convert_db_to_list(db_data: Any) -> List[Dict]:
    """Convert database data to list of dicts"""
    if isinstance(db_data, list):
        return db_data
    elif isinstance(db_data, dict):
        return [db_data]
    else:
        return []

class GetTotalDepositsOverPeriod(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_ids: list = None, start_date: str = None, end_date: str = None) -> str:
        if not account_ids or not start_date or not end_date:
            return json.dumps({'error': 'account_ids, start_date, and end_date are required'})
        transactions = load_json('transactions.json')
        transactions = _convert_db_to_list(transactions)
        total = 0.0
        for t in transactions:
            if t['account_id'] in account_ids and t['transaction_type'] == 'Deposit':
                t_date = t['transaction_date'][:10]
                if start_date <= t_date <= end_date:
                    total += t['amount']
        return json.dumps({'total_deposits': total}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'getTotalDepositsOverPeriod',
                'description': 'Sums all deposit-type transactions for a given date range.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'account_ids': {'type': 'array', 'items': {'type': 'string'}, 'description': 'List of account IDs'},
                        'start_date': {'type': 'string', 'description': 'Start date (YYYY-MM-DD)'},
                        'end_date': {'type': 'string', 'description': 'End date (YYYY-MM-DD)'}
                    },
                    'required': ['account_ids', 'start_date', 'end_date']
                }
            }
        }