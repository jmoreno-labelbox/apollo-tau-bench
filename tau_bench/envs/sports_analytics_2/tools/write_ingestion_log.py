from tau_bench.envs.tool import Tool
import json
from typing import Any

class WriteIngestionLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        logs = data.get("ingestion_logs", [])
        logs.append(kwargs)
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
