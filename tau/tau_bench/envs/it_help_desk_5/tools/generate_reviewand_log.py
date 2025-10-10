# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateReviewandLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], log_data) -> str:
        if log_data is None:
            return json.dumps({'status': 'error', 'description': 'The log_data field is required.'}, indent=2)

        formatted_date = FIXED_NOW.split('T')[0].replace('-','_')
        new_report = {
            "run_id": f"rpt_{formatted_date}_0000",
            "report_type": "review_log",
            "started_at": FIXED_NOW,
            "completed_at": FIXED_NOW,
            "output_path_pdf": f"s3://reports/Report_{formatted_date}.pdf",
        }

        reports = data.get('validation_issues', [])
        reports.append(new_report)

        return json.dumps({'status': 'ok', 'description': 'Successfully created pdf and added report to validation_issues.'})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'generate_review_and_log',
                'description': 'Generates a review packet pdf from input data and creates a log in validation_issues.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'log_data': {'type': 'string', 'description': 'The data to log in the report.'},
                    },
                    'required': ['log_data']
                }
            }
        }
