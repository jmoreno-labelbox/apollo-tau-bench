from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ModifyRecord(Tool):
    """Utility for updating fields of any existing record, including project, article, user, submission, or funding source."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        record_type: str = None, 
        record_id: str = None, 
        modifications: dict[str, Any] = None,
        status: str = None,
        linked_articles: list = None,
        funding_source_id: str = None,
        lead_researcher_id: Any = None,
        assigned_reviewers: list = None,
        publication_date: str = None,
        end_date: str = None,
        logs: list = None,
        institution: str = None,
        team_members: list = None
    ) -> str:
        if not record_type or not record_id:
            payload = {"error": "The parameters 'record_type' and 'record_id' are required."}
            out = json.dumps(payload, indent=2)
            return out

        table_map = {
            "article": (data.get("articles", {}).values()), "article_id"),
            "project": (data.get("projects", {}).values()), "project_id"),
            "user": (data.get("users", {}).values()), "user_id"),
            "submission": (data.get("submissions", {}).values()), "submission_id"),
            "funding_source": (data.get("funding_sources", {}).values()), "funding_source_id"),
            "user_preference": (data.get("user_preferences", {}).values()), "preference_id"),
            "subscription": (data.get("subscriptions", {}).values()), "subscription_id"),
        }

        if record_type not in table_map:
            payload = {"error": f"Invalid record type: {record_type}"}
            out = json.dumps(payload, indent=2)
            return out

        target_list, id_key = table_map[record_type]

        for item in target_list:
            if item.get(id_key) == record_id:
                # Apply modifications from the modifications parameter
                if modifications:
                    for key, value in modifications.items():
                        item[key] = value
                
                # Apply modifications from individual parameters
                individual_params = {
                    "status": status,
                    "linked_articles": linked_articles,
                    "funding_source_id": funding_source_id,
                    "lead_researcher_id": lead_researcher_id,
                    "assigned_reviewers": assigned_reviewers,
                    "publication_date": publication_date,
                    "end_date": end_date,
                    "logs": logs,
                    "institution": institution,
                    "team_members": team_members
                }
                
                for key, value in individual_params.items():
                    if value is not None:
                        item[key] = value
                        
                payload = item
                out = json.dumps(payload, indent=2)
                return out
        payload = {
            "error": f"Record of type '{record_type}' with ID '{record_id}' not found."
        }
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ModifyRecord",
                "description": "Modifies fields of an existing record, such as a project, article, user, submission, or funding source. Can accept individual field parameters or a modifications object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record_type": {
                            "type": "string",
                            "description": "The type of the record to be modified.",
                            "enum": [
                                "article",
                                "project",
                                "user",
                                "submission",
                                "funding_source",
                                "user_preference",
                                "subscription",
                            ],
                        },
                        "record_id": {
                            "type": "string",
                            "description": "The unique ID of the record to be modified.",
                        },
                        "modifications": {
                            "type": "object",
                            "description": "A dictionary of field modifications.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status field to update.",
                        },
                        "linked_articles": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of linked article IDs.",
                        },
                        "funding_source_id": {
                            "type": "string",
                            "description": "The funding source ID.",
                        },
                        "lead_researcher_id": {
                            "description": "The lead researcher ID (can be string or array).",
                        },
                        "assigned_reviewers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of assigned reviewer IDs.",
                        },
                        "publication_date": {
                            "type": "string",
                            "description": "The publication date.",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date.",
                        },
                        "logs": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of log entries.",
                        },
                        "institution": {
                            "type": "string",
                            "description": "The institution name.",
                        },
                        "team_members": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of team member IDs.",
                        },
                    },
                    "required": ["record_type", "record_id"],
                },
            },
        }
