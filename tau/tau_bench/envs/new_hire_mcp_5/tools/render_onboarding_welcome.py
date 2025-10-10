# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RenderOnboardingWelcome(Tool):
    """
    Render onboarding welcome email content by:
      - confirming candidate_id exists (candidates.json)
      - reading template from /onboarding/templates/Welcome-Email-Template.md (onboarding_files)
      - replacing {{name}}, {{role}}, {{start_date}} (case-insensitive)
    Returns: {candidate_id, file_path, content_text}
    """

    @staticmethod
    def _candidate_exists(data: Dict[str, Any], cand_id: str) -> bool:
        return any(r.get("candidate_id") == cand_id for r in list(data.get("candidates", {}).values()))

    @staticmethod
    def _get_template_text(data: Dict[str, Any]) -> str:
        for f in list(data.get("onboarding_files", {}).values()):
            if f.get("file_path") == TEMPLATE_WELCOME_PATH:
                return f.get("content_text", "")
        return ""

    @staticmethod
    def _fill(template: str, name: str, role: str, start_date: str) -> str:
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        name = kwargs.get("candidate_name", "")
        role = kwargs.get("role_title", "")
        start_date = kwargs.get("start_date", "")

        if not RenderOnboardingWelcome._candidate_exists(data, cand_id):
            return json.dumps({"error": f"candidate_id {cand_id} not found"}, indent=2)

        template_text = RenderOnboardingWelcome._get_template_text(data)
        if not template_text:
            return json.dumps({"error": f"template not found at {TEMPLATE_WELCOME_PATH}"}, indent=2)

        content = RenderOnboardingWelcome._fill(template_text, name, role, start_date)
        return json.dumps({
            "candidate_id": cand_id,
            "file_path": TEMPLATE_WELCOME_PATH,
            "content_text": content
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "render_onboarding_welcome",
                "description": "Return onboarding welcome email content from the stored template with placeholders filled.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "candidate_name": {"type": "string"},
                        "role_title": {"type": "string"},
                        "start_date": {"type": "string"}
                    },
                    "required": ["candidate_id", "candidate_name", "role_title", "start_date"]
                }
            }
        }
