# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_tickets_for_pending(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], plan_id: str, tracker_project: str, timestamp: str, request_id: str) -> str:
        items = data.get("fix_items", [])
        tickets = data.setdefault("tickets", [])
        day = (timestamp or "").split("T")[0]
        pending_ids = []
        for it in items:
            if not isinstance(it, dict) or it.get("plan_id") != plan_id:
                continue
            status = (it.get("status") or "").upper()
            if status != "APPLIED":
                iid = it.get("item_id")
                if iid:
                    pending_ids.append(iid)

        existing_ids = {t.get("ticket_id") for t in tickets if isinstance(t, dict)}
        created: List[str] = []
        for iid in pending_ids:
            ticket_id = f"tix-{iid}"
            if ticket_id in existing_ids:
                created.append(ticket_id)
                continue
            row = {
                "ticket_id": ticket_id,
                "plan_id": plan_id,
                "item_id": iid,
                "project": tracker_project,
                "status": "OPEN",
                "day": day,
                "request_id": request_id,
            }
            tickets.append(row)
            created.append(ticket_id)
            existing_ids.add(ticket_id)

        return json.dumps({"plan_id": plan_id, "ticket_ids": created, "count": len(created)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_tickets_for_pending",
            "description":"Create idempotent tracker tickets (tix-<item_id>) for all non-APPLIED items in a plan.",
            "parameters":{"type":"object","properties":{
                "plan_id":{"type":"string"},
                "tracker_project":{"type":"string"},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"},
            },"required":["plan_id","tracker_project","timestamp","request_id"]}
        }}
