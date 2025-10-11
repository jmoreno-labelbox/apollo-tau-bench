# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], receiver, sender, subject, text_content, timestamp) -> str:
        emails = data.get('emails', [])
        new_id_num = max((int(e['email_id'][3:]) for e in emails), default=0) + 1
        new_email_id = f"EM-{new_id_num:03d}"
        new_email = {
                "email_id": new_email_id,
                "sender": sender,
                "receiver": receiver,
                "subject": subject,
                "text_content": text_content,
                "timestamp": timestamp,
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
