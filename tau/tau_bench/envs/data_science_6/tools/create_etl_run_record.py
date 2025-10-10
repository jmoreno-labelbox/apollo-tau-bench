# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateEtlRunRecord(Tool):
    @staticmethod
    def _parse_iso(ts: str) -> Optional[datetime]:
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        input_paths = kwargs.get("input_paths", [])
        output_paths = kwargs.get("output_paths", [])
        started_ts = kwargs.get("started_ts")
        finished_ts_nullable = kwargs.get("finished_ts_nullable")
        messages = kwargs.get("messages", [])

        if not run_id or not isinstance(input_paths, list) or not isinstance(output_paths, list):
            return json.dumps({"error": "Missing or invalid: run_id, input_paths, output_paths."})
        if not started_ts or not CreateEtlRunRecord._parse_iso(started_ts):
            return json.dumps({"error": "Invalid started_ts (ISO 8601 UTC)."})
        if finished_ts_nullable is not None and not CreateEtlRunRecord._parse_iso(finished_ts_nullable):
            return json.dumps({"error": "Invalid finished_ts_nullable (ISO 8601 UTC or null)."})
        if not isinstance(messages, list):
            return json.dumps({"error": "messages must be a list."})

        etl_runs = data.get("etl_runs", [])
        for rec in etl_runs:
            if rec.get("run_id") == run_id:
                return json.dumps(rec)

        new_rec = {
            "run_id": run_id,
            "input_paths": input_paths,
            "output_paths": output_paths,
            "started_ts": started_ts,
            "finished_ts_nullable": finished_ts_nullable,
            "messages": messages
        }
        etl_runs.append(new_rec)
        data["etl_runs"] = etl_runs
        return json.dumps(new_rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"create_etl_run_record",
                "description":"Create an ETL run record with the canonical MWP fields only.",
                "parameters":{
                    "type":"object",
                    "properties":{
                        "run_id":{"type":"string"},
                        "input_paths":{"type":"array","items":{"type":"string"}},
                        "output_paths":{"type":"array","items":{"type":"string"}},
                        "started_ts":{"type":"string"},
                        "finished_ts_nullable":{"type":["string","null"]},
                        "messages":{"type":"array","items":{"type":"string"}}
                    },
                    "required":["run_id","input_paths","output_paths","started_ts","messages"]
                }
            }
        }
