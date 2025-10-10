# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAirportByCode(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], iata_code: str) -> str:
        for a in list(data.get("airports", {}).values()):
            if a.get("iata_code") == iata_code:
                return _j(a)
        return _j({"airport_id": "ARP_"+iata_code, "iata_code": iata_code,})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_airport_by_code",
            "description":"Return one airport by IATA code.",
            "parameters":{"type":"object","properties":{"iata_code":{"type":"string"}},"required":["iata_code"]}
        }}
