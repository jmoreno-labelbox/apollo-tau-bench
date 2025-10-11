# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _err(msg: str, code: str = "bad_request", ) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

def _as_int(x) -> Optional[int]:
    try:
        return int(x)
    except Exception:
        return None

class FetchMortgageRatesForClientTool(Tool):
    """Gets available mortgage rates based on client qualification."""

    @staticmethod
    def invoke(data: Dict[str, Any], credit_score, region) -> str:
        credit_score = _as_int(credit_score)
        if credit_score is None or not region:
            return _err("credit_score (int) and region (string) are required")

        rates = []
        # Generate a lender mapping for quick name identification.
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

        # Select best_available_rate from qualifying options first; if none, then from all available (with higher penalty).
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
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        # The tool avoids directly retrieving client profiles to uphold privacy measures.
        return {
            "type": "function",
            "function": {
                "name": "fetch_mortgage_rates_for_client",
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