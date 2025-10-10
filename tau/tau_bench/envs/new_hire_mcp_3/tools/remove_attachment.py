# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveAttachment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        attach_id = kwargs.get("attachment_id")
        attachments = data.get("attachments", [])
        data["attachments"] = [a for a in attachments if a.get("attachment_id") != attach_id]
        return json.dumps({"removed_attachment_id": attach_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"remove_attachment",
            "description":"Remove an attachment by ID.",
            "parameters":{"type":"object","properties":{"attachment_id":{"type":"string"}},"required":["attachment_id"]}
        }}
