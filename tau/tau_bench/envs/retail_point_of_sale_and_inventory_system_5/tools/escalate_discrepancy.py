# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EscalateDiscrepancy(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"escalated": True, "level": kwargs.get("escalation_level", "regional")}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
