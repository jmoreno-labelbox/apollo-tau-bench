from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class WriteIngestionLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        logs = data.get("ingestion_logs", {}).values()
        data["ingestion_logs"][kwargs["ingestion_log_id"]] = kwargs
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteIngestionLog",
                "description": "Writes an ingestion log row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {"type": "string"},
                        "status_code": {"type": "integer"},
                        "records_ingested": {"type": "integer"},
                    },
                    "required": ["source_name", "status_code"],
                },
            },
        }
