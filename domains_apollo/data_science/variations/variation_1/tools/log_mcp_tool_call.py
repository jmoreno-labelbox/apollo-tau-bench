from tau_bench.envs.tool import Tool
import json
from typing import Any

class LogMcpToolCall(Tool):
    def invoke(
        data: dict[str, Any],
        called_ts: str = None,
        params_json: str = None,
        response_meta_nullable: str = None,
        server_names: str = None,
        tool_names: str = None
    ) -> str:
        req = ["server_names"]
        err = _require({"server_names": server_names}, req)
        if err:
            return err
        row = {
            "server_names": server_names,
            "tool_names": tool_names,
            "params_json": params_json,
            "response_meta_nullable": response_meta_nullable,
            "called_ts": called_ts,
        }
        payload = _append(data.setdefault("mcp_tool_calls", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "logMcpToolCall",
                "description": "Logs a synthetic MCP tool call for traceability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_names": {"type": "array", "items": {"type": "string"}},
                        "tool_names": {"type": "array", "items": {"type": "string"}},
                        "params_json": {"type": "string"},
                        "response_meta_nullable": {"type": "string"},
                        "called_ts": {"type": "string"},
                    },
                    "required": ["server_names"],
                },
            },
        }
