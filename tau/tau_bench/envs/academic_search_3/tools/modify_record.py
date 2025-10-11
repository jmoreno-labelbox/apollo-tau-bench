# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ModifyRecord(Tool):
    """
    Tool to modify fields of any existing record, such as project, article, user, submission, or funding source.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        record_type = kwargs.pop('record_type', None)
        record_id = kwargs.pop('record_id', None)

        if not record_type or not record_id:
            return json.dumps({"error": "The parameters 'record_type' and 'record_id' are required."}, indent=2)

        table_map = {
            "article": (list(data.get('articles', {}).values()), 'article_id'),
            "project": (list(data.get('projects', {}).values()), 'project_id'),
            "user": (list(data.get('users', {}).values()), 'user_id'),
            "submission": (list(data.get('submissions', {}).values()), 'submission_id'),
            "funding_source": (list(data.get('funding_sources', {}).values()), 'funding_source_id'),
            "user_preference": (data.get('user_preferences', []), 'preference_id'),
            "subscription": (list(data.get('subscriptions', {}).values()), 'subscription_id')
        }

        if record_type not in table_map:
            return json.dumps({"error": f"Invalid record type: {record_type}"}, indent=2)

        target_list, id_key = table_map[record_type]

        for item in target_list:
            if item.get(id_key) == record_id:
                # Modify the item using the leftover kwargs.
                for key, value in kwargs.items():
                    item[key] = value
                return json.dumps(item, indent=2)

        return json.dumps({"error": f"Record of type '{record_type}' with ID '{record_id}' not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_record",
                "description": "Modifies fields of an existing record, such as a project, article, user, submission, or funding source.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record_type": {
                            "type": "string",
                            "description": "The type of the record to be modified.",
                            "enum": ["article", "project", "user", "submission", "funding_source", "user_preference", "subscription"]
                        },
                        "record_id": {
                            "type": "string",
                            "description": "The unique ID of the record to be modified."
                        },
                    },
                    "required": ["record_type", "record_id"]
                }
            }
        }
