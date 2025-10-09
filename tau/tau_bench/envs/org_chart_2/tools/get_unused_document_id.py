from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUnusedDocumentId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        documents = data.get("documents", {}).values()
        prefix = "DOC"
        start_num = 10000

        if not documents:
            payload = f"{prefix}{start_num}"
            out = json.dumps(payload, indent=2)
            return out

        max_id_num = 0
        for doc in documents:
            doc_id = doc.get("doc_id", "")
            if doc_id.startswith(prefix):
                try:
                    num = int(doc_id[len(prefix) :])
                    if num > max_id_num:
                        max_id_num = num
                except (ValueError, TypeError):
                    continue

        next_id_num = max(start_num, max_id_num) + 1
        payload = f"{prefix}{next_id_num}"
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUnusedDocumentId",
                "description": "Return a document ID that is not currently in use.",
                "parameters": {},
            },
        }
