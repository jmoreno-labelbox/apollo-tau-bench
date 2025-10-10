# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterHRMemos(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], first_name, last_name, type) -> str:
        memos = data.get('hr_memos')
        memo_type = type

        if first_name is None or last_name is None:
            if memo_type is not None:
                temp_memos = [memo for memo in memos if memo['type'] == memo_type]
            else:
                return json.dumps({'status': 'error', 'reason': 'Insufficient information to filter memos.'}, indent=2)
        else:
            temp_memos = [memo for memo in memos if memo['first_name'] == first_name and memo['last_name'] == last_name]

        if len(temp_memos) == 0:
            return json.dumps({'status': 'error', 'reason': 'Unable to find specified memos'}, indent=2)

        return json.dumps(temp_memos, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'filter_hr_memos',
                'description': 'Filters HR memos for matching criteria.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'first_name': {'type': 'string', 'description': 'The first name of the person being searched for.'},
                        'last_name': {'type': 'string', 'description': 'The last name of the person being searched for.'},
                        'type': {'type': 'string', 'description': 'The type of memo being searched for.'},
                    },
                }
            }
        }
