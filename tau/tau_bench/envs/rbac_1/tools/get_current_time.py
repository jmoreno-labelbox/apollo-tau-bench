# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCurrentTime(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        return json.dumps({"current_time": NOW.strftime(DT_STR_FORMAT)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_current_time",
                        "description": "Returns the current date and time.",
                        "parameters": {
                                "type": "object",
                                "properties": {},
                                "required": []
                        }
                }
        }
