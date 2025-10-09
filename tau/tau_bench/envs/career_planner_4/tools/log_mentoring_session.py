from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class LogMentoringSession(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
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
        payload = {"success": f"Mentoring session logged for {mentee_id} with {mentor_id}"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "logMentoringSession",
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
