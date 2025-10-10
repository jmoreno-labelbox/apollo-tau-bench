# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMtpTimestamps(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"started_ts":"2024-03-17T09:30:00Z","finished_ts_nullable":"2024-03-17T11:15:00Z"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_mtp_timestamps","description":"Returns canonical started_ts and finished_ts for MTP.","parameters":{"type":"object","properties":{},"required":[]}}}
