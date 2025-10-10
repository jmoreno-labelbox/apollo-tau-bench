# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_gmail_thread(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], subject: str, sender_email: str, recipients: List[str], labels: List[str], timestamp: str, request_id: str) -> str:
        threads = _table(data, "gmail_threads")
        thr_id = _id_from_request("thr", request_id)
        if thr_id:
            for t in threads:
                if isinstance(t, dict) and t.get("thread_id") == thr_id:
                    return json.dumps(t, indent=2)

        row = {
            "thread_id": thr_id or _get_next_id("thread", [r.get("thread_id", "") for r in threads if isinstance(r, dict)]),
            "subject": subject,
            "to": _norm_list(recipients),
            "current_labels": _norm_list(labels),
            "sender_email": sender_email,
            "day": _ymd(timestamp),
        }
        threads.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"create_gmail_thread","description":"Create or reuse a deterministic thread (thr_<request_id>).","parameters":{"type":"object","properties":{"subject":{"type":"string"},"sender_email":{"type":"string"},"recipients":{"type":"array","items":{"type":"string"}},"labels":{"type":"array","items":{"type":"string"}},"timestamp":{"type":"string"},"request_id":{"type":"string"}},"required":["subject","sender_email","recipients","labels","timestamp","request_id"]}}}
