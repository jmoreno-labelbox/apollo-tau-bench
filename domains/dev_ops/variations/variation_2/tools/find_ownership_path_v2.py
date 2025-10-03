from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindOwnershipPathV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], contains: str) -> str:
        pass
        ownership = _get_table(data, "ownership_map")
        key = (contains or "").lower()
        candidates = [
            o
            for o in ownership
            if key in (o.get("file_path") or "").lower()
            or key in (o.get("module_or_path") or "").lower()
        ]
        if not candidates:
            payload = {"file_path": None}
            out = json.dumps(payload, indent=2)
            return out
        chosen = sorted(candidates, key=lambda x: x.get("id", ""))[0]
        payload = {"file_path": chosen.get("file_path")}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindOwnershipPathV2",
                "description": "Finds an ownership_map file_path containing the given substring (deterministic by id).",
                "parameters": {
                    "type": "object",
                    "properties": {"contains": {"type": "string"}},
                    "required": ["contains"],
                },
            },
        }
