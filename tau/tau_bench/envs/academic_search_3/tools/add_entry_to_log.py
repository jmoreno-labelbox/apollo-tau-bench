from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddEntryToLog(Tool):
    """Utility for appending a log note to a user, project, submission, or article."""

    @staticmethod
    def invoke(data: dict[str, Any], *, notes: Any = None, user_id: str = None, project_id: str = None, submission_id: str = None, article_id: str = None) -> str:
        target_list = None
        target_id_key = None
        target_id_value = None

        if user_id is not None:
            target_list = data.get("users", {}).values()
            target_id_key = "user_id"
            target_id_value = user_id
        elif project_id is not None:
            target_list = data.get("projects", {}).values()
            target_id_key = "project_id"
            target_id_value = project_id
        elif submission_id is not None:
            target_list = data.get("submissions", {}).values()
            target_id_key = "submission_id"
            target_id_value = submission_id
        elif article_id is not None:
            target_list = data.get("articles", {}).values()
            target_id_key = "article_id"
            target_id_value = article_id
        else:
            payload = {
                "error": "Either user_id, project_id, submission_id, or article_id is required."
            }
            out = json.dumps(payload, indent=2)
            return out

        for item in target_list:
            if item.get(target_id_key) == target_id_value:
                if "logs" not in item:
                    item["logs"] = []
                item["logs"].append(notes)
                payload = item
                out = json.dumps(payload, indent=2)
                return out
        payload = {
            "error": f"Item with ID '{target_id_value}' not found in the specified table."
        }
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddEntryToLog",
                "description": "Adds a log entry for a user, project, submission, or article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user to add the log to.",
                        },
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project to add the log to.",
                        },
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to add the log to.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to add the log to.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "The content of the log note.",
                        },
                    },
                    "required": ["notes"],
                },
            },
        }
