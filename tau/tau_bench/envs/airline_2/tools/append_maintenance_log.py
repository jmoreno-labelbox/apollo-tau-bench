# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AppendMaintenanceLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], aircraft_id: str, maintenance_type: str, description: str, event_timestamp_utc: str, technician_id: Optional[str]=None,
        work_order_id: Optional[str]=None ,ata_chapter: Optional[str]=None,corrective_action: Optional[str]=None,mel_cdl_reference: Optional[str]=None,next_due: Optional[str]=None
               ) -> str:
        logs = data.setdefault("maintenance_logs", [])
        new_id = _next_numeric_suffix("ML", logs, "log_id")
        rec = {
            "log_id": new_id,
            "aircraft": {"aircraft_id": aircraft_id},
            "event_timestamp_utc": event_timestamp_utc,
            "maintenance_type": maintenance_type,
            "description": description,
            "status": "Logged",
            "technician_id": technician_id,
            "work_order_id": work_order_id,
            "ata_chapter": ata_chapter,
            "corrective_action": corrective_action,
            "mel_cdl_reference": mel_cdl_reference,
            "next_due": next_due
        }
        logs.append(rec)
        return _j(rec)

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"append_maintenance_log",
            "description":"Append a maintenance log with deterministic ID (ML###).",
            "parameters":{"type":"object","properties":{
                "aircraft_id":{"type":"string"},
                "maintenance_type":{"type":"string"},
                "description":{"type":"string"},
                "event_timestamp_utc":{"type":"string"},
                "technician_id": {"type": "string"},
                "work_order_id": {"type":"string"},
                "ata_chapter": {"type":"string"},
                "corrective_action": {"type":"string"},
                "mel_cdl_reference": {"type":"string"},
                "next_due": {"type":"string"}
            },"required":["aircraft_id","maintenance_type","description","event_timestamp_utc"]}
        }}
