# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class LogMcpToolCall(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], called_ts, params_json, response_meta_nullable, server_names, tool_names) -> str:
        req = ["server_names"]
        err = _require(kwargs, req)
        if err: return err
        row = {"server_names": server_names, "tool_names": tool_names,
               "params_json": params_json, "response_meta_nullable": response_meta_nullable,
               "called_ts": called_ts}
        return json.dumps(_append(data.setdefault("mcp_tool_calls", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "log_mcp_tool_call",
            "description": "Logs a synthetic MCP tool call for traceability.",
            "parameters": {"type": "object", "properties": {
                "server_names": {"type": "array", "items": {"type": "string"}},
                "tool_names": {"type": "array", "items": {"type": "string"}},
                "params_json": {"type": "string"},
                "response_meta_nullable": {"type": "string"},
                "called_ts": {"type": "string"}},
                "required": ["server_names"]}}}
