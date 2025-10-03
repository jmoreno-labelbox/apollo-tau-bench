from domains.dto import Task, Action
import hashlib

# Helper to generate deterministic adjustment and transfer IDs

def adj_id(store_id, sku):
    return f"ADJ-{hashlib.sha256(f'{store_id}-{sku}'.encode()).hexdigest()[:6].upper()}"

def trf_id(from_store, to_store, sku):
    return f"TRF-{hashlib.sha256(f'{from_store}-{to_store}-{sku}'.encode()).hexdigest()[:6].upper()}"

TASKS = [
    Task(
        annotator="0",
        user_id="task_001",
        instruction=(
            "On 2025-09-01, at STORE-001, compliance officer EMP-1002 carries out a thorough expired product review. The officer reviews inventory for SKU GROC-ALMBTR500, confirms product expiration dates, marks expired products as of 2025-09-01, compiles all active promotions for the SKU, implements a clearance discount of 25% for expired items with a minimum quantity of 1, verifies the clearance against inventory levels with a minimum threshold of 20%, and records the compliance review with timestamp '2025-09-01T13:45:00Z', photo 'compliance001.jpg', and digital signature 'SIG-COMP-001'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500"}),
            Action(name="GetProductInfo", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="FlagExpiredProducts", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "as_of_date": "2025-09-01"}),
            Action(name="ListActivePromotions", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500"}),
            Action(name="ApplyBulkDiscount", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "discount_percent": 25, "min_quantity": 1}),
            Action(name="CheckSafetyStock", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "min_percent": 20}),
            Action(name="GetEmployeeInfo", kwargs={"employee_id": "EMP-1002"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1002", "timestamp": "2025-09-01T13:45:00Z", "photo": "compliance001.jpg", "digital_signature": "SIG-COMP-001"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "system_count": 60}',
            '"product_info": {"sku": "GROC-ALMBTR500", "name": "Organic Almond Butter 500g", "unit_cost": 7.85}',
            '"expired_flagged": true',
            '"active_promotions": []',
            '"clearance_discount_applied": true',
            '"safety_stock_ok": true',
            '"employee_info": {"employee_id": "EMP-1002", "name": "Sarah Anderson", "role": "Cashier"}',
            '"audit_log": {"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1002", "timestamp": "2025-09-01T13:45:00Z", "photo": "compliance001.jpg", "digital_signature": "SIG-COMP-001"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_002",
        instruction="Perform an audit at STORE-005 for SKU AUDIO-BTSPKR02. Auditor EMP-1017 will inspect inventory, execute a physical count, and log the findings. System count is 20, physical count is 20, unit cost is 78.0. Document result as discrepancy_logged with timestamp '2025-07-01T14:00:00Z', photo 'photo023.jpg', and digital signature 'SIG-023'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-005", "sku": "AUDIO-BTSPKR02"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-005", "sku": "AUDIO-BTSPKR02", "auditor_id": "EMP-1017"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 20, "physical_count": 20, "unit_cost": 78.0}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-005", "sku": "AUDIO-BTSPKR02", "auditor_id": "EMP-1017", "timestamp": "2025-07-01T14:00:00Z", "photo": "photo023.jpg", "digital_signature": "SIG-023"}),
        ],
        outputs=[
            '"system_count": 20',
            '"physical_count": 20',
            '"discrepancy_amount": 0',
            '"audit_log": {"store_id": "STORE-005", "sku": "AUDIO-BTSPKR02", "auditor_id": "EMP-1017", "timestamp": "2025-07-01T14:00:00Z", "photo": "photo023.jpg", "digital_signature": "SIG-023"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_003",
        instruction=(
            "On 2025-07-25, at STORE-001, auditor EMP-1002 executes a detailed restock audit for SKU HOME-DESKLMP01. The auditor assesses current inventory levels, confirms product information, checks employee authorization, restocks 8 units, and documents the entire process with timestamp '2025-07-25T13:00:00Z', photo 'photo072.jpg', and digital signature 'SIG-072'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetEmployeeInfo", kwargs={"employee_id": "EMP-1002"}),
            Action(name="RestockLowInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "quantity": 8}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-25T13:00:00Z", "photo": "photo072.jpg", "digital_signature": "SIG-072"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"product_info": {"sku": "HOME-DESKLMP01", "name": "LumiLux LED Desk Lamp", "unit_cost": 17.2}',
            '"employee_info": {"employee_id": "EMP-1002", "name": "Sarah Anderson", "role": "Cashier"}',
            '"restock_triggered": true',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-25T13:00:00Z", "photo": "photo072.jpg", "digital_signature": "SIG-072"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_004",
        instruction="Conduct an audit at STORE-001 for SKU ELEC-4KTV55. Auditor EMP-1002 will verify inventory, carry out a physical count (system: 8, physical: 8, unit cost: 480.0), calculate discrepancy, create an inventory adjustment, require dual approval, and document the audit with timestamp '2025-07-01T18:00:00Z', photo 'photo049.jpg', and digital signature 'SIG-049'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "ELEC-4KTV55"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "ELEC-4KTV55", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 8, "physical_count": 8, "unit_cost": 480.0}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "ELEC-4KTV55", "amount": 0.0}),
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "ELEC-4KTV55")}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "ELEC-4KTV55", "auditor_id": "EMP-1002", "timestamp": "2025-07-01T18:00:00Z", "photo": "photo049.jpg", "digital_signature": "SIG-049"}),
        ],
        outputs=[
            '"system_count": 8',
            '"physical_count": 8',
            '"discrepancy_amount": 0.0',
            f'"adjustment_id": "{adj_id("STORE-001", "ELEC-4KTV55")}"',
            '"dual_approved": true',
            '"audit_log": {"store_id": "STORE-001", "sku": "ELEC-4KTV55", "timestamp": "2025-07-01T18:00:00Z", "photo": "photo049.jpg", "digital_signature": "SIG-049"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_005",
        instruction=(
            "On 2025-08-04, at STORE-001, auditor EMP-1002 inspects inventory and product information for SKU HOME-DESKLMP01, retrieves employee info for EMP-1002, calculates a discrepancy (system: 45, physical: 40, unit cost: $17.2), creates an inventory adjustment, requires dual approval from EMP-1003, and logs the audit with timestamp '2025-08-04T09:00:00Z', photo 'photo105.jpg', and digital signature 'SIG-105'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetEmployeeInfo", kwargs={"employee_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": 86.0}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1003"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-08-04T09:00:00Z", "photo": "photo105.jpg", "digital_signature": "SIG-105"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"product_info": {"sku": "HOME-DESKLMP01", "name": "LumiLux LED Desk Lamp", "unit_cost": 17.2}',
            '"employee_info": {"employee_id": "EMP-1002", "name": "Sarah Anderson", "role": "Cashier"}',
            '"discrepancy_amount": 86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": 86.0}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1003", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-08-04T09:00:00Z", "photo": "photo105.jpg", "digital_signature": "SIG-105"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_006",
        instruction="On 2025-07-15, at STORE-001, auditor EMP-1001 reviews inventory for SKU ELEC-4KTV55, conducts a physical count, calculates discrepancy using unit_cost $480.0, creates an inventory adjustment, requires dual approval from EMP-1003, and logs the audit with timestamp '2025-07-15T09:00:00Z', photo 'photo000a.jpg', and digital signature 'SIG-000A'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "ELEC-4KTV55"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "ELEC-4KTV55", "auditor_id": "EMP-1001"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 8, "physical_count": 8, "unit_cost": 480.0}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "ELEC-4KTV55", "amount": 0.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "ELEC-4KTV55"), "approver_id": "EMP-1003"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "ELEC-4KTV55", "auditor_id": "EMP-1001", "timestamp": "2025-07-15T09:00:00Z", "photo": "photo000a.jpg", "digital_signature": "SIG-000A"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "ELEC-4KTV55", "system_count": 8}',
            '"physical_count": 8',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "ELEC-4KTV55")}", "store_id": "STORE-001", "sku": "ELEC-4KTV55", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "ELEC-4KTV55")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "ELEC-4KTV55", "auditor_id": "EMP-1001", "timestamp": "2025-07-15T09:00:00Z", "photo": "photo000a.jpg", "digital_signature": "SIG-000A"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_007",
        instruction="Perform an audit at STORE-001 for SKU HOME-BTHTWL01. Auditor EMP-1002 will check inventory, execute a physical count (system: 100, physical: 100, unit cost: 6.0), calculate discrepancy, and document the audit with timestamp '2025-07-01T21:00:00Z', photo 'photo040.jpg', and digital signature 'SIG-040'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 100, "physical_count": 100, "unit_cost": 6.0}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "timestamp": "2025-07-01T21:00:00Z", "photo": "photo040.jpg", "digital_signature": "SIG-040"}),
        ],
        outputs=[
            '"system_count": 100',
            '"physical_count": 100',
            '"discrepancy_amount": 0.0',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "timestamp": "2025-07-01T21:00:00Z", "photo": "photo040.jpg", "digital_signature": "SIG-040"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_008",
        instruction="Audit STORE-002 for SKU CLTH-SLFJEAN34. Auditor EMP-1013 will verify inventory, perform a physical count, and log the findings. System count is 30, physical count is 30, unit cost is 22.0. Document result as discrepancy_logged. Include timestamp '2025-07-01T12:00:00Z', photo 'photo008.jpg', and digital signature 'SIG-008'. All values must be sourced from tool outputs or instructions, not assumed.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-002", "sku": "CLTH-SLFJEAN34"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-002", "sku": "CLTH-SLFJEAN34", "auditor_id": "EMP-1013"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 30, "physical_count": 30, "unit_cost": 22.0}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-002", "sku": "CLTH-SLFJEAN34", "auditor_id": "EMP-1013", "result": "discrepancy_logged", "timestamp": "2025-07-01T12:00:00Z", "photo": "photo008.jpg", "digital_signature": "SIG-008"}),
        ],
        outputs=[
            '"system_count": 30',
            '"physical_count": 30',
            '"discrepancy_amount": 0.0',
            '"audit_log": {"store_id": "STORE-002", "sku": "CLTH-SLFJEAN34", "system_count": 30, "physical_count": 30, "timestamp": "2025-07-01T12:00:00Z", "photo": "photo008.jpg", "digital_signature": "SIG-008"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_009",
        instruction=(
            "On 2025-07-02, at STORE-001, auditor EMP-1002 inspects inventory and product information for SKU HOME-DESKLMP01, retrieves employee info for EMP-1002, calculates a discrepancy (system: 45, physical: 40, unit cost: $17.2), creates an inventory adjustment, requires dual approval from EMP-1003, and documents the audit with timestamp '2025-07-02T10:00:00Z', photo 'photo009.jpg', and digital signature 'SIG-009'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetEmployeeInfo", kwargs={"employee_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1003"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-02T10:00:00Z", "photo": "photo009.jpg", "digital_signature": "SIG-009"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"product_info": {"sku": "HOME-DESKLMP01", "name": "LumiLux LED Desk Lamp", "unit_cost": 17.2}',
            '"employee_info": {"employee_id": "EMP-1002", "name": "Sarah Anderson", "role": "Cashier"}',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1003", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-02T10:00:00Z", "photo": "photo009.jpg", "digital_signature": "SIG-009"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_010",
        instruction=(
            "On 2025-07-22, at STORE-003, obtain transaction details for transaction TXN-0003. Then, initiate a recount for SKU GROC-ALMBTR500 with a discrepancy threshold of 5. Auditor EMP-2010 logs the audit with timestamp '2025-07-22T10:00:00Z', photo 'photo010.jpg', and digital signature 'SIG-010'."
        ),
        actions=[
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0003"}),
            Action(name="TriggerRecountIfNeeded", kwargs={"store_id": "STORE-003", "sku": "GROC-ALMBTR500", "discrepancy_threshold": 5}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-003", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-2010", "timestamp": "2025-07-22T10:00:00Z", "photo": "photo010.jpg", "digital_signature": "SIG-010"}),
        ],
        outputs=[
            '"transaction_details": {"transaction_id": "TXN-0003", "sku": "GROC-ALMBTR500", "quantity": 2, "total": 5.0}',
            '"recount_triggered": true',
            '"audit_log": {"store_id": "STORE-003", "sku": "GROC-ALMBTR500", "timestamp": "2025-07-22T10:00:00Z", "photo": "photo010.jpg", "digital_signature": "SIG-010"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_011",
        instruction=(
            "On 2025-07-03, at STORE-001, auditor EMP-1002 conducts a stock audit for SKU HOME-BTHTWL01. The system indicates 100 units, and the physical count matches at 100. The unit cost is $6.0. The auditor calculates the discrepancy with these values, generates an inventory adjustment for 0.0, and records the audit with timestamp '2025-07-03T09:00:00Z', photo 'photo011.jpg', and digital signature 'SIG-011'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 100, "physical_count": 100, "unit_cost": 6.0}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": 0.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "timestamp": "2025-07-03T09:00:00Z", "photo": "photo011.jpg", "digital_signature": "SIG-011"}),
        ],
        outputs=[
            '"system_count": 100',
            '"physical_count": 100',
            '"discrepancy_amount": 0.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": 0.0, "reason": "audit_discrepancy"}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "timestamp": "2025-07-03T09:00:00Z", "photo": "photo011.jpg", "digital_signature": "SIG-011"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_012",
        instruction=(
            "On 2025-07-25, at STORE-001, auditor EMP-1002 identifies a discrepancy for SKU HOME-DESKLMP01. The system reflects 45 units, while the physical count is 40, and the unit cost stands at $17.2. The auditor reviews product and employee details, initiates an inventory adjustment to address the discrepancy with reason 'audit_discrepancy', necessitates dual approval from EMP-1031, and documents the audit with auditor_id EMP-1002, timestamp '2025-07-25T09:00:00Z', photo 'photo070.jpg', and digital signature 'SIG-070'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetEmployeeInfo", kwargs={"employee_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1031"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-25T09:00:00Z", "photo": "photo070.jpg", "digital_signature": "SIG-070"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"product_info": {"sku": "HOME-DESKLMP01", "name": "LumiLux LED Desk Lamp", "unit_cost": 17.2}',
            '"employee_info": {"employee_id": "EMP-1002", "name": "Sarah Anderson", "role": "Cashier"}',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1031", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-25T09:00:00Z", "photo": "photo070.jpg", "digital_signature": "SIG-070"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_013",
        instruction=(
            "On 2025-07-05, at STORE-001, auditor EMP-1008 uncovers a discrepancy for SKU HOME-DESKLMP01. The system records 45 units, while the physical count shows 40, and the unit cost is $17.2. The auditor produces an inventory adjustment for the discrepancy with reason 'audit_discrepancy'. No dual approval is needed as the amount is below $1,000. The auditor logs the audit with timestamp '2025-07-05T09:00:00Z', photo 'photo013.jpg', and digital signature 'SIG-013'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1008"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1008", "timestamp": "2025-07-05T09:00:00Z", "photo": "photo013.jpg", "digital_signature": "SIG-013"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-013", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-05T09:00:00Z", "photo": "photo013.jpg", "digital_signature": "SIG-013"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_014",
        instruction=(
            "On 2025-07-04, at STORE-001, auditor EMP-1014 executes a stock audit for SKU HOME-DESKLMP01. The system shows 45 units, and the physical count reveals 40. The unit cost is $17.2. The auditor calculates the discrepancy with these figures, establishes an inventory adjustment with reason 'audit_discrepancy', and logs the audit with timestamp '2025-07-04T09:00:00Z', photo 'photo014.jpg', and digital signature 'SIG-014'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1014"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1014", "timestamp": "2025-07-04T09:00:00Z", "photo": "photo014.jpg", "digital_signature": "SIG-014"}),
        ],
        outputs=[
            '"system_count": 45',
            '"physical_count": 40',
            '"discrepancy_amount": 86.0',
            '"adjustment_id": "ADJ-HOME-DESKLMP01-STORE-001"',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-04T09:00:00Z", "photo": "photo014.jpg", "digital_signature": "SIG-014"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_015",
        instruction=(
            "On 2025-07-06, at STORE-001, auditor EMP-1009 discovers a discrepancy for SKU HOME-DESKLMP01. The system reports 45 units, the physical count is 40, and the unit cost is $17.2. The auditor creates an inventory adjustment for the discrepancy with reason 'audit_discrepancy'. The auditor logs the audit with timestamp '2025-07-06T09:00:00Z', photo 'photo015.jpg', and digital signature 'SIG-015'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1009"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1009", "timestamp": "2025-07-06T09:00:00Z", "photo": "photo015.jpg", "digital_signature": "SIG-015"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-015", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-06T09:00:00Z", "photo": "photo015.jpg", "digital_signature": "SIG-015"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_016",
        instruction=(
            "On 2025-07-06, at STORE-001, auditor EMP-1002 marks expired products for SKU HOME-BTHTWL01 as of 2025-07-06, retrieves product details, obtains employee information, generates an inventory adjustment for 5 expired units (unit cost $6.0, amount: -30.0, reason: 'expired_stock'), requires dual approval from EMP-1003, and records the audit with timestamp '2025-07-06T10:00:00Z', photo 'photo016.jpg', and digital signature 'SIG-016'."
        ),
        actions=[
            Action(name="FlagExpiredProducts", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "as_of_date": "2025-07-06"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-BTHTWL01"}),
            Action(name="GetEmployeeInfo", kwargs={"employee_id": "EMP-1002"}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": -30.0, "reason": "expired_stock"}),
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "HOME-BTHTWL01"), "approver_id": "EMP-1003"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "timestamp": "2025-07-06T10:00:00Z", "photo": "photo016.jpg", "digital_signature": "SIG-016"}),
        ],
        outputs=[
            '"expired_batches": ["BATCH-20240501"]',
            '"product_info": {"sku": "HOME-BTHTWL01", "name": "UltraSoft Cotton Bath Towel", "unit_cost": 6.0}',
            '"employee_info": {"employee_id": "EMP-1002", "name": "Sarah Anderson", "role": "Cashier"}',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": -30.0, "reason": "expired_stock"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "timestamp": "2025-07-06T10:00:00Z", "photo": "photo016.jpg", "digital_signature": "SIG-016"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_017",
        instruction=(
            "On 2025-07-03, at STORE-002, retrieve store inventory for SKU BAKERY-BREAD500. If the inventory counts 10 or more, implement a bulk discount of 10% on SKU BAKERY-BREAD500. Auditor EMP-1017 documents the audit with timestamp '2025-07-03T10:00:00Z', photo 'photo017.jpg', and digital signature 'SIG-017'. (In this instance, inventory is 0, hence no discount is applied.)"
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-002", "sku": "BAKERY-BREAD500"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-002", "sku": "BAKERY-BREAD500", "auditor_id": "EMP-1017", "timestamp": "2025-07-03T10:00:00Z", "photo": "photo017.jpg", "digital_signature": "SIG-017"}),
        ],
        outputs=[
            '"system_count": 0',
            '"audit_log": {"store_id": "STORE-002", "sku": "BAKERY-BREAD500", "timestamp": "2025-07-03T10:00:00Z", "photo": "photo017.jpg", "digital_signature": "SIG-017"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_018",
        instruction=(
            "On 2025-07-24, at STORE-001, auditor EMP-1002 identifies a discrepancy for SKU HOME-DESKLMP01. The system indicates 45 units, the physical count is 40, and the unit cost is $17.2. The auditor generates an inventory adjustment for the discrepancy, requests dual approval from EMP-1003, and documents the audit with timestamp '2025-07-24T09:00:00Z', photo 'photo068.jpg', and digital signature 'SIG-068'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1003"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-24T09:00:00Z", "photo": "photo068.jpg", "digital_signature": "SIG-068"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1003", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-24T09:00:00Z", "photo": "photo068.jpg", "digital_signature": "SIG-068"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_019",
        instruction=(
            "On 2025-07-05, at STORE-001, auditor EMP-1019 conducts a stock audit for SKU HOME-DESKLMP01. The system shows 45 units, and the physical count is 40. The unit cost stands at $17.2. The auditor computes the discrepancy with these values, establishes an inventory adjustment with reason 'audit_discrepancy', and logs the audit with timestamp '2025-07-05T12:00:00Z', photo 'photo019.jpg', and digital signature 'SIG-019'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1019"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1019", "timestamp": "2025-07-05T12:00:00Z", "photo": "photo019.jpg", "digital_signature": "SIG-019"}),
        ],
        outputs=[
            '"system_count": 45',
            '"physical_count": 40',
            '"discrepancy_amount": 86.0',
            '"adjustment_id": "ADJ-HOME-DESKLMP01-STORE-001"',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-05T12:00:00Z", "photo": "photo019.jpg", "digital_signature": "SIG-019"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_020",
        instruction="Conduct an audit at STORE-001, SKU HOME-BTHTWL01. Auditor EMP-1033 will verify inventory, carry out a physical count (system: 100, physical: 100, unit cost: 6.0), calculate the discrepancy, and document the audit with timestamp '2025-07-01T21:00:00Z', photo 'photo020.jpg', and digital signature 'SIG-020'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1033"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 100, "physical_count": 100, "unit_cost": 6.0}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1033", "result": "discrepancy_logged", "timestamp": "2025-07-01T21:00:00Z", "photo": "photo020.jpg", "digital_signature": "SIG-020"}),
        ],
        outputs=[
            '"system_count": 100',
            '"physical_count": 100',
            '"discrepancy_amount": 0.0',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "timestamp": "2025-07-01T21:00:00Z", "photo": "photo020.jpg", "digital_signature": "SIG-020"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_021",
        instruction="Handle audit for STORE-003, SKU ELEC-RCHAA04. Auditor EMP-1015 will review inventory, execute a physical count, and record the outcome. System count is 90, physical count is 90, unit cost is 9.9. Record outcome as discrepancy_logged.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "auditor_id": "EMP-1015"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 90, "physical_count": 90, "unit_cost": 9.9}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "auditor_id": "EMP-1015", "result": "discrepancy_logged"}),
        ],
        outputs=[
            '"system_count": 90',
            '"physical_count": 90',
            '"discrepancy_amount": 0',
            '"audit_log": {"store_id": "STORE-003", "sku": "ELEC-RCHAA04"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_022",
        instruction="Conduct an audit for STORE-002, SKU CLTH-WINJKT01. Auditor EMP-1016 will assess inventory, carry out a physical count, and record the outcome. System count is 6, physical count is 6, unit cost is 110.0. Record outcome as discrepancy_logged. Add timestamp '2025-07-01T22:00:00Z', photo 'photo022.jpg', and digital signature 'SIG-022'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-002", "sku": "CLTH-WINJKT01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-002", "sku": "CLTH-WINJKT01", "auditor_id": "EMP-1016"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 6, "physical_count": 6, "unit_cost": 110.0}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-002", "sku": "CLTH-WINJKT01", "auditor_id": "EMP-1016", "result": "discrepancy_logged", "timestamp": "2025-07-01T22:00:00Z", "photo": "photo022.jpg", "digital_signature": "SIG-022"}),
        ],
        outputs=[
            '"system_count": 6',
            '"physical_count": 6',
            '"discrepancy_amount": 0',
            '"audit_log": {"store_id": "STORE-002", "sku": "CLTH-WINJKT01"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_023",
        instruction="Perform an audit for STORE-002, SKU SMRT-THERM02. Auditor EMP-1008 will review inventory, execute a physical count (system: 15, physical: 15, unit cost: 98.0), calculate discrepancy, create an inventory adjustment, and log audit with timestamp '2025-07-01T18:30:00Z', photo 'photo050.jpg', and digital signature 'SIG-050'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-002", "sku": "SMRT-THERM02"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-002", "sku": "SMRT-THERM02", "auditor_id": "EMP-1008"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 15, "physical_count": 15, "unit_cost": 98.0}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-002", "sku": "SMRT-THERM02", "amount": 0.0}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-002", "sku": "SMRT-THERM02", "auditor_id": "EMP-1008", "timestamp": "2025-07-01T18:30:00Z", "photo": "photo050.jpg", "digital_signature": "SIG-050"}),
        ],
        outputs=[
            '"system_count": 15',
            '"physical_count": 15',
            '"discrepancy_amount": 0.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-SMRT-THERM02-STORE-002", "store_id": "STORE-002", "sku": "SMRT-THERM02", "amount": 0.0}',
            '"audit_log": {"store_id": "STORE-002", "sku": "SMRT-THERM02", "timestamp": "2025-07-01T18:30:00Z", "photo": "photo050.jpg", "digital_signature": "SIG-050"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_024",
        instruction="Conduct an audit for STORE-002, SKU AUDIO-NCEBUDS01. Auditor EMP-1018 will assess inventory, perform a physical count, and record the outcome. System count is 22, physical count is 22, unit cost is 82.0. Record outcome as discrepancy_logged.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-002", "sku": "AUDIO-NCEBUDS01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-002", "sku": "AUDIO-NCEBUDS01", "auditor_id": "EMP-1018"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 22, "physical_count": 22, "unit_cost": 82.0}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-002", "sku": "AUDIO-NCEBUDS01", "auditor_id": "EMP-1018", "result": "discrepancy_logged"}),
        ],
        outputs=[
            '"system_count": 22',
            '"physical_count": 22',
            '"discrepancy_amount": 0',
            '"audit_log": {"store_id": "STORE-002", "sku": "AUDIO-NCEBUDS01"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_025",
        instruction="Carry out an audit for STORE-001, SKU SPORT-YOGMAT01. Auditor EMP-1019 will check inventory, execute a physical count, and record the outcome. System count is 60, physical count is 60, unit cost is 13.8. Record outcome as discrepancy_logged.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "SPORT-YOGMAT01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "SPORT-YOGMAT01", "auditor_id": "EMP-1019"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 60, "physical_count": 60, "unit_cost": 13.8}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "SPORT-YOGMAT01", "auditor_id": "EMP-1019", "result": "discrepancy_logged"}),
        ],
        outputs=[
            '"system_count": 60',
            '"physical_count": 60',
            '"discrepancy_amount": 0',
            '"audit_log": {"store_id": "STORE-001", "sku": "SPORT-YOGMAT01"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_026",
        instruction=(
            "On 2025-07-10, at STORE-001, auditor EMP-1012 identifies a discrepancy for SKU HOME-DESKLMP01. The system shows 45 units, physical count is 40, and the unit cost is $17.2. The auditor creates an inventory adjustment for the discrepancy with reason 'audit_discrepancy'. The auditor records the audit with timestamp '2025-07-10T09:00:00Z', photo 'photo026.jpg', and digital signature 'SIG-026'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1012"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1012", "timestamp": "2025-07-10T09:00:00Z", "photo": "photo026.jpg", "digital_signature": "SIG-026"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-026", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-10T09:00:00Z", "photo": "photo026.jpg", "digital_signature": "SIG-026"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_027",
        instruction="Execute an audit for STORE-003, SKU KITCH-FRYPAN10. Auditor EMP-1015 will review inventory, perform a physical count (system: 40, physical: 40, unit cost: 12.2), calculate discrepancy, and log audit with timestamp '2025-07-01T13:30:00Z', photo 'photo027.jpg', and digital signature 'SIG-027'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-003", "sku": "KITCH-FRYPAN10"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-003", "sku": "KITCH-FRYPAN10", "auditor_id": "EMP-1015"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 40, "physical_count": 40, "unit_cost": 12.2}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-003", "sku": "KITCH-FRYPAN10", "auditor_id": "EMP-1015", "result": "discrepancy_logged", "timestamp": "2025-07-01T13:30:00Z", "photo": "photo027.jpg", "digital_signature": "SIG-027"}),
        ],
        outputs=[
            '"system_count": 40',
            '"physical_count": 40',
            '"discrepancy_amount": 0.0',
            '"audit_log": {"store_id": "STORE-003", "sku": "KITCH-FRYPAN10", "timestamp": "2025-07-01T13:30:00Z", "photo": "photo027.jpg", "digital_signature": "SIG-027"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_028",
        instruction="Following a transfer from STORE-002 to STORE-003 for SKU CLTH-SLFJEAN34, if a loss is identified, Auditor EMP-1004 will review inventory and perform a physical count. Utilize the system_count as the quantity returned by the inventory check and the physical_count from the physical count. Acquire unit cost from product information. If a loss is detected, adjust the inventory and document the outcome, adhering to all required approval and audit procedures. All values must be derived from tool outputs or the instruction, not assumed.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-002", "sku": "CLTH-SLFJEAN34"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-002", "sku": "CLTH-SLFJEAN34", "auditor_id": "EMP-1004"}),
            Action(name="GetProductInfo", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={
                "system_count": 30,
                "physical_count": 30,
                "unit_cost": 22.0
            }),
            Action(name="CreateInventoryAdjustment", kwargs={
                "store_id": "STORE-002",
                "sku": "CLTH-SLFJEAN34",
                "amount": 0.0,
                "reason": "transfer_loss"
            }),
            Action(name="DualApproval", kwargs={
                "adjustment_id": adj_id("STORE-002", "CLTH-SLFJEAN34")
            }),
            Action(name="LogAuditResult", kwargs={
                "store_id": "STORE-002",
                "sku": "CLTH-SLFJEAN34",
                "auditor_id": "EMP-1004",
                "result": "discrepancy_logged",
                "timestamp": "2025-07-01T18:40:00Z",
                "photo": "photo028.jpg",
                "digital_signature": "SIG-028"
            }),
        ],
        outputs=[
            '"system_count": 30',
            '"physical_count": 30',
            '"discrepancy_amount": 0.0',
            f'"adjustment_id": "{adj_id("STORE-002", "CLTH-SLFJEAN34")}"',
            '"dual_approved": true',
            '"audit_log": {"store_id": "STORE-002", "sku": "CLTH-SLFJEAN34", "timestamp": "2025-07-01T18:40:00Z", "photo": "photo028.jpg", "digital_signature": "SIG-028"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_029",
        instruction=(
            "On 2025-07-11, at STORE-001, auditor EMP-1013 discovers a discrepancy for SKU HOME-DESKLMP01. The system shows 45 units, physical count is 40, and the unit cost is $17.2. The auditor creates an inventory adjustment for the discrepancy with reason 'audit_discrepancy', and logs the audit with auditor_id EMP-1013, timestamp '2025-07-11T09:00:00Z', photo 'photo029.jpg', and digital signature 'SIG-029'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1013"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1013", "timestamp": "2025-07-11T09:00:00Z", "photo": "photo029.jpg", "digital_signature": "SIG-029"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1013", "timestamp": "2025-07-11T09:00:00Z", "photo": "photo029.jpg", "digital_signature": "SIG-029"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_030",
        instruction=(
            "On 2025-07-11, at STORE-001, auditor EMP-1030 conducts a stock audit for SKU HOME-DESKLMP01. The system shows 45 units, and the physical count is 40. The unit cost is $17.2. The auditor computes the discrepancy using these values, creates an inventory adjustment with reason 'audit_discrepancy', and logs the audit with timestamp '2025-07-11T09:00:00Z', photo 'photo030.jpg', and digital signature 'SIG-030'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1030"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1030", "timestamp": "2025-07-11T09:00:00Z", "photo": "photo030.jpg", "digital_signature": "SIG-030"}),
        ],
        outputs=[
            '"system_count": 45',
            '"physical_count": 40',
            '"discrepancy_amount": 86.0',
            '"adjustment_id": "ADJ-HOME-DESKLMP01-STORE-001"',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-11T09:00:00Z", "photo": "photo030.jpg", "digital_signature": "SIG-030"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_031",
        instruction=(
            "On 2025-07-12, at STORE-001, auditor EMP-1031 conducts a stock audit for SKU HOME-DESKLMP01. The system displays 45 units, and the physical count is 40. The unit cost is $17.2. The auditor calculates the discrepancy using these values, generates an inventory adjustment with reason 'audit_discrepancy', and records the audit with timestamp '2025-07-12T09:00:00Z', photo 'photo031.jpg', and digital signature 'SIG-031'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1031"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1031", "timestamp": "2025-07-12T09:00:00Z", "photo": "photo031.jpg", "digital_signature": "SIG-031"}),
        ],
        outputs=[
            '"system_count": 45',
            '"physical_count": 40',
            '"discrepancy_amount": 86.0',
            '"adjustment_id": "ADJ-HOME-DESKLMP01-STORE-001"',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-12T09:00:00Z", "photo": "photo031.jpg", "digital_signature": "SIG-031"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_032",
        instruction="Conduct an audit at STORE-002 for SKU SMRT-THERM02. Auditor EMP-1008 will review inventory, carry out a physical count, and document the result. System count is 15, physical count is 15, unit cost is 98.0. Document result as discrepancy_logged.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-002", "sku": "SMRT-THERM02"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-002", "sku": "SMRT-THERM02", "auditor_id": "EMP-1008"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 15, "physical_count": 15, "unit_cost": 98.0}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-002", "sku": "SMRT-THERM02", "auditor_id": "EMP-1008", "result": "discrepancy_logged"}),
        ],
        outputs=[
            '"system_count": 15',
            '"physical_count": 15',
            '"discrepancy_amount": 0',
            '"audit_log": {"store_id": "STORE-002", "sku": "SMRT-THERM02"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_033",
        instruction="Facilitate the transfer of 12 units of BOOK-KDSSTY01 from STORE-001 to STORE-003. Document and update compliance.",
        actions=[
            Action(name="CheckSafetyStock", kwargs={"store_id": "STORE-001", "sku": "BOOK-KDSSTY01", "min_percent": 20}),
            Action(name="CreateTransferOrder", kwargs={"from_store": "STORE-001", "to_store": "STORE-003", "sku": "BOOK-KDSSTY01", "quantity": 12}),
            Action(name="LogTransfer", kwargs={"from_store": "STORE-001", "to_store": "STORE-003", "sku": "BOOK-KDSSTY01", "quantity": 12}),
            Action(name="UpdateTransferCompliance", kwargs={"transfer_id": trf_id("STORE-001", "STORE-003", "BOOK-KDSSTY01"), "status": "logged"}),
        ],
        outputs=[
            f'"transfer_id": "{trf_id("STORE-001", "STORE-003", "BOOK-KDSSTY01")}"',
            '"compliance_status": "logged"'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_034",
        instruction="Conduct an audit at STORE-003 for SKU ELEC-RCHAA04. Auditor EMP-1015 will review inventory, perform a physical count (system: 90, physical: 90, unit cost: 9.9), calculate the discrepancy, and only initiate a recount if the discrepancy surpasses the threshold of 40. Utilize the threshold of 40. Record the audit with timestamp '2025-07-01T16:00:00Z', photo 'photo034.jpg', and digital signature 'SIG-034'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "auditor_id": "EMP-1015"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 90, "physical_count": 90, "unit_cost": 9.9}),
            # No recount triggered since discrepancy is 0, which is below threshold
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "auditor_id": "EMP-1015", "result": "discrepancy_logged", "timestamp": "2025-07-01T16:00:00Z", "photo": "photo034.jpg", "digital_signature": "SIG-034"}),
        ],
        outputs=[
            '"system_count": 90',
            '"physical_count": 90',
            '"discrepancy_amount": 0.0',
            '"audit_log": {"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "timestamp": "2025-07-01T16:00:00Z", "photo": "photo034.jpg", "digital_signature": "SIG-034"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_035",
        instruction="Facilitate the transfer of 8 units of HOME-DESKLMP01 from STORE-001 to STORE-002. A compliance review is required for policy adherence.",
        actions=[
            Action(name="CheckSafetyStock", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "min_percent": 20}),
            Action(name="CreateTransferOrder", kwargs={"from_store": "STORE-001", "to_store": "STORE-002", "sku": "HOME-DESKLMP01", "quantity": 8}),
            Action(name="ComplianceReview", kwargs={"transfer_id": trf_id("STORE-001", "STORE-002", "HOME-DESKLMP01")}),
            Action(name="LogTransfer", kwargs={"from_store": "STORE-001", "to_store": "STORE-002", "sku": "HOME-DESKLMP01", "quantity": 8}),
            Action(name="UpdateTransferCompliance", kwargs={"transfer_id": trf_id("STORE-001", "STORE-002", "HOME-DESKLMP01"), "status": "compliance_reviewed"}),
        ],
        outputs=[
            f'"transfer_id": "{trf_id("STORE-001", "STORE-002", "HOME-DESKLMP01")}"',
            '"compliance_reviewed": true',
            '"compliance_status": "compliance_reviewed"'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_036",
        instruction="Conduct an audit at STORE-002 for SKU CLTH-WINJKT01. Auditor EMP-1009 will review inventory, perform a physical count (system: 6, physical: 6, unit cost: 110.0), calculate discrepancy, and record the audit with timestamp '2025-07-01T17:00:00Z', photo 'photo036.jpg', and digital signature 'SIG-036'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-002", "sku": "CLTH-WINJKT01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-002", "sku": "CLTH-WINJKT01", "auditor_id": "EMP-1009"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 6, "physical_count": 6, "unit_cost": 110.0}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-002", "sku": "CLTH-WINJKT01", "auditor_id": "EMP-1009", "result": "discrepancy_logged", "timestamp": "2025-07-01T17:00:00Z", "photo": "photo036.jpg", "digital_signature": "SIG-036"}),
        ],
        outputs=[
            '"system_count": 6',
            '"physical_count": 6',
            '"discrepancy_amount": 0.0',
            '"audit_log": {"store_id": "STORE-002", "sku": "CLTH-WINJKT01", "timestamp": "2025-07-01T17:00:00Z", "photo": "photo036.jpg", "digital_signature": "SIG-036"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_037",
        instruction=(
            "On 2025-07-02, at STORE-001, auditor EMP-1002 identifies a discrepancy for SKU HOME-DESKLMP01. The system displays 45 units, physical count is 40, and the unit cost is $17.2. The auditor generates an inventory adjustment for the discrepancy with reason 'audit_discrepancy', and records the audit with result 'discrepancy_logged', timestamp '2025-07-02T09:00:00Z', photo 'photo002.jpg', and digital signature 'SIG-002'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "result": "discrepancy_logged", "timestamp": "2025-07-02T09:00:00Z", "photo": "photo002.jpg", "digital_signature": "SIG-002"}),
        ],
        outputs=[
            '"system_count": 45',
            '"physical_count": 40',
            '"discrepancy_amount": 86.0',
            '"adjustment_id": "ADJ-AAD81F"',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-02T09:00:00Z", "photo": "photo002.jpg", "digital_signature": "SIG-002"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_038",
        instruction=(
            "On 2025-07-12, at STORE-001, auditor EMP-1002 detects a major discrepancy for SKU HOME-DESKLMP01. The system shows 45 units, physical count is 40, and the unit cost is $17.2. The auditor verifies product and employee information, generates an inventory adjustment for the discrepancy with reason 'audit_discrepancy', escalates the discrepancy to the regional level, and documents the audit with timestamp '2025-07-12T09:00:00Z', photo 'photo038.jpg', and digital signature 'SIG-038'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetEmployeeInfo", kwargs={"employee_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="EscalateDiscrepancy", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": 86.0, "escalation_level": "regional"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-12T09:00:00Z", "photo": "photo038.jpg", "digital_signature": "SIG-038"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"product_info": {"sku": "HOME-DESKLMP01", "name": "LumiLux LED Desk Lamp", "unit_cost": 17.2}',
            '"employee_info": {"employee_id": "EMP-1002", "name": "Sarah Anderson", "role": "Cashier"}',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"escalation": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": 86.0, "escalation_level": "regional"}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-12T09:00:00Z", "photo": "photo038.jpg", "digital_signature": "SIG-038"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_039",
        instruction=(
            "On 2025-07-12, at STORE-001, auditor EMP-1013 identifies a discrepancy for SKU HOME-DESKLMP01. The system shows 45 units, physical count is 40, and the unit cost is $17.2. The auditor generates an inventory adjustment for the discrepancy with reason 'audit_discrepancy', requires dual approval by EMP-1014, and records the audit with timestamp '2025-07-12T10:00:00Z', photo 'photo039.jpg', and digital signature 'SIG-039'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1013"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1014"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1013", "timestamp": "2025-07-12T10:00:00Z", "photo": "photo039.jpg", "digital_signature": "SIG-039"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1014", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1013", "timestamp": "2025-07-12T10:00:00Z", "photo": "photo039.jpg", "digital_signature": "SIG-039"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_040",
        instruction="Conduct an audit at STORE-001 for SKU HOME-BTHTWL01. Auditor EMP-1002 will review inventory, perform a physical count (system: 100, physical: 100, unit cost: 6.0), calculate discrepancy, and document the audit with timestamp '2025-07-01T21:00:00Z', photo 'photo040.jpg', and digital signature 'SIG-040'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 100, "physical_count": 100, "unit_cost": 6.0}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "result": "discrepancy_logged", "timestamp": "2025-07-01T21:00:00Z", "photo": "photo040.jpg", "digital_signature": "SIG-040"}),
        ],
        outputs=[
            '"system_count": 100',
            '"physical_count": 100',
            '"discrepancy_amount": 0.0',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "timestamp": "2025-07-01T21:00:00Z", "photo": "photo040.jpg", "digital_signature": "SIG-040"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_041",
        instruction="Review STORE-003, SKU ELEC-RCHAA04. Auditor EMP-1015 will verify inventory, conduct a physical count, and document the outcome. System count is 90, physical count is 90, unit cost is 9.9. Record the result as discrepancy_logged.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "auditor_id": "EMP-1015"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 90, "physical_count": 90, "unit_cost": 9.9}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "auditor_id": "EMP-1015", "result": "discrepancy_logged"}),
        ],
        outputs=[
            '"system_count": 90',
            '"physical_count": 90',
            '"discrepancy_amount": 0.0',
            '"audit_log": {"store_id": "STORE-003", "sku": "ELEC-RCHAA04"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_042",
        instruction="Move 12 units of BOOK-KDSSTY01 from STORE-001 to STORE-003. Record and update compliance.",
        actions=[
            Action(name="CheckSafetyStock", kwargs={"store_id": "STORE-001", "sku": "BOOK-KDSSTY01", "min_percent": 20}),
            Action(name="CreateTransferOrder", kwargs={"from_store": "STORE-001", "to_store": "STORE-003", "sku": "BOOK-KDSSTY01", "quantity": 12}),
            Action(name="LogTransfer", kwargs={"from_store": "STORE-001", "to_store": "STORE-003", "sku": "BOOK-KDSSTY01", "quantity": 12}),
            Action(name="UpdateTransferCompliance", kwargs={"transfer_id": trf_id("STORE-001", "STORE-003", "BOOK-KDSSTY01"), "status": "logged"}),
        ],
        outputs=[
            f'"transfer_id": "{trf_id("STORE-001", "STORE-003", "BOOK-KDSSTY01")}"',
            '"compliance_status": "logged"'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_043",
        instruction="Review STORE-003, SKU ELEC-RCHAA04. Auditor EMP-1015 will verify inventory and conduct a physical count. Utilize the system_count from get_store_inventory (90) and the physical_count from get_physical_count (90). Calculate the discrepancy using these values and the unit cost from products.json (9.9). Since the discrepancy is 0, refrain from triggering a recount (threshold is 40). Document the audit with result 'discrepancy_logged', timestamp '2025-07-01T22:00:00Z', photo 'photo043.jpg', and digital signature 'SIG-043'. All values must be derived from tool outputs or the instruction, not assumed.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "auditor_id": "EMP-1015"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 90, "physical_count": 90, "unit_cost": 9.9}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "auditor_id": "EMP-1015", "result": "discrepancy_logged", "timestamp": "2025-07-01T22:00:00Z", "photo": "photo043.jpg", "digital_signature": "SIG-043"}),
        ],
        outputs=[
            '"system_count": 90',
            '"physical_count": 90',
            '"discrepancy_amount": 0.0',
            '"audit_log": {"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "timestamp": "2025-07-01T22:00:00Z", "photo": "photo043.jpg", "digital_signature": "SIG-043"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_044",
        instruction="Move 8 units of HOME-DESKLMP01 from STORE-001 to STORE-002. Compliance review necessary for policy.",
        actions=[
            Action(name="CheckSafetyStock", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "min_percent": 20}),
            Action(name="CreateTransferOrder", kwargs={"from_store": "STORE-001", "to_store": "STORE-002", "sku": "HOME-DESKLMP01", "quantity": 8}),
            Action(name="ComplianceReview", kwargs={"transfer_id": trf_id("STORE-001", "STORE-002", "HOME-DESKLMP01")}),
            Action(name="LogTransfer", kwargs={"from_store": "STORE-001", "to_store": "STORE-002", "sku": "HOME-DESKLMP01", "quantity": 8}),
            Action(name="UpdateTransferCompliance", kwargs={"transfer_id": trf_id("STORE-001", "STORE-002", "HOME-DESKLMP01"), "status": "compliance_reviewed"}),
        ],
        outputs=[
            f'"transfer_id": "{trf_id("STORE-001", "STORE-002", "HOME-DESKLMP01")}"',
            '"compliance_reviewed": true',
            '"compliance_status": "compliance_reviewed"'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_045",
        instruction="Review STORE-002, SKU CLTH-WINJKT01. Auditor EMP-1009 will verify inventory, conduct a physical count (system: 6, physical: 6, unit cost: 110.0), calculate the discrepancy, and document the audit with timestamp '2025-07-01T23:00:00Z', photo 'photo045.jpg', and digital signature 'SIG-045'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-002", "sku": "CLTH-WINJKT01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-002", "sku": "CLTH-WINJKT01", "auditor_id": "EMP-1009"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 6, "physical_count": 6, "unit_cost": 110.0}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-002", "sku": "CLTH-WINJKT01", "auditor_id": "EMP-1009", "result": "discrepancy_logged", "timestamp": "2025-07-01T23:00:00Z", "photo": "photo045.jpg", "digital_signature": "SIG-045"}),
        ],
        outputs=[
            '"system_count": 6',
            '"physical_count": 6',
            '"discrepancy_amount": 0.0',
            '"audit_log": {"store_id": "STORE-002", "sku": "CLTH-WINJKT01", "timestamp": "2025-07-01T23:00:00Z", "photo": "photo045.jpg", "digital_signature": "SIG-045"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_046",
        instruction=(
            "On 2025-07-12, at STORE-001, auditor EMP-1013 discovers a discrepancy for SKU HOME-DESKLMP01. The system indicates 45 units, physical count is 40, and the unit cost is $17.2. The auditor generates an inventory adjustment for the discrepancy with reason 'audit_discrepancy', requires dual approval by EMP-1014, and documents the audit with timestamp '2025-07-12T10:00:00Z', photo 'photo039.jpg', and digital signature 'SIG-039'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1013"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1014"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1013", "timestamp": "2025-07-12T10:00:00Z", "photo": "photo039.jpg", "digital_signature": "SIG-039"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1014", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1013", "timestamp": "2025-07-12T10:00:00Z", "photo": "photo039.jpg", "digital_signature": "SIG-039"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_047",
        instruction=(
            "On 2025-08-24, at STORE-003, auditor EMP-3001 enumerates all SKUs, checks for active promotions for SKU ELEC-RCHAA04, and documents the audit with result 'promotion_checked', timestamp '2025-08-24T11:00:00Z', photo 'photo077_new.jpg', and digital signature 'SIG-077N'. If any validation fails, stop and refrain from executing further actions."
        ),
        actions=[
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-003"}),
            # Only proceed if SKU list succeeds:
            Action(name="ListActivePromotions", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "auditor_id": "EMP-3001", "result": "promotion_checked", "timestamp": "2025-08-24T11:00:00Z", "photo": "photo077_new.jpg", "digital_signature": "SIG-077N"}),
        ],
        outputs=[
            '"skus": ["ELEC-RCHAA04", "HOME-BTHTWL01", "GROC-ALMBTR500"]',
            '"active_promotions": ["PROMO-10PCT-OFF", "PROMO-BUY1GET1"]',
            '"audit_log": {"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "auditor_id": "EMP-3001", "result": "promotion_checked", "timestamp": "2025-08-24T11:00:00Z", "photo": "photo077_new.jpg", "digital_signature": "SIG-077N"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_048",
        instruction="Review STORE-001, SKU BOOK-KDSSTY01. Auditor EMP-1002 will verify inventory, conduct a physical count (system: 40, physical: 40, unit cost: 4.2), calculate the discrepancy, and escalate to compliance only if the discrepancy exceeds $40. Document the audit with timestamp '2025-07-01T17:30:00Z', photo 'photo048.jpg', and digital signature 'SIG-048'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "BOOK-KDSSTY01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "BOOK-KDSSTY01", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 40, "physical_count": 40, "unit_cost": 4.2}),
            # No escalation since discrepancy is 0, which is not > $40
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "BOOK-KDSSTY01", "auditor_id": "EMP-1002", "result": "discrepancy_logged", "timestamp": "2025-07-01T17:30:00Z", "photo": "photo048.jpg", "digital_signature": "SIG-048"}),
        ],
        outputs=[
            '"system_count": 40',
            '"physical_count": 40',
            '"discrepancy_amount": 0.0',
            '"escalated": false',
            '"audit_log": {"store_id": "STORE-001", "sku": "BOOK-KDSSTY01", "timestamp": "2025-07-01T17:30:00Z", "photo": "photo048.jpg", "digital_signature": "SIG-048"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_049",
        instruction=(
            "On 2025-07-15, at STORE-001, auditor EMP-1015 identifies a discrepancy for SKU HOME-DESKLMP01. The system indicates 45 units, physical count is 40, and the unit cost is $17.2. The auditor generates an inventory adjustment for the discrepancy with reason 'audit_discrepancy', requires dual approval by EMP-1016, and documents the audit with timestamp '2025-07-15T09:00:00Z', photo 'photo049.jpg', and digital signature 'SIG-049'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1015"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1016"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1015", "timestamp": "2025-07-15T09:00:00Z", "photo": "photo049.jpg", "digital_signature": "SIG-049"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1016", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-15T09:00:00Z", "photo": "photo049.jpg", "digital_signature": "SIG-049"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_050",
        instruction=(
            "On 2025-08-04, at STORE-001, auditor EMP-1002 verifies inventory and product information for SKU HOME-DESKLMP01, retrieves employee information for EMP-1002, calculates a discrepancy (system: 45, physical: 40, unit cost: $17.2), creates an inventory adjustment, requires dual approval by EMP-1003, and documents the audit with timestamp '2025-08-04T09:00:00Z', photo 'photo105.jpg', and digital signature 'SIG-105'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetEmployeeInfo", kwargs={"employee_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": 86.0}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1003"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-08-04T09:00:00Z", "photo": "photo105.jpg", "digital_signature": "SIG-105"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"product_info": {"sku": "HOME-DESKLMP01", "name": "LumiLux LED Desk Lamp", "unit_cost": 17.2}',
            '"employee_info": {"employee_id": "EMP-1002", "name": "Sarah Anderson", "role": "Cashier"}',
            '"discrepancy_amount": 86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": 86.0}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1003", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-08-04T09:00:00Z", "photo": "photo105.jpg", "digital_signature": "SIG-105"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_051",
        instruction="Handle the transfer of 12 units of BOOK-KDSSTY01 from STORE-001 to STORE-003. Document and refresh compliance.",
        actions=[
            Action(name="CheckSafetyStock", kwargs={"store_id": "STORE-001", "sku": "BOOK-KDSSTY01", "min_percent": 20}),
            Action(name="CreateTransferOrder", kwargs={"from_store": "STORE-001", "to_store": "STORE-003", "sku": "BOOK-KDSSTY01", "quantity": 12}),
            Action(name="LogTransfer", kwargs={"from_store": "STORE-001", "to_store": "STORE-003", "sku": "BOOK-KDSSTY01", "quantity": 12}),
            Action(name="UpdateTransferCompliance", kwargs={"transfer_id": trf_id("STORE-001", "STORE-003", "BOOK-KDSSTY01"), "status": "logged"}),
        ],
        outputs=[
            f'"transfer_id": "{trf_id("STORE-001", "STORE-003", "BOOK-KDSSTY01")}"',
            '"compliance_status": "logged"'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_052",
        instruction="At STORE-001, replenish 10 units of SKU HOME-DESKLMP01, verify inventory, retrieve product and employee information for EMP-1002, and record the audit with timestamp '2025-07-15T09:00:00Z', photo 'photo052.jpg', and digital signature 'SIG-052'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="RestockLowInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "quantity": 10}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetEmployeeInfo", kwargs={"employee_id": "EMP-1002"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-15T09:00:00Z", "photo": "photo052.jpg", "digital_signature": "SIG-052"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"restock_triggered": true',
            '"product_info": {"sku": "HOME-DESKLMP01", "name": "Desk Lamp", "unit_cost": 17.2}',
            '"employee_info": {"employee_id": "EMP-1002", "name": "Sarah Anderson", "role": "Cashier"}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-15T09:00:00Z", "photo": "photo052.jpg", "digital_signature": "SIG-052"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_053",
        instruction="On 2025-07-10, at STORE-001, auditor EMP-1002 verifies inventory for SKU GROC-ALMBTR500. The system count reports 60 (from inventory), the physical count is 60 (from get_physical_count), and the unit cost is $7.85 (from get_product_info). The auditor calculates the discrepancy, generates an inventory adjustment, and records the audit with timestamp '2025-07-10T09:00:00Z', photo 'photo053.jpg', and digital signature 'SIG-053'. If any validation fails (including if get_store_inventory, get_physical_count, or get_product_info returns empty or fails), cease operations and refrain from additional actions. All parameters must be derived from tool outputs or the instruction.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1002"}),
            Action(name="GetProductInfo", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 60, "physical_count": 60, "unit_cost": 7.85}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "amount": 0.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1002", "timestamp": "2025-07-10T09:00:00Z", "photo": "photo053.jpg", "digital_signature": "SIG-053"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "system_count": 60}',
            '"physical_count": 60',
            '"product_info": {"sku": "GROC-ALMBTR500", "name": "Organic Almond Butter 500g", "unit_cost": 7.85}',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "GROC-ALMBTR500")}", "store_id": "STORE-001", "sku": "GROC-ALMBTR500", "amount": 0.0, "reason": "audit_discrepancy"}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1002", "timestamp": "2025-07-10T09:00:00Z", "photo": "photo053.jpg", "digital_signature": "SIG-053"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_054",
        instruction="On 2025-07-11, at STORE-001, auditor EMP-1002 verifies inventory for SKU HOME-DESKLMP01, gathers complete product information (all fields), conducts a physical count, calculates the discrepancy as (system_count - physical_count) × unit_cost (should be positive if system_count > physical_count), produces an inventory adjustment, and records the audit with timestamp '2025-07-11T09:00:00Z', photo 'photo054.jpg', and digital signature 'SIG-054'. If any validation fails (including if get_store_inventory, get_product_info, or get_physical_count returns empty or fails), cease operations and refrain from additional actions. All parameters must be derived from tool outputs or the instruction.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": 86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-11T09:00:00Z", "photo": "photo054.jpg", "digital_signature": "SIG-054"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"product_info": {"sku": "HOME-DESKLMP01", "name": "LumiLux LED Desk Lamp", "unit_cost": 17.2, "category": "Home & Kitchen", "price": 34.99, "description": "Dimmable LED lamp with USB charging port and color modes.", "brand": "LumiLux", "status": "active", "barcode": "0123456789022", "tax_rate": 0.0825, "discount_rate": 0.08, "supplier_id": "SUP-1002", "weight_kg": 1.1, "dimensions_cm": "18x18x42", "created_at": "2025-02-18T10:12:00Z", "updated_at": "2025-05-03T10:12:00Z"}',
            '"physical_count": 40',
            '"discrepancy_amount": 86.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "HOME-DESKLMP01")}", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": 86.0, "reason": "audit_discrepancy"}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-11T09:00:00Z", "photo": "photo054.jpg", "digital_signature": "SIG-054"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_055",
        instruction="On 2025-07-16, at STORE-001, auditor EMP-1002 verifies inventory for SKU HOME-DESKLMP01, retrieves product information, conducts a physical count, calculates the discrepancy using unit_cost $17.2, generates an inventory adjustment, seeks approval from EMP-1003, and records the audit with timestamp '2025-07-16T10:00:00Z', photo 'photo000b.jpg', and digital signature 'SIG-000B'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "HOME-DESKLMP01"), "approver_id": "EMP-1003"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-16T10:00:00Z", "photo": "photo000b.jpg", "digital_signature": "SIG-000B"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"product_info": {"sku": "HOME-DESKLMP01", "name": "LumiLux LED Desk Lamp", "unit_cost": 17.2}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "HOME-DESKLMP01")}", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "HOME-DESKLMP01")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1002", "timestamp": "2025-07-16T10:00:00Z", "photo": "photo000b.jpg", "digital_signature": "SIG-000B"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_056",
        instruction=(
            "On 2025-07-31, at STORE-001, verify safety stock for SKU HOME-DESKLMP01, retrieve product information, calculate discrepancy (system: 45, physical: 40, unit cost: $17.2), and escalate the discrepancy to the regional level. Auditor EMP-1001 records the audit with timestamp '2025-07-31T09:00:00Z', photo 'photo101.jpg', and digital signature 'SIG-101'."
        ),
        actions=[
            Action(name="CheckSafetyStock", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="EscalateDiscrepancy", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": 86.0, "escalation_level": "regional"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1001", "timestamp": "2025-07-31T09:00:00Z", "photo": "photo101.jpg", "digital_signature": "SIG-101"}),
        ],
        outputs=[
            '"safety_stock_ok": true',
            '"product_info": {"sku": "HOME-DESKLMP01", "name": "Desk Lamp", "unit_cost": 17.2}',
            '"discrepancy_amount": -86.0',
            '"escalation": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": 86.0, "escalation_level": "regional"}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-31T09:00:00Z", "photo": "photo101.jpg", "digital_signature": "SIG-101"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_057",
        instruction=(
            "On 2025-07-03, at STORE-001, auditor EMP-1006 identifies a discrepancy for SKU HOME-DESKLMP01. The system indicates 45 units, the physical count is 40, and the unit cost is $17.2. The auditor generates an inventory adjustment for the discrepancy with reason 'audit_discrepancy', requires dual approval from EMP-1007, and records the audit with timestamp '2025-07-03T09:00:00Z', photo 'photo006.jpg', and digital signature 'SIG-006'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1006"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1007"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1006", "timestamp": "2025-07-03T09:00:00Z", "photo": "photo006.jpg", "digital_signature": "SIG-006"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1007", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-03T09:00:00Z", "photo": "photo006.jpg", "digital_signature": "SIG-006"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_058",
        instruction="Audit STORE-002, SKU SMRT-THERM02. Auditor EMP-1005 will verify inventory and conduct a physical count. Utilize the system_count from get_store_inventory (15) and the physical_count from get_physical_count (15). Calculate the discrepancy using these values and the unit cost from products.json (98.0). Since the discrepancy is 0, no adjustment is required. Record the audit with timestamp '2025-07-01T10:00:00Z', photo 'photo004.jpg', and digital signature 'SIG-004'. All values must be derived from tool outputs or the instruction, not assumed.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-002", "sku": "SMRT-THERM02"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-002", "sku": "SMRT-THERM02", "auditor_id": "EMP-1005"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 15, "physical_count": 15, "unit_cost": 98.0}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-002", "sku": "SMRT-THERM02", "auditor_id": "EMP-1005", "timestamp": "2025-07-01T10:00:00Z", "photo": "photo004.jpg", "digital_signature": "SIG-004"}),
        ],
        outputs=[
            '"system_count": 15',
            '"physical_count": 15',
            '"discrepancy_amount": 0.0',
            '"audit_log": {"store_id": "STORE-002", "sku": "SMRT-THERM02", "timestamp": "2025-07-01T10:00:00Z", "photo": "photo004.jpg", "digital_signature": "SIG-004"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_059",
        instruction=(
            "On 2025-07-13, at STORE-001 and STORE-002, auditor EMP-1037 enumerates all SKUs, marks expired products for SKU HOME-BTHTWL01 in STORE-001 and for SKU CLTH-WINJKT01 in STORE-002 as of 2025-07-13, and records the audit with timestamp '2025-07-13T09:00:00Z', photo 'photo004.jpg', and digital signature 'SIG-004'. Only mark SKUs that are available in each store."
        ),
        actions=[
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-001"}),
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-002"}),
            Action(name="FlagExpiredProducts", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "as_of_date": "2025-07-13"}),
            Action(name="FlagExpiredProducts", kwargs={"store_id": "STORE-002", "sku": "CLTH-WINJKT01", "as_of_date": "2025-07-13"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1037", "result": "flagged_products", "timestamp": "2025-07-13T09:00:00Z", "photo": "photo004.jpg", "digital_signature": "SIG-004"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-002", "sku": "CLTH-WINJKT01", "auditor_id": "EMP-1037", "result": "flagged_products", "timestamp": "2025-07-13T09:00:00Z", "photo": "photo004.jpg", "digital_signature": "SIG-004"}),
        ],
        outputs=[
            '"skus_store_001": ["HOME-BTHTWL01", "ELEC-RCHAA04", "GROC-ALMBTR500"]',
            '"skus_store_002": ["CLTH-WINJKT01", "AUDIO-NCEBUDS01", "SMRT-THERM02"]',
            '"flagged_products_store_001": true',
            '"flagged_products_store_002": true',
            '"audit_log_store_001": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1037", "result": "flagged_products", "timestamp": "2025-07-13T09:00:00Z", "photo": "photo004.jpg", "digital_signature": "SIG-004"}',
            '"audit_log_store_002": {"store_id": "STORE-002", "sku": "CLTH-WINJKT01", "auditor_id": "EMP-1037", "result": "flagged_products", "timestamp": "2025-07-13T09:00:00Z", "photo": "photo004.jpg", "digital_signature": "SIG-004"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_060",
        instruction="Audit STORE-001, SKU GROC-SPRWAT6P. Auditor EMP-1021 will verify inventory, conduct a physical count, and record the outcome. The system count is 130, the physical count is 130, and the unit cost is 3.4. Record the outcome as discrepancy_logged.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "GROC-SPRWAT6P"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "GROC-SPRWAT6P", "auditor_id": "EMP-1021"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 130, "physical_count": 130, "unit_cost": 3.4}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "GROC-SPRWAT6P", "auditor_id": "EMP-1021", "result": "discrepancy_logged"}),
        ],
        outputs=[
            '"system_count": 130',
            '"physical_count": 130',
            '"discrepancy_amount": 0',
            '"audit_log": {"store_id": "STORE-001", "sku": "GROC-SPRWAT6P"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_061",
        instruction="Conduct an audit at STORE-001 for SKU HOM-COFMKR12. Auditor EMP-1022 will review inventory, execute a physical count, and document the outcome. System count is 25, physical count is 25, unit cost is 34.5. Document the outcome as discrepancy_logged.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOM-COFMKR12"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOM-COFMKR12", "auditor_id": "EMP-1022"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 25, "physical_count": 25, "unit_cost": 34.5}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOM-COFMKR12", "auditor_id": "EMP-1022", "result": "discrepancy_logged"}),
        ],
        outputs=[
            '"system_count": 25',
            '"physical_count": 25',
            '"discrepancy_amount": 0',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOM-COFMKR12"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_062",
        instruction="Execute an audit at STORE-003 for SKU OFFC-ERGCHR01. Auditor EMP-1023 will verify inventory, carry out a physical count, and document the outcome. System count is 10, physical count is 10, unit cost is 140.0. Document the outcome as discrepancy_logged.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-003", "sku": "OFFC-ERGCHR01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-003", "sku": "OFFC-ERGCHR01", "auditor_id": "EMP-1023"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 10, "physical_count": 10, "unit_cost": 140.0}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-003", "sku": "OFFC-ERGCHR01", "auditor_id": "EMP-1023", "result": "discrepancy_logged"}),
        ],
        outputs=[
            '"system_count": 10',
            '"physical_count": 10',
            '"discrepancy_amount": 0',
            '"audit_log": {"store_id": "STORE-003", "sku": "OFFC-ERGCHR01"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_063",
        instruction="Perform an audit at STORE-001 for SKU ELEC-4KTV55. Auditor EMP-1024 will assess inventory, conduct a physical count, and document the outcome. System count is 8, physical count is 8, unit cost is 480.0. Document the outcome as discrepancy_logged.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "ELEC-4KTV55"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "ELEC-4KTV55", "auditor_id": "EMP-1024"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 8, "physical_count": 8, "unit_cost": 480.0}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "ELEC-4KTV55", "auditor_id": "EMP-1024", "result": "discrepancy_logged"}),
        ],
        outputs=[
            '"system_count": 8',
            '"physical_count": 8',
            '"discrepancy_amount": 0',
            '"audit_log": {"store_id": "STORE-001", "sku": "ELEC-4KTV55"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_064",
        instruction=(
            "On 2025-07-18, at STORE-001, auditor EMP-1018 identifies a discrepancy for SKU HOME-DESKLMP01. The system indicates 45 units, the physical count is 40, and the unit cost is $17.2. The auditor will initiate an inventory adjustment for the discrepancy with reason 'audit_discrepancy', which requires dual approval by EMP-1019, and document the audit with timestamp '2025-07-18T09:00:00Z', photo 'photo062.jpg', and digital signature 'SIG-062'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1018"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1019"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1018", "timestamp": "2025-07-18T09:00:00Z", "photo": "photo062.jpg", "digital_signature": "SIG-062"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1019", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-18T09:00:00Z", "photo": "photo062.jpg", "digital_signature": "SIG-062"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_065",
        instruction=(
            "On 2025-08-13, at STORE-001, auditor EMP-1002 reviews inventory and product details for SKU SPORT-YOGMAT01, retrieves employee information for EMP-1002, calculates a discrepancy (system: 60, physical: 59, unit cost: $13.8), initiates an inventory adjustment, requires dual approval by EMP-1003, and documents the audit with timestamp '2025-08-13T09:00:00Z', photo 'photo113.jpg', and digital signature 'SIG-113'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "SPORT-YOGMAT01"}),
            Action(name="GetProductInfo", kwargs={"sku": "SPORT-YOGMAT01"}),
            Action(name="GetEmployeeInfo", kwargs={"employee_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 60, "physical_count": 59, "unit_cost": 13.8}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "SPORT-YOGMAT01", "amount": -13.8, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "SPORT-YOGMAT01"), "approver_id": "EMP-1003"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "SPORT-YOGMAT01", "auditor_id": "EMP-1002", "timestamp": "2025-08-13T09:00:00Z", "photo": "photo113.jpg", "digital_signature": "SIG-113"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "SPORT-YOGMAT01", "system_count": 60}',
            '"product_info": {"sku": "SPORT-YOGMAT01", "name": "FlexFit Premium Yoga Mat", "unit_cost": 13.8}',
            '"employee_info": {"employee_id": "EMP-1002", "name": "Sarah Anderson", "role": "Cashier"}',
            '"discrepancy_amount": -13.8',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "SPORT-YOGMAT01")}", "store_id": "STORE-001", "sku": "SPORT-YOGMAT01", "amount": -13.8, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "SPORT-YOGMAT01")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "SPORT-YOGMAT01", "auditor_id": "EMP-1002", "timestamp": "2025-08-13T09:00:00Z", "photo": "photo113.jpg", "digital_signature": "SIG-113"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_066",
        instruction=(
            "On 2025-07-20, at STORE-001, auditor EMP-1022 discovers a discrepancy for SKU HOME-DESKLMP01. The system displays 45 units, the physical count is 40, and the unit cost is $17.2. The auditor will create an inventory adjustment for the discrepancy with reason 'audit_discrepancy', which requires dual approval by EMP-1023, and document the audit with timestamp '2025-07-20T09:00:00Z', photo 'photo064.jpg', and digital signature 'SIG-064'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1022"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1023"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1022", "timestamp": "2025-07-20T09:00:00Z", "photo": "photo064.jpg", "digital_signature": "SIG-064"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1023", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-20T09:00:00Z", "photo": "photo064.jpg", "digital_signature": "SIG-064"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_067",
        instruction=(
            "On 2025-07-21, at STORE-001, auditor EMP-1024 identifies a discrepancy for SKU HOME-DESKLMP01. The system shows 45 units, the physical count is 40, and the unit cost is $17.2. The auditor will create an inventory adjustment for the discrepancy with reason 'audit_discrepancy', necessitating dual approval by EMP-1025, and document the audit with timestamp '2025-07-21T09:00:00Z', photo 'photo065.jpg', and digital signature 'SIG-065'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1024"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1025"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1024", "timestamp": "2025-07-21T09:00:00Z", "photo": "photo065.jpg", "digital_signature": "SIG-065"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1025", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-21T09:00:00Z", "photo": "photo065.jpg", "digital_signature": "SIG-065"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_068",
        instruction=(
            "On 2025-07-22, at STORE-001, auditor EMP-1026 discovers a discrepancy for SKU HOME-DESKLMP01. The system indicates 45 units, the physical count is 40, and the unit cost is $17.2. The auditor will initiate an inventory adjustment for the discrepancy with reason 'audit_discrepancy', which requires dual approval by EMP-1027, and document the audit with timestamp '2025-07-22T09:00:00Z', photo 'photo066.jpg', and digital signature 'SIG-066'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1026"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1027"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1026", "timestamp": "2025-07-22T09:00:00Z", "photo": "photo066.jpg", "digital_signature": "SIG-066"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1027", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-22T09:00:00Z", "photo": "photo066.jpg", "digital_signature": "SIG-066"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_069",
        instruction=(
            "On 2025-07-23, at STORE-001, auditor EMP-1028 uncovers a discrepancy for SKU HOME-DESKLMP01. The system reports 45 units, the physical count is 40, and the unit cost is $17.2. The auditor will create an inventory adjustment for the discrepancy with reason 'audit_discrepancy', necessitating dual approval by EMP-1029, and document the audit with timestamp '2025-07-23T09:00:00Z', photo 'photo067.jpg', and digital signature 'SIG-067'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1028"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1029"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1028", "timestamp": "2025-07-23T09:00:00Z", "photo": "photo067.jpg", "digital_signature": "SIG-067"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1029", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1028", "timestamp": "2025-07-23T09:00:00Z", "photo": "photo067.jpg", "digital_signature": "SIG-067"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_070",
        instruction=(
            "On 2025-07-03, at STORE-001, auditor EMP-1007 finds a discrepancy for SKU HOME-DESKLMP01. The system shows 45 units, physical count is 40, and the unit cost is $17.2. The auditor will create an inventory adjustment for the discrepancy with reason 'audit_discrepancy', requires dual approval by EMP-1008, and logs the audit with timestamp '2025-07-03T10:00:00Z', photo 'photo007.jpg', and digital signature 'SIG-007'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1007"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": 86.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1008"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1007", "timestamp": "2025-07-03T10:00:00Z", "photo": "photo007.jpg", "digital_signature": "SIG-007"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": 86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": 86.0, "reason": "audit_discrepancy"}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1008", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-03T10:00:00Z", "photo": "photo007.jpg", "digital_signature": "SIG-007"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_071",
        instruction=(
            "On 2025-07-25, at STORE-001, auditor EMP-1001 discovers a discrepancy for SKU HOME-DESKLMP01. The system indicates 45 units, the physical count is 40, and the unit cost is $17.2. The auditor retrieves product info, generates an inventory adjustment for the discrepancy citing 'audit_discrepancy' as the reason, mandates dual approval from EMP-1002, and records the audit with timestamp '2025-07-25T09:00:00Z', photo 'photo070.jpg', and digital signature 'SIG-070'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1001"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1002"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1001", "timestamp": "2025-07-25T09:00:00Z", "photo": "photo070.jpg", "digital_signature": "SIG-070"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"product_info": {"sku": "HOME-DESKLMP01", "name": "Desk Lamp", "unit_cost": 17.2}',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"dual_approval": {"adjustment_id": "ADJ-AAD81F", "approver_id": "EMP-1002", "approved": true}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-25T09:00:00Z", "photo": "photo070.jpg", "digital_signature": "SIG-070"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_072",
        instruction="On 2025-07-17, at STORE-001, auditor EMP-1003 evaluates inventory for SKU GROC-ALMBTR500, obtains product info, conducts a physical count, calculates the discrepancy using unit_cost $7.85, creates an inventory adjustment, requires dual approval from EMP-1001, logs the audit with timestamp '2025-07-17T11:00:00Z', photo 'photo000c.jpg', and digital signature 'SIG-000C', and subsequently flags expired products as of 2025-07-17.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500"}),
            Action(name="GetProductInfo", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1003"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 60, "physical_count": 60, "unit_cost": 7.85}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "amount": 0.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "GROC-ALMBTR500"), "approver_id": "EMP-1001"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1003", "timestamp": "2025-07-17T11:00:00Z", "photo": "photo000c.jpg", "digital_signature": "SIG-000C"}),
            Action(name="FlagExpiredProducts", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "as_of_date": "2025-07-17"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "system_count": 60}',
            '"product_info": {"sku": "GROC-ALMBTR500", "name": "Organic Almond Butter 500g", "unit_cost": 7.85}',
            '"physical_count": 60',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "GROC-ALMBTR500")}", "store_id": "STORE-001", "sku": "GROC-ALMBTR500", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "GROC-ALMBTR500")}", "approver_id": "EMP-1001", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1003", "timestamp": "2025-07-17T11:00:00Z", "photo": "photo000c.jpg", "digital_signature": "SIG-000C"}',
            '"expired_flagged": true'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_073",
        instruction=(
            "On 2025-07-25, at STORE-001, retrieve all transactions, fetch transaction details for TXN-0001, gather customer info for CUST-5001, and log the audit for SKU GROC-ALMBTR500 with auditor_id EMP-1002, timestamp '2025-07-25T14:00:00Z', photo 'photo073.jpg', and digital signature 'SIG-073'."
        ),
        actions=[
            Action(name="ListStoreTransactions", kwargs={"store_id": "STORE-001"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="GetCustomerInfo", kwargs={"customer_id": "CUST-5001"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1002", "timestamp": "2025-07-25T14:00:00Z", "photo": "photo073.jpg", "digital_signature": "SIG-073"}),
        ],
        outputs=[
            '"transactions": ["TXN-0001", "TXN-0008", "TXN-0012"]',
            '"transaction_details": {"transaction_id": "TXN-0001", "sku": "GROC-ALMBTR500", "quantity": 2, "total": 5.0}',
            '"customer_info": {"customer_id": "CUST-5001", "name": "Emma Wilson", "loyalty_points": 1240}',
            '"audit_log": {"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "timestamp": "2025-07-25T14:00:00Z", "photo": "photo073.jpg", "digital_signature": "SIG-073"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_074",
        instruction=(
            "On 2025-08-10, at STORE-001, auditor EMP-1002 assesses inventory and product info for SKU GROC-ALMBTR500, gathers employee info for EMP-1002, calculates a discrepancy (system: 60, physical: 58, unit cost: $7.85), creates an inventory adjustment, requires dual approval from EMP-1003, and logs the audit with timestamp '2025-08-10T09:00:00Z', photo 'photo110.jpg', and digital signature 'SIG-110'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500"}),
            Action(name="GetProductInfo", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="GetEmployeeInfo", kwargs={"employee_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 60, "physical_count": 58, "unit_cost": 7.85}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "amount": -15.7, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "GROC-ALMBTR500"), "approver_id": "EMP-1003"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1002", "timestamp": "2025-08-10T09:00:00Z", "photo": "photo110.jpg", "digital_signature": "SIG-110"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "system_count": 60}',
            '"product_info": {"sku": "GROC-ALMBTR500", "name": "Organic Almond Butter 500g", "unit_cost": 7.85}',
            '"employee_info": {"employee_id": "EMP-1002", "name": "Sarah Anderson", "role": "Cashier"}',
            '"discrepancy_amount": -15.7',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "GROC-ALMBTR500")}", "store_id": "STORE-001", "sku": "GROC-ALMBTR500", "amount": -15.7, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "GROC-ALMBTR500")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1002", "timestamp": "2025-08-10T09:00:00Z", "photo": "photo110.jpg", "digital_signature": "SIG-110"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_075",
        instruction=(
            "On 2025-07-08, identify expired products for SKU HOME-BTHTWL01 in STORE-001 (batch BATCH-20240501, 8 units, expired as of 2025-07-08, unit cost $6.0). Generate an inventory adjustment for the expired batch (amount: -48.0), require dual approval, and auditor EMP-1002 logs the action with result 'expired_flagged', timestamp '2025-07-08T09:00:00Z', photo 'photo064.jpg', and digital signature 'SIG-064'."
            "Create an inventory adjustment for the expired batch (amount: -48.0), require dual approval, and auditor EMP-1002 logs the action with result 'expired_flagged', timestamp '2025-07-08T09:00:00Z', photo 'photo064.jpg', and digital signature 'SIG-064'."
        ),
        actions=[
            Action(name="FlagExpiredProducts", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "as_of_date": "2025-07-08"}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": -48.0, "reason": "expired_batch"}),
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "HOME-BTHTWL01")}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "result": "expired_flagged", "timestamp": "2025-07-08T09:00:00Z", "photo": "photo064.jpg", "digital_signature": "SIG-064"}),
        ],
        outputs=[
            '"expired_batches": ["BATCH-20240501"]',
            f'"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}"',
            '"dual_approved": true',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "timestamp": "2025-07-08T09:00:00Z", "photo": "photo064.jpg", "digital_signature": "SIG-064"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_076",
        instruction="Conduct an audit at STORE-001 for SKU HOME-BTHTWL01. Auditor EMP-1002 will review inventory, execute a physical count (system: 100, physical: 100, unit cost: 6.0), assess discrepancy, create an inventory adjustment, require dual approval, and log the audit with timestamp '2025-07-01T10:00:00Z', photo 'photo001.jpg', and digital signature 'SIG-001'. With a discrepancy of 0, no escalation, recount, or transfer actions will be necessary.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 100, "physical_count": 100, "unit_cost": 6.0}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": 0.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "HOME-BTHTWL01")}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "result": "discrepancy_logged", "timestamp": "2025-07-01T10:00:00Z", "photo": "photo001.jpg", "digital_signature": "SIG-001"}),
        ],
        outputs=[
            '"system_count": 100',
            '"physical_count": 100',
            '"discrepancy_amount": 0.0',
            f'"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}"',
            '"dual_approved": true',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "timestamp": "2025-07-01T10:00:00Z", "photo": "photo001.jpg", "digital_signature": "SIG-001"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_077",
        instruction=(
            "On 2025-10-12, at STORE-001, auditor EMP-1002 examines inventory for SKU GROC-ALMBTR500, carries out a physical count, calculates discrepancy using unit_cost $7.85, creates an inventory adjustment, requires dual approval from EMP-1003, logs the audit with timestamp '2025-10-12T10:00:00Z', photo 'photo112.jpg', and digital signature 'SIG-112', and then flags expired products as of 2025-10-12. Should any validation fail, cease operations and avoid further actions. All parameters must be derived from tool outputs or the instruction."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 60, "physical_count": 60, "unit_cost": 7.85}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "amount": 0.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "GROC-ALMBTR500"), "approver_id": "EMP-1003"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1002", "timestamp": "2025-10-12T10:00:00Z", "photo": "photo112.jpg", "digital_signature": "SIG-112"}),
            Action(name="FlagExpiredProducts", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "as_of_date": "2025-10-12"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "system_count": 60}',
            '"physical_count": 60',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "GROC-ALMBTR500")}", "store_id": "STORE-001", "sku": "GROC-ALMBTR500", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "GROC-ALMBTR500")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1002", "timestamp": "2025-10-12T10:00:00Z", "photo": "photo112.jpg", "digital_signature": "SIG-112"}',
            '"expired_flagged": true'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_078",
        instruction=(
            "On 2025-09-08, at STORE-001, auditor EMP-1002 enumerates all SKUs, assesses inventory for SKU HOME-BTHTWL01, flags expired products as of 2025-09-08, establishes an inventory adjustment for expired stock (amount: -12.0), requires dual approval from EMP-1003, and records the audit with result 'expired_flagged', timestamp '2025-09-08T10:00:00Z', photo 'photo078_new.jpg', and digital signature 'SIG-078N'. If any validation fails (such as if list_store_skus does not include the SKU, get_store_inventory yields empty, or any tool call encounters an error), cease operations and avoid further actions. All parameters must be sourced from tool outputs or the instruction."
        ),
        actions=[
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-001"}),
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01"}),
            # Only proceed if get_store_inventory returns a valid record:
            Action(name="FlagExpiredProducts", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "as_of_date": "2025-09-08"}),
            # Only proceed if expired products are flagged:
            Action(name="CreateInventoryAdjustment", kwargs={
                "store_id": "STORE-001",
                "sku": "HOME-BTHTWL01",
                "amount": -12.0,
                "reason": "expired_stock"
            }),
            # Only proceed if adjustment creation succeeds:
            Action(name="DualApproval", kwargs={
                "adjustment_id": adj_id("STORE-001", "HOME-BTHTWL01"),
                "approver_id": "EMP-1003"
            }),
            # Only proceed if dual approval succeeds:
            Action(name="LogAuditResult", kwargs={
                "store_id": "STORE-001",
                "sku": "HOME-BTHTWL01",
                "auditor_id": "EMP-1002",
                "result": "expired_flagged",
                "timestamp": "2025-09-08T10:00:00Z",
                "photo": "photo078_new.jpg",
                "digital_signature": "SIG-078N"
            }),
        ],
        outputs=[
            '"skus": ["HOME-BTHTWL01", "ELEC-RCHAA04", "GROC-ALMBTR500"]',
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "system_count": 100}',
            '"expired_batches": ["BATCH-20250901"]',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": -12.0, "reason": "expired_stock"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "result": "expired_flagged", "timestamp": "2025-09-08T10:00:00Z", "photo": "photo078_new.jpg", "digital_signature": "SIG-078N"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_079",
        instruction=(
            "On 2025-10-12, at STORE-001, auditor EMP-1002 inspects inventory for SKU GROC-ALMBTR500, executes a physical count, computes discrepancy using unit_cost $7.85, creates an inventory adjustment, requires dual approval by EMP-1003, logs the audit with timestamp '2025-10-12T10:00:00Z', photo 'photo112.jpg', and digital signature 'SIG-112', and then flags expired products as of 2025-10-12. In case any validation fails (including if get_store_inventory yields empty, or any tool call encounters an error), cease operations and avoid further actions. All parameters must be derived from tool outputs or the instruction."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500"}),
            # Only proceed if get_store_inventory returns a valid record:
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1002"}),
            # Only proceed if get_physical_count returns a valid count:
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 60, "physical_count": 60, "unit_cost": 7.85}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "amount": 0.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "GROC-ALMBTR500"), "approver_id": "EMP-1003"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1002", "timestamp": "2025-10-12T10:00:00Z", "photo": "photo112.jpg", "digital_signature": "SIG-112"}),
            Action(name="FlagExpiredProducts", kwargs={"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "as_of_date": "2025-10-12"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "system_count": 60}',
            '"physical_count": 60',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "GROC-ALMBTR500")}", "store_id": "STORE-001", "sku": "GROC-ALMBTR500", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "GROC-ALMBTR500")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "GROC-ALMBTR500", "auditor_id": "EMP-1002", "timestamp": "2025-10-12T10:00:00Z", "photo": "photo112.jpg", "digital_signature": "SIG-112"}',
            '"expired_flagged": true'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_080",
        instruction=(
            "On 2025-08-27, at STORE-003, auditor EMP-3001 lists all SKUs, examines inventory for SKU ELEC-RCHAA04, performs a physical count, computes discrepancy using unit_cost $9.9, creates an inventory adjustment, requires dual approval from EMP-3002, and logs the audit with timestamp '2025-08-27T09:00:00Z', photo 'photo080_new.jpg', and digital signature 'SIG-080N'. Should any validation fail (including if get_store_inventory yields empty, or if any tool call encounters an error), cease operations and avoid further actions. All parameters must be sourced from tool outputs or the instruction."
        ),
        actions=[
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-003"}),
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04"}),
            # Only proceed if get_store_inventory returns a valid record:
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "auditor_id": "EMP-3001"}),
            # Only proceed if physical count succeeds:
            Action(name="ComputeDiscrepancyAmount", kwargs={
                "system_count": 90,
                "physical_count": 90,
                "unit_cost": 9.9
            }),
            # Only proceed if discrepancy computation succeeds:
            Action(name="CreateInventoryAdjustment", kwargs={
                "store_id": "STORE-003",
                "sku": "ELEC-RCHAA04",
                "amount": 0.0,
                "reason": "audit_discrepancy"
            }),
            # Only proceed if adjustment creation succeeds:
            Action(name="DualApproval", kwargs={
                "adjustment_id": adj_id("STORE-003", "ELEC-RCHAA04"),
                "approver_id": "EMP-3002"
            }),
            # Only proceed if dual approval succeeds:
            Action(name="LogAuditResult", kwargs={
                "store_id": "STORE-003",
                "sku": "ELEC-RCHAA04",
                "auditor_id": "EMP-3001",
                "timestamp": "2025-08-27T09:00:00Z",
                "photo": "photo080_new.jpg",
                "digital_signature": "SIG-080N"
            }),
        ],
        outputs=[
            '"skus": ["ELEC-RCHAA04", "HOME-BTHTWL01", "GROC-ALMBTR500"]',
            '"store_inventory": {"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "system_count": 90}',
            '"physical_count": 90',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-003", "ELEC-RCHAA04")}", "store_id": "STORE-003", "sku": "ELEC-RCHAA04", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-003", "ELEC-RCHAA04")}", "approver_id": "EMP-3002", "approved": true}}',
            '"audit_log": {"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "auditor_id": "EMP-3001", "timestamp": "2025-08-27T09:00:00Z", "photo": "photo080_new.jpg", "digital_signature": "SIG-080N"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_081",
        instruction=(
            "On 2025-09-03, at STORE-003, auditor EMP-3001 compiles a list of all SKUs, verifies inventory for SKU ELEC-RCHAA04, conducts a physical count, calculates discrepancy using unit_cost $9.9, generates an inventory adjustment, requires dual approval by EMP-3002, and records the audit with timestamp '2025-09-03T09:00:00Z', photo 'photo081_new.jpg', and digital signature 'SIG-081N'. Should any validation fail (including if get_store_inventory returns empty, or if any tool call fails), cease operations and refrain from executing subsequent actions. All parameters must be derived from tool outputs or the instruction."
        ),
        actions=[
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-003"}),
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04"}),
            # Only proceed if get_store_inventory returns a valid record:
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "auditor_id": "EMP-3001"}),
            # Only proceed if physical count succeeds:
            Action(name="ComputeDiscrepancyAmount", kwargs={
                "system_count": 90,
                "physical_count": 90,
                "unit_cost": 9.9
            }),
            # Only proceed if discrepancy computation succeeds:
            Action(name="CreateInventoryAdjustment", kwargs={
                "store_id": "STORE-003",
                "sku": "ELEC-RCHAA04",
                "amount": 0.0,
                "reason": "audit_discrepancy"
            }),
            # Only proceed if adjustment creation succeeds:
            Action(name="DualApproval", kwargs={
                "adjustment_id": adj_id("STORE-003", "ELEC-RCHAA04"),
                "approver_id": "EMP-3002"
            }),
            # Only proceed if dual approval succeeds:
            Action(name="LogAuditResult", kwargs={
                "store_id": "STORE-003",
                "sku": "ELEC-RCHAA04",
                "auditor_id": "EMP-3001",
                "timestamp": "2025-09-03T09:00:00Z",
                "photo": "photo081_new.jpg",
                "digital_signature": "SIG-081N"
            }),
        ],
        outputs=[
            '"skus": ["ELEC-RCHAA04", "HOME-BTHTWL01", "GROC-ALMBTR500"]',
            '"store_inventory": {"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "system_count": 90}',
            '"physical_count": 90',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-003", "ELEC-RCHAA04")}", "store_id": "STORE-003", "sku": "ELEC-RCHAA04", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-003", "ELEC-RCHAA04")}", "approver_id": "EMP-3002", "approved": true}}',
            '"audit_log": {"store_id": "STORE-003", "sku": "ELEC-RCHAA04", "auditor_id": "EMP-3001", "timestamp": "2025-09-03T09:00:00Z", "photo": "photo081_new.jpg", "digital_signature": "SIG-081N"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_082",
        instruction=(
            "On 2025-09-04, at STORE-001, auditor EMP-1002 compiles a list of all SKUs, verifies inventory for SKU HOME-BTHTWL01, conducts a physical count, calculates discrepancy using unit_cost $6.0, generates an inventory adjustment, requires dual approval by EMP-1003, and records the audit with timestamp '2025-09-04T10:00:00Z', photo 'photo082_new.jpg', and digital signature 'SIG-082N'. Should any validation fail (including if get_store_inventory returns empty, or if any tool call fails), cease operations and refrain from executing subsequent actions. All parameters must be derived from tool outputs or the instruction."
        ),
        actions=[
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-001"}),
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01"}),
            # Only proceed if get_store_inventory returns a valid record:
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002"}),
            # Only proceed if physical count succeeds:
            Action(name="ComputeDiscrepancyAmount", kwargs={
                "system_count": 100,
                "physical_count": 100,
                "unit_cost": 6.0
            }),
            # Only proceed if discrepancy computation succeeds:
            Action(name="CreateInventoryAdjustment", kwargs={
                "store_id": "STORE-001",
                "sku": "HOME-BTHTWL01",
                "amount": 0.0,
                "reason": "audit_discrepancy"
            }),
            # Only proceed if adjustment creation succeeds:
            Action(name="DualApproval", kwargs={
                "adjustment_id": adj_id("STORE-001", "HOME-BTHTWL01"),
                "approver_id": "EMP-1003"
            }),
            # Only proceed if dual approval succeeds:
            Action(name="LogAuditResult", kwargs={
                "store_id": "STORE-001",
                "sku": "HOME-BTHTWL01",
                "auditor_id": "EMP-1002",
                "timestamp": "2025-09-04T10:00:00Z",
                "photo": "photo082_new.jpg",
                "digital_signature": "SIG-082N"
            }),
        ],
        outputs=[
            '"skus": ["HOME-BTHTWL01", "ELEC-RCHAA04", "GROC-ALMBTR500"]',
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "system_count": 100}',
            '"physical_count": 100',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "timestamp": "2025-09-04T10:00:00Z", "photo": "photo082_new.jpg", "digital_signature": "SIG-082N"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_083",
        instruction=(
            "On 2025-10-10, at STORE-001, auditor EMP-1002 compiles a list of all SKUs, verifies inventory for SKU HOME-BTHTWL01, conducts a physical count, calculates discrepancy using unit_cost $6.0, generates an inventory adjustment, requires dual approval by EMP-1003, conducts a compliance review of the adjustment (using compliance_review tool), and records the audit with timestamp '2025-10-10T10:00:00Z', photo 'photo110.jpg', and digital signature 'SIG-110'. Should any validation fail, cease operations and refrain from executing subsequent actions. All parameters must be derived from tool outputs or the instruction."
        ),
        actions=[
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-001"}),
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 100, "physical_count": 100, "unit_cost": 6.0}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": 0.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "HOME-BTHTWL01"), "approver_id": "EMP-1003"}),
            Action(name="ComplianceReview", kwargs={"adjustment_id": adj_id("STORE-001", "HOME-BTHTWL01")}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "timestamp": "2025-10-10T10:00:00Z", "photo": "photo110.jpg", "digital_signature": "SIG-110"}),
        ],
        outputs=[
            '"skus": ["HOME-BTHTWL01", "ELEC-RCHAA04", "GROC-ALMBTR500"]',
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "system_count": 100}',
            '"physical_count": 100',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "approver_id": "EMP-1003", "approved": true}}',
            f'"compliance_reviewed": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "reviewed": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "timestamp": "2025-10-10T10:00:00Z", "photo": "photo110.jpg", "digital_signature": "SIG-110"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_084",
        instruction=(
            "On 2025-07-25, at STORE-001, compile a list of all employees, obtain product info for SKU HOME-BTHTWL01, generate an inventory adjustment for 10 expired units (unit cost $6.0, amount: -60.0, reason: 'expired_stock'), and auditor EMP-1002 records the audit for SKU HOME-BTHTWL01 with timestamp '2025-07-25T11:00:00Z', photo 'photo084.jpg', and digital signature 'SIG-084'."
        ),
        actions=[
            Action(name="ListStoreEmployees", kwargs={"store_id": "STORE-001"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-BTHTWL01"}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": -60.0, "reason": "expired_stock"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "timestamp": "2025-07-25T11:00:00Z", "photo": "photo084.jpg", "digital_signature": "SIG-084"}),
        ],
        outputs=[
            '"employees": ["EMP-1002", "EMP-1003", "EMP-1004"]',
            '"product_info": {"sku": "HOME-BTHTWL01", "name": "UltraSoft Cotton Bath Towel", "unit_cost": 6.0}',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": -60.0, "reason": "expired_stock"}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "timestamp": "2025-07-25T11:00:00Z", "photo": "photo084.jpg", "digital_signature": "SIG-084"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_085",
        instruction=(
            "On 2025-09-06, at STORE-001, auditor EMP-1002 obtains product info for SKU HOME-BTHTWL01, verifies inventory, conducts a physical count, calculates discrepancy using unit_cost $6.0, generates an inventory adjustment, requires dual approval by EMP-1003, and records the audit with timestamp '2025-09-06T10:00:00Z', photo 'photo085_new.jpg', and digital signature 'SIG-085N'. Should any validation fail (including if get_product_info or get_store_inventory returns empty, or if any tool call fails), cease operations and refrain from executing subsequent actions. All parameters must be derived from tool outputs or the instruction."
        ),
        actions=[
            Action(name="GetProductInfo", kwargs={"sku": "HOME-BTHTWL01"}),
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={
                "system_count": 100,
                "physical_count": 100,
                "unit_cost": 6.0
            }),
            Action(name="CreateInventoryAdjustment", kwargs={
                "store_id": "STORE-001",
                "sku": "HOME-BTHTWL01",
                "amount": 0.0,
                "reason": "audit_discrepancy"
            }),
            Action(name="DualApproval", kwargs={
                "adjustment_id": adj_id("STORE-001", "HOME-BTHTWL01"),
                "approver_id": "EMP-1003"
            }),
            Action(name="LogAuditResult", kwargs={
                "store_id": "STORE-001",
                "sku": "HOME-BTHTWL01",
                "auditor_id": "EMP-1002",
                "timestamp": "2025-09-06T10:00:00Z",
                "photo": "photo085_new.jpg",
                "digital_signature": "SIG-085N"
            }),
        ],
        outputs=[
            '"product_info": {"sku": "HOME-BTHTWL01", "name": "UltraSoft Cotton Bath Towel", "unit_cost": 6.0}',
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "system_count": 100}',
            '"physical_count": 100',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "timestamp": "2025-09-06T10:00:00Z", "photo": "photo085_new.jpg", "digital_signature": "SIG-085N"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_086",
        instruction=(
            "On 2025-07-26, at STORE-001, compile a list of all SKUs in inventory, obtain product info for each, then auditor EMP-1001 records the audit for SKU HOME-BTHTWL01 with timestamp '2025-07-26T09:00:00Z', photo 'photo086.jpg', and digital signature 'SIG-086'."
        ),
        actions=[
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-001"}),
            Action(name="GetProductInfo", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="GetProductInfo", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-BTHTWL01"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetProductInfo", kwargs={"sku": "BOOK-KDSSTY01"}),
            Action(name="GetProductInfo", kwargs={"sku": "SPORT-YOGMAT01"}),
            Action(name="GetProductInfo", kwargs={"sku": "GROC-SPRWAT6P"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1001", "timestamp": "2025-07-26T09:00:00Z", "photo": "photo086.jpg", "digital_signature": "SIG-086"}),
        ],
        outputs=[
            '"skus": ["ELEC-4KTV55", "HOM-COFMKR12", "GROC-ALMBTR500", "HOME-BTHTWL01", "HOME-DESKLMP01", "BOOK-KDSSTY01", "SPORT-YOGMAT01", "GROC-SPRWAT6P"]',
            '"product_info_1": {"sku": "ELEC-4KTV55", "name": "UltraVision 55\" 4K Smart TV", "unit_cost": 480.0}',
            '"product_info_2": {"sku": "HOM-COFMKR12", "name": "BrewMaster 12-Cup Coffee Maker", "unit_cost": 34.5}',
            '"product_info_3": {"sku": "GROC-ALMBTR500", "name": "Organic Almond Butter 500g", "unit_cost": 7.85}',
            '"product_info_4": {"sku": "HOME-BTHTWL01", "name": "UltraSoft Cotton Bath Towel", "unit_cost": 6.0}',
            '"product_info_5": {"sku": "HOME-DESKLMP01", "name": "LumiLux LED Desk Lamp", "unit_cost": 17.2}',
            '"product_info_6": {"sku": "BOOK-KDSSTY01", "name": "Adventures in Sillytown", "unit_cost": 4.2}',
            '"product_info_7": {"sku": "SPORT-YOGMAT01", "name": "FlexFit Premium Yoga Mat", "unit_cost": 13.8}',
            '"product_info_8": {"sku": "GROC-SPRWAT6P", "name": "SparkleLife Sparkling Water 1L (6 Pack)", "unit_cost": 3.4}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "timestamp": "2025-07-26T09:00:00Z", "photo": "photo086.jpg", "digital_signature": "SIG-086"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_087",
        instruction=(
            "On 2025-09-10, at STORE-001, auditor EMP-1002 compiles a list of all SKUs, verifies inventory for SKU BOOK-KDSSTY01, conducts a physical count, calculates discrepancy using unit_cost $4.2, generates an inventory adjustment, requires dual approval by EMP-1003, and records the audit with timestamp '2025-09-10T10:00:00Z', photo 'photo089_new.jpg', and digital signature 'SIG-089N'. Should any validation fail (including if get_store_inventory returns empty, or if any tool call fails), cease operations and refrain from executing subsequent actions. All parameters must be derived from tool outputs or the instruction."
        ),
        actions=[
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-001"}),
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "BOOK-KDSSTY01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "BOOK-KDSSTY01", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={
                "system_count": 40,
                "physical_count": 40,
                "unit_cost": 4.2
            }),
            Action(name="CreateInventoryAdjustment", kwargs={
                "store_id": "STORE-001",
                "sku": "BOOK-KDSSTY01",
                "amount": 0.0,
                "reason": "audit_discrepancy"
            }),
            Action(name="DualApproval", kwargs={
                "adjustment_id": adj_id("STORE-001", "BOOK-KDSSTY01"),
                "approver_id": "EMP-1003"
            }),
            Action(name="LogAuditResult", kwargs={
                "store_id": "STORE-001",
                "sku": "BOOK-KDSSTY01",
                "auditor_id": "EMP-1002",
                "timestamp": "2025-09-10T10:00:00Z",
                "photo": "photo089_new.jpg",
                "digital_signature": "SIG-089N"
            }),
        ],
        outputs=[
            '"skus": ["BOOK-KDSSTY01", "HOME-BTHTWL01", "GROC-ALMBTR500"]',
            '"store_inventory": {"store_id": "STORE-001", "sku": "BOOK-KDSSTY01", "system_count": 40}',
            '"physical_count": 40',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "BOOK-KDSSTY01")}", "store_id": "STORE-001", "sku": "BOOK-KDSSTY01", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "BOOK-KDSSTY01")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "BOOK-KDSSTY01", "auditor_id": "EMP-1002", "timestamp": "2025-09-10T10:00:00Z", "photo": "photo089_new.jpg", "digital_signature": "SIG-089N"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_088",
        instruction=(
            "On 2025-07-26, at STORE-001, compile a list of all SKUs in inventory, obtain product info for each, then auditor EMP-1001 records the audit for SKU HOME-BTHTWL01 with timestamp '2025-07-26T09:00:00Z', photo 'photo086.jpg', and digital signature 'SIG-086'."
        ),
        actions=[
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-001"}),
            Action(name="GetProductInfo", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="GetProductInfo", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-BTHTWL01"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetProductInfo", kwargs={"sku": "BOOK-KDSSTY01"}),
            Action(name="GetProductInfo", kwargs={"sku": "SPORT-YOGMAT01"}),
            Action(name="GetProductInfo", kwargs={"sku": "GROC-SPRWAT6P"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1001", "timestamp": "2025-07-26T09:00:00Z", "photo": "photo086.jpg", "digital_signature": "SIG-086"}),
        ],
        outputs=[
            '"skus": ["ELEC-4KTV55", "HOM-COFMKR12", "GROC-ALMBTR500", "HOME-BTHTWL01", "HOME-DESKLMP01", "BOOK-KDSSTY01", "SPORT-YOGMAT01", "GROC-SPRWAT6P"]',
            '"product_info_1": {"sku": "ELEC-4KTV55", "name": "UltraVision 55\" 4K Smart TV", "unit_cost": 480.0}',
            '"product_info_2": {"sku": "HOM-COFMKR12", "name": "BrewMaster 12-Cup Coffee Maker", "unit_cost": 34.5}',
            '"product_info_3": {"sku": "GROC-ALMBTR500", "name": "Organic Almond Butter 500g", "unit_cost": 7.85}',
            '"product_info_4": {"sku": "HOME-BTHTWL01", "name": "UltraSoft Cotton Bath Towel", "unit_cost": 6.0}',
            '"product_info_5": {"sku": "HOME-DESKLMP01", "name": "LumiLux LED Desk Lamp", "unit_cost": 17.2}',
            '"product_info_6": {"sku": "BOOK-KDSSTY01", "name": "Adventures in Sillytown", "unit_cost": 4.2}',
            '"product_info_7": {"sku": "SPORT-YOGMAT01", "name": "FlexFit Premium Yoga Mat", "unit_cost": 13.8}',
            '"product_info_8": {"sku": "GROC-SPRWAT6P", "name": "SparkleLife Sparkling Water 1L (6 Pack)", "unit_cost": 3.4}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "timestamp": "2025-07-26T09:00:00Z", "photo": "photo086.jpg", "digital_signature": "SIG-086"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_089",
        instruction=(
            "On 2025-09-05, at STORE-001, auditor EMP-1002 compiles a list of all SKUs, verifies inventory for SKU HOME-BTHTWL01, conducts a physical count, calculates discrepancy using unit_cost $6.0, generates an inventory adjustment, requires dual approval by EMP-1003, and records the audit with timestamp '2025-09-05T10:00:00Z', photo 'photo083_new.jpg', and digital signature 'SIG-083N'. Should any validation fail (including if get_store_inventory returns empty, or if any tool call fails), cease operations and refrain from executing subsequent actions. All parameters must be derived from tool outputs or the instruction."
        ),
        actions=[
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-001"}),
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={
                "system_count": 100,
                "physical_count": 100,
                "unit_cost": 6.0
            }),
            Action(name="CreateInventoryAdjustment", kwargs={
                "store_id": "STORE-001",
                "sku": "HOME-BTHTWL01",
                "amount": 0.0,
                "reason": "audit_discrepancy"
            }),
            Action(name="DualApproval", kwargs={
                "adjustment_id": adj_id("STORE-001", "HOME-BTHTWL01"),
                "approver_id": "EMP-1003"
            }),
            Action(name="LogAuditResult", kwargs={
                "store_id": "STORE-001",
                "sku": "HOME-BTHTWL01",
                "auditor_id": "EMP-1002",
                "timestamp": "2025-09-05T10:00:00Z",
                "photo": "photo083_new.jpg",
                "digital_signature": "SIG-083N"
            }),
        ],
        outputs=[
            '"skus": ["HOME-BTHTWL01", "ELEC-RCHAA04", "GROC-ALMBTR500"]',
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "system_count": 100}',
            '"physical_count": 100',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "timestamp": "2025-09-05T10:00:00Z", "photo": "photo083_new.jpg", "digital_signature": "SIG-083N"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_090",
        instruction=(
            "On 2025-09-11, at STORE-001, auditor EMP-1002 compiles a list of all SKUs, verifies inventory for SKU ELEC-4KTV55, conducts a physical count, calculates discrepancy using unit_cost $480.0, generates an inventory adjustment, requires dual approval by EMP-1003, and records the audit with timestamp '2025-09-11T10:00:00Z', photo 'photo090_new.jpg', and digital signature 'SIG-090N'. Should any validation fail (including if get_store_inventory returns empty, or if any tool call fails), cease operations and refrain from executing subsequent actions. All parameters must be derived from tool outputs or the instruction."
        ),
        actions=[
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-001"}),
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "ELEC-4KTV55"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "ELEC-4KTV55", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={
                "system_count": 8,
                "physical_count": 8,
                "unit_cost": 480.0
            }),
            Action(name="CreateInventoryAdjustment", kwargs={
                "store_id": "STORE-001",
                "sku": "ELEC-4KTV55",
                "amount": 0.0,
                "reason": "audit_discrepancy"
            }),
            Action(name="DualApproval", kwargs={
                "adjustment_id": adj_id("STORE-001", "ELEC-4KTV55"),
                "approver_id": "EMP-1003"
            }),
            Action(name="LogAuditResult", kwargs={
                "store_id": "STORE-001",
                "sku": "ELEC-4KTV55",
                "auditor_id": "EMP-1002",
                "timestamp": "2025-09-11T10:00:00Z",
                "photo": "photo090_new.jpg",
                "digital_signature": "SIG-090N"
            }),
        ],
        outputs=[
            '"skus": ["ELEC-4KTV55", "HOME-BTHTWL01", "GROC-ALMBTR500"]',
            '"store_inventory": {"store_id": "STORE-001", "sku": "ELEC-4KTV55", "system_count": 8}',
            '"physical_count": 8',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "ELEC-4KTV55")}", "store_id": "STORE-001", "sku": "ELEC-4KTV55", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "ELEC-4KTV55")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "ELEC-4KTV55", "auditor_id": "EMP-1002", "timestamp": "2025-09-11T10:00:00Z", "photo": "photo090_new.jpg", "digital_signature": "SIG-090N"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_091",
        instruction="On 2025-11-03, handle the transfer of 15 units of SKU HOME-BTHTWL01 from STORE-002 to STORE-001. Prior to the transfer, ensure that STORE-002 meets the required safety stock threshold of 20%. Auditor EMP-2004 will log the transfer and update compliance with timestamp '2025-11-03T12:00:00Z', photo 'photo202.jpg', and digital signature 'SIG-202'.",
        actions=[
            Action(name="CheckSafetyStock", kwargs={"store_id": "STORE-002", "sku": "HOME-BTHTWL01", "min_percent": 20}),
            Action(name="CreateTransferOrder", kwargs={"from_store": "STORE-002", "to_store": "STORE-001", "sku": "HOME-BTHTWL01", "quantity": 15}),
            Action(name="LogTransfer", kwargs={"from_store": "STORE-002", "to_store": "STORE-001", "sku": "HOME-BTHTWL01", "quantity": 15}),
            Action(name="UpdateTransferCompliance", kwargs={"transfer_id": trf_id("STORE-002", "STORE-001", "HOME-BTHTWL01"), "status": "logged"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-002", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-2004", "timestamp": "2025-11-03T12:00:00Z", "photo": "photo202.jpg", "digital_signature": "SIG-202"}),
        ],
        outputs=[
            f'"transfer_id": "{trf_id("STORE-002", "STORE-001", "HOME-BTHTWL01")}"',
            '"compliance_status": "logged"',
            '"audit_log": {"store_id": "STORE-002", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-2004", "timestamp": "2025-11-03T12:00:00Z", "photo": "photo202.jpg", "digital_signature": "SIG-202"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_092",
        instruction=(
            "On 2025-07-28, at STORE-001, auditor EMP-1092 verifies inventory for SKU HOME-DESKLMP01, obtains product info, executes a physical count, and if a discrepancy is detected, generates an inventory adjustment and records the audit with timestamp '2025-07-28T09:00:00Z', photo 'photo092.jpg', and digital signature 'SIG-092'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1092"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1092", "timestamp": "2025-07-28T09:00:00Z", "photo": "photo092.jpg", "digital_signature": "SIG-092"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"product_info": {"sku": "HOME-DESKLMP01", "name": "LumiLux LED Desk Lamp", "unit_cost": 17.2}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-28T09:00:00Z", "photo": "photo092.jpg", "digital_signature": "SIG-092"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_093",
        instruction=(
            "On 2025-10-13, at STORE-001, auditor EMP-1002 compiles a list of all SKUs, checks inventory for SKU HOME-BTHTWL01, conducts a physical count, calculates discrepancy using unit_cost $6.0, generates an inventory adjustment, needs dual approval from EMP-1003, logs the audit with timestamp '2025-10-13T10:00:00Z', photo 'photo091.jpg', and digital signature 'SIG-091', and subsequently initiates a transfer of 10 units to STORE-003 with compliance review. If any validation is unsuccessful, pause and do not undertake further actions. All parameters must derive from tool outputs or the instruction."
        ),
        actions=[
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-001"}),
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 100, "physical_count": 100, "unit_cost": 6.0}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": 0.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "HOME-BTHTWL01"), "approver_id": "EMP-1003"}),
            Action(name="LogAuditResult", kwargs={
                "store_id": "STORE-001",
                "sku": "HOME-BTHTWL01",
                "auditor_id": "EMP-1002",
                "timestamp": "2025-10-13T10:00:00Z",
                "photo": "photo091.jpg",
                "digital_signature": "SIG-091"
            }),
            Action(name="CreateTransferOrder", kwargs={"from_store": "STORE-001", "to_store": "STORE-003", "sku": "HOME-BTHTWL01", "quantity": 10}),
            Action(name="ComplianceReview", kwargs={"transfer_id": trf_id("STORE-001", "STORE-003", "HOME-BTHTWL01")}),
        ],
        outputs=[
            '"skus": ["HOME-BTHTWL01", "ELEC-RCHAA04", "GROC-ALMBTR500"]',
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "system_count": 100}',
            '"physical_count": 100',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "timestamp": "2025-10-13T10:00:00Z", "photo": "photo091.jpg", "digital_signature": "SIG-091"}',
            f'"transfer_order": {{"transfer_id": "{trf_id("STORE-001", "STORE-003", "HOME-BTHTWL01")}", "from_store": "STORE-001", "to_store": "STORE-003", "sku": "HOME-BTHTWL01", "quantity": 10}}',
            '"compliance_reviewed": true'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_094",
        instruction=(
            "On 2025-07-29, at STORE-001, auditor EMP-1094 verifies inventory for SKU HOME-DESKLMP01, acquires product info, performs a physical count, and if a discrepancy is identified, produces an inventory adjustment and records the audit with timestamp '2025-07-29T09:00:00Z', photo 'photo094.jpg', and digital_signature 'SIG-094'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1094"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1094", "timestamp": "2025-07-29T09:00:00Z", "photo": "photo094.jpg", "digital_signature": "SIG-094"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"product_info": {"sku": "HOME-DESKLMP01", "name": "LumiLux LED Desk Lamp", "unit_cost": 17.2}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-29T09:00:00Z", "photo": "photo094.jpg", "digital_signature": "SIG-094"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_095",
        instruction=(
            "On 2025-07-29, at STORE-001, auditor EMP-1095 verifies inventory for SKU HOME-DESKLMP01, acquires product info, conducts a physical count, and if a discrepancy is identified, produces an inventory adjustment and records the audit with timestamp '2025-07-29T10:00:00Z', photo 'photo095.jpg', and digital_signature 'SIG-095'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1095"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1095", "timestamp": "2025-07-29T10:00:00Z", "photo": "photo095.jpg", "digital_signature": "SIG-095"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"product_info": {"sku": "HOME-DESKLMP01", "name": "LumiLux LED Desk Lamp", "unit_cost": 17.2}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-29T10:00:00Z", "photo": "photo095.jpg", "digital_signature": "SIG-095"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_096",
        instruction=(
            "On 2025-07-29, at STORE-001, auditor EMP-1096 verifies inventory for SKU HOME-DESKLMP01, acquires product info, conducts a physical count, and if a discrepancy is identified, produces an inventory adjustment and records the audit with timestamp '2025-07-29T11:00:00Z', photo 'photo096.jpg', and digital signature 'SIG-096'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1096"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1096", "timestamp": "2025-07-29T11:00:00Z", "photo": "photo096.jpg", "digital_signature": "SIG-096"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "HOME-DESKLMP01")}", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1096", "timestamp": "2025-07-29T11:00:00Z", "photo": "photo096.jpg", "digital_signature": "SIG-096"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_097",
        instruction=(
            "On 2025-10-13, at STORE-001, auditor EMP-1002 compiles a list of all SKUs, checks inventory for SKU HOME-BTHTWL01, conducts a physical count, calculates discrepancy using unit_cost $6.0, generates an inventory adjustment, needs dual approval from EMP-1003, logs the audit with timestamp '2025-10-13T10:00:00Z', photo 'photo113.jpg', and digital signature 'SIG-113', and then initiates a transfer of 10 units to STORE-003 with compliance review. If any validation is unsuccessful (including if get_store_inventory returns empty, or any tool call fails), pause and do not undertake further actions. All parameters must derive from tool outputs or the instruction."
        ),
        actions=[
            Action(name="ListStoreSkus", kwargs={"store_id": "STORE-001"}),
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01"}),
            # Only proceed if get_store_inventory returns a valid record:
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002"}),
            # Only proceed if get_physical_count returns a valid count:
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 100, "physical_count": 100, "unit_cost": 6.0}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": 0.0, "reason": "audit_discrepancy"}),
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "HOME-BTHTWL01"), "approver_id": "EMP-1003"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "timestamp": "2025-10-13T10:00:00Z", "photo": "photo113.jpg", "digital_signature": "SIG-113"}),
            Action(name="CreateTransferOrder", kwargs={"from_store": "STORE-001", "to_store": "STORE-003", "sku": "HOME-BTHTWL01", "quantity": 10}),
            Action(name="ComplianceReview", kwargs={"transfer_id": trf_id("STORE-001", "STORE-003", "HOME-BTHTWL01")}),
        ],
        outputs=[
            '"skus": ["HOME-BTHTWL01", "ELEC-RCHAA04", "GROC-ALMBTR500"]',
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "system_count": 100}',
            '"physical_count": 100',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "approver_id": "EMP-1003", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1002", "timestamp": "2025-10-13T10:00:00Z", "photo": "photo113.jpg", "digital_signature": "SIG-113"}',
            f'"transfer_order": {{"transfer_id": "{trf_id("STORE-001", "STORE-003", "HOME-BTHTWL01")}", "from_store": "STORE-001", "to_store": "STORE-003", "sku": "HOME-BTHTWL01", "quantity": 10}}',
            f'"compliance_reviewed": {{"transfer_id": "{trf_id("STORE-001", "STORE-003", "HOME-BTHTWL01")}", "reviewed": true}}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_098",
        instruction="Transfer 8 units of CLTH-SLFJEAN34 from STORE-002 to STORE-004. Utilize the transfer_id and adjustment_id returned by the respective create_* actions for all compliance and approval steps. Auditor EMP-1050 will confirm store_id, sku, and auditor_id before all operations. Document and update compliance. Require dual approval on adjustment_id. Escalate to compliance if transfer value exceeds $100.0. Document audit with timestamp '2025-07-03T09:00:00Z', photo 'photo080.jpg', and digital signature 'SIG-080'. Adjustment amount is -176.0 (8 units x $22.0).",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-002", "sku": "CLTH-SLFJEAN34"}),
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-004", "sku": "CLTH-SLFJEAN34"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-002", "sku": "CLTH-SLFJEAN34", "auditor_id": "EMP-1050"}),
            Action(name="LogTransfer", kwargs={"from_store": "STORE-002", "to_store": "STORE-004", "sku": "CLTH-SLFJEAN34", "quantity": 8}),
            Action(name="CreateTransferOrder", kwargs={"from_store": "STORE-002", "to_store": "STORE-004", "sku": "CLTH-SLFJEAN34", "quantity": 8}),
            # Use the transfer_id returned by create_transfer_order for all subsequent steps
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-002", "sku": "CLTH-SLFJEAN34", "amount": -176.0}),
            # Use the adjustment_id returned by create_inventory_adjustment for all subsequent steps
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-002", "CLTH-SLFJEAN34")}),
            Action(name="UpdateTransferCompliance", kwargs={"transfer_id": trf_id("STORE-002", "STORE-004", "CLTH-SLFJEAN34"), "status": "dual_approved"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-002", "sku": "CLTH-SLFJEAN34", "auditor_id": "EMP-1050", "timestamp": "2025-07-03T09:00:00Z", "photo": "photo080.jpg", "digital_signature": "SIG-080"}),
        ],
        outputs=[
            f'"transfer_id": "{trf_id("STORE-002", "STORE-004", "CLTH-SLFJEAN34")}"',
            f'"adjustment_id": "{adj_id("STORE-002", "CLTH-SLFJEAN34")}"',
            '"dual_approved": true',
            '"compliance_status": "dual_approved"',
            '"audit_log": {"store_id": "STORE-002", "sku": "CLTH-SLFJEAN34", "timestamp": "2025-07-03T09:00:00Z", "photo": "photo080.jpg", "digital_signature": "SIG-080"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_099",
        instruction="On 2025-07-03, at STORE-001, auditor EMP-1061 verifies inventory and product info for SKU HOME-BTHTWL01, conducts a physical count, computes discrepancy, generates an inventory adjustment, requires dual approval from EMP-1002, and documents the audit with timestamp '2025-07-03T00:00:00Z', photo 'photo098.jpg', and digital signature 'SIG-098'.",
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01"}),
            Action(name="GetProductInfo", kwargs={"sku": "HOME-BTHTWL01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1061"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 100, "physical_count": 100, "unit_cost": 6.0}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": 0.0, "reason": "audit_discrepancy"}),
            # Use the adjustment_id returned by create_inventory_adjustment for dual_approval
            Action(name="DualApproval", kwargs={"adjustment_id": adj_id("STORE-001", "HOME-BTHTWL01"), "approver_id": "EMP-1002"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "auditor_id": "EMP-1061", "timestamp": "2025-07-03T00:00:00Z", "photo": "photo098.jpg", "digital_signature": "SIG-098"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "system_count": 100}',
            '"product_info": {"sku": "HOME-BTHTWL01", "name": "UltraSoft Cotton Bath Towel", "unit_cost": 6.0}',
            '"physical_count": 100',
            '"discrepancy_amount": 0.0',
            f'"inventory_adjustment": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "store_id": "STORE-001", "sku": "HOME-BTHTWL01", "amount": 0.0, "reason": "audit_discrepancy"}}',
            f'"dual_approval": {{"adjustment_id": "{adj_id("STORE-001", "HOME-BTHTWL01")}", "approver_id": "EMP-1002", "approved": true}}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-BTHTWL01", "timestamp": "2025-07-03T00:00:00Z", "photo": "photo098.jpg", "digital_signature": "SIG-098"}'
        ],
    ),
    Task(
        annotator="0",
        user_id="task_100",
        instruction=(
            "On 2025-07-19, at STORE-001, auditor EMP-1020 identifies a discrepancy for SKU HOME-DESKLMP01. The system shows 45 units, the physical count is 40, and the unit cost is $17.2. The auditor produces an inventory adjustment for the discrepancy with reason 'audit_discrepancy' and logs the audit with timestamp '2025-07-19T09:00:00Z', photo 'photo063.jpg', and digital signature 'SIG-063'."
        ),
        actions=[
            Action(name="GetStoreInventory", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01"}),
            Action(name="GetPhysicalCount", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1020"}),
            Action(name="ComputeDiscrepancyAmount", kwargs={"system_count": 45, "physical_count": 40, "unit_cost": 17.2}),
            Action(name="CreateInventoryAdjustment", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}),
            Action(name="LogAuditResult", kwargs={"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "auditor_id": "EMP-1020", "timestamp": "2025-07-19T09:00:00Z", "photo": "photo063.jpg", "digital_signature": "SIG-063"}),
        ],
        outputs=[
            '"store_inventory": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "system_count": 45}',
            '"physical_count": 40',
            '"discrepancy_amount": -86.0',
            '"inventory_adjustment": {"adjustment_id": "ADJ-AAD81F", "store_id": "STORE-001", "sku": "HOME-DESKLMP01", "amount": -86.0, "reason": "audit_discrepancy"}',
            '"audit_log": {"store_id": "STORE-001", "sku": "HOME-DESKLMP01", "timestamp": "2025-07-19T09:00:00Z", "photo": "photo063.jpg", "digital_signature": "SIG-063"}'
        ],
    )
]
