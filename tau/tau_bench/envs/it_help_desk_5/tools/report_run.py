# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReportRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], report_type, run_data) -> str:

        if report_type is None or run_data is None:
            return json.dumps({'status': 'error', 'description': 'The report_type and data fields are required.'}, indent=2)

        run_date = FIXED_NOW.split('T')[0].replace('-','_')
        new_report = {
            "run_id": f"rpt_{run_date}_0000",
            "report_type": report_type,
            "started_at": FIXED_NOW,
            "completed_at": FIXED_NOW,
            "output_path_pdf": f"s3://reports/{report_type}_{run_date}.pdf",
        }

        reports = data.get('report_runs')
        reports.append(new_report)

        return json.dumps({'status': 'ok', 'description': 'Successfully created report pdf and saved a log in report_runs.'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'report_run',
                'description': 'Creates a report log in report_runs.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'report_type': {'type': 'string', 'description': 'The type of the report to write.'},
                        'run_data': {'type': 'array', 'item': {'type': 'string'}, 'description': 'The data to include in the run.'}
                    },
                    'required': ['report_type', 'run_data']
                }
            }
        }
