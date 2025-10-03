from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetMcpToolCallsByServer(Tool):
    """Provides flattened MCP tool call entries filtered by the server name."""

    @staticmethod
    def invoke(data: dict[str, Any], server_name: str) -> str:
        rows = data.get("mcp_tool_calls", [])
        out: list[dict[str, Any]] = []
        for row in rows:
            servers = row.get("server_names", [])
            tools = row.get("tool_names", [])
            params = row.get("params_json", [])
            metas = row.get("response_meta_nullable", [])
            times = row.get("called_ts", [])
            for i, s in enumerate(servers):
                if s == server_name:
                    out.append(
                        {
                            "server_name": s,
                            "tool_name": tools[i] if i < len(tools) else None,
                            "params_json": params[i] if i < len(params) else None,
                            "response_meta_nullable": (
                                metas[i] if i < len(metas) else None
                            ),
                            "called_ts": times[i] if i < len(times) else None,
                        }
                    )
        payload = {"items": out}
        out_str = json.dumps(payload)
        return out_str

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMcpToolCallsByServer",
                "description": "Returns flattened MCP tool call entries filtered by server name.",
                "parameters": {
                    "type": "object",
                    "properties": {"server_name": {"type": "string"}},
                    "required": ["server_name"],
                },
            },
        }
