# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Notify(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], summary, recipient_ids = []) -> str:

        if len(recipient_ids) == 0 or summary is None:
            return json.dumps({'status': 'error', 'reason': 'The recipient_ids and summary fields are required.'}, indent=2)

        return json.dumps({'status': 'ok', 'recipients': recipient_ids, 'summary': summary}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'notify',
                'description': 'Notifies employees in recipient_ids with the contents of summary.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'recipient_ids': {'type': 'array', 'items': {'type': 'string'}, 'description': 'The ids of the recipients to notify.'},
                        'summary': {'type': 'string', 'description': 'The summary to send to each recipient.'},
                    },
                    'required': ['recipient_ids', 'summary']
                }
            }
        }
