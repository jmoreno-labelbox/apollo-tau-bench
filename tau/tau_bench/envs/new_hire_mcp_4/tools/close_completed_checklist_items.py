# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CloseCompletedChecklistItems(Tool):
    @staticmethod
    def invoke(db: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]; due_lte = kwargs.get("due_date_lte")
        items = db.get("checklist_items", [])
        updated = 0
        for it in items:
            if it.get("candidate_id") != cand_id: continue
            if it.get("status") != "Completed": continue
            if it.get("completed_ts"): continue
            if due_lte and it.get("due_date") and it["due_date"] > due_lte: continue
            it["completed_ts"] = _fixed_ts(None); updated += 1
        return json.dumps({"updated": updated}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"close_completed_checklist_items",
            "description":"Backfill completed_ts for completed checklist items.",
            "parameters":{"type":"object","properties":{
                "candidate_id":{"type":"string"},
                "due_date_lte":{"type":"string"}
            },"required":["candidate_id"]}
        }}
