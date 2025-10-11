# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddAttachment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], attachment) -> str:
        new_attach = attachment or {}
        attachments = list(data.get("attachments", {}).values())
        attachments.append(new_attach)
        data["attachments"] = attachments
        return json.dumps({"added_attachment": new_attach}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_attachment",
            "description":"Add a new attachment.",
            "parameters":{"type":"object","properties":{"attachment":{"type":"object"}},"required":["attachment"]}
        }}
