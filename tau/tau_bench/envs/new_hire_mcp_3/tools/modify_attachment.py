# Sierra Copyright

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso




def _fixed_now_iso():
    return datetime.utcnow().isoformat() + "Z"

class ModifyAttachment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], attachment_id, updates) -> str:
        updates = updates or {}
        attach_id = attachment_id
        attachments = list(data.get("attachments", {}).values())
        for a in attachments:
            if a.get("attachment_id") == attach_id:
                a.update(updates)
                a["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_attachment_id": attach_id, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_attachment",
            "description":"Update an attachment metadata.",
            "parameters":{"type":"object","properties":{"attachment_id":{"type":"string"},"updates":{"type":"object"}},"required":["attachment_id","updates"]}
        }}