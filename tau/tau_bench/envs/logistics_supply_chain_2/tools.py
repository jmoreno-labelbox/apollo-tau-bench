import json
from typing import Dict, Any
from domains.dto import Tool
from datetime import datetime


class GetCarrierBySCAC(Tool):
    """Tool to retrieve details of a carrier by carrier SCAC."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carrier_scac = kwargs.get("carrier_scac")
        carriers = data.get("carriers", [])
        for carrier in carriers:
            if carrier["scac"] == carrier_scac:
                return json.dumps(carrier, indent=2)
        return json.dumps({"error": f"Carrier with scac {carrier_scac} not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_carrier_by_scac",
                "description": "Retrieve Carrier details by carrier SCAC.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_scac": {
                            "type": "string",
                            "description": "Unique Carrier identifier."
                        }
                    },
                    "required": ["carrier_scac"]
                }
            }
        }


class GetActiveCarriers(Tool):
    """Tool to retrieve all active carriers."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carriers = data.get("carriers", [])
        list_of_carriers = kwargs.get("list_of_scacs", None)
        if list_of_carriers:
            active_carriers = [carrier['scac'] for carrier in carriers if
                               carrier.get("active_status") and carrier['scac'] in list_of_carriers]
        else:
            active_carriers = [carrier['scac'] for carrier in carriers if carrier.get("active_status")]
        return json.dumps(active_carriers, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_active_carriers",
                "description": "Retrieve all active carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_scacs": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of SCACs to choose from."
                        }
                    }
                }
            }
        }


class GetCarriersByRegion(Tool):
    """Tool to retrieve carriers by region."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carriers = data.get("carriers", [])
        region = kwargs.get("region", None)
        list_of_carriers = kwargs.get("list_of_scacs", None)
        if region:
            active_carriers = [carrier['scac'] for carrier in carriers if carrier.get("active_status") and region.lower() in carrier.get("regional_coverage").lower()]
        else:
            active_carriers = [carrier['scac'] for carrier in carriers if carrier.get("active_status")]
        if list_of_carriers:
            active_carriers = [carrier for carrier in active_carriers if carrier in list_of_carriers]
        return json.dumps(active_carriers, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_carriers_by_region",
                "description": "Retrieve all active carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "region": {
                            "type": "string",
                            "description": "Region eg. Global"
                        },
                        "list_of_scacs": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of SCACs to choose from."
                        }
                    }
                }
            }
        }




class GetCarriersByMode(Tool):
    """Tool to retrieve carriers by supported mode."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carriers = data.get("carriers", [])
        mode = kwargs.get("mode", None)
        list_of_carriers = kwargs.get("list_of_scacs", None)
        if mode:
            active_carriers = [carrier['scac'] for carrier in carriers if carrier.get("active_status") and mode in carrier.get("supported_modes")]
        else:
            active_carriers = [carrier['scac'] for carrier in carriers if carrier.get("active_status")]
        if list_of_carriers:
            active_carriers = [carrier for carrier in active_carriers if carrier in list_of_carriers]
        return json.dumps(active_carriers, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_carriers_by_mode",
                "description": "Retrieve all active carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mode": {
                            "type": "string",
                            "description": "Mode eg. Air, Sea, Truck"
                        },
                        "list_of_scacs": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of SCACs to choose from."
                        }
                    }
                }
            }
        }


class GetTopRatedCarriers(Tool):
    """Tool to return carriers sorted by highest average_rating."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carriers = data.get("carriers", [])
        list_of_carriers = kwargs.get("list_of_scacs", None)
        sorted_carriers = sorted(
            carriers,
            key=lambda c: c.get("performance_metrics", {}).get("average_rating", 0),
            reverse=True
        )
        if list_of_carriers:
            return json.dumps([[sc['scac'], sc['performance_metrics']['average_rating']] for sc in sorted_carriers if sc['scac'] in list_of_carriers],
                              indent=2)
        return json.dumps([[sc['scac'], sc['performance_metrics']['average_rating']] for sc in sorted_carriers], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_top_rated_carriers",
                "description": "Retrieve carriers sorted by highest average rating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_scacs": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of carriers to choose from."
                        }
                    }
                }
            }
        }


class GetOnTimeDeliveryStats(Tool):
    """Tool to calculate average on-time delivery percentage across all carriers."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carriers = data.get("carriers", [])
        list_of_carriers = kwargs.get("list_of_scacs", None)
        if not carriers:
            return json.dumps({"average_on_time_delivery": 0.0}, indent=2)
        if list_of_carriers:
            carriers = [c for c in carriers if c["scac"] in list_of_carriers]
        total = sum(c.get("performance_metrics", {}).get("on_time_delivery_percentage", 0) for c in carriers)
        average = total / len(carriers)
        return json.dumps({"average_on_time_delivery": average}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_on_time_delivery_stats",
                "description": "Calculate average on-time delivery percentage across all carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_scacs": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of carriers to choose from."
                        }
                    }
                }
            }
        }


class UpdateCarrier(Tool):
    """Tool to update carrier information."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carrier_scac = kwargs.get("carrier_scac")
        updates = kwargs.get("updates")
        carriers = data.get("carriers", [])

        for carrier in carriers:
            if carrier["scac"] == carrier_scac:
                carrier.update(updates)
                return json.dumps({"success": f"carrier {carrier_scac} updated"}, indent=2)
        return json.dumps({"error": f"carrier_id {carrier_scac} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_carrier",
                "description": "Update carrier information by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_scac": {"type": "string", "description": "The carrier ID to update"},
                        "updates": {"type": "object", "description": "Fields and values to update"}
                    },
                    "required": ["carrier_scac", "updates"]
                }
            }
        }


class GetShipmentById(Tool):
    """Tool to retrieve details of a shipment by shipment ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        shipment_id = kwargs.get("shipment_id")
        shipments = data.get("inbound_shipments", [])
        for shipment in shipments:
            if shipment["shipment_id"] == shipment_id:
                return json.dumps(shipment, indent=2)
        return json.dumps({"error": f"Shipment with ID {shipment_id} not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_shipment_by_id",
                "description": "Retrieve shipment details by shipment ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {
                            "type": "string",
                            "description": "Unique shipment identifier (e.g., 'SHIP-0012')."
                        }
                    },
                    "required": ["shipment_id"]
                }
            }
        }


class GetShipmentsByStatus(Tool):
    """Tool to retrieve shipments filtered by status (e.g., 'In Transit', 'Received')."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status", "").lower()
        list_of_shipments = kwargs.get("list_of_ids", None)
        shipments = data.get("inbound_shipments", [])
        filtered = [s['shipment_id'] for s in shipments if s.get("status", "").lower() == status]
        if list_of_shipments:
            filtered = [s for s in filtered if s in list_of_shipments]
        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_shipments_by_status",
                "description": "Retrieve shipments filtered by status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Shipment status to filter by (e.g., 'In Transit')."
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of shipments to choose from."
                        }
                    },
                    "required": ["status"]
                }
            }
        }


class GetDelayedShipments(Tool):
    """Tool to retrieve shipments whose expected arrival date is past but actual arrival date is missing."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        from datetime import datetime
        shipments = data.get("inbound_shipments", [])
        list_of_shipments = kwargs.get("list_of_ids", None)
        today = datetime.strptime(kwargs.get('today'), "%Y-%m-%d").date()
        delayed = []
        for s in shipments:
            expected_arrival = s.get("expected_arrival_date")
            actual_arrival = s.get("actual_arrival_date")
            if expected_arrival and actual_arrival is None:
                try:
                    expected_date = datetime.strptime(expected_arrival, "%Y-%m-%d").date()
                    if expected_date < today:
                        delayed.append(s['shipment_id'])
                except Exception:
                    pass
        if list_of_shipments:
            delayed = [d for d in delayed if d in list_of_shipments]
        return json.dumps(delayed, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_delayed_shipments",
                "description": "Retrieve shipments past expected arrival date but not yet arrived.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "today": {"type": "string", "description": "Reference date"},
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of shipments to choose from."
                        }
                    },
                    "required": ["today"]
                }
            }
        }


class FilterInboundShipments(Tool):
    """Tool to retrieve inbound shipments by key and value."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        shipments = data.get("inbound_shipments", [])
        key = kwargs.get("key")
        value = kwargs.get("value")
        list_of_shipments = kwargs.get("list_of_ids", None)
        result = [item['shipment_id'] for item in shipments if item[key].lower() == value.lower()]
        if list_of_shipments:
            result = [r for r in result if r in list_of_shipments]
        if result:
            return json.dumps({key: value, 'result': result}, indent=2)
        return json.dumps({"error": f"No matching shipments found for {key} {value}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filter_inbound_shipments",
                "description": "Retrieve inbound shipments based on key and value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of shipments to choose from."
                        },
                        "key": {
                            "type": "string",
                            "description": "Key to consider like carrier_scac."
                        },
                        "value": {
                            "type": "string",
                            "description": "Value to consider for this skey."
                        }
                    }
                }
            }
        }


class UpdateInboundShipment(Tool):
    """Tool to update inbound shipment information."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        shipment_id = kwargs.get("shipment_id")
        updates = kwargs.get("updates")
        shipments = data.get("inbound_shipments", [])

        for shipment in shipments:
            if shipment["shipment_id"] == shipment_id:
                shipment.update(updates)
                return json.dumps({"success": f"inbound shipment {shipment_id} updated"}, indent=2)
        return json.dumps({"error": f"shipment_id {shipment_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inbound_shipment",
                "description": "Update inbound shipment by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "The inbound shipment ID to update"},
                        "updates": {"type": "object", "description": "Fields and values to update"}
                    },
                    "required": ["shipment_id", "updates"]
                }
            }
        }


class GetInventoryById(Tool):
    """Tool to retrieve inventory item by inventory ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_id = kwargs.get("inventory_id")
        inventories = data.get("inventory", [])
        for item in inventories:
            if item["inventory_id"] == inventory_id:
                return json.dumps(item, indent=2)
        return json.dumps({"error": f"Inventory with ID {inventory_id} not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_by_id",
                "description": "Retrieve inventory item details using inventory ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "Inventory ID (e.g., 'INV-0008')."
                        }
                    },
                    "required": ["inventory_id"]
                }
            }
        }


class GetInventoryBelowReorderPoint(Tool):
    """Tool to retrieve inventory items that are below reorder point."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventories = data.get("inventory", [])
        list_of_inventories = kwargs.get("list_of_ids", None)
        low_stock = [item['inventory_id'] for item in inventories if item["quantity_available"] < item["reorder_point"]]
        if list_of_inventories:
            low_stock = [ls for ls in low_stock if ls in list_of_inventories]
        return json.dumps(low_stock, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_below_reorder_point",
                "description": "Retrieve inventory items where available quantity is below reorder point.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of inventories to choose from."
                        }
                    }
                }
            }
        }


class GetInventoryByWarehouse(Tool):
    """Tool to retrieve inventory items stored in a specific warehouse."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        warehouse_id = kwargs.get("warehouse_id")
        list_of_inventories = kwargs.get("list_of_ids", None)
        inventories = data.get("inventory", [])
        filtered = [item['inventory_id'] for item in inventories if item["warehouse_id"] == warehouse_id]
        if list_of_inventories:
            filtered = [f for f in filtered if f in list_of_inventories]
        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_by_warehouse",
                "description": "Retrieve inventory items from a specific warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "Warehouse ID (e.g., 'WH-10')."
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of inventories to choose from."
                        }
                    },
                    "required": ["warehouse_id"]
                }
            }
        }


class GetExpiredInventory(Tool):
    """Tool to retrieve inventory items that are expired as of today."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        today = datetime.strptime(kwargs.get('today'), "%Y-%m-%d").date()
        inventories = data.get("inventory", [])
        list_of_inventories = kwargs.get("list_of_ids", None)
        expired = []
        for item in inventories:
            exp_date = item.get("expiration_date")
            if exp_date:
                try:
                    if datetime.strptime(exp_date, "%Y-%m-%d").date() < today:
                        expired.append(item['inventory_id'])
                except Exception:
                    continue
        if list_of_inventories:
            expired = [e for e in expired if e in list_of_inventories]
        return json.dumps(expired, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_expired_inventory",
                "description": "Retrieve inventory items that are expired.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "today": {"type": "string", "description": "Reference date"},
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of inventories to choose from."
                        }
                    },
                    "required": ["today"]
                }
            }
        }


class GetInventoryWithDamage(Tool):
    """Tool to retrieve inventory items with quantity_damaged > 0."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventories = data.get("inventory", [])
        threshold = kwargs.get("threshold", None)
        less_than_threshold = kwargs.get("less_than_threshold", "False")
        list_of_inventories = kwargs.get("list_of_ids", None)
        if threshold:
            if less_than_threshold == "True":
                damaged = [[item['inventory_id'], item['quantity_damaged']] for item in inventories if item["quantity_damaged"] < threshold]
            else:
                damaged = [[item['inventory_id'], item['quantity_damaged']] for item in inventories if
                           item["quantity_damaged"] > threshold]
        else:
            if less_than_threshold == "True":
                damaged = [[item['inventory_id'], item['quantity_damaged']] for item in inventories if item["quantity_damaged"] < 0]
            else:
                damaged = [[item['inventory_id'], item['quantity_damaged']] for item in inventories if item["quantity_damaged"] > 0]
        if list_of_inventories:
            damaged = [d for d in damaged if d[0] in list_of_inventories]
        return json.dumps(damaged, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_with_damage",
                "description": "Retrieve inventory items that have damaged stock.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of inventories to choose from."
                        },
                        "threshold": {
                            "type": "number",
                            "description": "Threshold value of quantity damaged."
                        },
                        "less_than_threshold": {
                            "type": "string",
                            "description": "'True' means value compared less than threshold."
                        }
                    }
                }
            }
        }


class FilterInventory(Tool):
    """Tool to retrieve inventory items by key and value."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventories = data.get("inventory", [])
        key = kwargs.get("key")
        value = kwargs.get("value")
        list_of_inventories = kwargs.get("list_of_ids", None)
        result = [item['inventory_id'] for item in inventories if item[key].lower() == value.lower()]
        if list_of_inventories:
            result = [r for r in result if r in list_of_inventories]
        if result:
            return json.dumps({key: value, 'result': result}, indent=2)
        return json.dumps({"error": f"No matching inventories found for {key} {value}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filter_inventory",
                "description": "Retrieve inventory items based on key and value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of inventories to choose from."
                        },
                        "key": {
                            "type": "string",
                            "description": "Key to consider like warehouse_id and sku."
                        },
                        "value": {
                            "type": "string",
                            "description": "Value to consider for this skey."
                        }
                    }
                }
            }
        }


class UpdateInventory(Tool):
    """Tool to update inventory record."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_id = kwargs.get("inventory_id")
        updates = kwargs.get("updates")
        inventories = data.get("inventory", [])

        for inv in inventories:
            if inv["inventory_id"] == inventory_id:
                inv.update(updates)
                return json.dumps({"success": f"inventory {inventory_id} updated"}, indent=2)
        return json.dumps({"error": f"inventory_id {inventory_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory",
                "description": "Update inventory record by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {"type": "string", "description": "The inventory ID to update"},
                        "updates": {"type": "object", "description": "Fields and values to update"}
                    },
                    "required": ["inventory_id", "updates"]
                }
            }
        }


class GetOutboundOrderById(Tool):
    """Tool to retrieve an outbound order by order ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        orders = data.get("outbound_orders", [])
        for order in orders:
            if order["order_id"] == order_id:
                return json.dumps(order, indent=2)
        return json.dumps({"error": f"Order with ID {order_id} not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_outbound_order_by_id",
                "description": "Retrieve outbound order using order ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order ID (e.g., 'ORD-0004')"
                        }
                    },
                    "required": ["order_id"]
                }
            }
        }


class GetOrdersByStatus(Tool):
    """Tool to retrieve outbound orders by status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        list_of_orders = kwargs.get("list_of_ids", None)
        orders = data.get("outbound_orders", [])
        result = [order['order_id'] for order in orders if order["status"].lower() == status.lower()]
        if list_of_orders:
            result = [r for r in result if r in list_of_orders]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_orders_by_status",
                "description": "Retrieve all outbound orders with a given status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Status of the order (e.g., 'Shipped', 'Delivered')"
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of orders to choose from."
                        }
                    },
                    "required": ["status"]
                }
            }
        }


class GetHighValueOutboundOrders(Tool):
    """Tool to retrieve outbound orders above a specified value."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        threshold = kwargs.get("min_value", 100000)
        list_of_orders = kwargs.get("list_of_ids", None)
        orders = data.get("outbound_orders", [])
        result = [order['order_id'] for order in orders if order.get("total_value", 0) >= threshold]
        if list_of_orders:
            result = [r for r in result if r in list_of_orders]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_high_value_outbound_orders",
                "description": "Retrieve outbound orders where total value exceeds the given threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "min_value": {
                            "type": "number",
                            "description": "Minimum total value (default is 100000)"
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of orders to choose from."
                        }
                    }
                }
            }
        }


class GetOrdersRequiringTemperatureControl(Tool):
    """Tool to retrieve orders that require temperature control."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        orders = data.get("outbound_orders", [])
        list_of_orders = kwargs.get("list_of_ids", None)
        result = [order['order_id'] for order in orders if order.get("temperature_control_required")]
        if list_of_orders:
            result = [r for r in result if r in list_of_orders]
        if len(result) == 0:
            return json.dumps("No temperature control required", indent=2)
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_orders_requiring_temperature_control",
                "description": "Retrieve outbound orders with temperature control requirements.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of orders to choose from."
                        }
                    }
                }
            }
        }


class UpdateOutboundOrder(Tool):
    """Tool to update outbound order details."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        updates = kwargs.get("updates")
        orders = data.get("outbound_orders", [])

        for order in orders:
            if order["order_id"] == order_id:
                order.update(updates)
                return json.dumps({"success": f"outbound order {order_id} updated"}, indent=2)
        return json.dumps({"error": f"order_id {order_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_outbound_order",
                "description": "Update outbound order by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The outbound order ID to update"},
                        "updates": {"type": "object", "description": "Fields and values to update"}
                    },
                    "required": ["order_id", "updates"]
                }
            }
        }


class GetProductBySKU(Tool):
    """Tool to retrieve a product by its SKU."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        products = data.get("product_master", [])
        for product in products:
            if product["sku"] == sku:
                return json.dumps(product, indent=2)
        return json.dumps({"error": f"SKU '{sku}' not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_by_sku",
                "description": "Retrieve a product's full details using its SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Product SKU (e.g., 'PHRM-DRUG-S19')"
                        }
                    },
                    "required": ["sku"]
                }
            }
        }


class GetHazmatProducts(Tool):
    """Tool to list all hazardous material products."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        products = data.get("product_master", [])
        list_of_products = kwargs.get("list_of_ids", None)
        result = [p['sku'] for p in products if p.get("hazmat_information", {}).get("is_hazmat")]
        if list_of_products:
            result = [r for r in result if r in list_of_products]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_hazmat_products",
                "description": "List all products classified as hazardous materials.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of products to choose from."
                        }
                    }
                }
            }
        }


class GetProductsByCategory(Tool):
    """Tool to retrieve products by category name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get("category", "").lower()
        list_of_products = kwargs.get("list_of_ids", None)
        products = data.get("product_master", [])
        result = [p['sku'] for p in products if p["category"].lower() == category]
        if list_of_products:
            result = [r for r in result if r in list_of_products]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_products_by_category",
                "description": "Get all products that belong to a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "Category name (e.g., 'Pharmaceuticals')"
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of products to choose from."
                        }
                    },
                    "required": ["category"]
                }
            }
        }


class GetProductsByStorageRequirement(Tool):
    """Tool to list products with specific storage requirements."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        keyword = kwargs.get("keyword", "").lower()
        list_of_products = kwargs.get("list_of_ids", None)
        products = data.get("product_master", [])
        result = [p['sku'] for p in products if keyword in p.get("storage_requirements", "").lower()]
        if list_of_products:
            result = [r for r in result if r in list_of_products]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_products_by_storage_requirement",
                "description": "Filter products that have specific storage requirement keywords.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keyword": {
                            "type": "string",
                            "description": "Keyword for storage requirement (e.g., 'refrigerated')"
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of products to choose from."
                        }
                    },
                    "required": ["keyword"]
                }
            }
        }


class UpdateProduct(Tool):
    """Tool to update product details."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        updates = kwargs.get("updates")
        products = data.get("product_master", [])

        for product in products:
            if product["sku"] == sku:
                product.update(updates)
                return json.dumps({"success": f"product {sku} updated"}, indent=2)
        return json.dumps({"error": f"sku {sku} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_product",
                "description": "Update product by SKU",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "The SKU to update"},
                        "updates": {"type": "object", "description": "Fields and values to update"}
                    },
                    "required": ["sku", "updates"]
                }
            }
        }


class GetSupplierByID(Tool):
    """Tool to retrieve a supplier's details by their ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get("supplier_id")
        list_of_suppliers = kwargs.get("list_of_ids", None)
        suppliers = data.get("supplier_master", [])
        for supplier in suppliers:
            if supplier["supplier_id"] == supplier_id:
                return json.dumps(supplier, indent=2)
        suppliers = [s for s in suppliers if s in list_of_suppliers]
        return json.dumps({"error": f"Supplier ID '{supplier_id}' not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_supplier_by_id",
                "description": "Retrieve supplier information using the supplier ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID (e.g., 'SUP-1005')"
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of suppliers to choose from."
                        }
                    },
                    "required": ["supplier_id"]
                }
            }
        }


class GetPreferredSuppliers(Tool):
    """Tool to list suppliers with 'Preferred' relationship status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_of_suppliers = kwargs.get("list_of_ids", None)
        suppliers = data.get("supplier_master", [])
        result = [s['supplier_id'] for s in suppliers if s["relationship_status"].lower() == "preferred"]
        if list_of_suppliers:
            result = [r for r in result if r in list_of_suppliers]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_preferred_suppliers",
                "description": "List all suppliers with 'Preferred' relationship status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of suppliers to choose from."
                        }
                    }
                }
            }
        }


class GetCertifiedSuppliers(Tool):
    """Tool to filter suppliers by certification keyword."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        keyword = kwargs.get("certification", "").lower()
        list_of_suppliers = kwargs.get("list_of_ids", None)
        suppliers = data.get("supplier_master", [])
        result = [
            s['supplier_id'] for s in suppliers
            if any(keyword in cert.lower() for cert in s.get("certifications", []))
        ]
        if list_of_suppliers:
            result = [r for r in result if r in list_of_suppliers]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_certified_suppliers",
                "description": "Find suppliers that hold a specific certification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification": {
                            "type": "string",
                            "description": "Certification name or keyword (e.g., 'ISO')"
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of suppliers to choose from."
                        }
                    },
                    "required": []
                }
            }
        }


class UpdateSupplier(Tool):
    """Tool to update supplier information."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get("supplier_id")
        updates = kwargs.get("updates")
        suppliers = data.get("supplier_master", [])

        for supplier in suppliers:
            if supplier["supplier_id"] == supplier_id:
                supplier.update(updates)
                return json.dumps({"success": f"supplier {supplier_id} updated"}, indent=2)
        return json.dumps({"error": f"supplier_id {supplier_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_supplier",
                "description": "Update supplier by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "The supplier ID to update"},
                        "updates": {"type": "object", "description": "Fields and values to update"}
                    },
                    "required": ["supplier_id", "updates"]
                }
            }
        }


class GetWarehouseByID(Tool):
    """Tool to retrieve a warehouse’s full details using its ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        warehouse_id = kwargs.get("warehouse_id")
        warehouses = data.get("warehouses", [])
        for warehouse in warehouses:
            if warehouse["warehouse_id"] == warehouse_id:
                return json.dumps(warehouse, indent=2)
        return json.dumps({"error": f"Warehouse ID '{warehouse_id}' not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_warehouse_by_id",
                "description": "Retrieve full warehouse details using warehouse ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "Warehouse ID (e.g., 'WH-14')"
                        }
                    },
                    "required": ["warehouse_id"]
                }
            }
        }


class GetWarehousesByOwnershipStatus(Tool):
    """Tool to retrieve a warehouses by ownership status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ownership_status = kwargs.get("ownership_status")
        list_of_ids = kwargs.get("list_of_ids", [])
        warehouses = data.get("warehouses", [])
        result = []
        for warehouse in warehouses:
            if warehouse["ownership_status"].lower() == ownership_status.lower():
                result.append(warehouse["warehouse_id"])
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_warehouses_by_ownership_status",
                "description": "Retrieve full warehouse details using warehouse ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ownership_status": {"type": "string", "description": "Owned, Leased"},
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of suppliers to choose from."
                        }
                    },
                    "required": ["ownership_status"]
                }
            }
        }


class UpdateWarehouse(Tool):
    """Tool to update warehouse details."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        warehouse_id = kwargs.get("warehouse_id")
        updates = kwargs.get("updates")
        warehouses = data.get("warehouses", [])

        for warehouse in warehouses:
            if warehouse["warehouse_id"] == warehouse_id:
                warehouse.update(updates)
                return json.dumps({"success": f"warehouse {warehouse_id} updated"}, indent=2)
        return json.dumps({"error": f"warehouse_id {warehouse_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_warehouse",
                "description": "Update warehouse by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "The warehouse ID to update"},
                        "updates": {"type": "object", "description": "Fields and values to update"}
                    },
                    "required": ["warehouse_id", "updates"]
                }
            }
        }


class CalculateTotal(Tool):
    """Tool to calculate totals."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        data_kw = kwargs.get("json")
        value_kw = kwargs.get("value")
        key_kw = kwargs.get("key")
        list_of_ids = kwargs.get("list_of_ids", None)
        dataset = data.get(data_kw, [])

        total = 0
        if list_of_ids:
            for instance in dataset:
                if instance[key_kw] in list_of_ids:
                    total += instance[value_kw]
        else:
            for instance in dataset:
                total += instance[value_kw]
        return json.dumps(total, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_total",
                "description": "Calculate total by IDs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "json": {
                            "type": "string",
                            "description": "json file name"
                        },
                        "key": {
                            "type": "string",
                            "description": "key name"
                        },
                        "value": {
                            "type": "string",
                            "description": "value name"
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of suppliers to choose from."
                        }
                    },
                    "required": ["data", "value", "key"]
                }
            }
        }


class CalculateAggregate(Tool):
    """Tool to calculate aggregates."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        agg_kw = kwargs.get("agg")
        data_kw = kwargs.get("json")
        value_kw = kwargs.get("value")
        value_kw2 = kwargs.get("value2", None)
        key_kw = kwargs.get("key")
        list_of_ids = kwargs.get("list_of_ids", None)
        dataset = data.get(data_kw, [])

        result = []
        for instance in dataset:
            if value_kw2:
                result.append([instance[key_kw], instance[value_kw][value_kw2]])
            else:
                result.append([instance[key_kw], instance[value_kw]])
        if list_of_ids:
            result = [r for r in result if r[0] in list_of_ids]
        result = sorted(result, key=lambda x: x[1])
        min_value = min([result[i][1] for i in range(len(result))])
        min_keys = [r[0] for r in result if r[1]==min_value]
        max_value = max([result[i][1] for i in range(len(result))])
        max_keys = [r[0] for r in result if r[1]==max_value]

        if agg_kw == "min":
            return json.dumps({
                key_kw: min_keys,
                value_kw: min_value
            }, indent=2)
        elif agg_kw == "max":
            return json.dumps({
                key_kw: max_keys,
                value_kw: max_value
            }, indent=2)
        elif agg_kw == "both":
            return json.dumps({
                'min_key': min_keys,
                'min_value': min_value,
                'max_key': max_keys,
                'max_value': max_value
            }, indent=2)
        elif agg_kw == "avg":
            return json.dumps(sum([r[1] for r in result])/len(result), indent=2)
        else:
            return json.dumps({"error": "No aggregate mentioned."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_aggregate",
                "description": "Calculate aggregate by IDs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "agg": {
                            "type": "string",
                            "description": "aggregate minimum, maximum, average"
                        },
                        "json": {
                            "type": "string",
                            "description": "json file name"
                        },
                        "key": {
                            "type": "string",
                            "description": "key name"
                        },
                        "value": {
                            "type": "string",
                            "description": "value name"
                        },
                        "value2": {
                            "type": "string",
                            "description": "value name"
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of suppliers to choose from."
                        }
                    },
                    "required": ["agg", "data", "value", "key"]
                }
            }
        }


class ReturnIds(Tool):
    """Tool to return list of ids."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        list_of_ids = kwargs.get("list_of_ids", [])
        return json.dumps(list_of_ids, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "return_ids",
                "description": "Return List of Ids",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of suppliers to choose from."
                        }
                    },
                    "required": []
                }
            }
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
    ReturnIds()
]
