# Copyright (c) Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class schedule_mentorship_session(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], relationship_id: str, session_date: str) -> str:
        sessions = data.setdefault("scheduled_mentorship_sessions", [])
        sessions.append(
            {
                "relationship_id": relationship_id,
                "session_date": session_date,
                "status": "Scheduled",
            }
        )
        return json.dumps({"scheduled_for": session_date})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "schedule_mentorship_session",
                "description": "Schedule a mentorship session for an existing relationship.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "relationship_id": {"type": "string"},
                        "session_date": {"type": "string"},
                    },
                    "required": ["relationship_id", "session_date"],
                },
            },
        }
