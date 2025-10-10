# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateBriefingDoc(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get("client_id")
        broker_id = kwargs.get("broker_id")
        version_tag = kwargs.get("version_tag", "v1")
        documents = data.get("documents", [])
        new_id = _next_auto_id(documents, "document_id")
        file_uri = f"https://test.storage.com/details/client_briefing_{client_id:03d}_{version_tag}.pdf"
        row = {
            "document_id": new_id,
            "entity_type": "client",
            "entity_id": client_id,
            "doc_type": "briefing_doc",
            "file_uri": file_uri,
            "created_by": broker_id,
            "created_at": _now_iso_fixed(),
        }
        documents.append(row)
        return json.dumps({"document_id": new_id, "file_uri": file_uri}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_briefing_doc",
                "description": "Create a client briefing document and persist it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "broker_id": {"type": "integer"},
                        "version_tag": {"type": "string"},
                    },
                    "required": ["client_id", "broker_id"],
                },
            },
        }
