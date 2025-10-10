from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os

class CreateSupportTicketForAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, account_id: str = None, reason: str = None) -> str:
        if not customer_id or not account_id or not reason:
            return json.dumps({'error': 'customer_id, account_id, and reason are required'})

        new_ticket = {
            "ticket_id": f"tkt_{generate_unique_id()}",
            "customer_id": customer_id,
            "status": "Open",
            "priority": "High",
            "channel": "System",
            "category": "Account Inquiry",
            "request_details": {
                "target_entity": "Account",
                "target_id": account_id,
                "operation": "INVESTIGATE",
                "parameters": {"reason": reason}
            }
        }

        return json.dumps({'success': True, 'ticket_created': new_ticket}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'createSupportTicketForAccount',
                'description': 'Creates a high-priority support ticket to investigate an issue related to an account.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {
                            'type': 'string',
                            'description': 'The ID of the customer reporting the issue.'
                        },
                        'account_id': {
                            'type': 'string',
                            'description': 'The ID of the account to be investigated.'
                        },
                        'reason': {
                            'type': 'string',
                            'description': 'The reason for creating the support ticket.'
                        }
                    },
                    'required': ['customer_id', 'account_id', 'reason']
                }
            }
        }
