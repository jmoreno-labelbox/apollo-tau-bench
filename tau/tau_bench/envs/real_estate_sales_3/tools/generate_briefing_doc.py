# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso
from . import _next_int_id






def _next_int_id(rows: List[Dict[str, Any]], key: str) -> int:
    return max((int(r.get(key, 0)) for r in rows), default=0) + 1

def _fixed_now_iso() -> str:
    return "2025-08-20T00:00:00Z"

class GenerateBriefingDoc(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], broker_id, client_id, version_tag = "v1") -> str:
        documents = data.get("documents", [])
        new_id = _next_int_id(documents, "document_id")
        file_uri = f"https://storage.example.com/briefings/client_briefing_{client_id:03d}_{version_tag}.pdf"
        row = {"document_id": new_id, "entity_type": "client", "entity_id": client_id,
               "doc_type": "briefing_doc", "file_uri": file_uri, "created_by": broker_id, "created_at": _fixed_now_iso()}
        documents.append(row)
        return json.dumps({"document_id": new_id, "file_uri": file_uri}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"generate_briefing_doc",
            "description":"Create a client briefing document and persist it.",
            "parameters":{"type":"object","properties":{
                "client_id":{"type":"integer"},"broker_id":{"type":"integer"},"version_tag":{"type":"string"}
            },"required":["client_id","broker_id"]}
        }}