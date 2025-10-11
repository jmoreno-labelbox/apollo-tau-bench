# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateLogEntry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], article_id, log_id_override, notes, user_id, relevance = 'medium') -> str:
        user_id,article_id,notes,relevance,log_id_override = user_id,article_id,notes,relevance,log_id_override

        if not all([user_id, notes]):
            return json.dumps({"error": "user_id and notes are required."})
        users, articles, logs = list(data.get('users', {}).values()), list(data.get('articles', {}).values()), list(data.get('research_logs', {}).values())
        if not any(u['user_id'] == user_id for u in users):
            return json.dumps({"error": f"User with ID '{user_id}' not found."})

        if article_id:
            if not any(a['article_id'] == article_id for a in articles):
                return json.dumps({"error": f"Article with ID '{article_id}' not found."})
        new_log_id = log_id_override if log_id_override else f"log_{uuid.uuid4().hex[:4]}"
        if log_id_override and any(log['log_id'] == log_id_override for log in logs):
            return json.dumps({"error": f"A log entry with the override ID '{log_id_override}' already exists."})
        new_log_entry = {"log_id": new_log_id, "researcher_id": user_id, "article_id": article_id, "entry_date": datetime.now().strftime('%Y-%m-%d'), "notes": notes, "relevance": relevance}
        logs.append(new_log_entry)

        if article_id:
            for user in users:
                if user['user_id'] == user_id and article_id not in user['logged_articles']:
                    user['logged_articles'].append(article_id)
                    break
        return json.dumps({"success": True, "log_entry": new_log_entry})
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {"type": "function", "function": {"name": "create_log_entry", "description": "Creates a new entry in the research log for a specific user and optionally for an article.", "parameters": {"type": "object", "properties": {"user_id": {"type": "string", "description": "The ID of the researcher creating the log."}, "article_id": {"type": "string", "description": "The ID of the article being logged. This is optional."}, "notes": {"type": "string", "description": "The personal notes about the article or task."}, "relevance": {"type": "string", "description": "The relevance of the entry. E.g., 'high', 'medium', 'low'. Defaults to 'medium'."}, "log_id_override": {"type": "string", "description": "Optional. A specific ID to assign to the new log entry for predictable referencing."}}, "required": ["user_id", "notes"]}}}
