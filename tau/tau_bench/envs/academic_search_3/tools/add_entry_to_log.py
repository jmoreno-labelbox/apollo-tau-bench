# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddEntryToLog(Tool):
    """Tool to add a log note to a user, project, submission or article."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        notes = kwargs.get('notes')
        target_list = None
        target_id_key = None
        target_id_value = None

        if 'user_id' in kwargs:
            target_list = list(data.get('users', {}).values())
            target_id_key = 'user_id'
            target_id_value = kwargs['user_id']
        elif 'project_id' in kwargs:
            target_list = list(data.get('projects', {}).values())
            target_id_key = 'project_id'
            target_id_value = kwargs['project_id']
        elif 'submission_id' in kwargs:
            target_list = list(data.get('submissions', {}).values())
            target_id_key = 'submission_id'
            target_id_value = kwargs['submission_id']
        elif 'article_id' in kwargs:
            target_list = list(data.get('articles', {}).values())
            target_id_key = 'article_id'
            target_id_value = kwargs['article_id']
        else:
            return json.dumps({"error": "Either user_id, project_id, submission_id, or article_id is required."}, indent=2)

        for item in target_list:
            if item.get(target_id_key) == target_id_value:
                if 'logs' not in item:
                    item['logs'] = []
                item['logs'].append(notes)
                return json.dumps(item, indent=2)

        return json.dumps({"error": f"Item with ID '{target_id_value}' not found in the specified table."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "add_entry_to_log", "description": "Adds a log entry for a user, project, submission, or article.", "parameters": {"type": "object", "properties": {
            "user_id": {"type": "string", "description": "The ID of the user to add the log to."},
            "project_id": {"type": "string", "description": "The ID of the project to add the log to."},
            "submission_id": {"type": "string", "description": "The ID of the submission to add the log to."},
            "article_id": {"type": "string", "description": "The ID of the article to add the log to."},
            "notes": {"type": "string", "description": "The content of the log note."}
        }, "required": ["notes"]}}}
