# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool












def _ymd(iso_ts: str) -> str:
    # '2024-08-23T10:00:00Z' -> '2024-08-23'
    return (iso_ts or "").split("T")[0]

def _table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    tbl = data.get(name)
    if not isinstance(tbl, list):
        tbl = []
        data[name] = tbl
    return tbl

def _norm_list(values: List[str]) -> List[str]:
    return sorted(list(dict.fromkeys(values or [])))

def _id_from_request(prefix: str, request_id: str) -> str:
    rid = (request_id or "").strip()
    if not rid:
        return None
    return f"{prefix}_{rid}"

def _get_next_id(prefix: str, existing_ids: List[str]) -> str:
    max_id_num = 0
    seen = False
    for s in existing_ids:
        if isinstance(s, str) and s.startswith(prefix + "_"):
            seen = True
            try:
                n = int(s.split("_")[-1])
                if n > max_id_num:
                    max_id_num = n
            except Exception:
                pass
    return f"{prefix}_{(1 if not seen else max_id_num + 1):03d}"

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