from tau_bench.envs.tool import Tool
import json
from typing import Any

class RecordMcpToolCall(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], server_name: str = None, tool_name: str = None, params_json: dict = {}, result_meta_json: dict = {}) -> str:
        rows = _ensure_list(data, "mcp_tool_calls")
        new_id = _next_seq_id(rows, "call_id")
        payload = {
            "call_id": new_id,
            "server_name": server_name,
            "tool_name": tool_name,
            "params_json": params_json,
            "result_meta_json": result_meta_json,
            "call_ts": NOW_TS,
        }
        rows.append(payload)
        payload = {"call_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordMcpToolCall",
                "description": "Insert an audit row for an MCP tool call.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_name": {"type": "string"},
                        "tool_name": {"type": "string"},
                        "params_json": {"type": "object"},
                        "result_meta_json": {"type": "object"},
                    },
                    "required": ["server_name", "tool_name", "params_json"],
                },
            },
        }
