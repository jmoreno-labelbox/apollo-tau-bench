# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso
from . import _next_int_id


class AttachDocumentToClient(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], client_id, created_by, doc_type, file_uri) -> str:
        documents = data.get("documents", [])
        new_id = _next_int_id(documents, "document_id")
        row = {"document_id": new_id, "entity_type": "client", "entity_id": client_id,
               "doc_type": doc_type or "briefing_doc", "file_uri": file_uri,
               "created_by": created_by, "created_at": _fixed_now_iso()}
        documents.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"attach_document_to_client",
            "description":"Attach a provided file_uri to a client as a document.",
            "parameters":{"type":"object","properties":{
                "client_id":{"type":"integer"},"file_uri":{"type":"string"},
                "doc_type":{"type":"string"},"created_by":{"type":"integer"}
            },"required":["client_id","file_uri"]}
        }}
