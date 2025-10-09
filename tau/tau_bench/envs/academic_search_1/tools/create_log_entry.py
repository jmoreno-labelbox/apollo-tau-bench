from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateLogEntry(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        article_id: str = None,
        notes: str = None,
        relevance: str = "medium",
        log_id_override: str = None
    ) -> str:
        if not all([user_id, notes]):
            payload = {"error": "user_id and notes are required."}
            out = json.dumps(payload)
            return out
        users, articles, logs = (
            data.get("users", []),
            data.get("articles", []),
            data.get("research_logs", []),
        )
        if not any(u["person_id"] == user_id for u in users):
            payload = {"error": f"User with ID '{user_id}' not found."}
            out = json.dumps(payload)
            return out

        if article_id:
            if not any(a["paper_id"] == article_id for a in articles):
                payload = {"error": f"Article with ID '{article_id}' not found."}
                out = json.dumps(payload)
                return out
        new_log_id = (
            log_id_override if log_id_override else f"log_{uuid.uuid4().hex[:4]}"
        )
        if log_id_override and any(log["record_log_id"] == log_id_override for log in logs):
            payload = {
                "error": f"A log entry with the override ID '{log_id_override}' already exists."
            }
            out = json.dumps(payload)
            return out
        new_log_entry = {
            "record_log_id": new_log_id,
            "investigator_id": user_id,
            "paper_id": article_id,
            "recorded_date": datetime.now().strftime("%Y-%m-%d"),
            "annotations": notes,
            "significance": relevance,
        }
        logs.append(new_log_entry)

        if article_id:
            for user in users:
                if (
                    user["person_id"] == user_id
                    and article_id not in user["recorded_papers"]
                ):
                    user["recorded_papers"].append(article_id)
                    break
        payload = {"success": True, "log_entry": new_log_entry}
        out = json.dumps(payload)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "CreateLogEntry",
                "description": "Creates a new entry in the research log for a specific user and optionally for an article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the researcher creating the log.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article being logged. This is optional.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "The personal notes about the article or task.",
                        },
                        "relevance": {
                            "type": "string",
                            "description": "The relevance of the entry. E.g., 'high', 'medium', 'low'. Defaults to 'medium'.",
                        },
                        "log_id_override": {
                            "type": "string",
                            "description": "Optional. A specific ID to assign to the new log entry for predictable referencing.",
                        },
                    },
                    "required": ["user_id", "notes"],
                },
            },
        }
