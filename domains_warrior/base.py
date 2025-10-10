import copy
from typing import Any, Dict, List

from domains.dto import Tool


class BaseDomain:
    def __init__(self, tools: List[Tool]):
        self.master_tools = tools
        self.database = None
        self.tools = copy.deepcopy(self.master_tools)

    def reset_database(self):
        raise NotImplementedError("Reset database not implemented")

    def reset_tools(self):
        self.tools = copy.deepcopy(self.master_tools)
        return True

    def get_tool_specifications(self) -> List[Dict[str, Any]]:
        return [tool.get_info() for tool in self.tools]

    def execute_tool(self, tool_name: str, kwargs: Dict[str, Any]) -> str:
        if self.database is None:
            raise ValueError("Database not loaded")

        for tool in self.tools:
            if tool.get_info()["function"]["name"] == tool_name:
                return tool.invoke(self.database, **kwargs)
        raise ValueError(f"Tool {tool_name} not found")

    def get_database(self) -> Dict[str, Any]:
        return copy.deepcopy(self.database)
