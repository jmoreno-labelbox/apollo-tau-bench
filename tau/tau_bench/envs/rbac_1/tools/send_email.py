# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        emails = data.get('emails', [])
        new_id_num = max((int(e['email_id'][3:]) for e in emails), default=0) + 1
        new_email_id = f"EM-{new_id_num:03d}"
        new_email = {
                "email_id": new_email_id,
                "sender": kwargs.get("sender"),
                "receiver": kwargs.get("receiver"),
                "subject": kwargs.get("subject"),
                "text_content": kwargs.get("text_content"),
                "timestamp": kwargs.get("timestamp"),
        }
        emails.append(new_email)
        data['emails'] = emails
        return json.dumps(new_email)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "send_email",
                        "description": "Sends an email to a specified recipient.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "receiver": {"type": "string"},
                                        "sender": {"type": "string"},
                                        "timestamp": {"type": "string"},
                                        "subject": {"type": "string"},
                                        "text_content": {"type": "string"}
                                },
                                "required": ["receiver", "sender", "timestamp", "subject", "text_content"]
                        }
                }
        }
