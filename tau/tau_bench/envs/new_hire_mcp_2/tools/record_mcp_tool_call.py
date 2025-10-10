# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordMcpToolCall(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], server_name, tool_name, params_json = {}, result_meta_json = {}) -> str:
        rows = _ensure_list(data, "mcp_tool_calls")
        new_id = _next_seq_id(rows, "call_id")
        payload = {"call_id": new_id, "server_name": server_name, "tool_name": tool_name,
                   "params_json": params_json, "result_meta_json": result_meta_json,
                   "call_ts": NOW_TS}
        rows.append(payload)
        return json.dumps({"call_id": new_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "record_mcp_tool_call", "description": "Insert an audit row for an MCP tool call.",
                             "parameters": {"type": "object", "properties": {"server_name": {"type": "string"},
                                                                             "tool_name": {"type": "string"},
                                                                             "params_json": {"type": "object"},
                                                                             "result_meta_json": {"type": "object"}},
                                            "required": ["server_name", "tool_name", "params_json"]}}}
