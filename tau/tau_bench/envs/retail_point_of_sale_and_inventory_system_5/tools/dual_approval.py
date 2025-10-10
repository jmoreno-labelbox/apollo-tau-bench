# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DualApproval(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"dual_approved": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
