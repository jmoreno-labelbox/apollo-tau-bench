# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_unused_document_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        documents = data.get("documents", [])
        prefix = "DOC"
        start_num = 10000

        if not documents:
            return json.dumps(f"{prefix}{start_num}", indent=2)

        max_id_num = 0
        for doc in documents:
            doc_id = doc.get("doc_id", "")
            if doc_id.startswith(prefix):
                try:
                    num = int(doc_id[len(prefix):])
                    if num > max_id_num:
                        max_id_num = num
                except (ValueError, TypeError):
                    continue

        next_id_num = max(start_num, max_id_num) + 1
        return json.dumps(f"{prefix}{next_id_num}", indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_unused_document_id",
                "description": "Return a document ID that is not currently in use.",
                "parameters": {},
            },
        }
