# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _next_int_id(rows: List[Dict[str, Any]], key: str) -> int:
    mx = 0
    for r in rows:
        try:
            v = int(r.get(key, 0))
            if v > mx:
                mx = v
        except Exception:
            continue
    return mx + 1

def _err(msg: str, code: str = "bad_request", ) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

def _as_int(x) -> Optional[int]:
    try:
        return int(x)
    except Exception:
        return None

class GenerateClientBriefingDocumentTool(Tool):
    """Generates a client briefing PDF and inserts a documents row (entity_type=client)."""

    @staticmethod
    def invoke(data: Dict[str, Any], client_id, created_by) -> str:
        client_id = _as_int(client_id)
        created_by = _as_int(created_by)
        if client_id is None or created_by is None:
            return _err("client_id and created_by are required")

        docs = data.setdefault("documents", [])
        document_id = _next_int_id(docs, "document_id")
        padded = str(client_id).zfill(3)
        uri = f"https://storage.example.com/briefings/client_briefing_{padded}.pdf"

        doc_row = {
            "document_id": document_id,
            "entity_type": "client",
            "entity_id": int(client_id),
            "doc_type": "briefing_doc",
            "file_uri": uri,
            "created_by": int(created_by),
            "created_at": HARD_TS,
        }
        docs.append(doc_row)

        return json.dumps({"document": doc_row}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_client_briefing_document",
                "description": (
                    "Generate client briefing PDF and insert into documents table."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "created_by": {"type": "integer"},
                    },
                    "required": ["client_id", "created_by"],
                },
            },
        }