import json
import random
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def get_current_year() -> int:
    pass
    return 2025


class GetProductDetails(Tool):
    """A utility for fetching all master data related to a specific product by its name."""

    @staticmethod
    def invoke(data: dict[str, Any], product_name: str = None) -> str:
        if not product_name:
            payload = {"error": "product_name is a required argument."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        product_master = data.get("product_master", {}).values()
        product = next(
            (p for p in product_master.values() if p.get("product_name") == product_name), None
        )
        if product:
            payload = product
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Product '{product_name}' not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductDetails",
                "description": "Retrieves all master data for a specific product by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_name": {
                            "type": "string",
                            "description": "The full, exact name of the product to search for.",
                        }
                    },
                    "required": ["product_name"],
                },
            },
        }


class ListWarehousesByCapability(Tool):
    """A utility to locate all warehouses that possess a particular certification."""

    @staticmethod
    def invoke(data: dict[str, Any], certification: str = None) -> str:
        if not certification:
            payload = {"error": "certification is a required argument."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        warehouses = data.get("warehouses", {}).values()
        matching_warehouses = [
            wh for wh in warehouses.values() if certification in wh.get("certifications", [])
        ]
        payload = matching_warehouses
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListWarehousesByCapability",
                "description": "Finds all warehouses that hold a specific certification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification": {
                            "type": "string",
                            "description": "The certification to filter warehouses by (e.g., 'FDA Registered').",
                        }
                    },
                    "required": ["certification"],
                },
            },
        }


class GetInventoryBySku(Tool):
    """A utility to obtain all inventory records for a specified SKU across all warehouses."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None) -> str:
        if not sku:
            payload = {"error": "sku is a required argument."}
            out = json.dumps(payload, indent=2)
            return out
        inventory = data.get("inventory", {}).values()
        sku_inventory = [item for item in inventory.values() if item.get("sku") == sku]
        payload = sku_inventory
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryBySku",
                "description": "Retrieves all inventory records for a specific SKU across all warehouses.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU to search for inventory records of.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }


class ListCarriersByMode(Tool):
    """A utility to identify all active carriers that facilitate a specific transport mode."""

    @staticmethod
    def invoke(data: dict[str, Any], mode: str = None) -> str:
        if not mode:
            payload = {"error": "mode is a required argument."}
            out = json.dumps(payload, indent=2)
            return out
        carriers = data.get("carriers", {}).values()
        matching_carriers = [
            c
            for c in carriers.values() if c.get("active_status") is True
            and mode.title() in c.get("supported_modes", [])
        ]
        payload = matching_carriers
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListCarriersByMode",
                "description": "Finds all active carriers for a given transportation mode.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mode": {
                            "type": "string",
                            "description": "The mode of transport to filter by (e.g., 'Air', 'Sea').",
                        }
                    },
                    "required": ["mode"],
                },
            },
        }


class CreateOutboundOrder(Tool):
    """A utility for generating a new outbound order within the system."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        customer_name: str = None,
        destination_city: str = None,
        priority_level: str = None,
        line_items: list[dict[str, Any]] = None
    ) -> str:
        if not all([customer_name, destination_city, priority_level, line_items]):
            payload = {
                "error": "customer_name, destination_city, priority_level, and line_items are required."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        outbound_orders = data.get("outbound_orders", {}).values()
        max_id = max(
            (int(o.get("order_id", "ORD-0").split("-")[1]) for o in outbound_orders.values()),
            default=0,
        )
        new_order_id = f"ORD-{max_id + 1:04d}"
        customer_details = next(
            (o for o in outbound_orders.values() if o.get("customer_name") == customer_name), {}
        )
        new_order = {
            "order_id": new_order_id,
            "sales_order_number": f"SO-2025-{max_id + 1:04d}",
            "customer_id": customer_details.get("customer_id"),
            "customer_name": customer_name,
            "customer_address": customer_details.get("customer_address"),
            "customer_city": destination_city,
            "customer_country": customer_details.get("customer_country"),
            "destination_address": customer_details.get("customer_address"),
            "destination_city": destination_city,
            "destination_country": customer_details.get("customer_country"),
            "status": "Pending",
            "number_of_line_items": len(line_items),
            "total_units": sum(item.get("quantity", 0) for item in line_items.values()),
            "priority_level": priority_level,
            "line_items": line_items,
            "warehouse_id": None,
            "actual_ship_date": None,
            "carrier_name": None,
            "tracking_number": None,
        }
        outbound_data["orders"][order_id] = new_order
        payload = {"order_id": new_order_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOutboundOrder",
                "description": "Creates a new outbound customer order with a 'Pending' status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_name": {"type": "string"},
                        "destination_city": {"type": "string"},
                        "priority_level": {"type": "string"},
                        "line_items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                    },
                    "required": [
                        "customer_name",
                        "destination_city",
                        "priority_level",
                        "line_items",
                    ],
                },
            },
        }


class ShipOutboundOrder(Tool):
    """Modifies an order to 'Shipped', designates a carrier, distributes inventory, and computes shipping expenses."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, warehouse_id: str = None, carrier_scac: str = None) -> str:
        if not all([order_id, warehouse_id, carrier_scac]):
            payload = {"error": "order_id, warehouse_id, and carrier_scac are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        order_to_update = next(
            (
                o
                for o in data.get("outbound_orders", {}).values()
                if o.get("order_id") == order_id
            ),
            None,
        )
        if not order_to_update:
            payload = {"error": f"Order '{order_id}' not found."}
            out = json.dumps(payload, indent=2)
            return out

        #--- NEW LOGIC INITIATION ---
        total_weight_kg = 0
        line_items = order_to_update.get("line_items", [])
        product_master = data.get("product_master", {}).values()
        for item in line_items:
            product = next(
                (p for p in product_master.values() if p.get("sku") == item["sku"]), None
            )
            if product:
                total_weight_kg += product.get("weight_kg", 0) * item["quantity"]

        #Predictable shipping cost assessment
        shipping_cost = round((total_weight_kg * 2.5) + 100, 2)
        order_to_update["shipping_cost"] = shipping_cost
        #--- NEW LOGIC CONCLUSION ---

        order_to_update["status"] = "Shipped"
        order_to_update["warehouse_id"] = warehouse_id
        carrier_name = next(
            (
                c.get("carrier_name")
                for c in data.get("carriers", {}).values()
                if c.get("scac") == carrier_scac
            ),
            "Unknown",
        )
        order_to_update["carrier_name"] = carrier_name
        order_to_update["carrier_scac"] = carrier_scac
        order_id_number = order_id.split("-")[1]
        order_to_update["tracking_number"] = f"{carrier_scac}-{order_id_number}"

        for item in line_items:
            for inv_record in data.get("inventory", {}).values():
                if (
                    inv_record.get("sku") == item.get("sku")
                    and inv_record.get("warehouse_id") == warehouse_id
                ):
                    inv_record["quantity_available"] -= item.get("quantity", 0)
                    inv_record["quantity_allocated"] += item.get("quantity", 0)
                    break
        payload = order_to_update
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ShipOutboundOrder",
                "description": "Updates an order's status to 'Shipped', adjusts inventory, and assigns a carrier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "warehouse_id": {"type": "string"},
                        "carrier_scac": {"type": "string"},
                    },
                    "required": ["order_id", "warehouse_id", "carrier_scac"],
                },
            },
        }


class FindInboundShipment(Tool):
    """Locates a particular inbound shipment according to supplier and origin."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_name: str = None, origin_city: str = None, status: str = None) -> str:
        if not all([supplier_name, origin_city]):
            payload = {"error": "supplier_name and origin_city are required arguments."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        shipments = data.get("inbound_shipments", {}).values()
        results = [
            s
            for s in shipments.values() if s.get("supplier_name") == supplier_name
            and s.get("origin_city") == origin_city
            and (not status or s.get("status") == status)
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindInboundShipment",
                "description": "Finds inbound shipments from a specific supplier and origin city, optionally filtering by status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_name": {"type": "string"},
                        "origin_city": {"type": "string"},
                        "status": {
                            "type": "string",
                            "description": "Optional status to filter by (e.g., 'In Transit').",
                        },
                    },
                    "required": ["supplier_name", "origin_city"],
                },
            },
        }


class UpdateShipmentStatus(Tool):
    """Modifies the status and remarks of a specific inbound shipment."""

    @staticmethod
    def invoke(data: dict[str, Any], shipment_id: str = None, new_status: str = None, notes: str = None) -> str:
        if not all([shipment_id, new_status, notes]):
            payload = {"error": "shipment_id, new_status, and notes are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        shipment_to_update = next(
            (
                s
                for s in data.get("inbound_shipments", {}).values()
                if s.get("shipment_id") == shipment_id
            ),
            None,
        )
        if not shipment_to_update:
            payload = {"error": f"Shipment '{shipment_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        shipment_to_update["status"] = new_status
        shipment_to_update["notes"] = notes
        payload = shipment_to_update
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateShipmentStatus",
                "description": "Updates the status and notes for a specific inbound shipment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string"},
                        "new_status": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["shipment_id", "new_status", "notes"],
                },
            },
        }


class LogSupplierPerformanceIssue(Tool):
    """Records a performance concern related to a supplier's record."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, issue_code: str = None, shipment_id: str = None) -> str:
        if not all([supplier_id, issue_code]):
            payload = {"error": "supplier_id and issue_code are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        supplier_to_update = next(
            (
                s
                for s in data.get("supplier_master", {}).values()
                if s.get("supplier_id") == supplier_id
            ),
            None,
        )
        if not supplier_to_update:
            payload = {"error": f"Supplier '{supplier_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if "performance_logs" not in supplier_to_update:
            supplier_to_update["performance_logs"] = []
        log_entry = {"issue_code": issue_code, "related_shipment": shipment_id}
        supplier_to_update["performance_logs"].append(log_entry)
        payload = supplier_to_update
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogSupplierPerformanceIssue",
                "description": "Logs a performance issue against a supplier's record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"},
                        "issue_code": {"type": "string"},
                        "shipment_id": {"type": "string"},
                    },
                    "required": ["supplier_id", "issue_code"],
                },
            },
        }


class GetWarehouseDetails(Tool):
    """Fetches all information for a specific warehouse using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_name: str = None) -> str:
        if not warehouse_name:
            payload = {"error": "warehouse_name is required."}
            out = json.dumps(payload, indent=2)
            return out
        warehouse = next(
            (
                w
                for w in data.get("warehouses", {}).values()
                if w.get("warehouse_name") == warehouse_name
            ),
            None,
        )
        if not warehouse:
            payload = {"error": f"Warehouse '{warehouse_name}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = warehouse
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWarehouseDetails",
                "description": "Retrieves all details for a specific warehouse by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"warehouse_name": {"type": "string"}},
                    "required": ["warehouse_name"],
                },
            },
        }


class InitiateWarehouseTransfer(Tool):
    """Facilitates a stock transfer between two warehouses, modifying inventory levels."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, quantity: int = None, from_warehouse_id: str = None, to_warehouse_id: str = None) -> str:
        if not all([sku, quantity, from_warehouse_id, to_warehouse_id]):
            payload = {
                    "error": "sku, quantity, from_warehouse_id, and to_warehouse_id are required."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        inventory = data.get("inventory", {}).values()
        source_inv = next(
            (
                i
                for i in inventory.values() if i.get("sku") == sku and i.get("warehouse_id") == from_warehouse_id
            ),
            None,
        )
        dest_inv = next(
            (
                i
                for i in inventory.values() if i.get("sku") == sku and i.get("warehouse_id") == to_warehouse_id
            ),
            None,
        )
        if not source_inv:
            payload = {
                    "error": f"SKU {sku} not found in source warehouse {from_warehouse_id}."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        if source_inv["quantity_available"] < quantity:
            payload = {"error": f"Insufficient available stock in {from_warehouse_id}."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        source_inv["quantity_available"] -= quantity
        source_inv["quantity_allocated"] += quantity
        if dest_inv:
            dest_inv["quantity_inbound"] += quantity
        else:
            product_details = next(
                (p for p in data.get("product_master", {}).values() if p.get("sku") == sku), {}
            )
            new_inv_record = {
                "inventory_id": f"INV-{random.randint(10000, 99999)}",
                "sku": sku,
                "product_name": product_details.get("product_name"),
                "warehouse_id": to_warehouse_id,
                "quantity_on_hand": 0,
                "quantity_available": 0,
                "quantity_allocated": 0,
                "quantity_inbound": quantity,
                "quantity_damaged": 0,
            }
            data["inventory"][inventory_id] = new_inv_record
        payload = {
                "status": "success",
                "transfer_id": f"T-{from_warehouse_id}-{to_warehouse_id}-{random.randint(1000, 9999)}",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InitiateWarehouseTransfer",
                "description": "Initiates a stock transfer of a specific SKU from a source warehouse to a destination warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string"},
                        "quantity": {"type": "integer"},
                        "from_warehouse_id": {"type": "string"},
                        "to_warehouse_id": {"type": "string"},
                    },
                    "required": [
                        "sku",
                        "quantity",
                        "from_warehouse_id",
                        "to_warehouse_id",
                    ],
                },
            },
        }


class UpdateWarehouseNotes(Tool):
    """Inserts or replaces notes for a particular warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str = None, notes: str = None) -> str:
        if not all([warehouse_id, notes]):
            payload = {"error": "warehouse_id and notes are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        warehouse = next(
            (
                w
                for w in data.get("warehouses", {}).values()
                if w.get("warehouse_id") == warehouse_id
            ),
            None,
        )
        if not warehouse:
            payload = {"error": f"Warehouse '{warehouse_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        new_note = f"{notes}"
        if "notes" in warehouse and warehouse["notes"]:
            warehouse["notes"] += f"\n{new_note}"
        else:
            warehouse["notes"] = new_note
        payload = warehouse
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateWarehouseNotes",
                "description": "Adds a new note to a specific warehouse's record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["warehouse_id", "notes"],
                },
            },
        }


class FindOrdersByCarrier(Tool):
    """Identifies all outbound orders allocated to a specific carrier, filtered by status."""

    @staticmethod
    def invoke(data: dict[str, Any], carrier_name: str = None, status: str = None) -> str:
        if not carrier_name:
            payload = {"error": "carrier_name is a required argument."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        orders = data.get("outbound_orders", {}).values()
        results = [
            o
            for o in orders.values() if o.get("carrier_name") == carrier_name
            and (not status or o.get("status") == status)
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindOrdersByCarrier",
                "description": "Finds all outbound orders assigned to a specific carrier, optionally filtering by status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_name": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["carrier_name"],
                },
            },
        }


class ReassignOrderCarrier(Tool):
    """Modifies the designated carrier for a particular outbound order."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, new_carrier_scac: str = None) -> str:
        if not all([order_id, new_carrier_scac]):
            payload = {"error": "order_id and new_carrier_scac are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        order = next(
            (
                o
                for o in data.get("outbound_orders", {}).values()
                if o.get("order_id") == order_id
            ),
            None,
        )
        if not order:
            payload = {"error": f"Order '{order_id}' not found."}
            out = json.dumps(payload, indent=2)
            return out
        new_carrier = next(
            (c for c in data.get("carriers", {}).values() if c.get("scac") == new_carrier_scac),
            None,
        )
        if not new_carrier:
            payload = {"error": f"New carrier with SCAC '{new_carrier_scac}' not found."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        order["carrier_name"] = new_carrier.get("carrier_name")
        order["carrier_scac"] = new_carrier.get("scac")
        order_id_number = order_id.split("-")[1]
        order["tracking_number"] = f"{new_carrier.get('scac')}-{order_id_number}"
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReassignOrderCarrier",
                "description": "Changes the assigned carrier for a specific outbound order and generates a new tracking number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "new_carrier_scac": {"type": "string"},
                    },
                    "required": ["order_id", "new_carrier_scac"],
                },
            },
        }


class LogAuditTrail(Tool):
    """Records a structured audit event to monitor significant system activities."""

    @staticmethod
    def invoke(data: dict[str, Any], audit_event: str = None, subject_id: str = None, outcome_code: str = None, outcome_details: dict = None) -> str:
        if not all([audit_event, subject_id, outcome_code]):
            payload = {"error": "audit_event, subject_id, and outcome_code are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if "audit_log" not in data:
            data["audit_log"] = []

        log_entry = {
            "event_type": audit_event,
            "subject_id": subject_id,
            "outcome_code": outcome_code,
            "outcome_details": outcome_details,
        }
        data["audit_log"].append(log_entry)
        payload = log_entry
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogAuditTrail",
                "description": "Logs a structured audit event for tracking important system actions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_event": {
                            "type": "string",
                            "description": "The type of event being logged (e.g., 'PRODUCT_RISK_AUDIT').",
                        },
                        "subject_id": {
                            "type": "string",
                            "description": "The ID of the primary entity this event relates to (e.g., a SKU or Order ID).",
                        },
                        "outcome_code": {
                            "type": "string",
                            "description": "A fixed code representing the outcome (e.g., 'RISK_IDENTIFIED').",
                        },
                        "outcome_details": {
                            "type": "object",
                            "description": "A dictionary of key-value pairs containing specific data about the outcome.",
                        },
                    },
                    "required": ["audit_event", "subject_id", "outcome_code"],
                },
            },
        }


class UpdateCarrierStatus(Tool):
    """Modifies the status of a carrier."""

    @staticmethod
    def invoke(data: dict[str, Any], carrier_name: str = None, status: str = None) -> str:
        if not all([carrier_name, status]):
            payload = {"error": "carrier_name and status are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        carrier_to_update = next(
            (
                c
                for c in data.get("carriers", {}).values()
                if c.get("carrier_name") == carrier_name
            ),
            None,
        )
        if not carrier_to_update:
            payload = {"error": f"Carrier '{carrier_name}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        carrier_to_update["active_status"] = status
        payload = {
                "carrier_id": carrier_to_update.get("carrier_id"),
                "carrier_name": carrier_name,
                "new_status": status,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCarrierStatus",
                "description": "Updates the operational status of a carrier (e.g., True, False, 'Under Review').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_name": {"type": "string"},
                        "status": {
                            "type": "string",
                            "description": "The new status to set for the carrier.",
                        },
                    },
                    "required": ["carrier_name", "status"],
                },
            },
        }


#--- NEW Retrieval Tools ---


class GetOutboundOrderDetails(Tool):
    """Fetches complete details for a single outbound order using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None) -> str:
        if not order_id:
            payload = {"error": "order_id is required."}
            out = json.dumps(payload, indent=2)
            return out
        order = next(
            (
                o
                for o in data.get("outbound_orders", {}).values()
                if o.get("order_id") == order_id
            ),
            None,
        )
        if not order:
            payload = {"error": f"Order '{order_id}' not found."}
            out = json.dumps(payload, indent=2)
            return out
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOutboundOrderDetails",
                "description": "Retrieves the full details for a single outbound order by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class GetInventoryDetails(Tool):
    """Obtains a single inventory record for a SKU located at a specific warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, warehouse_id: str = None) -> str:
        if not all([sku, warehouse_id]):
            payload = {"error": "sku and warehouse_id are required."}
            out = json.dumps(payload, indent=2)
            return out
        inventory_record = next(
            (
                i
                for i in data.get("inventory", {}).values()
                if i.get("sku") == sku and i.get("warehouse_id") == warehouse_id
            ),
            None,
        )
        if not inventory_record:
            payload = {
                    "error": f"Inventory for SKU '{sku}' not found at warehouse '{warehouse_id}'."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = inventory_record
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryDetails",
                "description": "Retrieves a single inventory record for a SKU at a specific warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string"},
                        "warehouse_id": {"type": "string"},
                    },
                    "required": ["sku", "warehouse_id"],
                },
            },
        }


class GetCarrierDetails(Tool):
    """Fetches complete details for a single carrier using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], carrier_name: str = None) -> str:
        if not carrier_name:
            payload = {"error": "carrier_name is required."}
            out = json.dumps(payload, indent=2)
            return out
        carrier = next(
            (
                c
                for c in data.get("carriers", {}).values()
                if carrier_name.lower() in c.get("carrier_name", "").lower()
            ),
            None,
        )
        if not carrier:
            payload = {"error": f"Carrier '{carrier_name}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = carrier
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCarrierDetails",
                "description": "Retrieves the full details for a single carrier by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"carrier_name": {"type": "string"}},
                    "required": ["carrier_name"],
                },
            },
        }


class UpdateInventoryDamageStatus(Tool):
    """Modifies the inventory count to transfer a quantity of units from 'available' to 'damaged'."""

    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None, damaged_quantity: int = None) -> str:
        if not all([inventory_id, damaged_quantity]):
            payload = {"error": "inventory_id and damaged_quantity are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        inventory_record = next(
            (
                i
                for i in data.get("inventory", {}).values()
                if i.get("inventory_id") == inventory_id
            ),
            None,
        )

        if not inventory_record:
            payload = {"error": f"Inventory record '{inventory_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if damaged_quantity > 0:
            if damaged_quantity > inventory_record.get("quantity_available", 0):
                payload = {
                        "error": f"Cannot mark {damaged_quantity} as damaged, only {inventory_record.get('quantity_available')} are available."
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            inventory_record["quantity_available"] -= damaged_quantity
            inventory_record["quantity_damaged"] += damaged_quantity
        elif damaged_quantity < 0:
            abs_damaged_quantity = abs(damaged_quantity)

            inventory_record["quantity_available"] += abs_damaged_quantity

            if abs_damaged_quantity > inventory_record.get("quantity_damaged", 0):
                inventory_record["quantity_damaged"] = 0
            else:
                inventory_record["quantity_damaged"] -= abs_damaged_quantity
        else:
            pass
        payload = inventory_record
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryDamageStatus",
                "description": "Updates an inventory record to reflect damaged goods by moving a quantity from 'available' to 'damaged'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "The ID of the inventory record to update.",
                        },
                        "damaged_quantity": {
                            "type": "integer",
                            "description": "The number of units to mark as damaged.",
                        },
                    },
                    "required": ["inventory_id", "damaged_quantity"],
                },
            },
        }


class CreatePurchaseOrder(Tool):
    """Generates a new purchase order along with a corresponding 'Planned' inbound shipment."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, line_items: list = None, priority: str = None) -> str:
        if not all([supplier_id, line_items, priority]):
            payload = {"error": "supplier_id, line_items, and priority are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        supplier = next(
            (
                s
                for s in data.get("supplier_master", {}).values()
                if s.get("supplier_id") == supplier_id
            ),
            None,
        )
        if not supplier:
            payload = {"error": f"Supplier '{supplier_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        inbound_shipments = data.get("inbound_shipments", {}).values()

        current_year_str = str(get_current_year())

        #Select POs exclusively for the current year
        pos_this_year = [
            s
            for s in inbound_shipments.values() if s.get("purchase_order_number", "").startswith(f"PO-{current_year_str}")
        ]

        #Identify the highest sequence number for the current year
        max_seq_num_this_year = 0
        if pos_this_year:
            max_seq_num_this_year = max(
                (
                    int(po.get("purchase_order_number").split("-")[2])
                    for po in pos_this_year
                ),
                default=0,
            )

        new_seq_num = max_seq_num_this_year + 1
        new_po_number = f"PO-{current_year_str}-{new_seq_num:04d}"
        #--- FINALIZED LOGIC END ---

        max_ship_id = max(
            (
                int(s.get("shipment_id", "SHIP-0").split("-")[1])
                for s in inbound_shipments.values()
            ),
            default=0,
        )
        new_shipment_id = f"SHIP-{max_ship_id + 1:04d}"

        first_sku = line_items[0]["sku"]
        dest_warehouse = next(
            (i for i in data.get("inventory", {}).values() if i.get("sku") == first_sku), {}
        )

        new_shipment = {
            "shipment_id": new_shipment_id,
            "purchase_order_number": new_po_number,
            "supplier_id": supplier_id,
            "supplier_name": supplier.get("supplier_name"),
            "origin_address": supplier.get("contact_information", {}).values()
            .get("address", {}).values()
            .get("street"),
            "origin_city": supplier.get("contact_information", {}).values()
            .get("address", {}).values()
            .get("city"),
            "origin_country": supplier.get("contact_information", {}).values()
            .get("address", {}).values()
            .get("country"),
            "destination_warehouse_id": dest_warehouse.get("warehouse_id"),
            "destination_warehouse_name": dest_warehouse.get("warehouse_name"),
            "status": "Planned",
            "priority_level": priority,
        }

        inbound_data["shipments"][shipment_id] = new_shipment
        payload = {"status": "success", "purchase_order_number": new_po_number}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePurchaseOrder",
                "description": "Creates a new purchase order for a supplier, which also generates a new 'Planned' inbound shipment record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier for the order.",
                        },
                        "line_items": {
                            "type": "array",
                            "description": "A list of products to order.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "priority": {
                            "type": "string",
                            "description": "The priority level for this order (e.g., 'High').",
                        },
                    },
                    "required": ["supplier_id", "line_items", "priority"],
                },
            },
        }


class GetPurchaseOrderDetails(Tool):
    """Fetches details of an inbound shipment using its Purchase Order number."""

    @staticmethod
    def invoke(data: dict[str, Any], po_number: str = None) -> str:
        if not po_number:
            payload = {"error": "po_number is required."}
            out = json.dumps(payload, indent=2)
            return out

        shipment = next(
            (
                s
                for s in data.get("inbound_shipments", {}).values()
                if s.get("purchase_order_number") == po_number
            ),
            None,
        )

        if not shipment:
            payload = {"error": f"Shipment for Purchase Order '{po_number}' not found."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = shipment
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPurchaseOrderDetails",
                "description": "Retrieves the shipment details associated with a given Purchase Order (PO) number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "po_number": {
                            "type": "string",
                            "description": "The Purchase Order number to search for.",
                        }
                    },
                    "required": ["po_number"],
                },
            },
        }


class GetOutboundOrderDetailsBySo(Tool):
    """Obtains order details by referencing the Sales Order (SO) number."""

    @staticmethod
    def invoke(data: dict[str, Any], sales_order_number: str = None) -> str:
        if not sales_order_number:
            payload = {"error": "sales_order_number is a required argument."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        order = next(
            (
                o
                for o in data.get("outbound_orders", {}).values()
                if o.get("sales_order_number") == sales_order_number
            ),
            None,
        )

        if not order:
            payload = {
                    "error": f"Order with Sales Order number '{sales_order_number}' not found."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOutboundOrderDetailsBySo",
                "description": "Retrieves the full details for a single outbound order by its Sales Order (SO) number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sales_order_number": {
                            "type": "string",
                            "description": "The Sales Order number (e.g., 'SO-2024-0001').",
                        }
                    },
                    "required": ["sales_order_number"],
                },
            },
        }


class CreateReturnAuthorization(Tool):
    """Generates a Return Merchandise Authorization (RMA) record for a customer return."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, line_items: list = None, reason: str = None) -> str:
        if not all([order_id, line_items, reason]):
            payload = {"error": "order_id, line_items, and reason are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if "rma_authorizations" not in data:
            data["rma_authorizations"] = []

        max_rma_num = max(
            (
                int(r.get("rma_id", "RMA-1000").split("-")[1])
                for r in data["rma_authorizations"].values()
            ),
            default=1000,
        )
        new_rma_id = f"RMA-{max_rma_num + 1}"

        rma_record = {
            "rma_id": new_rma_id,
            "order_id": order_id,
            "line_items_to_return": line_items,
            "reason": reason,
            "status": "Authorized",
        }
        data["rma_authorizations"].append(rma_record)
        payload = {"rma_id": new_rma_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReturnAuthorization",
                "description": "Creates a Return Merchandise Authorization (RMA) to formally approve a customer's return request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The original order ID the return is associated with.",
                        },
                        "line_items": {
                            "type": "array",
                            "description": "A list of products being returned.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the return provided by the customer.",
                        },
                    },
                    "required": ["order_id", "line_items", "reason"],
                },
            },
        }


class CreateInboundReturnShipment(Tool):
    """Establishes a new 'Planned' inbound shipment specifically for a customer return."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        rma_id: str = None, 
        from_customer_id: str = None, 
        to_warehouse_id: str = None, 
        carrier_scac: str = None
    ) -> str:
        if not all([rma_id, from_customer_id, to_warehouse_id, carrier_scac]):
            payload = {
                "error": "rma_id, from_customer_id, to_warehouse_id, and carrier_scac are required."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        inbound_shipments = data.get("inbound_shipments", {}).values()
        max_ship_id = max(
            (
                int(s.get("shipment_id", "SHIP-0").split("-")[1])
                for s in inbound_shipments.values()
            ),
            default=0,
        )
        new_shipment_id = f"SHIP-{max_ship_id + 1:04d}"

        customer = next(
            (
                o
                for o in data.get("outbound_orders", {}).values()
                if o.get("customer_id") == from_customer_id
            ),
            {},
        )
        warehouse = next(
            (
                w
                for w in data.get("warehouses", {}).values()
                if w.get("warehouse_id") == to_warehouse_id
            ),
            {},
        )

        new_shipment = {
            "shipment_id": new_shipment_id,
            "purchase_order_number": rma_id,  # Employing RMA as the reference identifier
            "supplier_id": from_customer_id,
            "supplier_name": "CUSTOMER_RETURN",
            "origin_address": customer.get("customer_address"),
            "origin_city": customer.get("customer_city"),
            "origin_country": customer.get("customer_country"),
            "destination_warehouse_id": to_warehouse_id,
            "destination_warehouse_name": warehouse.get("warehouse_name"),
            "carrier_name": next(
                (
                    c.get("carrier_name")
                    for c in data.get("carriers", {}).values()
                    if c.get("scac") == carrier_scac
                ),
                "Unknown",
            ),
            "carrier_scac": carrier_scac,
            "status": "Planned",
            "priority_level": "Medium",
        }
        inbound_data["shipments"][shipment_id] = new_shipment
        payload = new_shipment
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInboundReturnShipment",
                "description": "Creates a new 'Planned' inbound shipment to track the physical return of goods from a customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rma_id": {
                            "type": "string",
                            "description": "The RMA number authorizing this return shipment.",
                        },
                        "from_customer_id": {
                            "type": "string",
                            "description": "The ID of the customer returning the items.",
                        },
                        "to_warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse designated to receive the return.",
                        },
                        "carrier_scac": {
                            "type": "string",
                            "description": "The SCAC code of the carrier handling the return.",
                        },
                    },
                    "required": [
                        "rma_id",
                        "from_customer_id",
                        "to_warehouse_id",
                        "carrier_scac",
                    ],
                },
            },
        }


class UpdateOutboundOrderStatus(Tool):
    """Modifies the status of a current outbound order."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, new_status: str = None) -> str:
        if not all([order_id, new_status]):
            payload = {"error": "order_id and new_status are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        order = next(
            (
                o
                for o in data.get("outbound_orders", {}).values()
                if o.get("order_id") == order_id
            ),
            None,
        )
        if not order:
            payload = {"error": f"Order '{order_id}' not found."}
            out = json.dumps(payload, indent=2)
            return out

        if new_status == "Cancelled":
            for item in order.get("line_items", []):
                for inv_record in data.get("inventory", {}).values():
                    if inv_record.get("sku") == item.get("sku") and inv_record.get(
                        "warehouse_id"
                    ) == order.get("warehouse_id"):
                        inv_record["quantity_available"] += item.get("quantity", 0)
                        inv_record["quantity_allocated"] -= item.get("quantity", 0)
                        break

        order["status"] = new_status
        return_related_statuses = [
            "Returned",
            "Partially Returned",
            "Cancelled - Damaged Stock",  #Or other statuses that involve return/cancellation affecting returns
            "Processing Return",
            "Incorrect Item Returned",
            "Cancelled - Force Majeure",
            "On Hold - Fraud Investigation",  #Depending on the fraud/return policy
            "Cancelled - Expired Stock",
            "Cancelled",  #If a generic cancellation also involves a return
        ]
        if new_status in return_related_statuses:
            order["return_status"] = new_status
        else:
            order["return_status"] = "None"
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOutboundOrderStatus",
                "description": "Updates the status of an existing outbound order (e.g., to 'Partially Returned').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status to set for the order.",
                        },
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }


class IssueCustomerCreditMemo(Tool):
    """Generates a credit memo for a customer and records the financial transaction."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, customer_id: str = None, returned_items: list = None) -> str:
        if not all([order_id, customer_id, returned_items]):
            payload = {"error": "order_id, customer_id, and returned_items are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Predictable ID creation according to policy
        order_id_num = order_id.split("-")[1]
        credit_memo_id = f"CM-{order_id_num}"

        total_credit_value = 0
        product_master = data.get("product_master", {}).values()
        for item in returned_items:
            product = next(
                (p for p in product_master.values() if p.get("sku") == item["sku"]), None
            )
            if product:
                total_credit_value += product.get("unit_price", 0) * item["quantity"]

        if "credit_memos" not in data:
            data["credit_memos"] = []

        credit_memo = {
            "credit_memo_id": credit_memo_id,
            "original_order_id": order_id,
            "customer_id": customer_id,
            "credited_items": returned_items,
            "total_credit_value": round(total_credit_value, 2),
            "currency": "USD",
            "status": "Issued",
        }
        data["credit_memos"][credit_memo_id] = credit_memo
        payload = credit_memo
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "IssueCustomerCreditMemo",
                "description": "Issues a credit memo for a customer for returned goods and logs the financial transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The original order ID that is being credited.",
                        },
                        "customer_id": {
                            "type": "string",
                            "description": "The ID of the customer receiving the credit.",
                        },
                        "returned_items": {
                            "type": "array",
                            "description": "A list of items for which credit is being issued.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                    },
                    "required": ["order_id", "customer_id", "returned_items"],
                },
            },
        }


class GetReturnAuthorizationDetails(Tool):
    """Fetches details for a particular RMA."""

    @staticmethod
    def invoke(data: dict[str, Any], rma_id: str = None) -> str:
        if not rma_id:
            payload = {"error": "rma_id is required."}
            out = json.dumps(payload, indent=2)
            return out

        rma = next(
            (
                r
                for r in data.get("rma_authorizations", {}).values()
                if r.get("rma_id") == rma_id
            ),
            None,
        )
        if not rma:
            payload = {"error": f"RMA '{rma_id}' not found."}
            out = json.dumps(payload, indent=2)
            return out
        payload = rma
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReturnAuthorizationDetails",
                "description": "Retrieves the details of a specific Return Merchandise Authorization (RMA) by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rma_id": {
                            "type": "string",
                            "description": "The RMA ID to search for.",
                        }
                    },
                    "required": ["rma_id"],
                },
            },
        }


class GetCreditMemoDetails(Tool):
    """Obtains details for a specific credit memo."""

    @staticmethod
    def invoke(data: dict[str, Any], credit_memo_id: str = None) -> str:
        if not credit_memo_id:
            payload = {"error": "credit_memo_id is required."}
            out = json.dumps(payload, indent=2)
            return out

        memo = next(
            (
                m
                for m in data.get("credit_memos", {}).values()
                if m.get("credit_memo_id") == credit_memo_id
            ),
            None,
        )
        if not memo:
            payload = {"error": f"Credit Memo '{credit_memo_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = memo
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCreditMemoDetails",
                "description": "Retrieves the details of a specific credit memo by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "credit_memo_id": {
                            "type": "string",
                            "description": "The Credit Memo ID to search for.",
                        }
                    },
                    "required": ["credit_memo_id"],
                },
            },
        }


class GetKitComponents(Tool):
    """
    Fetches the list of component SKUs and their quantities for a specified virtual kit,
    identified by either SKU or a user-friendly name.
    """

    KITS_DATABASE = {
        "KIT-ROBO-S1": {
            "kit_name": "Basic Robotic Starter Kit",
            "components": [
                {
                    "sku": "TECH-ROBO-N14",
                    "quantity": 1,
                    "product_name": "Articulated Robotic Arm",
                },
                {
                    "sku": "TECH-BATT-Q17",
                    "quantity": 2,
                    "product_name": "Lithium‑Ion Battery Pack",
                },
            ],
        }
    }

    @staticmethod
    def invoke(data: dict[str, Any], kit_sku: str = None, kit_name: str = None) -> str:
        if not kit_sku and not kit_name:
            payload = {"error": "You must provide either 'kit_sku' or 'kit_name'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        kit_data = GetKitComponents.KITS_DATABASE.get(kit_sku) if kit_sku else None
        if not kit_data and kit_name:
            kit_data = next(
                (
                    v
                    for v in GetKitComponents.KITS_DATABASE.values()
                    if v["kit_name"].lower() == kit_name.lower()
                ),
                None,
            )

        if not kit_data:
            missing = f"SKU '{kit_sku}'" if kit_sku else f"name '{kit_name}'"
            payload = {"error": f"Kit with {missing} not found."}
            out = json.dumps(payload, indent=2)
            return out
        payload = kit_data["components"]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetKitComponents",
                "description": (
                    "Retrieves the bill of materials (component SKUs and their "
                    "quantities) for a virtual kit identified by SKU or name."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kit_sku": {
                            "type": "string",
                            "description": "The SKU of the virtual kit (e.g., 'KIT-ROBO-S1').",
                        },
                        "kit_name": {
                            "type": "string",
                            "description": "The friendly name of the virtual kit "
                            "(e.g., 'Basic Robotic Starter Kit').",
                        },
                    },
                    #No field is mandatory; at least one is required in the logic
                    "required": [],
                },
            },
        }


TOOLS = [
    GetProductDetails(),
    ListWarehousesByCapability(),
    GetInventoryBySku(),
    ListCarriersByMode(),
    CreateOutboundOrder(),
    ShipOutboundOrder(),
    FindInboundShipment(),
    UpdateShipmentStatus(),
    LogSupplierPerformanceIssue(),
    GetWarehouseDetails(),
    InitiateWarehouseTransfer(),
    UpdateWarehouseNotes(),
    FindOrdersByCarrier(),
    ReassignOrderCarrier(),
    LogAuditTrail(),
    UpdateCarrierStatus(),
    GetOutboundOrderDetails(),
    GetInventoryDetails(),
    GetCarrierDetails(),
    UpdateInventoryDamageStatus(),
    CreatePurchaseOrder(),
    GetPurchaseOrderDetails(),
    GetOutboundOrderDetailsBySo(),
    CreateReturnAuthorization(),
    CreateInboundReturnShipment(),
    UpdateOutboundOrderStatus(),
    IssueCustomerCreditMemo(),
    GetReturnAuthorizationDetails(),
    GetCreditMemoDetails(),
    GetKitComponents(),
]
