# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMcpToolCallsByServer(Tool):
    """
    Returns flattened MCP tool call entries filtered by server name.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], server_name: str) -> str:
        rows = list(data.get("mcp_tool_calls", {}).values())
        out: List[Dict[str, Any]] = []
        for row in rows:
            servers = row.get("server_names", [])
            tools = row.get("tool_names", [])
            params = row.get("params_json", [])
            metas = row.get("response_meta_nullable", [])
            times = row.get("called_ts", [])
            for i, s in enumerate(servers):
                if s == server_name:
                    out.append({
                        "server_name": s,
                        "tool_name": tools[i] if i < len(tools) else None,
                        "params_json": params[i] if i < len(params) else None,
                        "response_meta_nullable": metas[i] if i < len(metas) else None,
                        "called_ts": times[i] if i < len(times) else None
                    })
        return json.dumps({"items": out})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_mcp_tool_calls_by_server",
                "description": "Returns flattened MCP tool call entries filtered by server name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_name": {"type": "string"}
                    },
                    "required": ["server_name"]
                }
            }
        }
