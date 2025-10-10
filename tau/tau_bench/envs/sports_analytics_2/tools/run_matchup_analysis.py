# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RunMatchupAnalysis(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        opponent_team = kwargs.get("opponent_team")
        our_lineup = kwargs.get("our_lineup")
        return json.dumps({"matchup_analysis": f"matchups_vs_team_{opponent_team}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "run_matchup_analysis", "description": "Runs tactical matchup analysis between lineups.", "parameters": {"type": "object", "properties": {"opponent_team": {"type": "integer"}, "our_lineup": {"type": "string"}}, "required": ["opponent_team"]}}}
