# Copyright Sierra Corporation

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso
from . import _next_int_id


class SaveCompReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], client_id, created_by_broker_id, subject_property_id, final_status = "draft") -> str:

        reports = data.get("comp_reports", [])
        new_report_id = _next_int_id(reports, "report_id")
        doc_uri = f"https://storage.example.com/reports/comp_{new_report_id:03d}.pdf"
        rpt = {
            "report_id": new_report_id,
            "client_id": client_id,
            "subject_property_id": subject_property_id,
            "created_by_broker_id": created_by_broker_id,
            "created_at": _fixed_now_iso(),
            "doc_uri": doc_uri,
            "status": final_status
        }
        reports.append(rpt)

        comps_table = data.get("comparables", [])
        props = _index_by(list(data.get("properties", {}).values()), "property_id")
        subs = _index_by(list(data.get("listings", {}).values()), "property_id")
        candidates = []
        for lst in list(data.get("listings", {}).values()) or []:
            if lst.get("status") != "active": 
                continue
            pid = lst.get("property_id")
            if pid == subject_property_id: 
                continue
            pr = props.get(pid, {})
            candidates.append({
                "comp_property_id": pid,
                "similarity_score": 0.8, 
                "selection_reason": "Neighborhood/size proximity",
                "tie_breaker_notes": "Deterministic placeholder"
            })
        for comp in candidates[:3]:
            comp_id = _next_int_id(comps_table, "comp_id")
            comps_table.append({
                "comp_id": comp_id,
                "report_id": new_report_id,
                **comp
            })

        documents = data.get("documents", [])
        new_doc_id = _next_int_id(documents, "document_id")
        documents.append({
            "document_id": new_doc_id,
            "entity_type": "comp_report",
            "entity_id": new_report_id,
            "doc_type": "comp_report",
            "file_uri": doc_uri,
            "created_by": created_by_broker_id,
            "created_at": _fixed_now_iso()
        })

        audits = data.get("audit_events", [])
        new_audit_id = _next_int_id(audits, "event_id")
        audits.append({
            "event_id": new_audit_id,
            "actor_id": created_by_broker_id,
            "action": "comp_report_saved" if final_status != "sent_to_client" else "comp_report_sent",
            "entity_type": "comp_reports",
            "entity_id": new_report_id,
            "occurred_at": _fixed_now_iso(),
            "metadata_json": {"comps_count": min(3, len(candidates)), "search_tiers": "neighborhood_first_with_borders"}
        })

        return json.dumps({"report_id": new_report_id, "doc_uri": doc_uri, "status": final_status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"save_comp_report",
            "description":"Create/update a comp report; writes comp_reports, comparables, documents, audit_events.",
            "parameters":{"type":"object","properties":{
                "client_id":{"type":"integer"},
                "subject_property_id":{"type":"string"},
                "created_by_broker_id":{"type":"integer"},
                "final_status":{"type":"string"}
            },"required":["client_id","subject_property_id","created_by_broker_id"]}
        }}
