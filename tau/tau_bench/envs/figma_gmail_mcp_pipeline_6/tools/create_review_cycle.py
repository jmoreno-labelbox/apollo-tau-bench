# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_review_cycle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cycle_id: str, artifact_id: str, started_at: str, timestamp: str, request_id: str, recipients: List[str]) -> str:
        cycles = data.setdefault("review_cycles", [])
        for c in cycles:
            if isinstance(c, dict) and c.get("cycle_id") == cycle_id:
                if not c.get("recipients"):
                    c["recipients"] = sorted(list(dict.fromkeys(recipients or [])))
                return json.dumps(c, indent=2)
        row = {
            "cycle_id": cycle_id,
            "artifact_id": artifact_id,
            "status": "NEEDS_REVIEW",
            "started_at": started_at,
            "approvals_recorded": 0,
            "thread_id_nullable": None,
            "recipients": sorted(list(dict.fromkeys(recipients or []))),
            "sla_days": None,
            "day": (timestamp or "").split("T")[0],
        }
        cycles.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_review_cycle",
            "description":"Create or reuse a deterministic review cycle row; stores recipients.",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"},
                "artifact_id":{"type":"string"},
                "started_at":{"type":"string"},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"},
                "recipients":{"type":"array","items":{"type":"string"}}
            },"required":["cycle_id","artifact_id","started_at","timestamp","request_id","recipients"]}
        }}
