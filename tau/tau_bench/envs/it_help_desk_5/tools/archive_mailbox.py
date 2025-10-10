# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ArchiveMailbox(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get('employee_id')
        department = kwargs.get('department')
        if employee_id is None or department is None:
            return json.dumps({'status': 'error', 'description': 'The employee_id and department fields are required.'}, indent=2)

        mailboxes = data.get('mailboxes')
        archives = data.get('data_archives')

        for mailbox in mailboxes:
            if mailbox['employee_id'] == employee_id:
                archive = {
                    "archive_id": "arch_000000",
                    "employee_id": employee_id,
                    "mailbox_id": mailbox['mailbox_id'],
                    "archive_path": f"s3://corp-archives/mail/{employee_id}/{FIXED_NOW.split('T')[0]}",
                    "retention_policy": None,
                    "created_at": FIXED_NOW
                }
                if department == 'Finance':
                    archive['retention_policy'] = 'finance_7y'
                else:
                    archive['retention_policy'] = 'std_2y'

                archives.append(archive)

                return json.dumps({'status': 'ok', 'description': 'Successfully created mailbox'}, indent=2)
        return json.dumps({'status': 'error', 'description': 'Employee mailbox not found'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'archive_mailbox',
                'description': "Archives an employee's mailbox",
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'employee_id': {'type': 'string', 'description': 'The id of the employee to archive.'},
                        'department': {'type': 'string', 'description': "The employee's department."},
                    },
                    'required': ['employee_id', 'department']
                }
            }
        }
