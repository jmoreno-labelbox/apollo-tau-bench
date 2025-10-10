# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchGmailThreadsTool(Tool):
    """Search Gmail threads by label, participant, or topic keyword."""

    @staticmethod
    def invoke(data: Dict[str, Any], keyword, label, participant) -> str:

        threads = list(data.get("gmail_threads", {}).values())
        out = []
        for t in threads:
            if label and label not in (t.get("current_labels") or []):
                continue
            if participant:
                ps = (t.get("participants") or []) + (t.get("recipients") or [])
                if participant not in ps:
                    continue
            if keyword and keyword.lower() not in (t.get("subject","").lower()):
                continue
            out.append(_small_fields(t, ["thread_id","subject","current_labels","updated_ts"]))
        out.sort(key=lambda r: r.get("thread_id",""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"search_gmail_threads",
            "description":"Search Gmail threads by label, participant, or subject keyword.",
            "parameters":{"type":"object","properties":{
                "label":{"type":"string"},
                "participant":{"type":"string"},
                "keyword":{"type":"string"}
            }}
        }}
