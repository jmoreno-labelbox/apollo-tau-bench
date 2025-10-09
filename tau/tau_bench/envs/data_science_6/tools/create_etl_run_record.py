from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateEtlRunRecord(Tool):
    @staticmethod
    def _parse_iso(ts: str) -> datetime | None:
        pass
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(
        data: dict[str, Any],
        finished_ts_nullable: str = None,
        input_paths: list = [],
        messages: list = [],
        output_paths: list = [],
        run_id: str = None,
        started_ts: str = None
    ) -> str:
        if (
            not run_id
            or not isinstance(input_paths, list)
            or not isinstance(output_paths, list)
        ):
            payload = {"error": "Missing or invalid: run_id, input_paths, output_paths."}
            out = json.dumps(payload)
            return out
        if not started_ts or not CreateEtlRunRecord._parse_iso(started_ts):
            payload = {"error": "Invalid started_ts (ISO 8601 UTC)."}
            out = json.dumps(payload)
            return out
        if finished_ts_nullable is not None and not CreateEtlRunRecord._parse_iso(
            finished_ts_nullable
        ):
            payload = {"error": "Invalid finished_ts_nullable (ISO 8601 UTC or null)."}
            out = json.dumps(payload)
            return out
        if not isinstance(messages, list):
            payload = {"error": "messages must be a list."}
            out = json.dumps(payload)
            return out

        etl_runs = data.get("etl_runs", [])
        for rec in etl_runs:
            if rec.get("run_id") == run_id:
                payload = rec
                out = json.dumps(payload)
                return out

        new_rec = {
            "run_id": run_id,
            "input_paths": input_paths,
            "output_paths": output_paths,
            "started_ts": started_ts,
            "finished_ts_nullable": finished_ts_nullable,
            "messages": messages,
        }
        etl_runs.append(new_rec)
        data["etl_runs"] = etl_runs
        payload = new_rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateEtlRunRecord",
                "description": "Create an ETL run record with the canonical MWP fields only.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "input_paths": {"type": "array", "items": {"type": "string"}},
                        "output_paths": {"type": "array", "items": {"type": "string"}},
                        "started_ts": {"type": "string"},
                        "finished_ts_nullable": {"type": ["string", "null"]},
                        "messages": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "run_id",
                        "input_paths",
                        "output_paths",
                        "started_ts",
                        "messages",
                    ],
                },
            },
        }
