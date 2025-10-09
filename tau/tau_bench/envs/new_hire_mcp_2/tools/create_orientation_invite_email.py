from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateOrientationInviteEmail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        message_id: str = None,
        subject: str = None,
        body: str = None,
        to_emails: list[str] = None,
        candidate_id: str = None
    ) -> str:
        if to_emails is None:
            to_emails = []
        InsertEmail.invoke(
            data,
            message_id=message_id,
            subject=subject,
            body=body,
            to_emails=to_emails,
            candidate_id=candidate_id,
            draft_flag=False,
            sent_flag=True,
        )
        le = CreateOrGetEmailLabel.invoke
        info = json.loads(le(data, name="Orientation-Invite"))
        lid = info.get("label_id")
        AddLabelsToEmail.invoke(data, message_id=message_id, label_ids=[lid])
        payload = {"message_id": message_id, "label_id": lid}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createOrientationInviteEmail",
                "description": "Create an orientation invite email and label it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "body": {"type": "string"},
                        "to_emails": {"type": "array", "items": {"type": "string"}},
                        "candidate_id": {"type": "string"},
                    },
                    "required": [
                        "message_id",
                        "subject",
                        "body",
                        "to_emails",
                        "candidate_id",
                    ],
                },
            },
        }
