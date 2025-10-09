from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FetchMortgageRatesForClientTool(Tool):
    """Retrieves available mortgage rates according to client qualifications."""

    @staticmethod
    def invoke(data: dict[str, Any], credit_score: int = None, region: str = None) -> str:
        credit_score = _as_int(credit_score)
        if credit_score is None or not region:
            return _err("credit_score (int) and region (string) are required")

        rates = []
        # Establish a lender lookup map for effective name resolution
        lenders_map = {
            l.get("lender_id"): l.get("name") for l in data.get("lenders", [])
        }

        for r in data.get("mortgage_rates", []):
            if str(r.get("region")) != str(region):
                continue
            qualifies = credit_score >= _as_int(r.get("min_credit_score") or 0)
            lender_id = r.get("lender_id")
            lender_name = lenders_map.get(lender_id)
            rates.append(
                {
                    "rate_id": r.get("rate_id"),
                    "lender_id": lender_id,
                    "lender_name": lender_name,
                    "term_years": r.get("term_years"),
                    "apr_percent": r.get("apr_percent"),
                    "min_credit_score": r.get("min_credit_score"),
                    "qualifies": bool(qualifies),
                }
            )

        # Select best_available_rate from qualifying options, otherwise from all (with a higher penalty)
        best_rate = None
        best_term_years = None
        qualifying = [x for x in rates if x["qualifies"]]
        pool = qualifying if qualifying else rates
        if pool:
            best_rate_entry = min(
                (x for x in pool if x.get("apr_percent") is not None),
                key=lambda x: x.get("apr_percent"),
                default=None,
            )
            if best_rate_entry:
                best_rate = best_rate_entry.get("apr_percent")
                best_term_years = best_rate_entry.get("term_years")

        out = {
            "client_credit_score": credit_score,
            "region": region,
            "qualifying_rates": rates,
            "interest_rate": best_rate,
            "best_term_years": best_term_years,
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        #The tool refrains from directly retrieving client profiles to maintain privacy layers
        return {
            "type": "function",
            "function": {
                "name": "FetchMortgageRatesForClient",
                "description": (
                    "Get available mortgage rates for a given credit score and region."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "credit_score": {"type": "integer"},
                        "region": {"type": "string"},
                    },
                    "required": ["credit_score", "region"],
                },
            },
        }
