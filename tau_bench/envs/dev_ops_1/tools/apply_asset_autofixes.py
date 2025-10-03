from tau_bench.envs.tool import Tool
import json
from typing import Any

class ApplyAssetAutofixes(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], qa_json: Any, tex_report: Any) -> str:
        commits = _get_table(data, "commits")
        next_idx = _max_int_suffix(commits, "patch_id", "AF", 0) + 1
        patch_id = f"AF-{next_idx}"
        payload = {"patch_set": {"mechanical_changes": True, "patch_id": patch_id}}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyAssetAutofixes",
                "description": "Produces a deterministic patch_set representing mechanical fixes only.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "qa_json": {"type": "array"},
                        "tex_report": {"type": "array"},
                    },
                    "required": ["qa_json", "tex_report"],
                },
            },
        }
