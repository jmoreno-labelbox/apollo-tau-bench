from tau_bench.envs.tool import Tool
import json
from typing import Any

class RegisterQcFigure(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        created_ts: str = None,
        description: str = None,
        figure_path: str = None
    ) -> str:
        err = _require({"figure_path": figure_path}, ["figure_path"])
        if err:
            return err
        row = {
            "figure_path": figure_path,
            "description": description,
            "created_ts": created_ts,
        }
        payload = _append(data.setdefault("qc_figures", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterQcFigure",
                "description": "Registers a QC figure path and description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "figure_path": {"type": "string"},
                        "description": {"type": "string"},
                        "created_ts": {"type": "string"},
                    },
                    "required": ["figure_path"],
                },
            },
        }
