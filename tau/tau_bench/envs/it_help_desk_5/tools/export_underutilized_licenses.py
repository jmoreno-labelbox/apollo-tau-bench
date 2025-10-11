# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExportUnderutilizedLicenses(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], output_data) -> str:
        csv_data = output_data
        if csv_data is None:
            return json.dumps({'status': 'error', 'description': 'The data field is required.'}, indent=2)

        csv_path = 'reports/underutilized_licenses.csv'
        return json.dumps({'path': csv_path, 'licenses': csv_data})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'export_underutilized_licenses',
                'description': 'Exports a CSV underutilized licenses',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'output_data': {'type': 'array', 'items':{'type': 'string'}, 'description': 'The data to be written to a CSV.'},
                    },
                    'required': ['output_data']
                }
            }
        }
