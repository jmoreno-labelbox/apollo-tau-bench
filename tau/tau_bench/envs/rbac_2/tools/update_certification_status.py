# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCertificationStatus(Tool):
    """ Update the status of an access certification campaign. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        certification_id_to_update = kwargs.get("certification_id")
        new_status = kwargs.get("new_status")
        timestamp = kwargs.get("timestamp")
        try:
            certifications = data.get('certifications', [])
        except:
            certifications = []

        certification_found = False
        updated_certification = None
        for cert in certifications:
            if cert.get("certification_id") == certification_id_to_update:
                cert["status"] = new_status
                if new_status == "COMPLETED":
                    cert["completed_on"] = timestamp

                certification_found = True
                updated_certification = cert
                break

        if not certification_found:
            return json.dumps({"error": f"Certification with ID '{certification_id_to_update}' not found."})

        data['certifications'] = certifications

        return json.dumps({
            "message": "Certification campaign status updated successfully.",
            "certification_details": updated_certification
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_certification_status",
                "description": "Updates the status of an access certification campaign (e.g., to 'COMPLETED').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "The unique ID of the certification campaign to update."
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status to set for the campaign (e.g., 'COMPLETED')."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp to record as the completion time."
                        }
                    },
                    "required": ["certification_id", "new_status", "timestamp"]
                }
            }
        }
