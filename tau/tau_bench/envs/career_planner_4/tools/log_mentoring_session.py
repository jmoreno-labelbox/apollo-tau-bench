# Copyright Sierra

import uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class log_mentoring_session(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        mentee_id: str,
        mentor_id: str,
        session_date: str,
        notes: str,
    ) -> str:
        session = {
            "session_id": f"MS{uuid.uuid4().hex[:6]}",
            "mentee_id": mentee_id,
            "mentor_id": mentor_id,
            "session_date": session_date,
            "notes": notes,
        }
        data.setdefault("mentoring_sessions", []).append(session)
        return json.dumps(
            {"success": f"Mentoring session logged for {mentee_id} with {mentor_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "log_mentoring_session",
                "description": "Log a mentoring session",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mentee_id": {"type": "string"},
                        "mentor_id": {"type": "string"},
                        "session_date": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["mentee_id", "mentor_id", "session_date", "notes"],
                },
            },
        }
