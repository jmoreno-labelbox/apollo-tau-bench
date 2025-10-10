# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculatePropertyMetricsTool(Tool):
    """Calculates comprehensive property analysis metrics with market baseline and affordability."""

    @staticmethod
    def _estimate_rate(credit_score: Optional[int], region: Optional[str]) -> float:
        # mirror CalculateMortgagePaymentTool for consistency
        base = 6.8
        if credit_score is not None:
            if credit_score >= 760:
                base = 5.6
            elif credit_score >= 720:
                base = 5.9
            elif credit_score >= 680:
                base = 6.2
            elif credit_score >= 640:
                base = 6.5
            else:
                base = 6.9
        if region in {"TX", "FL"}:
            base -= 0.15
        elif region in {"NY", "CA"}:
            base += 0.15
        return round(base, 3)

    @staticmethod
    def _pmt(loan_amount: float, annual_rate_pct: float, years: int = 30) -> float:
        r = (annual_rate_pct / 100.0) / 12.0
        n = years * 12
        if r == 0:
            return loan_amount / n
        return loan_amount * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        subject_property_id = kwargs.get("subject_property_id")
        comparable_properties = kwargs.get("comparable_properties") or []
        client_budget = kwargs.get("client_budget") or {}
        if not subject_property_id:
            return _err("subject_property_id is required")

        # ---- Subject basics (simplified - no property details available) ----
        subj_listing = (
            _collect_listing_by_property(data, str(subject_property_id)) or {}
        )
        subj_price = subj_listing.get("list_price")
        # Note: sqft, tax_rate, neighborhood_id not available in current data structure

        # ---- Collect comparable prices/ppsf ----
        def _lp(pid_or_dict):
            if isinstance(pid_or_dict, dict):
                pid = (
                    pid_or_dict.get("property_id")
                    or pid_or_dict.get("id")
                    or pid_or_dict
                )
            else:
                pid = pid_or_dict
            l = _collect_listing_by_property(data, str(pid)) or {}
            price = l.get("list_price")
            ppsf = l.get("price_per_sqft")  # Use pre-calculated value from listings
            return price, ppsf

        comp_prices, comp_ppsf = [], []
        for c in comparable_properties:
            price, ppsf = _lp(c)
            if isinstance(price, (int, float)):
                comp_prices.append(float(price))
            if isinstance(ppsf, (int, float, float)):
                comp_ppsf.append(float(ppsf))
        comp_prices.sort()
        comp_ppsf.sort()

        # ---- Build market pool (simplified - use all listings as market) ----
        market_prices, market_ppsf = [], []
        for l in list(data.get("listings", {}).values()):
            if l.get("list_price"):
                market_prices.append(float(l["list_price"]))
            if l.get("price_per_sqft"):
                market_ppsf.append(float(l["price_per_sqft"]))

        market_prices.sort()
        market_ppsf.sort()

        # ---- Market position (use market pool when available, else comps) ----
        def _median(arr: List[float]) -> Optional[float]:
            if not arr:
                return None
            m = len(arr) // 2
            return arr[m] if len(arr) % 2 == 1 else (arr[m - 1] + arr[m]) / 2.0

        ref_prices = market_prices if market_prices else comp_prices
        ref_ppsf = market_ppsf if market_ppsf else comp_ppsf

        if subj_price is not None and ref_prices:
            below = sum(1 for x in ref_prices if x <= float(subj_price))
            price_percentile = int(round(100.0 * below / max(len(ref_prices), 1)))
            med = _median(ref_prices) or float(subj_price)
            delta = (float(subj_price) - med) / max(med, 1.0)
            market_comparison = (
                "below_average"
                if delta < -0.03
                else ("above_average" if delta > 0.03 else "at_market")
            )
            value_rating = (
                "good_value"
                if delta <= -0.05
                else ("fair" if abs(delta) <= 0.05 else "premium")
            )
        else:
            price_percentile, market_comparison, value_rating = 50, "at_market", "fair"

        # ---- Affordability (P&I + est. taxes if available) ----
        price_max = client_budget.get("price_max")
        within_budget = bool(
            price_max is None
            or (subj_price is not None and float(subj_price) <= float(price_max))
        )

        monthly_income = client_budget.get("monthly_income")
        client_id = _as_int(client_budget.get("client_id"))
        if monthly_income is None and client_id is not None:
            mp = _get_mortgage_profile(data, client_id)
            if mp and mp.get("annual_income"):
                monthly_income = float(mp["annual_income"]) / 12.0

        monthly_pni = None
        if subj_price is not None:
            # estimate 30y P&I from mortgage profile if possible
            credit, region = None, None
            if client_id is not None:
                mp = _get_mortgage_profile(data, client_id)
                if mp:
                    credit, region = mp.get("credit_score"), mp.get("region")
                    down = float(mp.get("down_payment") or 0.0)
                else:
                    down = 0.0
            else:
                down, credit, region = 0.0, None, None
            rate = CalculatePropertyMetricsTool._estimate_rate(_as_int(credit), region)
            loan_amount = max(0.0, float(subj_price) - float(down))
            monthly_pni = CalculatePropertyMetricsTool._pmt(loan_amount, rate, 30)

        # Note: Property tax data not available - using P&I only
        monthly_taxes = 0.0
        monthly_housing = monthly_pni

        ratio = (
            round(float(monthly_housing) / float(monthly_income), 3)
            if (monthly_income and monthly_housing)
            else None
        )
        recommendation = "financially_suitable"
        if not within_budget or (ratio is not None and ratio > 0.36):
            recommendation = "consider_lower_price_range"
        elif ratio is not None and ratio < 0.25:
            recommendation = "comfortable"

        # ---- Comparative analysis & unique advantages ----
        vs_comparables = "competitive"
        uniq = []

        if subj_price is not None and comp_prices:
            avg_comp = sum(comp_prices) / len(comp_prices)
            if subj_price < 0.95 * avg_comp:
                vs_comparables = "undervalued"
                uniq.append("pricing")
            elif subj_price > 1.05 * avg_comp:
                vs_comparables = "overpriced"

        # Price per sqft comparison (using pre-calculated values where available)
        subj_ppsf = subj_listing.get("price_per_sqft")
        if subj_ppsf and comp_ppsf:
            avg_ppsf = sum(comp_ppsf) / len(comp_ppsf)
            if float(subj_ppsf) < 0.95 * avg_ppsf:
                uniq.append("price_per_sqft")

        # Note: Amenity analysis not available - no property amenity data in current structure

        out = {
            "subject_property": str(subject_property_id),
            "market_position": {
                "price_percentile": price_percentile,
                "value_rating": value_rating,
                "market_comparison": market_comparison,
            },
            "affordability_analysis": {
                "within_budget": bool(within_budget),
                "monthly_housing_ratio": ratio,
                "recommendation": recommendation,
            },
            "comparative_analysis": {
                "vs_comparables": vs_comparables,
                "unique_advantages": uniq or ["none"],
            },
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_property_metrics",
                "description": (
                    "Calculate market position (vs comps & market pool), affordability (P&I + taxes), and comparative analysis."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_property_id": {"type": "string"},
                        "comparable_properties": {
                            "type": "array",
                            "description": "List of property_ids or dicts",
                        },
                        "client_budget": {
                            "type": "object",
                            "description": "Use client_id to pull mortgage profile",
                        },
                    },
                    "required": [
                        "subject_property_id",
                        "comparable_properties",
                        "client_budget",
                    ],
                },
            },
        }
