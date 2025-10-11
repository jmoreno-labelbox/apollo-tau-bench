# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _next_seq(rows, key, prefix):
    mx = 0
    pat = re.compile(rf"^{re.escape(prefix)}_(\d+)$")
    for r in rows:
        v = (r.get(key) or "")
        m = pat.match(v)
        if m:
            mx = max(mx, int(m.group(1)))
    return f"{prefix}_{mx+1}"

def _fixed_ts(ts: Optional[str]) -> str:
    return ts or "2025-09-01T00:00:00Z"

class RecordAccessChecks(Tool):
    @staticmethod
    def invoke(data, candidate_id, checks = []) -> str:
        cand_id = candidate_id
        rows = data.setdefault("access_checks", [])
        ids = []
        for i, chk in enumerate(checks):
            payload = {
                "access_check_id": _next_seq(rows, "access_check_id", "acc"),
                "candidate_id": cand_id,
                "system_name": chk["system_name"],
                "status": chk["status"],
                "note_nullable": chk.get("note"),
                "checked_ts": _fixed_ts(chk.get("checked_ts")),
            }
            rows.append(payload)
            ids.append(payload["access_check_id"])
        return json.dumps({"inserted": len(ids), "access_check_ids": ids}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_access_checks",
                "description": "Bulk insert access checks for candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "checks": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "system_name": {"type": "string"},
                                    "status": {"type": "string"},
                                    "note": {"type": "string"},
                                    "checked_ts": {"type": "string"}
                                },
                                "required": ["system_name", "status"]
                            }
                        }
                    },
                    "required": ["candidate_id", "checks"]
                }
            }
        }