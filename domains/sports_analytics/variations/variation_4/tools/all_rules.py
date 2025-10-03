from tau_bench.envs.tool import Tool
import json
from typing import Any

class AllRules(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], dbt_output_tables: list = None) -> str:
        payload = {"flagged_insights_dataframe": "flags_table"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "rules",
                "description": "Executes the rules engine over computed metrics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dbt_output_tables": {
                            "type": "array",
                            "items": {"type": "string"},
                        }
                    },
                    "required": ["dbt_output_tables"],
                },
            },
        }
