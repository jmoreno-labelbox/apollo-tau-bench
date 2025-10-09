from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RenderOnboardingWelcome(Tool):
    """
    Generate the onboarding welcome email content by:
      - verifying candidate_id is present (candidates.json)
      - loading template from /onboarding/templates/Welcome-Email-Template.md (onboarding_files)
      - substituting {{name}}, {{role}}, {{start_date}} (case-insensitive)
    Returns: {candidate_id, file_path, content_text}
    """

    @staticmethod
    def _candidate_exists(data: dict[str, Any], cand_id: str) -> bool:
        pass
        return any(r.get("candidate_id") == cand_id for r in data.get("candidates", {}).values()

    @staticmethod
    def _get_template_text(data: dict[str, Any]) -> str:
        pass
        for f in data.get("onboarding_files", {}).values():
            if f.get("file_path") == TEMPLATE_WELCOME_PATH:
                return f.get("content_text", "")
        return ""

    @staticmethod
    def _fill(template: str, name: str, role: str, start_date: str) -> str:
        pass
        repls = {
            r"\{\{\s*name\s*\}\}": name,
            r"\{\{\s*role\s*\}\}": role,
            r"\{\{\s*start[_\s]*date\s*\}\}": start_date,
        }
        out = template
        for pat, val in repls.items():
            out = re.sub(pat, val, out, flags=re.IGNORECASE)
        return out

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str, candidate_name: str = "", role_title: str = "", start_date: str = "") -> str:
        cand_id = candidate_id
        name = candidate_name
        role = role_title
        start_date = start_date

        if not RenderOnboardingWelcome._candidate_exists(data, cand_id):
            payload = {"error": f"candidate_id {cand_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        template_text = RenderOnboardingWelcome._get_template_text(data)
        if not template_text:
            payload = {"error": f"template not found at {TEMPLATE_WELCOME_PATH}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        content = RenderOnboardingWelcome._fill(template_text, name, role, start_date)
        payload = {
                "candidate_id": cand_id,
                "file_path": TEMPLATE_WELCOME_PATH,
                "content_text": content,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RenderOnboardingWelcome",
                "description": "Return onboarding welcome email content from the stored template with placeholders filled.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "candidate_name": {"type": "string"},
                        "role_title": {"type": "string"},
                        "start_date": {"type": "string"},
                    },
                    "required": [
                        "candidate_id",
                        "candidate_name",
                        "role_title",
                        "start_date",
                    ],
                },
            },
        }
