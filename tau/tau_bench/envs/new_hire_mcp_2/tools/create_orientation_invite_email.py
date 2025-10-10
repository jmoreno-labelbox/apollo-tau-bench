# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOrientationInviteEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        message_id = kwargs.get("message_id")
        subject = kwargs.get("subject")
        body = kwargs.get("body")
        to_emails = kwargs.get("to_emails", [])
        candidate_id = kwargs.get("candidate_id")
        InsertEmail.invoke(data, message_id=message_id, subject=subject, body=body, to_emails=to_emails,
                           candidate_id=candidate_id, draft_flag=False, sent_flag=True)
        le = CreateOrGetEmailLabel.invoke
        info = json.loads(le(data, name="Orientation-Invite"))
        lid = info.get("label_id")
        AddLabelsToEmail.invoke(data, message_id=message_id, label_ids=[lid])
        return json.dumps({"message_id": message_id, "label_id": lid}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_orientation_invite_email",
                                                 "description": "Create an orientation invite email and label it.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"message_id": {"type": "string"},
                                                                               "subject": {"type": "string"},
                                                                               "body": {"type": "string"},
                                                                               "to_emails": {"type": "array", "items": {
                                                                                   "type": "string"}},
                                                                               "candidate_id": {"type": "string"}},
                                                                "required": ["message_id", "subject", "body",
                                                                             "to_emails", "candidate_id"]}}}
