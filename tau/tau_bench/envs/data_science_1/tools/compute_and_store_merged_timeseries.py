# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require






def _require(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return json.dumps({"error": f"Missing required arguments: {', '.join(missing)}"}, indent=2)
    return None

def _append(table: List[Dict[str, Any]], row: Dict[str, Any]) -> Dict[str, Any]:
    table.append(row)
    return row

class ComputeAndStoreMergedTimeseries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        err = _require(kwargs, ["csv_path"])
        if err: return err
        allowed = ["csv_path", "columns", "row_count", "min_timestamp", "max_timestamp", "file_hash_sha256", "created_ts"]
        row = {k: kwargs[k] for k in allowed if k in kwargs}
        return json.dumps(_append(data.setdefault("processed_timeseries", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "compute_and_store_merged_timeseries",
            "description": "Registers a merged timeseries CSV artifact and its metadata.",
            "parameters": {"type": "object", "properties": {
                "csv_path": {"type": "string"},
                "columns": {"type": "array", "items": {"type": "string"}},
                "row_count": {"type": "integer"},
                "min_timestamp": {"type": "string"}, "max_timestamp": {"type": "string"},
                "file_hash_sha256": {"type": "string"},
                "created_ts": {"type": "string"}}, "required": ["csv_path"]}}}