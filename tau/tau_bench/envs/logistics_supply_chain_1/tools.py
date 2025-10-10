import json
import random
from typing import Dict, Any, List, Optional, Union
from domains.dto import Tool

def get_current_year() -> int:
    return 2025

class GetProductDetails(Tool):
    """A tool to retrieve all master data for a specific product by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_name = kwargs.get('product_name')
        if not product_name:
            return json.dumps({"error": "product_name is a required argument."}, indent=2)
        product_master = data.get('product_master', [])
        product = next((p for p in product_master if p.get('product_name') == product_name), None)
        if product:
            return json.dumps(product, indent=2)
        return json.dumps({"error": f"Product '{product_name}' not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_product_details", "description": "Retrieves all master data for a specific product by its exact name.", "parameters": {"type": "object", "properties": {"product_name": {"type": "string", "description": "The full, exact name of the product to search for."}}, "required": ["product_name"]}}}

class ListWarehousesByCapability(Tool):
    """A tool to find all warehouses that hold a specific certification."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        certification = kwargs.get('certification')
        if not certification:
            return json.dumps({"error": "certification is a required argument."}, indent=2)
        warehouses = data.get('warehouses', [])
        matching_warehouses = [wh for wh in warehouses if certification in wh.get('certifications', [])]
        return json.dumps(matching_warehouses, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_warehouses_by_capability", "description": "Finds all warehouses that hold a specific certification.", "parameters": {"type": "object", "properties": {"certification": {"type": "string", "description": "The certification to filter warehouses by (e.g., 'FDA Registered')."}}, "required": ["certification"]}}}

class GetInventoryBySku(Tool):
    """A tool to retrieve all inventory records for a given SKU across all warehouses."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get('sku')
        if not sku:
            return json.dumps({"error": "sku is a required argument."}, indent=2)
        inventory = data.get('inventory', [])
        sku_inventory = [item for item in inventory if item.get('sku') == sku]
        return json.dumps(sku_inventory, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_inventory_by_sku", "description": "Retrieves all inventory records for a specific SKU across all warehouses.", "parameters": {"type": "object", "properties": {"sku": {"type": "string", "description": "The SKU to search for inventory records of."}}, "required": ["sku"]}}}

class ListCarriersByMode(Tool):
    """A tool to find all active carriers that support a specific mode of transport."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        mode = kwargs.get('mode')
        if not mode:
            return json.dumps({"error": "mode is a required argument."}, indent=2)
        carriers = data.get('carriers', [])
        matching_carriers = [c for c in carriers if c.get('active_status') is True and mode.title() in c.get('supported_modes', [])]
        return json.dumps(matching_carriers, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_carriers_by_mode", "description": "Finds all active carriers for a given transportation mode.", "parameters": {"type": "object", "properties": {"mode": {"type": "string", "description": "The mode of transport to filter by (e.g., 'Air', 'Sea')."}}, "required": ["mode"]}}}

class CreateOutboundOrder(Tool):
    """A tool to create a new outbound order in the system."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_name = kwargs.get('customer_name')
        destination_city = kwargs.get('destination_city')
        priority_level = kwargs.get('priority_level')
        line_items = kwargs.get('line_items')
        if not all([customer_name, destination_city, priority_level, line_items]):
            return json.dumps({"error": "customer_name, destination_city, priority_level, and line_items are required."}, indent=2)
        outbound_orders = data.get('outbound_orders', [])
        max_id = max((int(o.get('order_id', 'ORD-0').split('-')[1]) for o in outbound_orders), default=0)
        new_order_id = f"ORD-{max_id + 1:04d}"
        customer_details = next((o for o in outbound_orders if o.get('customer_name') == customer_name), {})
        new_order = {"order_id": new_order_id, "sales_order_number": f"SO-2025-{max_id + 1:04d}", "customer_id": customer_details.get("customer_id"), "customer_name": customer_name, "customer_address": customer_details.get("customer_address"), "customer_city": destination_city, "customer_country": customer_details.get("customer_country"), "destination_address": customer_details.get("customer_address"), "destination_city": destination_city, "destination_country": customer_details.get("customer_country"), "status": "Pending", "number_of_line_items": len(line_items), "total_units": sum(item.get('quantity', 0) for item in line_items), "priority_level": priority_level, "line_items": line_items, "warehouse_id": None, "actual_ship_date": None, "carrier_name": None, "tracking_number": None}
        outbound_orders.append(new_order)
        return json.dumps({"order_id": new_order_id}, indent=2)


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_outbound_order", "description": "Creates a new outbound customer order with a 'Pending' status.", "parameters": {"type": "object", "properties": {"customer_name": {"type": "string"}, "destination_city": {"type": "string"}, "priority_level": {"type": "string"}, "line_items": {"type": "array", "items": {"type": "object", "properties": {"sku": {"type": "string"}, "quantity": {"type": "integer"}}, "required": ["sku", "quantity"]}}}, "required": ["customer_name", "destination_city", "priority_level", "line_items"]}}}

class ShipOutboundOrder(Tool):
    """Updates an order to 'Shipped', assigns a carrier, allocates inventory, and calculates shipping cost."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get('order_id')
        warehouse_id = kwargs.get('warehouse_id')
        carrier_scac = kwargs.get('carrier_scac')
        if not all([order_id, warehouse_id, carrier_scac]):
            return json.dumps({"error": "order_id, warehouse_id, and carrier_scac are required."}, indent=2)

        order_to_update = next((o for o in data.get('outbound_orders', []) if o.get('order_id') == order_id), None)
        if not order_to_update:
            return json.dumps({"error": f"Order '{order_id}' not found."}, indent=2)

        # --- NEW LOGIC START ---
        total_weight_kg = 0
        line_items = order_to_update.get("line_items", [])
        product_master = data.get('product_master', [])
        for item in line_items:
            product = next((p for p in product_master if p.get('sku') == item['sku']), None)
            if product:
                total_weight_kg += product.get('weight_kg', 0) * item['quantity']

        # Deterministic shipping cost calculation
        shipping_cost = round((total_weight_kg * 2.5) + 100, 2)
        order_to_update['shipping_cost'] = shipping_cost
        # --- NEW LOGIC END ---

        order_to_update['status'] = 'Shipped'
        order_to_update['warehouse_id'] = warehouse_id
        carrier_name = next((c.get('carrier_name') for c in data.get('carriers', []) if c.get('scac') == carrier_scac), "Unknown")
        order_to_update['carrier_name'] = carrier_name
        order_to_update['carrier_scac'] = carrier_scac
        order_id_number = order_id.split('-')[1]
        order_to_update['tracking_number'] = f"{carrier_scac}-{order_id_number}"

        for item in line_items:
            for inv_record in data.get('inventory', []):
                if inv_record.get('sku') == item.get('sku') and inv_record.get('warehouse_id') == warehouse_id:
                    inv_record['quantity_available'] -= item.get('quantity', 0)
                    inv_record['quantity_allocated'] += item.get('quantity', 0)
                    break

        return json.dumps(order_to_update, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "ship_outbound_order", "description": "Updates an order's status to 'Shipped', adjusts inventory, and assigns a carrier.", "parameters": {"type": "object", "properties": {"order_id": {"type": "string"}, "warehouse_id": {"type": "string"}, "carrier_scac": {"type": "string"}}, "required": ["order_id", "warehouse_id", "carrier_scac"]}}}

class FindInboundShipment(Tool):
    """Finds a specific inbound shipment based on supplier and origin."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_name = kwargs.get('supplier_name')
        origin_city = kwargs.get('origin_city')
        status = kwargs.get('status')
        if not all([supplier_name, origin_city]):
            return json.dumps({"error": "supplier_name and origin_city are required arguments."}, indent=2)
        shipments = data.get('inbound_shipments', [])
        results = [s for s in shipments if s.get('supplier_name') == supplier_name and s.get('origin_city') == origin_city and (not status or s.get('status') == status)]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_inbound_shipment", "description": "Finds inbound shipments from a specific supplier and origin city, optionally filtering by status.", "parameters": {"type": "object", "properties": {"supplier_name": {"type": "string"}, "origin_city": {"type": "string"}, "status": {"type": "string", "description": "Optional status to filter by (e.g., 'In Transit')."}}, "required": ["supplier_name", "origin_city"]}}}

class UpdateShipmentStatus(Tool):
    """Updates the status and notes of a specific inbound shipment."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        shipment_id = kwargs.get('shipment_id')
        new_status = kwargs.get('new_status')
        notes = kwargs.get('notes')
        if not all([shipment_id, new_status, notes]):
            return json.dumps({"error": "shipment_id, new_status, and notes are required."}, indent=2)
        shipment_to_update = next((s for s in data.get('inbound_shipments', []) if s.get('shipment_id') == shipment_id), None)
        if not shipment_to_update:
            return json.dumps({"error": f"Shipment '{shipment_id}' not found."}, indent=2)
        shipment_to_update['status'] = new_status
        shipment_to_update['notes'] = notes
        return json.dumps(shipment_to_update, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_shipment_status", "description": "Updates the status and notes for a specific inbound shipment.", "parameters": {"type": "object", "properties": {"shipment_id": {"type": "string"}, "new_status": {"type": "string"}, "notes": {"type": "string"}}, "required": ["shipment_id", "new_status", "notes"]}}}

class LogSupplierPerformanceIssue(Tool):
    """Logs a performance issue against a supplier's record."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get('supplier_id')
        issue_code = kwargs.get('issue_code')
        shipment_id = kwargs.get('shipment_id')
        if not all([supplier_id, issue_code]):
            return json.dumps({"error": "supplier_id and issue_code are required."}, indent=2)
        supplier_to_update = next((s for s in data.get('supplier_master', []) if s.get('supplier_id') == supplier_id), None)
        if not supplier_to_update:
            return json.dumps({"error": f"Supplier '{supplier_id}' not found."}, indent=2)
        if 'performance_logs' not in supplier_to_update:
            supplier_to_update['performance_logs'] = []
        log_entry = {"issue_code": issue_code, "related_shipment": shipment_id}
        supplier_to_update['performance_logs'].append(log_entry)
        return json.dumps(supplier_to_update, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "log_supplier_performance_issue", "description": "Logs a performance issue against a supplier's record.", "parameters": {"type": "object", "properties": {"supplier_id": {"type": "string"}, "issue_code": {"type": "string"}, "shipment_id": {"type": "string"}}, "required": ["supplier_id", "issue_code"]}}}

class GetWarehouseDetails(Tool):
    """Retrieves all details for a specific warehouse by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        warehouse_name = kwargs.get('warehouse_name')
        if not warehouse_name:
            return json.dumps({"error": "warehouse_name is required."}, indent=2)
        warehouse = next((w for w in data.get('warehouses', []) if w.get('warehouse_name') == warehouse_name), None)
        if not warehouse:
            return json.dumps({"error": f"Warehouse '{warehouse_name}' not found."}, indent=2)
        return json.dumps(warehouse, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_warehouse_details", "description": "Retrieves all details for a specific warehouse by its name.", "parameters": {"type": "object", "properties": {"warehouse_name": {"type": "string"}}, "required": ["warehouse_name"]}}}

class InitiateWarehouseTransfer(Tool):
    """Creates a stock transfer between two warehouses, adjusting inventory levels."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku, quantity, from_warehouse_id, to_warehouse_id = map(kwargs.get, ["sku", "quantity", "from_warehouse_id", "to_warehouse_id"])
        if not all([sku, quantity, from_warehouse_id, to_warehouse_id]):
            return json.dumps({"error": "sku, quantity, from_warehouse_id, and to_warehouse_id are required."}, indent=2)
        inventory = data.get('inventory', [])
        source_inv = next((i for i in inventory if i.get('sku') == sku and i.get('warehouse_id') == from_warehouse_id), None)
        dest_inv = next((i for i in inventory if i.get('sku') == sku and i.get('warehouse_id') == to_warehouse_id), None)
        if not source_inv:
            return json.dumps({"error": f"SKU {sku} not found in source warehouse {from_warehouse_id}."}, indent=2)
        if source_inv['quantity_available'] < quantity:
            return json.dumps({"error": f"Insufficient available stock in {from_warehouse_id}."}, indent=2)
        source_inv['quantity_available'] -= quantity
        source_inv['quantity_allocated'] += quantity
        if dest_inv:
            dest_inv['quantity_inbound'] += quantity
        else:
            product_details = next((p for p in data.get('product_master', []) if p.get('sku') == sku), {})
            new_inv_record = {"inventory_id": f"INV-{random.randint(10000, 99999)}", "sku": sku, "product_name": product_details.get("product_name"), "warehouse_id": to_warehouse_id, "quantity_on_hand": 0, "quantity_available": 0, "quantity_allocated": 0, "quantity_inbound": quantity, "quantity_damaged": 0}
            inventory.append(new_inv_record)
        return json.dumps({"status": "success", "transfer_id": f"T-{from_warehouse_id}-{to_warehouse_id}-{random.randint(1000, 9999)}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "initiate_warehouse_transfer", "description": "Initiates a stock transfer of a specific SKU from a source warehouse to a destination warehouse.", "parameters": {"type": "object", "properties": {"sku": {"type": "string"}, "quantity": {"type": "integer"}, "from_warehouse_id": {"type": "string"}, "to_warehouse_id": {"type": "string"}}, "required": ["sku", "quantity", "from_warehouse_id", "to_warehouse_id"]}}}

class UpdateWarehouseNotes(Tool):
    """Adds or overwrites notes for a specific warehouse."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        warehouse_id = kwargs.get('warehouse_id')
        notes = kwargs.get('notes')
        if not all([warehouse_id, notes]):
            return json.dumps({"error": "warehouse_id and notes are required."}, indent=2)
        warehouse = next((w for w in data.get('warehouses', []) if w.get('warehouse_id') == warehouse_id), None)
        if not warehouse:
            return json.dumps({"error": f"Warehouse '{warehouse_id}' not found."}, indent=2)
        new_note = f"{notes}"
        if 'notes' in warehouse and warehouse['notes']:
            warehouse['notes'] += f"\n{new_note}"
        else:
            warehouse['notes'] = new_note
        return json.dumps(warehouse, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_warehouse_notes", "description": "Adds a new note to a specific warehouse's record.", "parameters": {"type": "object", "properties": {"warehouse_id": {"type": "string"}, "notes": {"type": "string"}}, "required": ["warehouse_id", "notes"]}}}

class FindOrdersByCarrier(Tool):
    """Finds all outbound orders assigned to a specific carrier, filtering by status."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carrier_name = kwargs.get('carrier_name')
        status = kwargs.get('status')
        if not carrier_name:
            return json.dumps({"error": "carrier_name is a required argument."}, indent=2)
        orders = data.get('outbound_orders', [])
        results = [o for o in orders if o.get('carrier_name') == carrier_name and (not status or o.get('status') == status)]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_orders_by_carrier", "description": "Finds all outbound orders assigned to a specific carrier, optionally filtering by status.", "parameters": {"type": "object", "properties": {"carrier_name": {"type": "string"}, "status": {"type": "string"}}, "required": ["carrier_name"]}}}

class ReassignOrderCarrier(Tool):
    """Changes the assigned carrier for a specific outbound order."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get('order_id')
        new_carrier_scac = kwargs.get('new_carrier_scac')
        if not all([order_id, new_carrier_scac]):
            return json.dumps({"error": "order_id and new_carrier_scac are required."}, indent=2)
        order = next((o for o in data.get('outbound_orders', []) if o.get('order_id') == order_id), None)
        if not order:
            return json.dumps({"error": f"Order '{order_id}' not found."}, indent=2)
        new_carrier = next((c for c in data.get('carriers', []) if c.get('scac') == new_carrier_scac), None)
        if not new_carrier:
            return json.dumps({"error": f"New carrier with SCAC '{new_carrier_scac}' not found."}, indent=2)
        order['carrier_name'] = new_carrier.get('carrier_name')
        order['carrier_scac'] = new_carrier.get('scac')
        order_id_number = order_id.split('-')[1]
        order['tracking_number'] = f"{new_carrier.get('scac')}-{order_id_number}"
        return json.dumps(order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "reassign_order_carrier", "description": "Changes the assigned carrier for a specific outbound order and generates a new tracking number.", "parameters": {"type": "object", "properties": {"order_id": {"type": "string"}, "new_carrier_scac": {"type": "string"}}, "required": ["order_id", "new_carrier_scac"]}}}

class LogAuditTrail(Tool):
    """Logs a structured audit event for tracking important system actions."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        audit_event = kwargs.get('audit_event')
        subject_id = kwargs.get('subject_id')
        outcome_code = kwargs.get('outcome_code')
        outcome_details = kwargs.get('outcome_details') # This is a dictionary

        if not all([audit_event, subject_id, outcome_code]):
            return json.dumps({"error": "audit_event, subject_id, and outcome_code are required."}, indent=2)

        if 'audit_log' not in data:
            data['audit_log'] = []

        log_entry = {
            "event_type": audit_event,
            "subject_id": subject_id,
            "outcome_code": outcome_code,
            "outcome_details": outcome_details
        }
        data['audit_log'].append(log_entry)
        return json.dumps(log_entry, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_audit_trail",
                "description": "Logs a structured audit event for tracking important system actions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_event": {"type": "string", "description": "The type of event being logged (e.g., 'PRODUCT_RISK_AUDIT')."},
                        "subject_id": {"type": "string", "description": "The ID of the primary entity this event relates to (e.g., a SKU or Order ID)."},
                        "outcome_code": {"type": "string", "description": "A fixed code representing the outcome (e.g., 'RISK_IDENTIFIED')."},
                        "outcome_details": {"type": "object", "description": "A dictionary of key-value pairs containing specific data about the outcome."}
                    },
                    "required": ["audit_event", "subject_id", "outcome_code"]
                }
            }
        }

class UpdateCarrierStatus(Tool):
    """Updates the status of a carrier."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carrier_name, status = map(kwargs.get, ["carrier_name", "status"])
        if not all([carrier_name, status]):
            return json.dumps({"error": "carrier_name and status are required."}, indent=2)
        carrier_to_update = next((c for c in data.get('carriers', []) if c.get('carrier_name') == carrier_name), None)
        if not carrier_to_update:
            return json.dumps({"error": f"Carrier '{carrier_name}' not found."}, indent=2)
        carrier_to_update['active_status'] = status
        return json.dumps({"carrier_id": carrier_to_update.get('carrier_id'), "carrier_name": carrier_name, "new_status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_carrier_status", "description": "Updates the operational status of a carrier (e.g., True, False, 'Under Review').", "parameters": {"type": "object", "properties": {"carrier_name": {"type": "string"}, "status": {"type": "string", "description": "The new status to set for the carrier."}}, "required": ["carrier_name", "status"]}}}

# --- NEW Getter Tools ---

class GetOutboundOrderDetails(Tool):
    """Retrieves the full details for a single outbound order by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get('order_id')
        if not order_id:
            return json.dumps({"error": "order_id is required."}, indent=2)
        order = next((o for o in data.get('outbound_orders', []) if o.get('order_id') == order_id), None)
        if not order:
            return json.dumps({"error": f"Order '{order_id}' not found."}, indent=2)
        return json.dumps(order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_outbound_order_details", "description": "Retrieves the full details for a single outbound order by its ID.", "parameters": {"type": "object", "properties": {"order_id": {"type": "string"}}, "required": ["order_id"]}}}

class GetInventoryDetails(Tool):
    """Retrieves a single inventory record for a SKU at a specific warehouse."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku, warehouse_id = map(kwargs.get, ["sku", "warehouse_id"])
        if not all([sku, warehouse_id]):
            return json.dumps({"error": "sku and warehouse_id are required."}, indent=2)
        inventory_record = next((i for i in data.get('inventory', []) if i.get('sku') == sku and i.get('warehouse_id') == warehouse_id), None)
        if not inventory_record:
            return json.dumps({"error": f"Inventory for SKU '{sku}' not found at warehouse '{warehouse_id}'."}, indent=2)
        return json.dumps(inventory_record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_inventory_details", "description": "Retrieves a single inventory record for a SKU at a specific warehouse.", "parameters": {"type": "object", "properties": {"sku": {"type": "string"}, "warehouse_id": {"type": "string"}}, "required": ["sku", "warehouse_id"]}}}

class GetCarrierDetails(Tool):
    """Retrieves the full details for a single carrier by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carrier_name = kwargs.get('carrier_name')
        if not carrier_name:
            return json.dumps({"error": "carrier_name is required."}, indent=2)
        carrier = next(
                (
                    c for c in data.get('carriers', [])
                    if carrier_name.lower() in c.get('carrier_name', '').lower()
                ),
                None
            )
        if not carrier:
            return json.dumps({"error": f"Carrier '{carrier_name}' not found."}, indent=2)
        return json.dumps(carrier, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_carrier_details", "description": "Retrieves the full details for a single carrier by its name.", "parameters": {"type": "object", "properties": {"carrier_name": {"type": "string"}}, "required": ["carrier_name"]}}}

class UpdateInventoryDamageStatus(Tool):
    """Updates the inventory count to move a number of units from 'available' to 'damaged'."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_id = kwargs.get('inventory_id')
        damaged_quantity = kwargs.get('damaged_quantity')

        if not all([inventory_id, damaged_quantity]):
            return json.dumps({"error": "inventory_id and damaged_quantity are required."}, indent=2)

        inventory_record = next((i for i in data.get('inventory', []) if i.get('inventory_id') == inventory_id), None)

        if not inventory_record:
            return json.dumps({"error": f"Inventory record '{inventory_id}' not found."}, indent=2)

        if damaged_quantity > 0:
            if damaged_quantity > inventory_record.get('quantity_available', 0):
                return json.dumps({"error": f"Cannot mark {damaged_quantity} as damaged, only {inventory_record.get('quantity_available')} are available."}, indent=2)
            inventory_record['quantity_available'] -= damaged_quantity
            inventory_record['quantity_damaged'] += damaged_quantity
        elif damaged_quantity < 0:
            abs_damaged_quantity = abs(damaged_quantity)

            inventory_record['quantity_available'] += abs_damaged_quantity

            if abs_damaged_quantity > inventory_record.get('quantity_damaged', 0):
                inventory_record['quantity_damaged'] = 0
            else:
                inventory_record['quantity_damaged'] -= abs_damaged_quantity
        else:
            pass

        return json.dumps(inventory_record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_damage_status",
                "description": "Updates an inventory record to reflect damaged goods by moving a quantity from 'available' to 'damaged'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {"type": "string", "description": "The ID of the inventory record to update."},
                        "damaged_quantity": {"type": "integer", "description": "The number of units to mark as damaged."}
                    },
                    "required": ["inventory_id", "damaged_quantity"]
                }
            }
        }

class CreatePurchaseOrder(Tool):
    """Creates a new purchase order and a corresponding 'Planned' inbound shipment."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get('supplier_id')
        line_items = kwargs.get('line_items')
        priority = kwargs.get('priority')

        if not all([supplier_id, line_items, priority]):
            return json.dumps({"error": "supplier_id, line_items, and priority are required."}, indent=2)

        supplier = next((s for s in data.get('supplier_master', []) if s.get('supplier_id') == supplier_id), None)
        if not supplier:
            return json.dumps({"error": f"Supplier '{supplier_id}' not found."}, indent=2)

        inbound_shipments = data.get('inbound_shipments', [])

        current_year_str = str(get_current_year())

        # Filter POs for the current year only
        pos_this_year = [
            s for s in inbound_shipments
            if s.get('purchase_order_number', '').startswith(f"PO-{current_year_str}")
        ]

        # Find the max sequence number within the current year
        max_seq_num_this_year = 0
        if pos_this_year:
            max_seq_num_this_year = max(
                (int(po.get('purchase_order_number').split('-')[2]) for po in pos_this_year),
                default=0
            )

        new_seq_num = max_seq_num_this_year + 1
        new_po_number = f"PO-{current_year_str}-{new_seq_num:04d}"
        # --- CORRECTED LOGIC END ---

        max_ship_id = max((int(s.get('shipment_id', 'SHIP-0').split('-')[1]) for s in inbound_shipments), default=0)
        new_shipment_id = f"SHIP-{max_ship_id + 1:04d}"

        first_sku = line_items[0]['sku']
        dest_warehouse = next((i for i in data.get('inventory', []) if i.get('sku') == first_sku), {})

        new_shipment = {
            "shipment_id": new_shipment_id,
            "purchase_order_number": new_po_number,
            "supplier_id": supplier_id,
            "supplier_name": supplier.get('supplier_name'),
            "origin_address": supplier.get('contact_information', {}).get('address', {}).get('street'),
            "origin_city": supplier.get('contact_information', {}).get('address', {}).get('city'),
            "origin_country": supplier.get('contact_information', {}).get('address', {}).get('country'),
            "destination_warehouse_id": dest_warehouse.get('warehouse_id'),
            "destination_warehouse_name": dest_warehouse.get('warehouse_name'),
            "status": "Planned",
            "priority_level": priority
        }

        inbound_shipments.append(new_shipment)

        # The tool now correctly returns the PO number as determined by the policy
        return json.dumps({"status": "success", "purchase_order_number": new_po_number}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_purchase_order",
                "description": "Creates a new purchase order for a supplier, which also generates a new 'Planned' inbound shipment record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "The ID of the supplier for the order."},
                        "line_items": {
                            "type": "array",
                            "description": "A list of products to order.",
                            "items": {
                                "type": "object",
                                "properties": {"sku": {"type": "string"},"quantity": {"type": "integer"}},
                                "required": ["sku", "quantity"]
                            }
                        },
                        "priority": {"type": "string", "description": "The priority level for this order (e.g., 'High')."}
                    },
                    "required": ["supplier_id", "line_items", "priority"]
                }
            }
        }

class GetPurchaseOrderDetails(Tool):
    """Retrieves details of an inbound shipment by its Purchase Order number."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        po_number = kwargs.get('po_number')
        if not po_number:
            return json.dumps({"error": "po_number is required."}, indent=2)

        shipment = next((s for s in data.get('inbound_shipments', []) if s.get('purchase_order_number') == po_number), None)

        if not shipment:
            return json.dumps({"error": f"Shipment for Purchase Order '{po_number}' not found."}, indent=2)

        return json.dumps(shipment, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_purchase_order_details",
                "description": "Retrieves the shipment details associated with a given Purchase Order (PO) number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "po_number": {"type": "string", "description": "The Purchase Order number to search for."}
                    },
                    "required": ["po_number"]
                }
            }
        }

class GetOutboundOrderDetailsBySo(Tool):
    """Retrieves order details using the Sales Order (SO) number."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sales_order_number = kwargs.get('sales_order_number')
        if not sales_order_number:
            return json.dumps({"error": "sales_order_number is a required argument."}, indent=2)

        order = next((o for o in data.get('outbound_orders', []) if o.get('sales_order_number') == sales_order_number), None)

        if not order:
            return json.dumps({"error": f"Order with Sales Order number '{sales_order_number}' not found."}, indent=2)

        return json.dumps(order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_outbound_order_details_by_so",
                "description": "Retrieves the full details for a single outbound order by its Sales Order (SO) number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sales_order_number": {"type": "string", "description": "The Sales Order number (e.g., 'SO-2024-0001')."}
                    },
                    "required": ["sales_order_number"]
                }
            }
        }

class CreateReturnAuthorization(Tool):
    """Creates a Return Merchandise Authorization (RMA) record for a customer return."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get('order_id')
        line_items = kwargs.get('line_items')
        reason = kwargs.get('reason')

        if not all([order_id, line_items, reason]):
            return json.dumps({"error": "order_id, line_items, and reason are required."}, indent=2)

        if 'rma_authorizations' not in data:
            data['rma_authorizations'] = []

        max_rma_num = max((int(r.get('rma_id', 'RMA-1000').split('-')[1]) for r in data['rma_authorizations']), default=1000)
        new_rma_id = f"RMA-{max_rma_num + 1}"

        rma_record = {
            "rma_id": new_rma_id,
            "order_id": order_id,
            "line_items_to_return": line_items,
            "reason": reason,
            "status": "Authorized",
        }
        data['rma_authorizations'].append(rma_record)

        return json.dumps({"rma_id": new_rma_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_return_authorization",
                "description": "Creates a Return Merchandise Authorization (RMA) to formally approve a customer's return request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The original order ID the return is associated with."},
                        "line_items": {
                            "type": "array", "description": "A list of products being returned.",
                            "items": {"type": "object", "properties": {"sku": {"type": "string"}, "quantity": {"type": "integer"}}, "required": ["sku", "quantity"]}
                        },
                        "reason": {"type": "string", "description": "The reason for the return provided by the customer."}
                    },
                    "required": ["order_id", "line_items", "reason"]
                }
            }
        }

class CreateInboundReturnShipment(Tool):
    """Creates a new 'Planned' inbound shipment specifically for a customer return."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rma_id = kwargs.get('rma_id')
        from_customer_id = kwargs.get('from_customer_id')
        to_warehouse_id = kwargs.get('to_warehouse_id')
        carrier_scac = kwargs.get('carrier_scac')

        if not all([rma_id, from_customer_id, to_warehouse_id, carrier_scac]):
            return json.dumps({"error": "rma_id, from_customer_id, to_warehouse_id, and carrier_scac are required."}, indent=2)

        inbound_shipments = data.get('inbound_shipments', [])
        max_ship_id = max((int(s.get('shipment_id', 'SHIP-0').split('-')[1]) for s in inbound_shipments), default=0)
        new_shipment_id = f"SHIP-{max_ship_id + 1:04d}"

        customer = next((o for o in data.get('outbound_orders', []) if o.get('customer_id') == from_customer_id), {})
        warehouse = next((w for w in data.get('warehouses', []) if w.get('warehouse_id') == to_warehouse_id), {})

        new_shipment = {
            "shipment_id": new_shipment_id,
            "purchase_order_number": rma_id, # Using RMA as the reference number
            "supplier_id": from_customer_id,
            "supplier_name": "CUSTOMER_RETURN",
            "origin_address": customer.get("customer_address"),
            "origin_city": customer.get("customer_city"),
            "origin_country": customer.get("customer_country"),
            "destination_warehouse_id": to_warehouse_id,
            "destination_warehouse_name": warehouse.get("warehouse_name"),
            "carrier_name": next((c.get("carrier_name") for c in data.get('carriers', []) if c.get("scac") == carrier_scac), "Unknown"),
            "carrier_scac": carrier_scac,
            "status": "Planned",
            "priority_level": "Medium"
        }
        inbound_shipments.append(new_shipment)
        return json.dumps(new_shipment, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_inbound_return_shipment",
                "description": "Creates a new 'Planned' inbound shipment to track the physical return of goods from a customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rma_id": {"type": "string", "description": "The RMA number authorizing this return shipment."},
                        "from_customer_id": {"type": "string", "description": "The ID of the customer returning the items."},
                        "to_warehouse_id": {"type": "string", "description": "The ID of the warehouse designated to receive the return."},
                        "carrier_scac": {"type": "string", "description": "The SCAC code of the carrier handling the return."}
                    },
                    "required": ["rma_id", "from_customer_id", "to_warehouse_id", "carrier_scac"]
                }
            }
        }

class UpdateOutboundOrderStatus(Tool):
    """Updates the status of an existing outbound order."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get('order_id')
        new_status = kwargs.get('new_status')

        if not all([order_id, new_status]):
            return json.dumps({"error": "order_id and new_status are required."}, indent=2)

        order = next((o for o in data.get('outbound_orders', []) if o.get('order_id') == order_id), None)
        if not order:
            return json.dumps({"error": f"Order '{order_id}' not found."}, indent=2)

        if new_status == "Cancelled":
            for item in order.get("line_items", []):
                for inv_record in data.get('inventory', []):
                    if inv_record.get('sku') == item.get('sku') and inv_record.get('warehouse_id') == order.get('warehouse_id'):
                        inv_record['quantity_available'] += item.get('quantity', 0)
                        inv_record['quantity_allocated'] -= item.get('quantity', 0)
                        break

        order['status'] = new_status
        return_related_statuses = [
            "Returned",
            "Partially Returned",
            "Cancelled - Damaged Stock", # Ou outros status que impliquem devolução/cancelamento com impacto em retorno
            "Processing Return",
            "Incorrect Item Returned",
            "Cancelled - Force Majeure",
            "On Hold - Fraud Investigation", # Dependendo da política de fraude/retorno
            "Cancelled - Expired Stock",
            "Cancelled" # Se um cancelamento genérico também implica em retorno
        ]
        if new_status in return_related_statuses:
            order['return_status'] = new_status
        else:
            order['return_status'] = "None"
        return json.dumps(order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_outbound_order_status",
                "description": "Updates the status of an existing outbound order (e.g., to 'Partially Returned').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to update."},
                        "new_status": {"type": "string", "description": "The new status to set for the order."}
                    },
                    "required": ["order_id", "new_status"]
                }
            }
        }

class IssueCustomerCreditMemo(Tool):
    """Issues a credit memo for a customer and logs the financial transaction."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get('order_id')
        customer_id = kwargs.get('customer_id')
        returned_items = kwargs.get('returned_items')

        if not all([order_id, customer_id, returned_items]):
            return json.dumps({"error": "order_id, customer_id, and returned_items are required."}, indent=2)

        # Deterministic ID generation based on policy
        order_id_num = order_id.split('-')[1]
        credit_memo_id = f"CM-{order_id_num}"

        total_credit_value = 0
        product_master = data.get('product_master', [])
        for item in returned_items:
            product = next((p for p in product_master if p.get('sku') == item['sku']), None)
            if product:
                total_credit_value += product.get('unit_price', 0) * item['quantity']

        if 'credit_memos' not in data:
            data['credit_memos'] = []

        credit_memo = {
            "credit_memo_id": credit_memo_id,
            "original_order_id": order_id,
            "customer_id": customer_id,
            "credited_items": returned_items,
            "total_credit_value": round(total_credit_value, 2),
            "currency": "USD",
            "status": "Issued",
        }
        data['credit_memos'].append(credit_memo)

        return json.dumps(credit_memo, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "issue_customer_credit_memo",
                "description": "Issues a credit memo for a customer for returned goods and logs the financial transaction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The original order ID that is being credited."},
                        "customer_id": {"type": "string", "description": "The ID of the customer receiving the credit."},
                        "returned_items": {
                            "type": "array", "description": "A list of items for which credit is being issued.",
                            "items": {"type": "object", "properties": {"sku": {"type": "string"}, "quantity": {"type": "integer"}}, "required": ["sku", "quantity"]}
                        }
                    },
                    "required": ["order_id", "customer_id", "returned_items"]
                }
            }
        }

class GetReturnAuthorizationDetails(Tool):
    """Retrieves details of a specific RMA."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rma_id = kwargs.get('rma_id')
        if not rma_id:
            return json.dumps({"error": "rma_id is required."}, indent=2)

        rma = next((r for r in data.get('rma_authorizations', []) if r.get('rma_id') == rma_id), None)
        if not rma:
            return json.dumps({"error": f"RMA '{rma_id}' not found."}, indent=2)

        return json.dumps(rma, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_return_authorization_details",
                "description": "Retrieves the details of a specific Return Merchandise Authorization (RMA) by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"rma_id": {"type": "string", "description": "The RMA ID to search for."}},
                    "required": ["rma_id"]
                }
            }
        }

class GetCreditMemoDetails(Tool):
    """Retrieves details of a specific credit memo."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        credit_memo_id = kwargs.get('credit_memo_id')
        if not credit_memo_id:
            return json.dumps({"error": "credit_memo_id is required."}, indent=2)

        memo = next((m for m in data.get('credit_memos', []) if m.get('credit_memo_id') == credit_memo_id), None)
        if not memo:
            return json.dumps({"error": f"Credit Memo '{credit_memo_id}' not found."}, indent=2)

        return json.dumps(memo, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_credit_memo_details",
                "description": "Retrieves the details of a specific credit memo by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"credit_memo_id": {"type": "string", "description": "The Credit Memo ID to search for."}},
                    "required": ["credit_memo_id"]
                }
            }
        }

class GetKitComponents(Tool):
    """
    Retrieves the list of component SKUs and quantities for a given virtual kit,
    identified either by SKU or by human‑friendly name.
    """
    KITS_DATABASE = {
        "KIT-ROBO-S1": {
            "kit_name": "Basic Robotic Starter Kit",
            "components": [
                {"sku": "TECH-ROBO-N14", "quantity": 1, "product_name": "Articulated Robotic Arm"},
                {"sku": "TECH-BATT-Q17", "quantity": 2, "product_name": "Lithium‑Ion Battery Pack"}
            ]
        }
    }
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        kit_sku: str | None = kwargs.get("kit_sku")
        kit_name: str | None = kwargs.get("kit_name")

        if not kit_sku and not kit_name:
            return json.dumps(
                {"error": "You must provide either 'kit_sku' or 'kit_name'."},
                indent=2,
            )
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
            return json.dumps({"error": f"Kit with {missing} not found."}, indent=2)

        return json.dumps(kit_data["components"], indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_kit_components",
                "description": (
                    "Retrieves the bill of materials (component SKUs and their "
                    "quantities) for a virtual kit identified by SKU or name."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kit_sku": {
                            "type": "string",
                            "description": "The SKU of the virtual kit (e.g., 'KIT-ROBO-S1')."
                        },
                        "kit_name": {
                            "type": "string",
                            "description": "The friendly name of the virtual kit "
                                           "(e.g., 'Basic Robotic Starter Kit')."
                        }
                    },
                    # Nenhum campo é obrigatório; exige‑se pelo menos um na lógica
                    "required": []
                }
            }
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
    GetKitComponents()
]
