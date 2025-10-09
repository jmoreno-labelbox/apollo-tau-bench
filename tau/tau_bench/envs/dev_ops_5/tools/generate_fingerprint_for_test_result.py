from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GenerateFingerprintForTestResult(Tool):
    """Creates a consistent crash fingerprint from a test result."""

    @staticmethod
    def invoke(data: dict[str, Any], test_result_id: str = None) -> str:
        test_results = data.get("test_results", [])

        test_result = None
        for result in test_results:
            if result.get("id") == test_result_id:
                test_result = result
                break

        if not test_result:
            payload = {"error": f"Test result with ID '{test_result_id}' not found."}
            out = json.dumps(payload)
            return out

        failure_type = test_result.get("failure_type", "unknown").replace("_", "")
        stack_trace = test_result.get("stack_trace", "")
        top_frame = stack_trace.split("\n")[0] if stack_trace else "unknown_frame"

        module_or_function = (
            top_frame.split("!")[0].split("(")[0].strip()
            if "!" in top_frame
            else top_frame.split("(")[0].strip()
        )
        module_or_function = module_or_function.split("::")[-1]

        if "TextureLoadingTest" in module_or_function and "assertion" in failure_type:
            fingerprint = "renderer_character_load_access_violation_xyz"
        elif "NavigationMeshTest" in module_or_function and "timeout" in failure_type:
            fingerprint = "ai_navmesh_generation_timeout_abc"
        elif "ConnectionTest" in module_or_function and "network" in failure_type:
            fingerprint = "network_connection_timeout_30s_xyz"
        else:
            fingerprint = f"generic_{failure_type}_{module_or_function}"
        payload = {"fingerprint": fingerprint}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateFingerprintForTestResult",
                "description": "Generates a deterministic crash fingerprint from a test result to link it with crash events.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_result_id": {
                            "type": "string",
                            "description": "The unique ID of the test result.",
                        }
                    },
                    "required": ["test_result_id"],
                },
            },
        }
