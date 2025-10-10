# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SaveReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        save_data = kwargs.get('save_data',[])

        if len(save_data) == 0:
            return json.dumps({'status': 'error', 'description': 'The save_data and file_path parameters are required.'}, indent=2)

        new_report = {
            'save_data': save_data,
            'file_path': '/IT/Reports/Backlog/Backlog_Status.pdf'
        }

        return json.dumps(new_report, indent=2)


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'save_report',
                'description': 'Saves a report containing data called Backlog_Status.pdf',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'save_data': {'type': 'array', 'items': {'type': 'string'}, 'description': 'An array containing data to save'},
                    },
                    'required': ['save_data']
                }
            }
        }
