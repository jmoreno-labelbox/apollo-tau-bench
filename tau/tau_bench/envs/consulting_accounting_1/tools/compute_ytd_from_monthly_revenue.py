# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeYtdFromMonthlyRevenue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        year = kwargs.get("year")
        through = kwargs.get("through_month")
        if not year or not through:
            return json.dumps({"error":"year and through_month are required"}, indent=2)
        rows = [r for r in list(data.get("monthly_revenue", {}).values()) if str(r.get("month_year","")).startswith(f"{year}-")]
        total = 0.0
        for r in rows:
            try:
                m = int(r["month_year"].split("-")[1])
                if m <= through:
                    total += float(r.get("revenue",0.0))
            except Exception:
                continue
        return json.dumps({"year": year,"through_month": through,"ytd_revenue": round(total,2)}, indent=2)

    @staticmethod
    def get_info(self=None) -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"compute_ytd_from_monthly_revenue",
            "description":"Compute YTD revenue summing monthly_revenue rows up to a month.",
            "parameters":{"type":"object","properties":{
                "year":{"type":"integer"},
                "through_month":{"type":"integer"}
            },"required":["year","through_month"]}
        }}
