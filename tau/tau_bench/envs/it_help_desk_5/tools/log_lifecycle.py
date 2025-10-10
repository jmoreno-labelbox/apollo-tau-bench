# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogLifecycle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id, event, memo_id) -> str:
        if any([param is None for param in [employee_id, memo_id, event]]):
            return json.dumps({'status': 'error', 'description': 'The employee_id, memo_id, and event fields are required.'}, indent=2)

        lifecycle_items = data.get('lifecycle_queue')

        id = lifecycle_items[-1]['lifecycle_id'].split('_')
        new_lifecycle_id = f'{id[0]}_{str(int(id[1])+1).zfill(5)}'

        lifecycle = {
            "lifecycle_id": new_lifecycle_id,
            "memo_id": memo_id,
            "employee_ref": employee_id,
            "event": event,
            "status": "completed",
            "created_at": FIXED_NOW
        }

        lifecycle_items.append(lifecycle)

        return json.dumps({'status': 'ok', 'description': 'Successfully added log to lifecycle_queue'}, indent=2)


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'log_lifecycle',
                'description': 'Logs data to lifecycle_queue',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'employee_id': {'type': 'string', 'description': 'The id of the employee.'},
                        'memo_id': {'type': 'string', 'description': 'The id of the memo referenced.'},
                        'event': {'type': 'string', 'description': 'The event type of the log'}
                    },
                    'required': ['employee_id', 'memo_id', 'event']
                }
            }
        }
