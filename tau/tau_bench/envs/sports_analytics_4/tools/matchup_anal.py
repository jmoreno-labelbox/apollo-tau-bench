# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MatchupAnal(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], opponent_team, our_lineup) -> str:
        # return outcome
        return json.dumps({"matchup_analysis": f"matchups_vs_team_{opponent_team}"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # output result
        return {"type": "function", "function": {"name": "run_matchup_analysis", "description": "Executes tactical matchup analysis between lineups.", "parameters": {"type": "object", "properties": {"opponent_team": {"type": "integer"}, "our_lineup": {"type": "string"}}, "required": ["opponent_team"]}}}
