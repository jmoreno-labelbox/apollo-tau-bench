from tau_bench.envs.tool import Tool
import json
from typing import Any

class IngestLog(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], ingestion_log: dict = None, source_name: str = None, status_code: int = None, logs_ingested: int = None) -> str:
        logs = data.get("ingestion_logs", [])
        # Support both dict and individual parameters
        if ingestion_log is not None:
            logs.append(ingestion_log)
        else:
            log_entry = {}
            if source_name is not None:
                log_entry['source_name'] = source_name
            if status_code is not None:
                log_entry['status_code'] = status_code
            if logs_ingested is not None:
                log_entry['logs_ingested'] = logs_ingested
            logs.append(log_entry)
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "makeLogs",
                "description": "Persists an ingestion log row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {"type": "string"},
                        "status_code": {"type": "integer"},
                        "logs_ingested": {"type": "integer"},
                    },
                    "required": ["source_name", "status_code"],
                },
            },
        }
