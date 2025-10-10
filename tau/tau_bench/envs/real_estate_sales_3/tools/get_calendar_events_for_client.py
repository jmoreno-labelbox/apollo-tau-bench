# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCalendarEventsForClient(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("client_id")
        rows = [e for e in data.get("calendar_events", []) if e.get("client_id") == cid]
        return json.dumps({"client_id": cid, "events": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_calendar_events_for_client",
            "description":"List calendar events for a client.",
            "parameters":{"type":"object","properties":{"client_id":{"type":"integer"}},"required":["client_id"]}
        }}
