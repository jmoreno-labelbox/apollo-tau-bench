# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GeneratePersonalizedWelcomeFileTool(Tool):
    """Creates customized welcome markdown in onboarding_files table for one or more candidates."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, candidate_ids) -> str:

        ids_to_process = []
        if candidate_ids:
            ids_to_process.extend(candidate_ids)
        if candidate_id:
            ids_to_process.append(candidate_id)

        if not ids_to_process:
            return _err("candidate_id or candidate_ids is required.")

        candidates_map = {str(c.get("candidate_id")): c for c in data.get("candidates", [])}
        onboarding_files = data.setdefault("onboarding_files", [])
        created_files = []

        for cid in ids_to_process:
            candidate = candidates_map.get(cid)
            if not candidate:
                if len(ids_to_process) == 1:
                    return _err(f"Candidate '{cid}' not found.", code="not_found")
                continue

            # Static markdown template
            template_content = """
# Greetings, {{candidate_name}}!

We are thrilled to have you join us as a {{role_title}}. Your first day will be on {{start_date}}.
Your manager will be {{manager_email_nullable}}.

We've prepared this packet to help you get started.
"""

            context = candidate
            content = _render_template(template_content, context)

            new_file_path = f"/onboarding/{cid}/welcome_packet.md"

            new_file = {
                "file_path": new_file_path,
                "content_text": content,
                "mime_type": "text/markdown",
                "created_ts": HARD_TS,
                "updated_ts": HARD_TS,
                "candidate_id": cid
            }
            onboarding_files.append(new_file)
            created_files.append(new_file)

        return json.dumps(created_files, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_personalized_welcome_file",
                "description": "Creates customized welcome markdown for one or more candidates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "A single target candidate identifier."},
                        "candidate_ids": {"type": "array", "items": {"type": "string"}, "description": "A list of target candidate identifiers."}
                    },
                },
            },
        }
