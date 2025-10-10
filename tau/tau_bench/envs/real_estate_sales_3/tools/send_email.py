# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get("client_id")
        broker_id = kwargs.get("broker_id")
        subject = kwargs.get("subject")
        body_uri = kwargs.get("body_uri")
        template_code = kwargs.get("template_code")
        campaign_id = kwargs.get("campaign_id")
        emails = data.get("emails", [])
        new_email_id = _next_int_id(emails, "email_id")
        row = {
            "email_id": new_email_id, "client_id": client_id, "broker_id": broker_id,
            "subject": subject, "body_uri": body_uri, "template_code": template_code,
            "sent_at": _fixed_now_iso(), "campaign_id": campaign_id
        }
        emails.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"send_email",
            "description":"Persist an outbound email.",
            "parameters":{"type":"object","properties":{
                "client_id":{"type":"integer"},"broker_id":{"type":"integer"},
                "subject":{"type":"string"},"body_uri":{"type":"string"},
                "template_code":{"type":"string"},"campaign_id":{"type":["integer","null"]}
            },"required":["client_id","broker_id","subject","body_uri","template_code"]}
        }}
