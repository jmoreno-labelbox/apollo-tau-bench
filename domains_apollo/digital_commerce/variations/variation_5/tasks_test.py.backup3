from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="v5",
        user_id="task_001",
        instruction=(
            "You are Maria Garcia (emily.w@email.com). You aim to finalize a purchase of two units of a Wireless Mouse from CAT103."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="ListProductsInCategory", kwargs={"category_id": "CAT103"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1003", "quantity": 1}),
            Action(name="SetItemQuantity", kwargs={"cart_item_id": "C001:1003", "new_quantity": 2}),
            Action(name="PreviewCartTotals", kwargs={"cart_id": "C001"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":80.0,"discount_amount":0.0,"total_amount":80.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_002",
        instruction="You are Mike Rivera (tom.j@email.com). You intend to purchase a Wireless Mouse along with a Branded Hoodie (M), and decide to set the hoodie quantity to 2.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="GetProductByName", kwargs={"name": "Branded Hoodie (M)"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1003", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1006", "quantity": 2}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":160.0,"discount_amount":0.0,"total_amount":160.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_003",
        instruction=(
            "You are Alice Johnson (emily.w@email.com). You wish to include 1 Ergo Laptop Stand from CAT103 in your order."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Ergo Laptop Stand"}),
            Action(name="GetProductByName", kwargs={"name": "4K Webcam"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1010", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1018", "quantity": 1}),
            Action(name="SetItemQuantity", kwargs={"cart_item_id": "C001:1010", "new_quantity": 2}),
            Action(name="RemoveItemFromCart", kwargs={"cart_id": "C001", "product_id": "1018"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":110.0,"discount_amount":0.0,"total_amount":110.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_004",
        instruction=(
            "You are Daniel Kim from Platform Ops. You need to register a subnet group 'sgp-lab-01' with the name 'cache-subnet-lab' in VPC 'vpc-001' over subnets ['subnet-a9','subnet-b9']; verify it; then rename it to 'cache-subnet-lab-temp' with description 'Lab cache staging', verify again; and eventually rename it to 'cache-subnet-lab-renamed' with description 'Lab cache subnets' and read it back."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="CreateSubnetGroup", kwargs={"subnet_group_id": "sgp-lab-01","name": "cache-subnet-lab","description": "Initial","subnet_ids": ["subnet-a9", "subnet-b9"],"vpc_id": "vpc-001"}),
            Action(name="GetSubnetGroup", kwargs={"subnet_group_id": "sgp-lab-01"}),
            Action(name="UpdateSubnetGroupDescription", kwargs={"subnet_group_id": "sgp-lab-01","name": "cache-subnet-lab-temp","description": "Lab cache staging"}),
            Action(name="GetSubnetGroup", kwargs={"subnet_group_id": "sgp-lab-01"}),
            Action(name="UpdateSubnetGroupDescription", kwargs={"subnet_group_id": "sgp-lab-01","name": "cache-subnet-lab-renamed","description": "Lab cache subnets"}),
            Action(name="GetSubnetGroup", kwargs={"subnet_group_id": "sgp-lab-01"}),
        ],
        outputs=['{"subnet_group_id":"sgp-lab-01","name":"cache-subnet-lab-renamed"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_005",
        instruction=(
            "You are Maria Garcia (emily.w@email.com). You wish to purchase a ProBook X15. Following checkout, ensure the shipping address is set to: name 'Maria Garcia', line1 '123 Maple St', city 'Nashville', region 'TN', postal_code '37209', country 'US'."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "ProBook X15"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1001", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SetOrderShippingAddress", kwargs={"order_id": "O001","address": {"name": "Maria Garcia","line1": "123 Maple St","city": "Nashville","region": "TN","postal_code": "37209","country": "US"}}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":1500.0,"discount_amount":0.0,"total_amount":1500.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_006",
        instruction=(
            "As Mike Rivera (tom.j@email.com), you intend to execute a purchase under your B2B Wholesale terms (pricebook_id: 2), selecting a USB-C Hub (product_id: 1002). Create cart C001 for contact_id 205, add 1 USB-C Hub, then create order O001 from this cart."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetPricebookByName", kwargs={"name": "B2B Wholesale"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SwitchCartPricebook", kwargs={"cart_id": "C001", "pricebook_id": "2"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1002", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":60.0,"discount_amount":0.0,"total_amount":60.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_007",
        instruction=(
            "Acting as Priya Shah from Cloud Engineering, you aim to use the UAT cache subnet group within your environment to set up a temporary Redis cache 'ec-lab-01' (engine 'redis', node 'cache.t3.small', endpoint 'ec-lab-01.cache.local', port 6379) on the cache security group. You plan to transition it from 'Modifying' to 'Available', temporarily permit Redis 6379 from '10.2.0.0/16', and thereafter audit the rules while verifying the cache."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="ProvisionElasticacheCluster", kwargs={
                "cluster_id": "ec-lab-01","engine": "redis","node_type": "cache.t3.small","num_nodes": 1,
                "subnet_group_id": "esg-uat-1","security_group_id": "sg-cache",
                "auth_token_enabled": True,"transit_encryption_enabled": True,"at_rest_encryption_enabled": True,
                "endpoint": "ec-lab-01.cache.local","port": 6379,"created_at": "2025-08-06T12:00:00Z"}),
            Action(name="UpdateElasticacheClusterStatus", kwargs={"cluster_id": "ec-lab-01", "status": "Modifying", "changed_at": "2025-08-06T12:00:00Z"}),
            Action(name="UpdateElasticacheClusterStatus", kwargs={"cluster_id": "ec-lab-01", "status": "Available", "changed_at": "2025-08-06T12:00:00Z"}),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "ec-lab-01"}),
            Action(name="AddSecurityGroupRule", kwargs={"group_id": "sg-cache","direction": "ingress","protocol": "tcp","port": 6379,"cidr": "10.2.0.0/16","description": "Temporary allow for verification"}),
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=['{"cluster_id":"ec-lab-01","status":"Available"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_008",
        instruction="As David Chen (tom.j@email.com), your goal is to apply the WELCOME5 offer and purchase a USB-C Hub.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetOfferByCode", kwargs={"code": "WELCOME5"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1002", "quantity": 1}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C001", "code": "WELCOME5"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":75.0,"discount_amount":5.0,"total_amount":70.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_009",
        instruction=(
            "Identifying as Maria Garcia (emily.w@email.com), you wish to utilize your WINTER20 promotion, add a USB-C Hub and a 4K Webcam to your cart, check the totals, and finalize the order."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetOfferByCode", kwargs={"code": "WINTER20"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="GetProductByName", kwargs={"name": "4K Webcam"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1002", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1018", "quantity": 1}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C001", "code": "WINTER20"}),
            Action(name="PreviewCartTotals", kwargs={"cart_id": "C001"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":274.0,"discount_amount":54.8,"total_amount":219.2}'],
    ),

    Task(
        annotator="v5",
        user_id="task_010",
        instruction=(
            "Operating as David Chen from SRE, you plan to use the production cache subnet group to initiate a maintenance Redis cache 'ec-maint-01' (engine 'redis', node 'cache.t3.micro', endpoint 'ec-maint-01.cache.local', port 6379) on the cache security group 'sg-cache' and bring it online with authentication tokens off and encryption (in transit and at rest) disabled. After provisioning, verify the cluster details when it becomes Available. Subsequently, permit Redis 6379 from 10.0.0.0/16 with the exact description 'Temporary allow for verification' and confirm the active rules. Return the cluster id."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="ProvisionElasticacheCluster", kwargs={
                "cluster_id": "ec-maint-01","engine": "redis","node_type": "cache.t3.micro","num_nodes": 1,
                "subnet_group_id": "esg-prod-1","security_group_id": "sg-cache",
                "auth_token_enabled": False,"transit_encryption_enabled": False,"at_rest_encryption_enabled": False,
                "endpoint": "ec-maint-01.cache.local","port": 6379,"created_at": "2025-08-06T12:00:00Z"}),
            Action(name="UpdateElasticacheClusterStatus", kwargs={"cluster_id": "ec-maint-01", "status": "Modifying", "changed_at": "2025-08-06T12:00:00Z"}),
            Action(name="UpdateElasticacheClusterStatus", kwargs={"cluster_id": "ec-maint-01", "status": "Available", "changed_at": "2025-08-06T12:00:00Z"}),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "ec-maint-01"}),
            Action(name="AddSecurityGroupRule", kwargs={"group_id": "sg-cache","direction": "ingress","protocol": "tcp","port": 6379,"cidr": "10.0.0.0/16","description": "Temporary allow for verification"}),
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=['{"cluster_id":"ec-maint-01","final_status":"Available"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_011",
        instruction=(
            "You are Alice Johnson (emily.w@email.com). Your objective is to purchase a Wireless Mouse and a Branded Hoodie (M), and thereafter return just the mouse stating 'Customer changed mind' as the reason."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="GetProductByName", kwargs={"name": "Branded Hoodie (M)"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1003", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1006", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ListOrderItems", kwargs={"order_id": "O001"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O001", "lines": [{"product_id": "1003", "qty": 1}], "reason": "Customer changed mind"}),
        ],
        outputs=['{"order_id":"O001","items_processed":[{"product_id":"1003","quantity":1,"refund_amount":40.0,"reason":"Customer changed mind"}],"total_refund_amount":40.0,"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_012",
        instruction=(
            "You are Alex Nguyen from Cloud Engineering. Utilizing the production cache subnet group, your goal is to bring a small Redis cache 'ec-lite-01' (engine 'redis', node 'cache.t3.small', endpoint 'ec-lite-01.cache.local', port 6379) on security group 'sg-cache' online and verify its details. Permit a short-lived HTTPS egress on 443 specifically described as 'Temporary HTTPS egress for audit', then confirm the rule set. Return the cluster id."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="ProvisionElasticacheCluster", kwargs={
                "cluster_id": "ec-lite-01","engine": "redis","node_type": "cache.t3.small","num_nodes": 1,
                "subnet_group_id": "esg-prod-1","security_group_id": "sg-cache",
                "auth_token_enabled": True,"transit_encryption_enabled": True,"at_rest_encryption_enabled": True,
                "endpoint": "ec-lite-01.cache.local","port": 6379,"created_at": "2025-08-06T12:00:00Z"}),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "ec-lite-01"}),
            Action(name="UpdateElasticacheClusterStatus", kwargs={"cluster_id": "ec-lite-01", "status": "Available", "changed_at": "2025-08-06T12:00:00Z"}),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "ec-lite-01"}),
            Action(name="AddSecurityGroupRule", kwargs={"group_id": "sg-cache","direction": "egress","protocol": "tcp","port": 443,"cidr": "0.0.0.0/0","description": "Temporary HTTPS egress for audit"}),
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=['{"cluster_id":"ec-lite-01","status":"Available"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_013",
        instruction=(
            "You are Nora Patel (kevin.lee@starlight.net). Your intention is to purchase a ProBook X15 under B2B Wholesale terms."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="GetPricebookByName", kwargs={"name": "B2B Wholesale"}),
            Action(name="GetProductByName", kwargs={"name": "ProBook X15"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "210", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SwitchCartPricebook", kwargs={"cart_id": "C001", "pricebook_id": "2"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1001", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":1250.0,"discount_amount":0.0,"total_amount":1250.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_014",
        instruction="You are Maria Garcia (emily.w@email.com). You plan to apply the WINTER20 offer and proceed to purchase a Wireless Mouse.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetOfferByCode", kwargs={"code": "WINTER20"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1003", "quantity": 1}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C001", "code": "WINTER20"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":40.0,"discount_amount":8.0,"total_amount":32.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_015",
        instruction=(
            "You are David Chen (tom.j@email.com). Your task is to apply the WELCOME5 coupon, navigate through category CAT103 to select a 4K Webcam, review the totals, and then place the order."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetOfferByCode", kwargs={"code": "WELCOME5"}),
            Action(name="ListProductsInCategory", kwargs={"category_id": "CAT103"}),
            Action(name="GetProductByName", kwargs={"name": "4K Webcam"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1018", "quantity": 1}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C001", "code": "WELCOME5"}),
            Action(name="PreviewCartTotals", kwargs={"cart_id": "C001"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":199.0,"discount_amount":5.0,"total_amount":194.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_016",
        instruction=(
            "Identify as Mike Rivera (tom.j@email.com). Seek to obtain a Pro Gaming Mouse from CAT103 under B2B Wholesale conditions."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetPricebookByName", kwargs={"name": "B2B Wholesale"}),
            Action(name="ListProductsInCategory", kwargs={"category_id": "CAT103"}),
            Action(name="GetProductByName", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SwitchCartPricebook", kwargs={"cart_id": "C001", "pricebook_id": "2"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1013", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":65.0,"discount_amount":0.0,"total_amount":65.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_017",
        instruction=(
            "Identify as Nora Patel (kevin.lee@starlight.net). Aim to use the coupon B2BVOLUME15 and purchase two ProBook X15 devices."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="GetOfferByCode", kwargs={"code": "B2BVOLUME15"}),
            Action(name="GetProductByName", kwargs={"name": "ProBook X15"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "210", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1001", "quantity": 1}),
            Action(name="SetItemQuantity", kwargs={"cart_item_id": "C001:1001", "new_quantity": 2}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C001", "code": "B2BVOLUME15"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":2500.0,"discount_amount":375.0,"total_amount":2125.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_018",
        instruction="Act as David Chen (david.c@email.com). Intend to transition to the B2B Wholesale pricebook and acquire a Wireless Mouse.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "david.c@email.com"}),
            Action(name="GetPricebookByName", kwargs={"name": "B2B Wholesale"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SwitchCartPricebook", kwargs={"cart_id": "C001", "pricebook_id": "2"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1003", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":32.0,"discount_amount":0.0,"total_amount":32.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_019",
        instruction="Present yourself as Alice Johnson (emily.w@email.com). Plan to utilize WINTER20 and purchase a USB-C Hub.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetOfferByCode", kwargs={"code": "WINTER20"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1002", "quantity": 1}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C001", "code": "WINTER20"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":75.0,"discount_amount":15.0,"total_amount":60.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_020",
        instruction="Identify as Mike Rivera (tom.j@email.com). Plan to apply WELCOME5 and purchase a Pro Gaming Mouse.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetOfferByCode", kwargs={"code": "WELCOME5"}),
            Action(name="GetProductByName", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1013", "quantity": 1}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C001", "code": "WELCOME5"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":80.0,"discount_amount":5.0,"total_amount":75.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_021",
        instruction=(
            "As Taylor Reed from Security, document controlled connectivity using the cache group 'sg-cache': allow Redis on 6379 and metrics on 9121 from 10.140.0.0/16, and permit HTTPS egress on 443 to the internet. Provide the group id."
        ),
        actions=[
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
            Action(name="AddSecurityGroupRule", kwargs={
                "group_id": "sg-cache", "direction": "ingress", "protocol": "tcp", "port": 6379,
                "cidr": "10.140.0.0/16", "description": "Redis allow"}),
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
            Action(name="AddSecurityGroupRule", kwargs={
                "group_id": "sg-cache", "direction": "egress", "protocol": "tcp", "port": 443,
                "cidr": "0.0.0.0/0", "description": "HTTPS egress"}),
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
            Action(name="AddSecurityGroupRule", kwargs={
                "group_id": "sg-cache", "direction": "ingress", "protocol": "tcp", "port": 9121,
                "cidr": "10.140.0.0/16", "description": "Metrics scrapers"}),
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=['{"group_id":"sg-cache","changes_recorded":true}'],
    ),

    Task(
        annotator="v5",
        user_id="task_022",
        instruction=(
            "With the email 'tom.j@email.com', complete a purchase of 1 'Ergo Laptop Stand' using the WINTER20 promotion, using cart id C022 and order id O022. Return the order id."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetOfferByCode", kwargs={"code": "WINTER20"}),
            Action(name="GetProductByName", kwargs={"name": "Ergo Laptop Stand"}),
            Action(name="CreateCart", kwargs={"cart_id": "C022", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C022", "product_id": "1010", "quantity": 1}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C022", "code": "WINTER20"}),
            Action(name="CreateOrder", kwargs={"order_id": "O022", "cart_id": "C022", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O022","status":"Processing","subtotal":55.0,"discount_amount":11.0,"total_amount":44.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_023",
        instruction=(
            "Acting as Alice Johnson (emily.w@email.com), proceed to buy a Branded Hoodie (M) using the WELCOME5 promotion."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetOfferByCode", kwargs={"code": "WELCOME5"}),
            Action(name="GetProductByName", kwargs={"name": "Branded Hoodie (M)"}),
            Action(name="CreateCart", kwargs={"cart_id": "C023", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C023", "product_id": "1006", "quantity": 1}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C023", "code": "WELCOME5"}),
            Action(name="CreateOrder", kwargs={"order_id": "O023", "cart_id": "C023", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O023","status":"Processing","subtotal":60.0,"discount_amount":5.0,"total_amount":55.0}'],
    ),


    Task(
        annotator="v5",
        user_id="task_024",
        instruction=(
            "Under the identity of Nora Patel (kevin.lee@starlight.net), intend to purchase a Wireless Mouse from CAT103 using the WINTER20 promotion."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="GetOfferByCode", kwargs={"code": "WINTER20"}),
            Action(name="ListProductsInCategory", kwargs={"category_id": "CAT103"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="CreateCart", kwargs={"cart_id": "C024", "contact_id": "210", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C024", "product_id": "1003", "quantity": 1}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C024", "code": "WINTER20"}),
            Action(name="CreateOrder", kwargs={"order_id": "O024", "cart_id": "C024", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O024","status":"Processing","subtotal":32.0,"discount_amount":6.4,"total_amount":25.6}'],
    ),

    Task(
        annotator="v5",
        user_id="task_025",
        instruction=(
            "Being Alex Nguyen from Cloud Engineering, utilize the production cache subnet group to bring a small Redis cache 'ec-lite-02' (engine 'redis', node 'cache.t3.small', endpoint 'ec-lite-02.cache.local', port 6379) on the cache security group 'sg-cache' to Available and confirm its details. Afterwards, allow HTTPS egress on 443 with the exact description 'Temporary HTTPS egress for audit' and verify the rules. Provide the cluster id."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="ProvisionElasticacheCluster", kwargs={
                "cluster_id": "ec-lite-02", "engine": "redis", "node_type": "cache.t3.small", "num_nodes": 1,
                "subnet_group_id": "esg-prod-1", "security_group_id": "sg-cache",
                "auth_token_enabled": True, "transit_encryption_enabled": True, "at_rest_encryption_enabled": True,
                "endpoint": "ec-lite-02.cache.local", "port": 6379, "created_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "ec-lite-02"}),
            Action(name="UpdateElasticacheClusterStatus", kwargs={
                "cluster_id": "ec-lite-02", "status": "Available", "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "ec-lite-02"}),
            Action(name="AddSecurityGroupRule", kwargs={
                "group_id": "sg-cache", "direction": "egress", "protocol": "tcp", "port": 443,
                "cidr": "0.0.0.0/0", "description": "Temporary HTTPS egress for audit"
            }),
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=['{"cluster_id":"ec-lite-02","status":"Available"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_026",
        instruction=(
            "Your name is Alice Johnson (emily.w@email.com). You intend to apply the WINTER20 promotion to finalize the purchase of a USB-C Hub and a Wireless Mouse."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetOfferByCode", kwargs={"code": "WINTER20"}),
            Action(name="CreateCart", kwargs={"cart_id": "C026", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C026", "code": "WINTER20"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C026", "product_id": "1002", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C026", "product_id": "1003", "quantity": 1}),
            Action(name="PreviewCartTotals", kwargs={"cart_id": "C026"}),
            Action(name="CreateOrder", kwargs={"order_id": "O026", "cart_id": "C026", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O026","status":"Processing","subtotal":115.0,"discount_amount":23.0,"total_amount":92.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_027",
        instruction=(
            "Your goal is to acquire a Pro Gaming Mouse and a USB-C Hub under B2B Wholesale terms as Mike Rivera (tom.j@email.com)."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="GetPricebookByName", kwargs={"name": "B2B Wholesale"}),
            Action(name="CreateCart", kwargs={"cart_id": "C027", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C027", "product_id": "1013", "quantity": 1}),
            Action(name="SwitchCartPricebook", kwargs={"cart_id": "C027", "pricebook_id": "2"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C027", "product_id": "1002", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O027", "cart_id": "C027", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O027","status":"Processing","subtotal":125.0,"discount_amount":0.0,"total_amount":125.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_028",
        instruction=(
            "You identify as David Chen (tom.j@email.com). Your plan is to buy an Ergo Laptop Stand applying the WELCOME5 promotion and ensure the order reflects the exact shipping address you provided."
        ),
        actions=[
            Action(name="GetOfferByCode", kwargs={"code": "WELCOME5"}),
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Ergo Laptop Stand"}),
            Action(name="CreateCart", kwargs={"cart_id": "C028", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C028", "code": "WELCOME5"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C028", "product_id": "1010", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O028", "cart_id": "C028", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SetOrderShippingAddress", kwargs={
                "order_id": "O028",
                "address": {
                    "name": "David Chen",
                    "line1": "42 Ocean Ave",
                    "city": "Orlando",
                    "region": "FL",
                    "postal_code": "33101",
                    "country": "US"
                }
            }),
        ],
        outputs=['{"order_id":"O028","status":"Processing","subtotal":55.0,"discount_amount":5.0,"total_amount":50.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_029",
        instruction=(
            "Handle the registration of the cache subnet group 'sgp-audit-01' with the name 'cache-audit' in VPC 'vpc-001' using subnets ['subnet-a7','subnet-b7'] and the description 'Audit cache subnets' exactly as given, and confirm its setup. Following this, configure a minimal Redis cache 'ec-audit-01' (endpoint 'ec-audit-01.cache.local', port 6379) in the security group 'sg-cache', ensuring both auth tokens and encryption (in transit and at rest) are off, set it to Available, and affirm its details. Finally, execute a cluster listing for a quick check of inventory. Provide the cluster id after."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="CreateSubnetGroup", kwargs={
                "subnet_group_id": "sgp-audit-01", "name": "cache-audit", "description": "Audit cache group",
                "subnet_ids": ["subnet-a7", "subnet-b7"], "vpc_id": "vpc-001"
            }),
            Action(name="GetSubnetGroup", kwargs={"subnet_group_id": "sgp-audit-01"}),
            Action(name="ProvisionElasticacheCluster", kwargs={
                "cluster_id": "ec-audit-01", "engine": "redis", "node_type": "cache.t3.micro", "num_nodes": 1,
                "subnet_group_id": "sgp-audit-01", "security_group_id": "sg-cache",
                "auth_token_enabled": False, "transit_encryption_enabled": False, "at_rest_encryption_enabled": False,
                "endpoint": "ec-audit-01.cache.local", "port": 6379, "created_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="UpdateElasticacheClusterStatus", kwargs={
                "cluster_id": "ec-audit-01", "status": "Available", "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "ec-audit-01"}),
            Action(name="ListElasticacheClusters", kwargs={}),
        ],
        outputs=['{"cluster_id":"ec-audit-01","status":"Available","subnet_group_id":"sgp-audit-01"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_030",
        instruction=(
            "Identify as Mike Rivera (tom.j@email.com). Your intention is to purchase a USB-C Hub and a Wireless Mouse, verify the items on the order, and proceed to return the mouse with the reason 'Changed mind'."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="CreateCart", kwargs={"cart_id": "C030", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C030", "product_id": "1002", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C030", "product_id": "1003", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O030", "cart_id": "C030", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ListOrderItems", kwargs={"order_id": "O030"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O030", "lines": [{"product_id": "1003", "qty": 1}], "reason": "Changed mind"}),
        ],
        outputs=[
            '{"order_id":"O030","items_processed":[{"product_id":"1003","quantity":1,"refund_amount":40.0,"reason":"Changed mind"}],"total_refund_amount":40.0,"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_031",
        instruction=(
            "With 'emily.w@email.com', aim to purchase 1 'USB-C Hub', and then initiate and resolve a support case titled 'Package never arrived'. Utilize cart id C031, order id O031, and case id CASE031. Provide the order id upon completion."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="CreateCart", kwargs={"cart_id": "C031", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C031", "product_id": "1002", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O031", "cart_id": "C031", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="CreateCase", kwargs={"case_id": "CASE031", "order_id": "O031", "contact_id": "204", "subject": "Package never arrived", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="UpdateCaseStatus", kwargs={"case_id": "CASE031", "status": "Resolved"}),
        ],
        outputs=['{"case_id":"CASE031","final_status":"Resolved","order_id":"O031"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_032",
        instruction=(
            "As Alice Johnson (emily.w@email.com), ensure your order includes a 4K Webcam from CAT103 and omits the USB-C Hub."
        ),
        actions=[
            Action(name="ListProductsInCategory", kwargs={"category_id": "CAT103"}),
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="GetProductByName", kwargs={"name": "4K Webcam"}),
            Action(name="CreateCart", kwargs={"cart_id": "C032", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C032", "product_id": "1002", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C032", "product_id": "1018", "quantity": 1}),
            Action(name="RemoveItemFromCart", kwargs={"cart_id": "C032", "product_id": "1002"}),
            Action(name="CreateOrder", kwargs={"order_id": "O032", "cart_id": "C032", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O032","status":"Processing","subtotal":199.0,"discount_amount":0.0,"total_amount":199.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_033",
        instruction=(
            "Being Maria Garcia (emily.w@email.com), proceed to buy two units of Pro Gaming Mouse using the B2BVOLUME15 promotion."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetOfferByCode", kwargs={"code": "B2BVOLUME15"}),
            Action(name="GetProductByName", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="CreateCart", kwargs={"cart_id": "C033", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C033", "product_id": "1013", "quantity": 1}),
            Action(name="SetItemQuantity", kwargs={"cart_item_id": "C033:1013", "new_quantity": 2}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C033", "code": "B2BVOLUME15"}),
            Action(name="PreviewCartTotals", kwargs={"cart_id": "C033"}),
            Action(name="CreateOrder", kwargs={"order_id": "O033", "cart_id": "C033", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O033","status":"Processing","subtotal":160.0,"discount_amount":24.0,"total_amount":136.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_034",
        instruction=(
            "As David Chen (tom.j@email.com), seek to acquire a USB-C Hub from CAT103 employing B2B Wholesale pricing."
        ),
        actions=[
            Action(name="GetPricebookByName", kwargs={"name": "B2B Wholesale"}),
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="CreateCart", kwargs={"cart_id": "C034", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SwitchCartPricebook", kwargs={"cart_id": "C034", "pricebook_id": "2"}),
            Action(name="ListProductsInCategory", kwargs={"category_id": "CAT103"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C034", "product_id": "1002", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O034", "cart_id": "C034", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O034","status":"Processing","subtotal":60.0,"discount_amount":0.0,"total_amount":60.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_035",
        instruction=(
            "Utilizing 'kevin.lee@starlight.net', plan to purchase 1 'Wireless Mouse' and 1 'Branded Hoodie (M)' with cart id C035 and order id O035, then proceed to return precisely 1 'Wireless Mouse' and ensure the refund equals the actual amount paid. Provide the refund id."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="GetProductByName", kwargs={"name": "Branded Hoodie (M)"}),
            Action(name="CreateCart", kwargs={"cart_id": "C035", "contact_id": "210", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C035", "product_id": "1003", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C035", "product_id": "1006", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O035", "cart_id": "C035", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O035", "lines": [{"product_id": "1003", "qty": 1}], "reason": "Unwanted"}),
            Action(name="RefundOrderPartial", kwargs={"order_id": "O035", "amount": 32.0, "reason": "Return of Wireless Mouse"}),
        ],
        outputs=['{"refund_id":"RF_0001","order_id":"O035","amount":32.0,"kind":"partial","reason":"Return of Wireless Mouse"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_036",
        instruction=(
            "You are David Chen (david.c@email.com). Your objective is to buy a USB-C Hub using the WELCOME5 promotion and ensure there is a support case titled 'Gift receipt needed' linked to the order."
        ),
        actions=[
            Action(name="GetOfferByCode", kwargs={"code": "WELCOME5"}),
            Action(name="GetContactByEmail", kwargs={"email": "david.c@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="CreateCart", kwargs={"cart_id": "C036", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C036", "code": "WELCOME5"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C036", "product_id": "1002", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O036", "cart_id": "C036", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="CreateCase", kwargs={"case_id": "CASE036", "order_id": "O036", "contact_id": "208", "subject": "Gift receipt needed", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O036","status":"Processing","subtotal":60.0,"discount_amount":5.0,"total_amount":55.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_037",
        instruction=(
            "Assume the role of a Cloud Engineer. Employ the production cache subnet group to have a small Redis cache activated for this task’s cluster, ensuring auth tokens are disabled. Verify details after it is provisioned and reaches Available status. Retrieve the cluster id."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="ProvisionElasticacheCluster", kwargs={
                "cluster_id": "ec-scale-02", "engine": "redis", "node_type": "cache.t3.small", "num_nodes": 1,
                "subnet_group_id": "esg-prod-1", "security_group_id": "sg-cache",
                "auth_token_enabled": False, "transit_encryption_enabled": True, "at_rest_encryption_enabled": True,
                "endpoint": "ec-scale-02.cache.local", "port": 6379, "created_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="UpdateElasticacheClusterConfig", kwargs={
                "cluster_id": "ec-scale-02", "node_type": "cache.t3.medium", "num_nodes": 2, "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="UpdateElasticacheClusterStatus", kwargs={
                "cluster_id": "ec-scale-02", "status": "Available", "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "ec-scale-02"}),
        ],
        outputs=['{"cluster_id":"ec-scale-02","node_type":"cache.t3.medium","num_nodes":2,"status":"Available"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_038",
        instruction=(
            "As a Cloud Engineer, utilize the production cache subnet group (esg-uat-1) to set up a small Redis cache 'ec-throw-03' (cache.t3.micro, endpoint: ec-throw-03.cache.local:6379) for this task’s cluster, with auth tokens and encryption disabled (both in transit and at rest). Verify once it is Available and return the cluster id."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="ProvisionElasticacheCluster", kwargs={
                "cluster_id": "ec-throw-03", "engine": "redis", "node_type": "cache.t3.micro", "num_nodes": 1,
                "subnet_group_id": "esg-uat-1", "security_group_id": "sg-cache",
                "auth_token_enabled": False, "transit_encryption_enabled": False, "at_rest_encryption_enabled": False,
                "endpoint": "ec-throw-03.cache.local", "port": 6379, "created_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="UpdateElasticacheClusterStatus", kwargs={
                "cluster_id": "ec-throw-03", "status": "Available", "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="DeleteElasticacheCluster", kwargs={
                "cluster_id": "ec-throw-03", "deleted_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "ec-throw-03"}),
        ],
        outputs=['{"cluster_id":"ec-throw-03","status":"Deleted"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_039",
        instruction=(
            "You are Maria Garcia (emily.w@email.com, contact_id: 204). Create cart C039, add Pro Gaming Mouse (product_id: 1013), create order O039, then create case CASE039 titled 'Wrong color' and resolve it."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="CreateCart", kwargs={"cart_id": "C039", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C039", "product_id": "1013", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O039", "cart_id": "C039", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="CreateCase", kwargs={"case_id": "CASE039", "order_id": "O039", "contact_id": "204", "subject": "Wrong color", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="UpdateCaseStatus", kwargs={"case_id": "CASE039", "status": "Resolved"}),
        ],
        outputs=['{"case_id":"CASE039","final_status":"Resolved","order_id":"O039"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_040",
        instruction=(
            "Operaring as Alice Johnson (emily.w@email.com), compare the retail and wholesale totals for purchasing a USB-C Hub and proceed with the option yielding a lower total. If both totals are the same, retain your original pricing."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="CreateCart", kwargs={"cart_id": "C040", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C040", "product_id": "1002", "quantity": 1}),
            Action(name="PreviewCartTotals", kwargs={"cart_id": "C040"}),
            Action(name="GetPricebookByName", kwargs={"name": "B2B Wholesale"}),
            Action(name="SwitchCartPricebook", kwargs={"cart_id": "C040", "pricebook_id": "2"}),
            Action(name="PreviewCartTotals", kwargs={"cart_id": "C040"}),
            Action(name="CreateOrder", kwargs={"order_id": "O040", "cart_id": "C040", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O040","status":"Processing","subtotal":60.0,"discount_amount":0.0,"total_amount":60.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_041",
        instruction=(
            "Utilize 'david.c@email.com' to buy 1 '1TB NVMe SSD' with cart id C041 and order id O041, then accurately set the shipping address to 'David Chen, 900 Commerce Dr, Arlington, TX 75001, US' and annul the order. Provide the order id."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "david.c@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="CreateCart", kwargs={"cart_id": "C041", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C041", "product_id": "1016", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O041", "cart_id": "C041", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SetOrderShippingAddress", kwargs={
                "order_id": "O041",
                "address": {
                    "name": "David Chen",
                    "line1": "900 Commerce Dr",
                    "city": "Arlington",
                    "region": "TX",
                    "postal_code": "75001",
                    "country": "US"
                }
            }),
            Action(name="CancelOrder", kwargs={"order_id": "O041", "cancel_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O041","new_status":"Cancelled"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_042",
        instruction=(
            "You are David Chen (tom.j@email.com). Purchase two 1TB NVMe SSDs and return one citing 'Wrong capacity'."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="CreateCart", kwargs={"cart_id": "C042", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C042", "product_id": "1016", "quantity": 1}),
            Action(name="SetItemQuantity", kwargs={"cart_item_id": "C042:1016", "new_quantity": 2}),
            Action(name="CreateOrder", kwargs={"order_id": "O042", "cart_id": "C042", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O042", "lines": [{"product_id": "1016", "qty": 1}], "reason": "Wrong capacity"}),
        ],
        outputs=[
            '{"order_id":"O042","items_processed":[{"product_id":"1016","quantity":1,"refund_amount":120.0,"reason":"Wrong capacity"}],"total_refund_amount":120.0,"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_043",
        instruction="You are Maria Garcia (emily.w@email.com). Apply cart id C043 and order id O043. Acquire 4K Webcam, initiate case CASE043 'Defective lens', then return the merchandise and close the case.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "4K Webcam"}),
            Action(name="CreateCart", kwargs={"cart_id": "C043", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C043", "product_id": "1018", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O043", "cart_id": "C043", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="CreateCase", kwargs={"case_id": "CASE043", "order_id": "O043", "contact_id": "204", "subject": "Defective lens", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O043", "lines": [{"product_id": "1018", "qty": 1}], "reason": "Defective"}),
            Action(name="UpdateCaseStatus", kwargs={"case_id": "CASE043", "status": "Resolved"}),
        ],
        outputs=['{"order_id":"O043","return":{"items_processed":[{"product_id":"1018","quantity":1,"refund_amount":199.0,"reason":"Defective"}],"total_refund_amount":199.0},"case":{"case_id":"CASE043","final_status":"Resolved"}}'],
    ),

    Task(
        annotator="v5",
        user_id="task_044",
        instruction=(
            "You are Nora Patel (kevin.lee@starlight.net). Seek an order including a USB-C Hub and a Pro Gaming Mouse, with intentions to return the mouse under 'Not needed'."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="GetProductByName", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="CreateCart", kwargs={"cart_id": "C044", "contact_id": "210", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C044", "product_id": "1002", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C044", "product_id": "1013", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O044", "cart_id": "C044", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O044", "lines": [{"product_id": "1013", "qty": 1}], "reason": "Not needed"}),
        ],
        outputs=[
            '{"order_id":"O044","items_processed":[{"product_id":"1013","quantity":1,"refund_amount":65.0,"reason":"Not needed"}],"total_refund_amount":65.0,"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_045",
        instruction=(
            "Utilizing 'tom.j@email.com', aim to purchase 1 'Branded Hoodie (M)' and 1 'Wireless Mouse' using cart id C045 and order id O045, then review the items on the order and afterward cancel it. Return the order id."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Branded Hoodie (M)"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="CreateCart", kwargs={"cart_id": "C045", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C045", "product_id": "1006", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C045", "product_id": "1003", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O045", "cart_id": "C045", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ListOrderItems", kwargs={"order_id": "O045"}),
            Action(name="CancelOrder", kwargs={"order_id": "O045", "cancel_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O045","items":[{"product_id":"1006","qty":1,"unit_price":60.0,"line_subtotal":60.0},{"product_id":"1003","qty":1,"unit_price":40.0,"line_subtotal":40.0}],"order_update":{"order_id":"O045","new_status":"Cancelled"}}'],
    ),

    Task(
        annotator="v5",
        user_id="task_046",
        instruction="You identify as Alice Johnson (emily.w@email.com). Utilize cart id C046 and order id O046. Purchase Branded Hoodie (M), initiate a case CASE046 with the note 'Packaging damaged', proceed it to In Progress status, and then close it out.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Branded Hoodie (M)"}),
            Action(name="CreateCart", kwargs={"cart_id": "C046", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C046", "product_id": "1006", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O046", "cart_id": "C046", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="CreateCase", kwargs={"case_id": "CASE046", "order_id": "O046", "contact_id": "207", "subject": "Packaging damaged", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="UpdateCaseStatus", kwargs={"case_id": "CASE046", "status": "In Progress"}),
            Action(name="UpdateCaseStatus", kwargs={"case_id": "CASE046", "status": "Resolved"}),
        ],
        outputs=['{"case_id":"CASE046","final_status":"Resolved","order_id":"O046"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_047",
        instruction=(
            "You represent Priya Shah from Cloud Engineering. From the available subnet groups, select the UAT group 'esg-uat-1' to deploy a temporary Redis cache 'ec-lab-02' (endpoint 'ec-lab-02.cache.local', port 6379) on 'sg-cache', progress it from 'Modifying' to 'Available', and confirm the specifics. Return the cluster id."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="ProvisionElasticacheCluster", kwargs={
                "cluster_id": "ec-lab-02", "engine": "redis", "node_type": "cache.t3.small", "num_nodes": 1,
                "subnet_group_id": "esg-uat-1", "security_group_id": "sg-cache",
                "auth_token_enabled": True, "transit_encryption_enabled": True, "at_rest_encryption_enabled": True,
                "endpoint": "ec-lab-02.cache.local", "port": 6379, "created_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="UpdateElasticacheClusterStatus", kwargs={
                "cluster_id": "ec-lab-02", "status": "Modifying", "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="UpdateElasticacheClusterStatus", kwargs={
                "cluster_id": "ec-lab-02", "status": "Available", "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "ec-lab-02"}),
        ],
        outputs=['{"cluster_id":"ec-lab-02","status":"Available"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_048",
        instruction=(
            "You identify as Daniel Kim from Platform Ops. Register the subnet group 'sgp-green-01' with the designation 'cache-green' in VPC 'vpc-001', including subnets ['subnet-g1','subnet-g2'] with the description explicitly 'Green cache subnets' and verify its registration. Subsequently, set up a Redis cache 'ec-green-01' (endpoint 'ec-green-01.cache.local', port 6379) on 'sg-cache' without auth tokens and encryption (neither in transit nor at rest), bring it to an Available state, and verify the setup. Return the cluster id."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="CreateSubnetGroup", kwargs={
                "subnet_group_id": "sgp-green-01", "name": "cache-green", "description": "Green cache subnets",
                "subnet_ids": ["subnet-g1", "subnet-g2"], "vpc_id": "vpc-001"
            }),
            Action(name="GetSubnetGroup", kwargs={"subnet_group_id": "sgp-green-01"}),
            Action(name="ProvisionElasticacheCluster", kwargs={
                "cluster_id": "ec-green-01", "engine": "redis", "node_type": "cache.t3.micro", "num_nodes": 1,
                "subnet_group_id": "sgp-green-01", "security_group_id": "sg-cache",
                "auth_token_enabled": False, "transit_encryption_enabled": False, "at_rest_encryption_enabled": False,
                "endpoint": "ec-green-01.cache.local", "port": 6379, "created_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="UpdateElasticacheClusterStatus", kwargs={
                "cluster_id": "ec-green-01", "status": "Available", "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "ec-green-01"}),
        ],
        outputs=['{"cluster_id":"ec-green-01","status":"Available","subnet_group_id":"sgp-green-01"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_049",
        instruction=(
            "You represent Alex Nguyen from Cloud Engineering. Locate cache 'dcomm-uat-redis', adjust its size to 'cache.t3.medium' with 2 nodes for testing purposes, set it to 'Available', and verify the update."
        ),
        actions=[
            Action(name="ListElasticacheClusters", kwargs={}),
            Action(name="UpdateElasticacheClusterConfig", kwargs={
                "cluster_id": "dcomm-uat-redis", "node_type": "cache.t3.medium", "num_nodes": 2, "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="UpdateElasticacheClusterStatus", kwargs={
                "cluster_id": "dcomm-uat-redis", "status": "Available", "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
        ],
        outputs=['{"cluster_id":"dcomm-uat-redis","node_type":"cache.t3.medium","num_nodes":2,"status":"Available"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_050",
        instruction="You are Mike Rivera (tom.j@email.com). You want to use cart id C050 and order id O050. "
                    "Purchase a 4K Webcam, list the items on the order, then return the webcam with reason 'Not needed' "
                    "and show the refund amount.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "4K Webcam"}),
            Action(name="CreateCart", kwargs={"cart_id": "C050", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C050", "product_id": "1018", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O050", "cart_id": "C050", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ListOrderItems", kwargs={"order_id": "O050"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O050", "lines": [{"product_id": "1018", "qty": 1}], "reason": "Not needed"}),
        ],
        outputs=[
            '{"order_id":"O050","items":[{"product_id":"1018","qty":1,"unit_price":199.0,"line_subtotal":199.0}],"refund":{"total_refund_amount":199.0,"reason":"Not needed"}}'],
    ),

    Task(
        annotator="v5",
        user_id="task_051",
        instruction=(
            "Proceed to purchase Branded Hoodie (M) as Maria Garcia (emily.w@email.com) and initiate a support case titled 'Wrong size', ensuring resolution after creation."
        ),
        actions=[
            Action(name="GetProductByName", kwargs={"name": "Branded Hoodie (M)"}),
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="CreateCart", kwargs={"cart_id": "C051", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C051", "product_id": "1006", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O051", "cart_id": "C051", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="CreateCase", kwargs={"case_id": "CASE051", "order_id": "O051", "contact_id": "204", "subject": "Wrong size", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="UpdateCaseStatus", kwargs={"case_id": "CASE051", "status": "Resolved"}),
        ],
        outputs=['{"case_id":"CASE051","final_status":"Resolved","order_id":"O051"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_052",
        instruction=(
            "You need to act as Riley Chen from Networking. Establish the cache subnet group 'sgp-mini-01', labeled 'cache-mini', within VPC 'vpc-001' across subnets ['subnet-m1','subnet-m2'] with the exact description 'Mini cache group', and confirm the setup. Subsequently, set up a minimal Redis cache 'ec-mini-01' (endpoint 'ec-mini-01.cache.local', port 6379) on 'sg-cache', with auth tokens and encryption both disabled, transition it to Available, verify its specifications, and enumerate clusters for a swift inventory assessment. Provide the cluster id."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="CreateSubnetGroup", kwargs={
                "subnet_group_id": "sgp-mini-01", "name": "cache-mini", "description": "Mini cache group",
                "subnet_ids": ["subnet-m1", "subnet-m2"], "vpc_id": "vpc-001"
            }),
            Action(name="GetSubnetGroup", kwargs={"subnet_group_id": "sgp-mini-01"}),
            Action(name="ProvisionElasticacheCluster", kwargs={
                "cluster_id": "ec-mini-01", "engine": "redis", "node_type": "cache.t3.micro", "num_nodes": 1,
                "subnet_group_id": "sgp-mini-01", "security_group_id": "sg-cache",
                "auth_token_enabled": False, "transit_encryption_enabled": False, "at_rest_encryption_enabled": False,
                "endpoint": "ec-mini-01.cache.local", "port": 6379, "created_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="UpdateElasticacheClusterStatus", kwargs={
                "cluster_id": "ec-mini-01", "status": "Available", "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "ec-mini-01"}),
            Action(name="ListElasticacheClusters", kwargs={}),
        ],
        outputs=['{"cluster_id":"ec-mini-01","status":"Available","subnet_group_id":"sgp-mini-01"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_053",
        instruction="Assume the identity of Alice Johnson (emily.w@email.com). Utilize cart id C053 and order id O053 to apply WINTER20 and purchase a 1TB NVMe SSD.",
        actions=[
            Action(name="GetOfferByCode", kwargs={"code": "WINTER20"}),
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="CreateCart", kwargs={"cart_id": "C053", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C053", "product_id": "1016", "quantity": 1}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C053", "code": "WINTER20"}),
            Action(name="CreateOrder", kwargs={"order_id": "O053", "cart_id": "C053", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O053","status":"Processing","subtotal":120.0,"discount_amount":24.0,"total_amount":96.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_054",
        instruction="Take on the identity of David Chen (tom.j@email.com). Leverage cart id C054 and order id O054 to buy two Branded Hoodie (M), then proceed to return one due to wrong color.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Branded Hoodie (M)"}),
            Action(name="CreateCart", kwargs={"cart_id": "C054", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C054", "product_id": "1006", "quantity": 1}),
            Action(name="SetItemQuantity", kwargs={"cart_item_id": "C054:1006", "new_quantity": 2}),
            Action(name="CreateOrder", kwargs={"order_id": "O054", "cart_id": "C054", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O054", "lines": [{"product_id": "1006", "qty": 1}], "reason": "Wrong color"}),
        ],
        outputs=['{"order_id":"O054","items_processed":[{"product_id":"1006","quantity":1,"refund_amount":60.0,"reason":"Wrong color"}],"total_refund_amount":60.0,"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_055",
        instruction="Identify yourself as Mike Rivera (tom.j@email.com). Use cart id C055 and order id O055 to purchase ProBook X15, display the items, then revoke the order.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "ProBook X15"}),
            Action(name="CreateCart", kwargs={"cart_id": "C055", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C055", "product_id": "1001", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O055", "cart_id": "C055", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ListOrderItems", kwargs={"order_id": "O055"}),
            Action(name="CancelOrder", kwargs={"order_id": "O055", "cancel_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O055","new_status":"Cancelled"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_056",
        instruction="You are David Chen (david.c@email.com). You want to use cart id C056 and order id O056. "
                    "Buy a USB-C Hub, then issue a $5 partial refund with reason 'Goodwill' and show the refund record.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "david.c@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="CreateCart", kwargs={"cart_id": "C056", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C056", "product_id": "1002", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O056", "cart_id": "C056", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="RefundOrderPartial", kwargs={"order_id": "O056", "amount": 5.0, "reason": "Goodwill"}),
        ],
        outputs=['{"refund_id":"RF_0001","order_id":"O056","amount":5.0,"kind":"partial","reason":"Goodwill"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_057",
        instruction="You are Alice Johnson (emily.w@email.com). Switch to B2B Wholesale using cart id C057 and order id O057 and purchase a Wireless Mouse.",
        actions=[
            Action(name="GetPricebookByName", kwargs={"name": "B2B Wholesale"}),
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="CreateCart", kwargs={"cart_id": "C057", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SwitchCartPricebook", kwargs={"cart_id": "C057", "pricebook_id": "2"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C057", "product_id": "1003", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O057", "cart_id": "C057", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O057","status":"Processing","subtotal":32.0,"discount_amount":0.0,"total_amount":32.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_058",
        instruction="You are Maria Garcia (emily.w@email.com). You want to use use cart id C058 and order id O058. "
                    "You buy a Pro Gaming Mouse, then set the shipping address exactly to: "
                    "name 'Maria Garcia', line1 '123 Maple St', city 'Nashville', region 'TN', postal_code '37209', country 'US'.",
        actions=[
            Action(name="GetProductByName", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="CreateCart", kwargs={"cart_id": "C058", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C058", "product_id": "1013", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O058", "cart_id": "C058", "created_at": "2025-08-06T12:00:00Z"}),
            Action(
                name="SetOrderShippingAddress",
                kwargs={
                    "order_id": "O058",
                    "address": {
                        "name": "Maria Garcia",
                        "line1": "123 Maple St",
                        "city": "Nashville",
                        "region": "TN",
                        "postal_code": "37209",
                        "country": "US"}}),
        ],
        outputs=['{"order_id":"O058","status":"Processing","subtotal":80.0,"discount_amount":0.0,"total_amount":80.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_059",
        instruction=(
            "As Nora Patel (kevin.lee@starlight.net), acquire a USB-C Hub, list the order items, then initiate a return of the hub for 'Changed mind' and provide the refund details."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="CreateCart", kwargs={"cart_id": "C059", "contact_id": "210", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C059", "product_id": "1002", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O059", "cart_id": "C059", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ListOrderItems", kwargs={"order_id": "O059"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O059", "lines": [{"product_id": "1002", "qty": 1}], "reason": "Changed mind"}),
        ],
        outputs=[
            '{"order_id":"O059","items":[{"product_id":"1002","qty":1,"unit_price":60.0,"line_subtotal":60.0}],"refund":{"total_refund_amount":60.0,"reason":"Changed mind"},"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_060",
        instruction="You are David Chen (tom.j@email.com). Leverage cart id C060 and order id O060 to preview totals, then proceed to purchase a 1TB NVMe SSD.",
        actions=[
            Action(name="GetProductByName", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="CreateCart", kwargs={"cart_id": "C060", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C060", "product_id": "1016", "quantity": 1}),
            Action(name="PreviewCartTotals", kwargs={"cart_id": "C060"}),
            Action(name="CreateOrder", kwargs={"order_id": "O060", "cart_id": "C060", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O060","status":"Processing","subtotal":120.0,"discount_amount":0.0,"total_amount":120.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_061",
        instruction="Assume the identity of Maria Garcia (emily.w@email.com). Intend to use cart id C061 and order id O061. Purchase Pro Gaming Mouse, review the totals, and subsequently cancel the order.",
        actions=[
            Action(name="GetProductByName", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="CreateCart", kwargs={"cart_id": "C061", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C061", "product_id": "1013", "quantity": 1}),
            Action(name="PreviewCartTotals", kwargs={"cart_id": "C061"}),
            Action(name="CreateOrder", kwargs={"order_id": "O061", "cart_id": "C061", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="CancelOrder", kwargs={"order_id": "O061", "cancel_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O061","new_status":"Cancelled"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_062",
        instruction="You are to assume the identity of Mike Rivera (tom.j@email.com). Intend to use cart id C062 and order id O062. Purchase Ergo Laptop Stand and afterward initiate a return.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Ergo Laptop Stand"}),
            Action(name="CreateCart", kwargs={"cart_id": "C062", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C062", "product_id": "1010", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O062", "cart_id": "C062", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O062", "lines": [{"product_id": "1010", "qty": 1}], "reason": "Not needed"}),
        ],
        outputs=['{"order_id":"O062","items_processed":[{"product_id":"1010","quantity":1,"refund_amount":55.0,"reason":"Not needed"}],"total_refund_amount":55.0,"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_063",
        instruction="Pose as David Chen (david.c@email.com). Plan to use cart id C063 and order id O063. Acquire Wireless Mouse, create CASE063 'Charge discrepancy', and then resolve the case.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "david.c@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="CreateCart", kwargs={"cart_id": "C063", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C063", "product_id": "1003", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O063", "cart_id": "C063", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="CreateCase", kwargs={"case_id": "CASE063", "order_id": "O063", "contact_id": "208", "subject": "Charge discrepancy", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="UpdateCaseStatus", kwargs={"case_id": "CASE063", "status": "Resolved"}),
        ],
        outputs=['{"case_id":"CASE063","final_status":"Resolved","order_id":"O063"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_064",
        instruction=(
            "Act as Casey Brooks from Data Engineering. Using the production cache subnet group, initiate 'ec-analytics-03' on 'sg-cache' as a Redis cache (node type 'cache.t4g.small') with authentication tokens turned off and enable encryption both in transit and at rest; set its status to Available and verify details. Next, allow metrics access on TCP/9121 from 10.10.0.0/16 specifically described as 'Metrics scrapers' and display the created rules. Return the cluster id."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="ProvisionElasticacheCluster", kwargs={
                "cluster_id": "ec-analytics-03", "engine": "redis", "node_type": "cache.t4g.small", "num_nodes": 1,
                "subnet_group_id": "esg-prod-1", "security_group_id": "sg-cache",
                "auth_token_enabled": False, "transit_encryption_enabled": True, "at_rest_encryption_enabled": True,
                "endpoint": "ec-analytics-03.cache.local", "port": 6379, "created_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="UpdateElasticacheClusterStatus", kwargs={
                "cluster_id": "ec-analytics-03", "status": "Available", "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="AddSecurityGroupRule", kwargs={
                "group_id": "sg-cache", "direction": "ingress", "protocol": "tcp", "port": 9121,
                "cidr": "10.10.0.0/16", "description": "Metrics scrapers"
            }),
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=['{"cluster_id":"ec-analytics-03","status":"Available"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_065",
        instruction="Assume the identity of Nora Patel (kevin.lee@starlight.net). Plan to use cart id C065 and order id O065. Apply WINTER20 and purchase 1TB NVMe SSD.",
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="GetOfferByCode", kwargs={"code": "WINTER20"}),
            Action(name="CreateCart", kwargs={"cart_id": "C065", "contact_id": "210", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C065", "code": "WINTER20"}),
            Action(name="GetProductByName", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C065", "product_id": "1016", "quantity": 1}),
            Action(name="CreateOrder", kwargs={"order_id": "O065", "cart_id": "C065", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O065","status":"Processing","subtotal":95.0,"discount_amount":19.0,"total_amount":76.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_066",
        instruction=(
            "Acting as Alice Johnson (emily.w@email.com), purchase two Wireless Mouse units, then specify the shipping address precisely as: name 'Alice Johnson', line1 '77 Pine St', city 'Nashville', region 'TX', postal_code '73301', country 'US'. Following this, return one Wireless Mouse citing 'Changed mind' as the reason."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1003", "quantity": 1}),
            Action(name="SetItemQuantity", kwargs={"cart_item_id": "C001:1003", "new_quantity": 2}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SetOrderShippingAddress", kwargs={
                "order_id": "O001",
                "address": {"name": "Alice Johnson", "line1": "77 Pine St", "city": "Nashville", "region": "TX", "postal_code": "73301", "country": "US"}
            }),
            Action(name="ReturnOrder", kwargs={"order_id": "O001", "lines": [{"product_id": "1003", "qty": 1}], "reason": "Changed mind"}),
        ],
        outputs=[
            '{"order_id":"O001","items_processed":[{"product_id":"1003","quantity":1,"refund_amount":40.0,"reason":"Changed mind"}],"total_refund_amount":40.0,"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_067",
        instruction=(
            "Being Jordan Lee from SRE, select the UAT group 'esg-uat-1' from the list of subnet groups in the environment to initiate a small Redis cache 'ec-mod-01' (endpoint 'ec-mod-01.cache.local', port 6379) on 'sg-cache', ensuring that auth tokens and encryption (both in transit and at rest) are disabled. Transition it from 'Modifying' to 'Available' and confirm the details. Provide the cluster id."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="ProvisionElasticacheCluster", kwargs={
                "cluster_id": "ec-mod-01", "engine": "redis", "node_type": "cache.t3.micro", "num_nodes": 1,
                "subnet_group_id": "esg-uat-1", "security_group_id": "sg-cache",
                "auth_token_enabled": False, "transit_encryption_enabled": False, "at_rest_encryption_enabled": False,
                "endpoint": "ec-mod-01.cache.local", "port": 6379, "created_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="UpdateElasticacheClusterStatus",
                   kwargs={"cluster_id": "ec-mod-01", "status": "Modifying", "changed_at": "2025-08-06T12:00:00Z"}),
            Action(name="UpdateElasticacheClusterStatus",
                   kwargs={"cluster_id": "ec-mod-01", "status": "Available", "changed_at": "2025-08-06T12:00:00Z"}),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "ec-mod-01"}),
        ],
        outputs=['{"cluster_id":"ec-mod-01","status":"Available"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_068",
        instruction=(
            "Assume the identity of David Chen (tom.j@email.com). Add a USB-C Hub to your cart, switch to B2B Wholesale, and then proceed with placing the order."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1002", "quantity": 1}),
            Action(name="GetPricebookByName", kwargs={"name": "B2B Wholesale"}),
            Action(name="SwitchCartPricebook", kwargs={"cart_id": "C001", "pricebook_id": "2"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":60.0,"discount_amount":0.0,"total_amount":60.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_069",
        instruction=(
            "As Nora Patel (kevin.lee@starlight.net), proceed to purchase a 1TB NVMe SSD, review the items on the order, and then cancel the order."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="GetProductByName", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "210", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1016", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ListOrderItems", kwargs={"order_id": "O001"}),
            Action(name="CancelOrder", kwargs={"order_id": "O001", "cancel_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","items":[{"product_id":"1016","qty":1,"unit_price":95.0,"line_subtotal":95.0}],"order_update":{"order_id":"O001","new_status":"Cancelled"}}'],
    ),

    Task(
        annotator="v5",
        user_id="task_070",
        instruction=(
            "Playing the role of David Chen (david.c@email.com), buy a USB-C Hub along with a 4K Webcam, review the total amount, and proceed to finalize the order."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "david.c@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="GetProductByName", kwargs={"name": "4K Webcam"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1002", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1018", "quantity": 1}),
            Action(name="PreviewCartTotals", kwargs={"cart_id": "C001"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":230.0,"discount_amount":0.0,"total_amount":230.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_071",
        instruction=(
            "Identifying as Alice Johnson (emily.w@email.com), your objective is to acquire a USB-C Hub and subsequently apply WELCOME5 prior to placing the order."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1002", "quantity": 1}),
            Action(name="GetOfferByCode", kwargs={"code": "WELCOME5"}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C001", "code": "WELCOME5"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":75.0,"discount_amount":5.0,"total_amount":70.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_072",
        instruction=(
            "Represent yourself as Nora Patel (kevin.lee@starlight.net). Implement Standard Retail pricing to acquire a Wireless Mouse."
        ),
        actions=[
            Action(name="GetPricebookByName", kwargs={"name": "Standard Retail"}),
            Action(name="GetContactByEmail", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "210", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SwitchCartPricebook", kwargs={"cart_id": "C001", "pricebook_id": "1"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1003", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":40.0,"discount_amount":0.0,"total_amount":40.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_073",
        instruction=(
            "Present yourself as Mike Rivera (tom.j@email.com). Intend to buy a 4K Webcam and then configure the shipping address precisely to: name 'Mike Rivera', line1 '9 Elm Rd', city 'Boulder', region 'CO', postal_code '80202', country 'US'. Following this, ensure the order receipt is displayed."
        ),
        actions=[
            Action(name="GetProductByName", kwargs={"name": "4K Webcam"}),
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1018", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SetOrderShippingAddress", kwargs={
                "order_id": "O001",
                "address": {"name": "Mike Rivera", "line1": "9 Elm Rd", "city": "Boulder", "region": "CO", "postal_code": "80202", "country": "US"}
            }),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":199.0,"discount_amount":0.0,"total_amount":199.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_074",
        instruction=(
            "You are David Chen (tom.j@email.com). Proceed to buy a USB-C Hub and a Wireless Mouse, and subsequently return the mouse citing the reason 'Changed mind'."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1002", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1003", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O001", "lines": [{"product_id": "1003", "qty": 1}], "reason": "Changed mind"}),
        ],
        outputs=[
            '{"order_id":"O001","items_processed":[{"product_id":"1003","quantity":1,"refund_amount":40.0,"reason":"Changed mind"}],"total_refund_amount":40.0,"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_075",
        instruction=(
            "While using 'emily.w@email.com', you plan to buy 1 'Branded Hoodie (M)' with cart id C001 and order id O001, initiate a support case titled 'Cancel requested' with case id CASE075, then cancel the order and settle the case. Provide the order id."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Branded Hoodie (M)"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1006", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="CreateCase", kwargs={"case_id": "CASE075", "order_id": "O001", "contact_id": "204", "subject": "Cancel requested",
                                               "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="CancelOrder", kwargs={"order_id": "O001", "cancel_at": "2025-08-06T12:00:00Z"}),
            Action(name="UpdateCaseStatus", kwargs={"case_id": "CASE075", "status": "Resolved"}),
        ],
        outputs=['{"order_id":"O001","new_status":"Cancelled","case":{"case_id":"CASE075","final_status":"Resolved"}}'],
    ),

    Task(
        annotator="v5",
        user_id="task_076",
        instruction=(
            "You are Alice Johnson (emily.w@email.com). Begin by reviewing totals before purchasing a ProBook X15."
        ),
        actions=[
            Action(name="GetProductByName", kwargs={"name": "ProBook X15"}),
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1001", "quantity": 1}),
            Action(name="PreviewCartTotals", kwargs={"cart_id": "C001"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":1500.0,"discount_amount":0.0,"total_amount":1500.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_077",
        instruction=(
            "You are Taylor Reed from Security. Utilizing the cache group 'sg-cache', document controlled connectivity: grant access for Redis on 6379 from 10.150.0.0/16 with the description exactly 'Redis allow', then permit HTTPS egress on 443 with the description exactly 'HTTPS egress', listing rules after each step. Retrieve the group id."
        ),
        actions=[
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
            Action(name="AddSecurityGroupRule", kwargs={
                "group_id": "sg-cache", "direction": "ingress", "protocol": "tcp", "port": 6379,
                "cidr": "10.150.0.0/16", "description": "Redis allow"
            }),
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
            Action(name="AddSecurityGroupRule", kwargs={
                "group_id": "sg-cache", "direction": "egress", "protocol": "tcp", "port": 443,
                "cidr": "0.0.0.0/0", "description": "HTTPS egress"
            }),
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=['{"group_id":"sg-cache","changes_recorded":true}'],
    ),

    Task(
        annotator="v5",
        user_id="task_078",
        instruction=(
            "You are Mike Rivera (tom.j@email.com). Aim to complete a discounted purchase of Branded Hoodie (M) with the WINTER20 coupon, and ensure you preview the totals before finalizing the order. Display the subtotal, discount, and final total."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Branded Hoodie (M)"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1006", "quantity": 1}),
            Action(name="PreviewCartTotals", kwargs={"cart_id": "C001"}),
            Action(name="GetOfferByCode", kwargs={"code": "WINTER20"}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C001", "code": "WINTER20"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":60.0,"discount_amount":12.0,"total_amount":48.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_079",
        instruction=(
            "You are David Chen (david.c@email.com). From category CAT103, confirm the final basket includes USB-C Hub and omits 4K Webcam. Proceed with the purchase and present the order receipt."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "david.c@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="GetProductByName", kwargs={"name": "4K Webcam"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1002", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1018", "quantity": 1}),
            Action(name="RemoveItemFromCart", kwargs={"cart_id": "C001", "product_id": "1018"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":60.0,"discount_amount":0.0,"total_amount":60.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_080",
        instruction=(
            "You are David Chen (tom.j@email.com). Plan to purchase a ProBook X15. Post-checkout, set the shipping address precisely to: name 'David Chen', line1 '42 Ocean Ave', city 'Orlando', region 'FL', postal_code '33101', country 'US'. Next, return the ProBook X15 with reason 'Return within policy' and display the refund amount."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "ProBook X15"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1001", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SetOrderShippingAddress", kwargs={"order_id": "O001",
                                                              "address": {"name": "David Chen", "line1": "42 Ocean Ave", "city": "Orlando",
                                                                          "region": "FL", "postal_code": "33101", "country": "US"}}),
            Action(name="ReturnOrder", kwargs={"order_id": "O001", "lines": [{"product_id": "1001", "qty": 1}], "reason": "Return within policy"}),
        ],
        outputs=[
            '{"order_id":"O080","items_processed":[{"product_id":"1001","quantity":1,"refund_amount":1500.0,"reason":"Return within policy"}],"total_refund_amount":1500.0,"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_081",
        instruction=(
            "Assume the identity of Mike Rivera (tom.j@email.com). Your objective is to purchase a Pro Gaming Mouse. Once you proceed to checkout, update the shipping details to precisely: name 'Mike Rivera', line1 '9 Elm Rd', city 'Boulder', region 'CO', postal_code '80202', country 'US'. Subsequently, cancel the order and display the cancellation status."
        ),
        actions=[
            Action(name="GetProductByName", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1013", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SetOrderShippingAddress", kwargs={"order_id": "O001",
                                                              "address": {"name": "Mike Rivera", "line1": "9 Elm Rd", "city": "Boulder",
                                                                          "region": "CO", "postal_code": "80202", "country": "US"}}),
            Action(name="CancelOrder", kwargs={"order_id": "O001", "cancel_at": "2025-08-06T12:00:00Z"}),
        ],

        outputs=['{"order_id":"O081","new_status":"Cancelled"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_082",
        instruction=(
            "Assume you are Maria Garcia (emily.w@email.com). Your task is to purchase a 1TB NVMe SSD, and then process a return citing the reason 'Not needed' and display the refund total."
        ),
        actions=[
            Action(name="GetProductByName", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1016", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O001", "lines": [{"product_id": "1016", "qty": 1}], "reason": "Not needed"}),
        ],
        outputs=[
            '{"order_id":"O082","items_processed":[{"product_id":"1016","quantity":1,"refund_amount":120.0,"reason":"Not needed"}],"total_refund_amount":120.0,"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_083",
        instruction=(
            "Identify yourself as Alice Johnson (emily.w@email.com). Switch to B2B Wholesale to purchase a USB-C Hub, then initiate a case titled 'Need invoice copy' and finalize its resolution."
        ),
        actions=[
            Action(name="GetPricebookByName", kwargs={"name": "B2B Wholesale"}),
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SwitchCartPricebook", kwargs={"cart_id": "C001", "pricebook_id": "2"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1002", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="CreateCase", kwargs={"case_id": "CASE083", "order_id": "O001", "contact_id": "207", "subject": "Need invoice copy",
                                               "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="UpdateCaseStatus", kwargs={"case_id": "CASE083", "status": "Resolved"}),
        ],
        outputs=['{"case_id":"CASE083","final_status":"Resolved","order_id":"O083"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_084",
        instruction=(
            "Take on the role of Nora Patel (kevin.lee@starlight.net). Your action plan involves purchasing a 4K Webcam, followed by processing a full refund for the reason 'Goodwill' and presenting the refund documentation."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="GetProductByName", kwargs={"name": "4K Webcam"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "210", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1018", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="RefundOrderFull", kwargs={"order_id": "O001", "reason": "Goodwill"}),
        ],
        outputs=['{"refund_id":"RF_0001","order_id":"O084","amount":170.0,"kind":"full","reason":"Goodwill"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_085",
        instruction=(
            "Act as Priya Shah from Cloud Engineering. You should proceed to register a cache subnet group 'sgp-perf-02' (name 'perf-cache', VPC 'vpc-perf', subnets ['subnet-p3','subnet-p4']); verify its registration; deploy a Redis cache 'ec-perf-02' (endpoint 'ec-perf-02.cache.local', port 6379) under the cache security group 'sg-cache'; resize it to 'cache.m6g.large' with 2 nodes; ensure it is set to 'Available'; and retrieve the configuration."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="CreateSubnetGroup", kwargs={
                "subnet_group_id": "sgp-perf-02",
                "name": "perf-cache",
                "description": "Performance cache",
                "subnet_ids": ["subnet-p3", "subnet-p4"],
                "vpc_id": "vpc-perf"
            }),
            Action(name="GetSubnetGroup", kwargs={"subnet_group_id": "sgp-perf-02"}),
            Action(name="ProvisionElasticacheCluster", kwargs={
                "cluster_id": "ec-perf-02",
                "engine": "redis",
                "node_type": "cache.t3.medium",
                "num_nodes": 1,
                "subnet_group_id": "sgp-perf-02",
                "security_group_id": "sg-cache",
                "auth_token_enabled": True,
                "transit_encryption_enabled": True,
                "at_rest_encryption_enabled": True,
                "endpoint": "ec-perf-02.cache.local",
                "port": 6379,
                "created_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="UpdateElasticacheClusterConfig", kwargs={
                "cluster_id": "ec-perf-02",
                "node_type": "cache.m6g.large",
                "num_nodes": 2,
                "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="UpdateElasticacheClusterStatus", kwargs={
                "cluster_id": "ec-perf-02",
                "status": "Available",
                "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="GetElasticacheCluster", kwargs={"cluster_id": "ec-perf-02"}),
        ],
        outputs=['{"cluster_id":"ec-perf-02","node_type":"cache.m6g.large","num_nodes":2,"status":"Available"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_086",
        instruction=(
            "You are David Chen (tom.j@email.com). Intend to purchase two Wireless Mouse, afterwards decide to return one with the reason being 'Changed mind' and display the refund."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1003", "quantity": 1}),
            Action(name="SetItemQuantity", kwargs={"cart_item_id": "C001:1003", "new_quantity": 2}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O001", "lines": [{"product_id": "1003", "qty": 1}], "reason": "Changed mind"}),
        ],

        outputs=[
            '{"order_id":"O086","items_processed":[{"product_id":"1003","quantity":1,"refund_amount":40.0,"reason":"Changed mind"}],"total_refund_amount":40.0,"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_087",
        instruction=(
            "You are Maria Garcia (emily.w@email.com). Plan to purchase a USB-C Hub and a Wireless Mouse, subsequently decide to cancel the order."
        ),
        actions=[
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1002", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1003", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="CancelOrder", kwargs={"order_id": "O001", "cancel_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O087","new_status":"Cancelled"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_088",
        instruction=(
            "You are Mike Rivera (tom.j@email.com). Aim to add a 1TB NVMe SSD, transition to B2B Wholesale, and then finalize the order."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1016", "quantity": 1}),
            Action(name="GetPricebookByName", kwargs={"name": "B2B Wholesale"}),
            Action(name="SwitchCartPricebook", kwargs={"cart_id": "C001", "pricebook_id": "2"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O088","status":"Processing","subtotal":95.0,"discount_amount":0.0,"total_amount":95.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_089",
        instruction=(
            "You are David Chen (tom.j@email.com). Seek to add a 1TB NVMe SSD, then apply WELCOME5 and complete the order."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1016", "quantity": 1}),
            Action(name="GetOfferByCode", kwargs={"code": "WELCOME5"}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C001", "code": "WELCOME5"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],

        outputs=['{"order_id":"O089","status":"Processing","subtotal":120.0,"discount_amount":5.0,"total_amount":115.0}'],
    ),
    Task(
        annotator="v5",
        user_id="task_090",
        instruction=(
            "You are David Chen (david.c@email.com). Aim to purchase a Wireless Mouse, initiate a case titled 'Delayed shipment', and assign it to In Progress."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "david.c@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1003", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="CreateCase", kwargs={"case_id": "CASE090", "order_id": "O001", "contact_id": "208", "subject": "Delayed shipment", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="UpdateCaseStatus", kwargs={"case_id": "CASE090", "status": "In Progress"}),
        ],
        outputs=['{"case_id":"CASE090","status":"In Progress","order_id":"O001"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_091",
        instruction=(
            "Identify yourself as Nora Patel (kevin.lee@starlight.net). You intend to purchase a ProBook X15, then confirm the items on the order. Subsequently, return the laptop with the reason 'Not needed' and display the refund."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="GetProductByName", kwargs={"name": "ProBook X15"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "210", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1001", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ListOrderItems", kwargs={"order_id": "O001"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O001", "lines": [{"product_id": "1001", "qty": 1}], "reason": "Not needed"}),
        ],
        outputs=['{"order_id":"O001","items_processed":[{"product_id":"1001","quantity":1,"refund_amount":1250.0,"reason":"Not needed"}],"total_refund_amount":1250.0,"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_092",
        instruction=(
            "Assume the identity of Mike Rivera (tom.j@email.com). You need to apply WINTER20 and proceed to purchase a Wireless Mouse, followed by cancelling the order."
        ),
        actions=[
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetOfferByCode", kwargs={"code": "WINTER20"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1003", "quantity": 1}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C001", "code": "WINTER20"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="CancelOrder", kwargs={"order_id": "O001", "cancel_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","new_status":"Cancelled"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_093",
        instruction=(
            "Act as David Chen (tom.j@email.com). Your goal is to buy an Ergo Laptop Stand and set the shipping address precisely to: name 'David Chen', line1 '42 Ocean Ave', city 'Orlando', region 'FL', postal_code '33101', country 'US'. Subsequently, return the stand citing the reason 'Return within policy' and present the refund amount."
        ),
        actions=[
            Action(name="GetProductByName", kwargs={"name": "Ergo Laptop Stand"}),
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1010", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(
                name="SetOrderShippingAddress",
                kwargs={
                    "order_id": "O001",
                    "address": {
                        "name": "David Chen",
                        "line1": "42 Ocean Ave",
                        "city": "Orlando",
                        "region": "FL",
                        "postal_code": "33101",
                        "country": "US"
                    }
                }
            ),
            Action(name="ReturnOrder", kwargs={"order_id": "O001", "lines": [{"product_id": "1010", "qty": 1}], "reason": "Return within policy"}),
        ],
        outputs=['{"order_id":"O001","items_processed":[{"product_id":"1010","quantity":1,"refund_amount":55.0,"reason":"Return within policy"}],"total_refund_amount":55.0,"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_094",
        instruction=(
            "Pretend to be Maria Garcia (emily.w@email.com). Plan to purchase a 4K Webcam and then process a $20 partial refund with the reason 'Goodwill' while showing the refund record."
        ),
        actions=[
            Action(name="GetProductByName", kwargs={"name": "4K Webcam"}),
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "204", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1018", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="RefundOrderPartial", kwargs={"order_id": "O001", "amount": 20.0, "reason": "Goodwill"}),
        ],
        outputs=['{"refund_id":"RF_0001","order_id":"O001","amount":20.0,"kind":"partial","reason":"Goodwill"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_095",
        instruction=(
            "Take on the role of Alice Johnson (emily.w@email.com). You intend to browse through CAT103, apply B2BVOLUME15, and then acquire a Pro Gaming Mouse."
        ),
        actions=[
            Action(name="ListProductsInCategory", kwargs={"category_id": "CAT103"}),
            Action(name="GetOfferByCode", kwargs={"code": "B2BVOLUME15"}),
            Action(name="GetProductByName", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="GetContactByEmail", kwargs={"email": "emily.w@email.com"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "207", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1013", "quantity": 1}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C001", "code": "B2BVOLUME15"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":80.0,"discount_amount":12.0,"total_amount":68.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_096",
        instruction=(
            "As David Chen (david.c@email.com), you intend to use Standard Retail pricing for purchasing a 1TB NVMe SSD. Before completing the order, review the totals, then proceed to finalize the checkout and display the receipt."
        ),
        actions=[
            Action(name="GetPricebookByName", kwargs={"name": "Standard Retail"}),
            Action(name="GetContactByEmail", kwargs={"email": "david.c@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SwitchCartPricebook", kwargs={"cart_id": "C001", "pricebook_id": "1"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1016", "quantity": 1}),
            Action(name="PreviewCartTotals", kwargs={"cart_id": "C001"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":120.0,"discount_amount":0.0,"total_amount":120.0}'],
    ),

    Task(
        annotator="v5",
        user_id="task_097",
        instruction=(
            "Being Mike Rivera (tom.j@email.com), you wish to switch to B2B Wholesale pricing, acquire a Wireless Mouse and a USB-C Hub, subsequently return the mouse stating the reason 'Not needed' and present the refund."
        ),
        actions=[
            Action(name="GetPricebookByName", kwargs={"name": "B2B Wholesale"}),
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="GetProductByName", kwargs={"name": "USB-C Hub"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "205", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SwitchCartPricebook", kwargs={"cart_id": "C001", "pricebook_id": "2"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1003", "quantity": 1}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1002", "quantity": 1}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="ReturnOrder", kwargs={"order_id": "O001", "lines": [{"product_id": "1003", "qty": 1}], "reason": "Not needed"}),
        ],
        outputs=['{"order_id":"O001","items_processed":[{"product_id":"1003","quantity":1,"refund_amount":32.0,"reason":"Not needed"}],"total_refund_amount":32.0,"order_status":"Return Pending"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_098",
        instruction=(
            "As Taylor Reed from Security, within the 'sg-cache' group, you aim to have policy updates documented: permit Redis on 6379 from 10.160.0.0/16 with the description exactly 'Redis allow' and permit HTTPS egress on 443 with the description exactly 'HTTPS egress', ensuring the rules remain visible. Return the group id."
        ),
        actions=[
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
            Action(name="AddSecurityGroupRule", kwargs={
                "group_id": "sg-cache", "direction": "ingress", "protocol": "tcp", "port": 6379,
                "cidr": "10.160.0.0/16", "description": "Redis allow"
            }),
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
            Action(name="AddSecurityGroupRule", kwargs={
                "group_id": "sg-cache", "direction": "egress", "protocol": "tcp", "port": 443,
                "cidr": "0.0.0.0/0", "description": "HTTPS egress"
            }),
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=['{"group_id":"sg-cache","changes_recorded":true}'],
    ),

    Task(
        annotator="v5",
        user_id="task_099",
        instruction=(
            "In your role as Priya Shah from Cloud Engineering, leverage the production cache subnet group from your environment to implement 'ec-metrics-02' (endpoint 'ec-metrics-02.cache.local', port 6379) in the cache security group, designate it as 'Available', enable metrics collection on TCP/9121, and enumerate the rules for auditing."
        ),
        actions=[
            Action(name="ListSubnetGroups", kwargs={}),
            Action(name="ProvisionElasticacheCluster", kwargs={
                "cluster_id": "ec-metrics-02", "engine": "redis", "node_type": "cache.t3.small", "num_nodes": 1,
                "subnet_group_id": "esg-prod-1", "security_group_id": "sg-cache",
                "auth_token_enabled": True, "transit_encryption_enabled": True, "at_rest_encryption_enabled": True,
                "endpoint": "ec-metrics-02.cache.local", "port": 6379, "created_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="UpdateElasticacheClusterStatus", kwargs={
                "cluster_id": "ec-metrics-02", "status": "Available", "changed_at": "2025-08-06T12:00:00Z"
            }),
            Action(name="AddSecurityGroupRule", kwargs={
                "group_id": "sg-cache", "direction": "ingress", "protocol": "tcp", "port": 9121,
                "cidr": "10.20.0.0/16", "description": "Metrics scrapers"
            }),
            Action(name="ListSecurityGroupRules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=['{"cluster_id":"ec-metrics-02","status":"Available"}'],
    ),

    Task(
        annotator="v5",
        user_id="task_100",
        instruction=(
            "Acting as David Chen (tom.j@email.com), you plan to apply the WINTER20 coupon to purchase a Wireless Mouse. Once checkout is complete, set the shipping address precisely as: name 'David Chen', line1 '42 Ocean Ave', city 'Orlando', region 'FL', postal_code '33101', country 'US'."
        ),
        actions=[
            Action(name="GetOfferByCode", kwargs={"code": "WINTER20"}),
            Action(name="GetContactByEmail", kwargs={"email": "tom.j@email.com"}),
            Action(name="GetProductByName", kwargs={"name": "Wireless Mouse"}),
            Action(name="ReserveCartId", kwargs={}),
            Action(name="CreateCart", kwargs={"cart_id": "C001", "contact_id": "208", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="AddItemToCart", kwargs={"cart_id": "C001", "product_id": "1003", "quantity": 1}),
            Action(name="ApplyOfferToCart", kwargs={"cart_id": "C001", "code": "WINTER20"}),
            Action(name="ReserveOrderId", kwargs={}),
            Action(name="CreateOrder", kwargs={"order_id": "O001", "cart_id": "C001", "created_at": "2025-08-06T12:00:00Z"}),
            Action(name="SetOrderShippingAddress", kwargs={
                "order_id": "O001",
                "address": {"name": "David Chen","line1": "42 Ocean Ave","city": "Orlando","region": "FL","postal_code": "33101","country": "US"}
            }),
        ],
        outputs=['{"order_id":"O001","status":"Processing","subtotal":40.0,"discount_amount":8.0,"total_amount":32.0}'],
    ),
]
