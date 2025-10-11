# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PrepareStakeholderOutputs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], metrics_id, predictions_id) -> str:
        output_id = "STAKEHOLDER_OUTPUT_001"

        # In a practical situation, this would transfer files to a designated 'deliverables' folder.
        # This is where we generate the record.
        output_entry = {
            "stakeholder_output_id": output_id,
            "final_predictions_id": predictions_id,
            "final_metrics_id": metrics_id,
            "status": "ready",
            "predictions_csv_path": f"/deliverables/final_predictions_{output_id}.csv",
            "metrics_json_path": f"/deliverables/final_metrics_{output_id}.json",
        }

        data.setdefault("stakeholder_outputs.json", []).append(output_entry)
        return json.dumps(output_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PrepareStakeholderOutputs",
                "description": "Finalizes the modeling run by creating a record pointing to the definitive prediction and metrics files.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "predictions_id": {
                            "type": "string",
                            "description": "The ID of the final predictions.",
                        },
                        "metrics_id": {
                            "type": "string",
                            "description": "The ID of the final metrics.",
                        },
                    },
                    "required": ["predictions_id", "metrics_id"],
                },
            },
        }
