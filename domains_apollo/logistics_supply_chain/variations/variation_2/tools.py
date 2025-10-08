import json
from datetime import datetime
from typing import Any

from domains.dto import Tool


class GetCarrierBySCAC(Tool):
    """Utility for obtaining carrier information using the carrier SCAC."""

    @staticmethod
    def invoke(data: dict[str, Any], carrier_scac: str) -> str:
        carriers = data.get("carriers", [])
        for carrier in carriers:
            if carrier["scac"] == carrier_scac:
                payload = carrier
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Carrier with scac {carrier_scac} not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCarrierByScac",
                "description": "Retrieve Carrier details by carrier SCAC.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_scac": {
                            "type": "string",
                            "description": "Unique Carrier identifier.",
                        }
                    },
                    "required": ["carrier_scac"],
                },
            },
        }


class GetActiveCarriers(Tool):
    """Utility for fetching all currently active carriers."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_scacs: list[str] = None) -> str:
        carriers = data.get("carriers", [])
        if list_of_scacs:
            active_carriers = [
                carrier["scac"]
                for carrier in carriers
                if carrier.get("active_status") and carrier["scac"] in list_of_scacs
            ]
        else:
            active_carriers = [
                carrier["scac"] for carrier in carriers if carrier.get("active_status")
            ]
        payload = active_carriers
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetActiveCarriers",
                "description": "Retrieve all active carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_scacs": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of SCACs to choose from.",
                        }
                    },
                },
            },
        }


class GetCarriersByRegion(Tool):
    """Utility for obtaining carriers based on their geographical region."""

    @staticmethod
    def invoke(data: dict[str, Any], region: str = None, list_of_scacs: list[str] = None) -> str:
        carriers = data.get("carriers", [])
        if region:
            active_carriers = [
                carrier["scac"]
                for carrier in carriers
                if carrier.get("active_status")
                and region.lower() in carrier.get("regional_coverage").lower()
            ]
        else:
            active_carriers = [
                carrier["scac"] for carrier in carriers if carrier.get("active_status")
            ]
        if list_of_scacs:
            active_carriers = [
                carrier for carrier in active_carriers if carrier in list_of_scacs
            ]
        payload = active_carriers
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCarriersByRegion",
                "description": "Retrieve all active carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "region": {
                            "type": "string",
                            "description": "Region eg. Global",
                        },
                        "list_of_scacs": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of SCACs to choose from.",
                        },
                    },
                },
            },
        }


class GetCarriersByMode(Tool):
    """Utility for fetching carriers according to their supported transportation mode."""

    @staticmethod
    def invoke(data: dict[str, Any], mode: str = None, list_of_scacs: list[str] = None) -> str:
        carriers = data.get("carriers", [])
        if mode:
            active_carriers = [
                carrier["scac"]
                for carrier in carriers
                if carrier.get("active_status")
                and mode in carrier.get("supported_modes")
            ]
        else:
            active_carriers = [
                carrier["scac"] for carrier in carriers if carrier.get("active_status")
            ]
        if list_of_scacs:
            active_carriers = [
                carrier for carrier in active_carriers if carrier in list_of_scacs
            ]
        payload = active_carriers
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCarriersByMode",
                "description": "Retrieve all active carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mode": {
                            "type": "string",
                            "description": "Mode eg. Air, Sea, Truck",
                        },
                        "list_of_scacs": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of SCACs to choose from.",
                        },
                    },
                },
            },
        }


class GetTopRatedCarriers(Tool):
    """Utility for listing carriers arranged by their highest average rating."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_scacs: list[str] = None) -> str:
        carriers = data.get("carriers", [])
        sorted_carriers = sorted(
            carriers,
            key=lambda c: c.get("performance_metrics", {}).get("average_rating", 0),
            reverse=True,
        )
        if list_of_scacs:
            payload = [
                [sc["scac"], sc["performance_metrics"]["average_rating"]]
                for sc in sorted_carriers
                if sc["scac"] in list_of_scacs
            ]
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = [
            [sc["scac"], sc["performance_metrics"]["average_rating"]]
            for sc in sorted_carriers
        ]
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTopRatedCarriers",
                "description": "Retrieve carriers sorted by highest average rating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_scacs": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of carriers to choose from.",
                        }
                    },
                },
            },
        }


class GetOnTimeDeliveryStats(Tool):
    """Utility for computing the average percentage of on-time deliveries for all carriers."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_scacs: list[str] = None) -> str:
        carriers = data.get("carriers", [])
        if not carriers:
            payload = {"average_on_time_delivery": 0.0}
            out = json.dumps(payload, indent=2)
            return out
        if list_of_scacs:
            carriers = [c for c in carriers if c["scac"] in list_of_scacs]
        total = sum(
            c.get("performance_metrics", {}).get("on_time_delivery_percentage", 0)
            for c in carriers
        )
        average = total / len(carriers)
        payload = {"average_on_time_delivery": average}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOnTimeDeliveryStats",
                "description": "Calculate average on-time delivery percentage across all carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_scacs": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of carriers to choose from.",
                        }
                    },
                },
            },
        }


class UpdateCarrier(Tool):
    """Utility for modifying carrier details."""

    @staticmethod
    def invoke(data: dict[str, Any], carrier_scac: str = None, updates: dict[str, Any] = None) -> str:
        carriers = data.get("carriers", [])

        for carrier in carriers:
            if carrier["scac"] == carrier_scac:
                carrier.update(updates)
                payload = {"success": f"carrier {carrier_scac} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"carrier_id {carrier_scac} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCarrier",
                "description": "Update carrier information by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_scac": {
                            "type": "string",
                            "description": "The carrier ID to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Fields and values to update",
                        },
                    },
                    "required": ["carrier_scac", "updates"],
                },
            },
        }


class GetShipmentById(Tool):
    """Utility for obtaining shipment information using the shipment ID."""

    @staticmethod
    def invoke(data: dict[str, Any], shipment_id: str) -> str:
        shipments = data.get("inbound_shipments", [])
        for shipment in shipments:
            if shipment["shipment_id"] == shipment_id:
                payload = shipment
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Shipment with ID {shipment_id} not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetShipmentById",
                "description": "Retrieve shipment details by shipment ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {
                            "type": "string",
                            "description": "Unique shipment identifier (e.g., 'SHIP-0012').",
                        }
                    },
                    "required": ["shipment_id"],
                },
            },
        }


class GetShipmentsByStatus(Tool):
    """Utility for fetching shipments based on their status (e.g., 'In Transit', 'Received')."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = "", list_of_ids: list = None) -> str:
        status = status.lower()
        list_of_shipments = list_of_ids
        shipments = data.get("inbound_shipments", [])
        filtered = [
            s["shipment_id"] for s in shipments if s.get("status", "").lower() == status
        ]
        if list_of_shipments:
            filtered = [s for s in filtered if s in list_of_shipments]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetShipmentsByStatus",
                "description": "Retrieve shipments filtered by status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Shipment status to filter by (e.g., 'In Transit').",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of shipments to choose from.",
                        },
                    },
                    "required": ["status"],
                },
            },
        }


class GetDelayedShipments(Tool):
    """Utility for obtaining shipments where the expected arrival date has passed but the actual arrival date is not recorded."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_ids: list = None, today: str = None) -> str:
        from datetime import datetime

        shipments = data.get("inbound_shipments", [])
        today_date = datetime.strptime(today, "%Y-%m-%d").date()
        delayed = []
        for s in shipments:
            expected_arrival = s.get("expected_arrival_date")
            actual_arrival = s.get("actual_arrival_date")
            if expected_arrival and actual_arrival is None:
                try:
                    expected_date = datetime.strptime(
                        expected_arrival, "%Y-%m-%d"
                    ).date()
                    if expected_date < today_date:
                        delayed.append(s["shipment_id"])
                except Exception:
                    pass
        if list_of_ids:
            delayed = [d for d in delayed if d in list_of_ids]
        payload = delayed
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDelayedShipments",
                "description": "Retrieve shipments past expected arrival date but not yet arrived.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "today": {"type": "string", "description": "Reference date"},
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of shipments to choose from.",
                        },
                    },
                    "required": ["today"],
                },
            },
        }


class FilterInboundShipments(Tool):
    """Utility for fetching inbound shipments based on specific key-value pairs."""

    @staticmethod
    def invoke(data: dict[str, Any], key: str, value: str, list_of_ids: list[str] = None) -> str:
        shipments = data.get("inbound_shipments", [])
        result = [
            item["shipment_id"]
            for item in shipments
            if item[key].lower() == value.lower()
        ]
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        if result:
            payload = {key: value, "result": result}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"No matching shipments found for {key} {value}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterInboundShipments",
                "description": "Retrieve inbound shipments based on key and value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of shipments to choose from.",
                        },
                        "key": {
                            "type": "string",
                            "description": "Key to consider like carrier_scac.",
                        },
                        "value": {
                            "type": "string",
                            "description": "Value to consider for this skey.",
                        },
                    },
                },
            },
        }


class UpdateInboundShipment(Tool):
    """Utility for modifying details of inbound shipments."""

    @staticmethod
    def invoke(data: dict[str, Any], shipment_id: str = None, updates: dict[str, Any] = None) -> str:
        shipments = data.get("inbound_shipments", [])

        for shipment in shipments:
            if shipment["shipment_id"] == shipment_id:
                shipment.update(updates)
                payload = {"success": f"inbound shipment {shipment_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"shipment_id {shipment_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInboundShipment",
                "description": "Update inbound shipment by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {
                            "type": "string",
                            "description": "The inbound shipment ID to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Fields and values to update",
                        },
                    },
                    "required": ["shipment_id", "updates"],
                },
            },
        }


class GetInventoryById(Tool):
    """Utility for obtaining an inventory item using its inventory ID."""

    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None) -> str:
        inventories = data.get("inventory", [])
        for item in inventories:
            if item["inventory_id"] == inventory_id:
                payload = item
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Inventory with ID {inventory_id} not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryById",
                "description": "Retrieve inventory item details using inventory ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "Inventory ID (e.g., 'INV-0008').",
                        }
                    },
                    "required": ["inventory_id"],
                },
            },
        }


class GetInventoryBelowReorderPoint(Tool):
    """Utility for fetching inventory items that fall below the reorder threshold."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_ids: list[str] = None) -> str:
        inventories = data.get("inventory", [])
        low_stock = [
            item["inventory_id"]
            for item in inventories
            if item["quantity_available"] < item["reorder_point"]
        ]
        if list_of_ids:
            low_stock = [ls for ls in low_stock if ls in list_of_ids]
        payload = low_stock
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryBelowReorderPoint",
                "description": "Retrieve inventory items where available quantity is below reorder point.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of inventories to choose from.",
                        }
                    },
                },
            },
        }


class GetInventoryByWarehouse(Tool):
    """Utility for obtaining inventory items located in a designated warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str, list_of_ids: list[str] = None) -> str:
        inventories = data.get("inventory", [])
        filtered = [
            item["inventory_id"]
            for item in inventories
            if item["warehouse_id"] == warehouse_id
        ]
        if list_of_ids:
            filtered = [f for f in filtered if f in list_of_ids]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryByWarehouse",
                "description": "Retrieve inventory items from a specific warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "Warehouse ID (e.g., 'WH-10').",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of inventories to choose from.",
                        },
                    },
                    "required": ["warehouse_id"],
                },
            },
        }


class GetExpiredInventory(Tool):
    """Utility for fetching inventory items that have expired as of the current date."""

    @staticmethod
    def invoke(data: dict[str, Any], today: str, list_of_ids: list[str] = None) -> str:
        today_date = datetime.strptime(today, "%Y-%m-%d").date()
        inventories = data.get("inventory", [])
        expired = []
        for item in inventories:
            exp_date = item.get("expiration_date")
            if exp_date:
                try:
                    if datetime.strptime(exp_date, "%Y-%m-%d").date() < today_date:
                        expired.append(item["inventory_id"])
                except Exception:
                    continue
        if list_of_ids:
            expired = [e for e in expired if e in list_of_ids]
        payload = expired
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetExpiredInventory",
                "description": "Retrieve inventory items that are expired.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "today": {"type": "string", "description": "Reference date"},
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of inventories to choose from.",
                        },
                    },
                    "required": ["today"],
                },
            },
        }


class GetInventoryWithDamage(Tool):
    """Utility for obtaining inventory items that have a quantity damaged greater than zero."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        threshold: int = None,
        less_than_threshold: str = "False",
        list_of_ids: list = None
    ) -> str:
        inventories = data.get("inventory", [])
        if threshold:
            if less_than_threshold == "True":
                damaged = [
                    [item["inventory_id"], item["quantity_damaged"]]
                    for item in inventories
                    if item["quantity_damaged"] < threshold
                ]
            else:
                damaged = [
                    [item["inventory_id"], item["quantity_damaged"]]
                    for item in inventories
                    if item["quantity_damaged"] > threshold
                ]
        else:
            if less_than_threshold == "True":
                damaged = [
                    [item["inventory_id"], item["quantity_damaged"]]
                    for item in inventories
                    if item["quantity_damaged"] < 0
                ]
            else:
                damaged = [
                    [item["inventory_id"], item["quantity_damaged"]]
                    for item in inventories
                    if item["quantity_damaged"] > 0
                ]
        if list_of_ids:
            damaged = [d for d in damaged if d[0] in list_of_ids]
        payload = damaged
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryWithDamage",
                "description": "Retrieve inventory items that have damaged stock.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of inventories to choose from.",
                        },
                        "threshold": {
                            "type": "number",
                            "description": "Threshold value of quantity damaged.",
                        },
                        "less_than_threshold": {
                            "type": "string",
                            "description": "'True' means value compared less than threshold.",
                        },
                    },
                },
            },
        }


class FilterInventory(Tool):
    """Utility for fetching inventory items based on specific key-value criteria."""

    @staticmethod
    def invoke(data: dict[str, Any], key: str, value: str, list_of_ids: list[str] = None) -> str:
        inventories = data.get("inventory", [])
        result = [
            item["inventory_id"]
            for item in inventories
            if item[key].lower() == value.lower()
        ]
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        if result:
            payload = {key: value, "result": result}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"No matching inventories found for {key} {value}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterInventory",
                "description": "Retrieve inventory items based on key and value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of inventories to choose from.",
                        },
                        "key": {
                            "type": "string",
                            "description": "Key to consider like warehouse_id and sku.",
                        },
                        "value": {
                            "type": "string",
                            "description": "Value to consider for this skey.",
                        },
                    },
                },
            },
        }


class UpdateInventory(Tool):
    """Utility for modifying inventory records."""

    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None, updates: dict[str, Any] = None) -> str:
        inventories = data.get("inventory", [])

        for inv in inventories:
            if inv["inventory_id"] == inventory_id:
                inv.update(updates)
                payload = {"success": f"inventory {inventory_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"inventory_id {inventory_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventory",
                "description": "Update inventory record by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "The inventory ID to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Fields and values to update",
                        },
                    },
                    "required": ["inventory_id", "updates"],
                },
            },
        }


class GetOutboundOrderById(Tool):
    """Utility for obtaining an outbound order using its order ID."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        orders = data.get("outbound_orders", [])
        for order in orders:
            if order["order_id"] == order_id:
                payload = order
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Order with ID {order_id} not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOutboundOrderById",
                "description": "Retrieve outbound order using order ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order ID (e.g., 'ORD-0004')",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }


class GetOrdersByStatus(Tool):
    """Utility for fetching outbound orders based on their status."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str, list_of_ids: list[str] = None) -> str:
        orders = data.get("outbound_orders", [])
        result = [
            order["order_id"]
            for order in orders
            if order["status"].lower() == status.lower()
        ]
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrdersByStatus",
                "description": "Retrieve all outbound orders with a given status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Status of the order (e.g., 'Shipped', 'Delivered')",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of orders to choose from.",
                        },
                    },
                    "required": ["status"],
                },
            },
        }


class GetHighValueOutboundOrders(Tool):
    """Utility for obtaining outbound orders that exceed a certain value."""

    @staticmethod
    def invoke(data: dict[str, Any], min_value: int = 100000, list_of_ids: list = None) -> str:
        orders = data.get("outbound_orders", [])
        result = [
            order["order_id"]
            for order in orders
            if order.get("total_value", 0) >= min_value
        ]
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHighValueOutboundOrders",
                "description": "Retrieve outbound orders where total value exceeds the given threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "min_value": {
                            "type": "number",
                            "description": "Minimum total value (default is 100000)",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of orders to choose from.",
                        },
                    },
                },
            },
        }


class GetOrdersRequiringTemperatureControl(Tool):
    """Utility for fetching orders that necessitate temperature regulation."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_ids: list[str] = None) -> str:
        orders = data.get("outbound_orders", [])
        result = [
            order["order_id"]
            for order in orders
            if order.get("temperature_control_required")
        ]
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        if len(result) == 0:
            payload = "No temperature control required"
            out = json.dumps(payload, indent=2)
            return out
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrdersRequiringTemperatureControl",
                "description": "Retrieve outbound orders with temperature control requirements.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of orders to choose from.",
                        }
                    },
                },
            },
        }


class UpdateOutboundOrder(Tool):
    """Utility for modifying details of outbound orders."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, updates: dict[str, Any] = None) -> str:
        orders = data.get("outbound_orders", [])

        for order in orders:
            if order["order_id"] == order_id:
                order.update(updates)
                payload = {"success": f"outbound order {order_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"order_id {order_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOutboundOrder",
                "description": "Update outbound order by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The outbound order ID to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Fields and values to update",
                        },
                    },
                    "required": ["order_id", "updates"],
                },
            },
        }


class GetProductBySKU(Tool):
    """Utility for obtaining a product using its SKU."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str) -> str:
        products = data.get("product_master", [])
        for product in products:
            if product["sku"] == sku:
                payload = product
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"SKU '{sku}' not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductBySku",
                "description": "Retrieve a product's full details using its SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Product SKU (e.g., 'PHRM-DRUG-S19')",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }


class GetHazmatProducts(Tool):
    """Utility for compiling a list of all hazardous material products."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_ids: list[str] = None) -> str:
        products = data.get("product_master", [])
        result = [
            p["sku"]
            for p in products
            if p.get("hazmat_information", {}).get("is_hazmat")
        ]
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHazmatProducts",
                "description": "List all products classified as hazardous materials.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of products to choose from.",
                        }
                    },
                },
            },
        }


class GetProductsByCategory(Tool):
    """Utility for fetching products based on their category name."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = "", list_of_ids: list = None) -> str:
        category = category.lower()
        list_of_products = list_of_ids
        products = data.get("product_master", [])
        result = [p["sku"] for p in products if p["category"].lower() == category]
        if list_of_products:
            result = [r for r in result if r in list_of_products]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductsByCategory",
                "description": "Get all products that belong to a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "Category name (e.g., 'Pharmaceuticals')",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of products to choose from.",
                        },
                    },
                    "required": ["category"],
                },
            },
        }


class GetProductsByStorageRequirement(Tool):
    """Utility for compiling a list of products that have particular storage needs."""

    @staticmethod
    def invoke(data: dict[str, Any], keyword: str = "", list_of_ids: list = None) -> str:
        keyword = keyword.lower()
        list_of_products = list_of_ids
        products = data.get("product_master", [])
        result = [
            p["sku"]
            for p in products
            if keyword in p.get("storage_requirements", "").lower()
        ]
        if list_of_products:
            result = [r for r in result if r in list_of_products]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductsByStorageRequirement",
                "description": "Filter products that have specific storage requirement keywords.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keyword": {
                            "type": "string",
                            "description": "Keyword for storage requirement (e.g., 'refrigerated')",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of products to choose from.",
                        },
                    },
                    "required": ["keyword"],
                },
            },
        }


class UpdateProduct(Tool):
    """Utility for modifying product information."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, updates: dict[str, Any] = None) -> str:
        products = data.get("product_master", [])

        for product in products:
            if product["sku"] == sku:
                product.update(updates)
                payload = {"success": f"product {sku} updated"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"sku {sku} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProduct",
                "description": "Update product by SKU",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "The SKU to update"},
                        "updates": {
                            "type": "object",
                            "description": "Fields and values to update",
                        },
                    },
                    "required": ["sku", "updates"],
                },
            },
        }


class GetSupplierByID(Tool):
    """Utility for obtaining supplier information using their ID."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str, list_of_ids: list = None) -> str:
        suppliers = data.get("supplier_master", [])
        for supplier in suppliers:
            if supplier["supplier_id"] == supplier_id:
                payload = supplier
                out = json.dumps(payload, indent=2)
                return out
        suppliers = [s for s in suppliers if s in list_of_ids]
        payload = {"error": f"Supplier ID '{supplier_id}' not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupplierById",
                "description": "Retrieve supplier information using the supplier ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID (e.g., 'SUP-1005')",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of suppliers to choose from.",
                        },
                    },
                    "required": ["supplier_id"],
                },
            },
        }


class GetPreferredSuppliers(Tool):
    """Utility for compiling a list of suppliers that have a 'Preferred' relationship status."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_ids: list[str] = None) -> str:
        suppliers = data.get("supplier_master", [])
        result = [
            s["supplier_id"]
            for s in suppliers
            if s["relationship_status"].lower() == "preferred"
        ]
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPreferredSuppliers",
                "description": "List all suppliers with 'Preferred' relationship status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of suppliers to choose from.",
                        }
                    },
                },
            },
        }


class GetCertifiedSuppliers(Tool):
    """Utility for fetching suppliers based on a certification keyword."""

    @staticmethod
    def invoke(data: dict[str, Any], certification: str = "", list_of_ids: list = None) -> str:
        keyword = certification.lower()
        list_of_suppliers = list_of_ids
        suppliers = data.get("supplier_master", [])
        result = [
            s["supplier_id"]
            for s in suppliers
            if any(keyword in cert.lower() for cert in s.get("certifications", []))
        ]
        if list_of_suppliers:
            result = [r for r in result if r in list_of_suppliers]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCertifiedSuppliers",
                "description": "Find suppliers that hold a specific certification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification": {
                            "type": "string",
                            "description": "Certification name or keyword (e.g., 'ISO')",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of suppliers to choose from.",
                        },
                    },
                    "required": [],
                },
            },
        }


class UpdateSupplier(Tool):
    """Utility for modifying supplier details."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, updates: dict[str, Any] = None) -> str:
        suppliers = data.get("supplier_master", [])

        for supplier in suppliers:
            if supplier["supplier_id"] == supplier_id:
                supplier.update(updates)
                payload = {"success": f"supplier {supplier_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"supplier_id {supplier_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSupplier",
                "description": "Update supplier by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The supplier ID to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Fields and values to update",
                        },
                    },
                    "required": ["supplier_id", "updates"],
                },
            },
        }


class GetWarehouseByID(Tool):
    """Utility for obtaining complete details of a warehouse via its ID."""
    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str = None) -> str:
        warehouses = data.get("warehouses", [])
        for warehouse in warehouses:
            if warehouse["warehouse_id"] == warehouse_id:
                payload = warehouse
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Warehouse ID '{warehouse_id}' not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWarehouseById",
                "description": "Retrieve full warehouse details using warehouse ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "Warehouse ID (e.g., 'WH-14')",
                        }
                    },
                    "required": ["warehouse_id"],
                },
            },
        }


class GetWarehousesByOwnershipStatus(Tool):
    """Utility for fetching warehouses based on their ownership status."""

    @staticmethod
    def invoke(data: dict[str, Any], ownership_status: str, list_of_ids: list = None) -> str:
        if list_of_ids is None:
            list_of_ids = []
        warehouses = data.get("warehouses", [])
        result = []
        for warehouse in warehouses:
            if warehouse["ownership_status"].lower() == ownership_status.lower():
                result.append(warehouse["warehouse_id"])
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWarehousesByOwnershipStatus",
                "description": "Retrieve full warehouse details using warehouse ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ownership_status": {
                            "type": "string",
                            "description": "Owned, Leased",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of suppliers to choose from.",
                        },
                    },
                    "required": ["ownership_status"],
                },
            },
        }


class UpdateWarehouse(Tool):
    """Utility for modifying warehouse information."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str = None, updates: dict[str, Any] = None) -> str:
        warehouses = data.get("warehouses", [])

        for warehouse in warehouses:
            if warehouse["warehouse_id"] == warehouse_id:
                warehouse.update(updates)
                payload = {"success": f"warehouse {warehouse_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"warehouse_id {warehouse_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateWarehouse",
                "description": "Update warehouse by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The warehouse ID to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Fields and values to update",
                        },
                    },
                    "required": ["warehouse_id", "updates"],
                },
            },
        }


class CalculateTotal(Tool):
    """Utility for computing total amounts."""

    @staticmethod
    def invoke(data: dict[str, Any], json: str = None, value: str = None, key: str = None, list_of_ids: list = None, json_name: str = None) -> str:
        # Support both 'json' and 'json_name' for backward compatibility
        data_key = json_name or json
        dataset = data.get(data_key, [])

        total = 0
        if list_of_ids:
            for instance in dataset:
                if instance[key] in list_of_ids:
                    total += instance[value]
        else:
            for instance in dataset:
                total += instance[value]
        payload = total
        import json as json_module
        out = json_module.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotal",
                "description": "Calculate total by IDs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "json": {"type": "string", "description": "json file name"},
                        "key": {"type": "string", "description": "key name"},
                        "value": {"type": "string", "description": "value name"},
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of suppliers to choose from.",
                        },
                    },
                    "required": ["data", "value", "key"],
                },
            },
        }


class CalculateAggregate(Tool):
    """Utility for computing aggregate values."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        agg: str,
        json: str = None,
        value: str = None,
        key: str = None,
        value2: str = None,
        list_of_ids: list = None,
        json_name: str = None
    ) -> str:
        import json as json_module
        # Support both 'json' and 'json_name' for backward compatibility
        data_key = json_name or json
        dataset = data.get(data_key, [])

        result = []
        for instance in dataset:
            if value2:
                result.append([instance[key], instance[value][value2]])
            else:
                result.append([instance[key], instance[value]])
        if list_of_ids:
            result = [r for r in result if r[0] in list_of_ids]
        result = sorted(result, key=lambda x: x[1])
        min_value = min([result[i][1] for i in range(len(result))])
        min_keys = [r[0] for r in result if r[1] == min_value]
        max_value = max([result[i][1] for i in range(len(result))])
        max_keys = [r[0] for r in result if r[1] == max_value]

        if agg == "min":
            payload = {key: min_keys, value: min_value}
            out = json_module.dumps(payload, indent=2)
            return out
        elif agg == "max":
            payload = {key: max_keys, value: max_value}
            out = json_module.dumps(payload, indent=2)
            return out
        elif agg == "both":
            payload = {
                "min_key": min_keys,
                "min_value": min_value,
                "max_key": max_keys,
                "max_value": max_value,
            }
            out = json_module.dumps(payload, indent=2)
            return out
        elif agg == "avg":
            payload = sum([r[1] for r in result]) / len(result)
            out = json_module.dumps(payload, indent=2)
            return out
        else:
            payload = {"error": "No aggregate mentioned."}
            out = json_module.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateAggregate",
                "description": "Calculate aggregate by IDs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "agg": {
                            "type": "string",
                            "description": "aggregate minimum, maximum, average",
                        },
                        "json": {"type": "string", "description": "json file name"},
                        "key": {"type": "string", "description": "key name"},
                        "value": {"type": "string", "description": "value name"},
                        "value2": {"type": "string", "description": "value name"},
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of suppliers to choose from.",
                        },
                    },
                    "required": ["agg", "data", "value", "key"],
                },
            },
        }


class ReturnIds(Tool):
    """Utility for providing a list of identifiers."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_ids: list = None) -> str:
        if list_of_ids is None:
            list_of_ids = []
        payload = list_of_ids
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReturnIds",
                "description": "Return List of Ids",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of suppliers to choose from.",
                        }
                    },
                    "required": [],
                },
            },
        }


TOOLS = [
    GetCarrierBySCAC(),
    GetActiveCarriers(),
    GetCarriersByRegion(),
    GetCarriersByMode(),
    GetTopRatedCarriers(),
    GetOnTimeDeliveryStats(),
    UpdateCarrier(),
    GetShipmentById(),
    GetShipmentsByStatus(),
    GetDelayedShipments(),
    FilterInboundShipments(),
    UpdateInboundShipment(),
    GetInventoryById(),
    GetInventoryBelowReorderPoint(),
    GetInventoryByWarehouse(),
    GetExpiredInventory(),
    GetInventoryWithDamage(),
    FilterInventory(),
    UpdateInventory(),
    GetOutboundOrderById(),
    GetOrdersByStatus(),
    GetHighValueOutboundOrders(),
    GetOrdersRequiringTemperatureControl(),
    UpdateOutboundOrder(),
    GetProductBySKU(),
    GetHazmatProducts(),
    GetProductsByCategory(),
    GetProductsByStorageRequirement(),
    UpdateProduct(),
    GetSupplierByID(),
    GetPreferredSuppliers(),
    GetCertifiedSuppliers(),
    UpdateSupplier(),
    GetWarehouseByID(),
    GetWarehousesByOwnershipStatus(),
    UpdateWarehouse(),
    CalculateTotal(),
    CalculateAggregate(),
    ReturnIds(),
]
