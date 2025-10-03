# Digital Commerce Domain Data Model

The datasets are divided into two distinct but interconnected domains:

1.  **Digital Salesforce Commerce Operations:** This schema represents the core business data of an e-commerce platform. It includes entities related to customers, products, sales, and service. The agent interacts with this data to fulfill business-process-oriented tasks like processing returns or managing orders.

2.  **Salesforce Platform Configuration:** This model represents the administrative and infrastructural state of the Salesforce and AWS environments. It includes entities related to API settings, cache configurations, and cloud resources. The agent interacts with this data to perform technical, platform-management SOPs.

---

## 1. Digital Salesforce Commerce Operations Datasets

This relational schema models the day-to-day operations of the e-commerce business.

### `accounts`

This table represents customer accounts, which can be either individual consumers (B2C) or companies (B2B).

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `account_id` | INTEGER | Primary key for the account. |
| `account_name` | VARCHAR | The name of the company or individual. |
| `default_pricebook_id` | INTEGER | Foreign key to `pricebooks`. Defines the pricing tier for this account. |
| `type` | VARCHAR | The type of account (e.g., 'B2B Customer', 'B2C Customer'). |
| `billing_street` | VARCHAR | Billing street address. |
| `shipping_street` | VARCHAR | Shipping street address. |
| `created_at` | TIMESTAMP | Timestamp of account creation. |

### `contacts`

This table stores information about individual people associated with accounts. A contact is the primary actor for placing orders and creating support cases.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `contact_id` | INTEGER | Primary key for the contact. |
| `account_id` | INTEGER | Foreign key to `accounts`. |
| `first_name` | VARCHAR | Contact's first name. |
| `last_name` | VARCHAR | Contact's last name. |
| `email` | VARCHAR | Contact's unique email address, used as a key identifier. |
| `phone` | VARCHAR | Contact's phone number. |

### `products`

This table contains the master list of all items available for sale. Note that pricing is handled separately in pricebooks.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `product_id` | INTEGER | Primary key for the product. |
| `category_id` | INTEGER | Foreign key to `categories`. |
| `sku` | VARCHAR | The unique Stock Keeping Unit for the product. |
| `name` | VARCHAR | The display name of the product. |
| `description` | TEXT | A detailed description of the product. |
| `stock_quantity` | INTEGER | The current number of units in inventory. |

### `catalogs` & `categories`

These tables organize products into a navigable hierarchy.

**`catalogs`**

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `catalog_id` | INTEGER | Primary key for the catalog (e.g., "Spring Collection"). |
| `name` | VARCHAR | The name of the catalog. |
| `is_active` | BOOLEAN | Indicates if the catalog is currently live. |

**`categories`**

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `category_id` | INTEGER | Primary key for the category. |
| `catalog_id` | INTEGER | Foreign key to `catalogs`. |
| `parent_category_id` | INTEGER | Self-referencing key for creating sub-categories. |
| `name` | VARCHAR | The name of the category (e.g., "Footwear"). |

### `pricebooks` & `pricebook_entries`

These tables manage complex pricing rules, allowing different prices for the same product based on customer segment.

**`pricebooks`**

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `pricebook_id` | INTEGER | Primary key for the price book. |
| `name` | VARCHAR | Name of the price book (e.g., "Standard Retail", "VIP Gold"). |
| `is_standard` | BOOLEAN | Indicates if this is the default price book. |

**`pricebook_entries`**

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `pricebook_entry_id` | INTEGER | Primary key for the entry. |
| `pricebook_id` | INTEGER | Foreign key to `pricebooks`. |
| `product_id` | INTEGER | Foreign key to `products`. |
| `price` | DECIMAL | The price of the product within this specific price book. |

### `offers`

This table stores promotional offers and discount codes.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `offer_id` | INTEGER | Primary key for the offer. |
| `offer_code` | VARCHAR | The user-facing code to apply the offer (e.g., "WINTER20"). |
| `discount_type` | VARCHAR | Type of discount ('PERCENTAGE', 'FIXED_AMOUNT'). |
| `discount_value` | DECIMAL | The numeric value of the discount. |
| `is_active` | BOOLEAN | Indicates if the offer can be used. |

### `carts` & `cart_items`

These tables represent a user's shopping cart before a purchase is finalized.

**`carts`**

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `cart_id` | INTEGER | Primary key for the cart. |
| `contact_id` | INTEGER | Foreign key to `contacts`, identifying the cart owner. |

**`cart_items`**

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `cart_item_id` | INTEGER | Primary key for the line item. |
| `cart_id` | INTEGER | Foreign key to `carts`. |
| `product_id` | INTEGER | Foreign key to `products`. |
| `quantity` | INTEGER | Number of units of the product in the cart. |

### `orders` & `order_items`

These tables store the final, confirmed transactional records after a checkout is complete.

**`orders`**

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `order_id` | INTEGER | Primary key for the order. |
| `contact_id` | INTEGER | Foreign key to `contacts`. |
| `applied_offer_id` | INTEGER | Foreign key to `offers` if a discount was used. |
| `status` | VARCHAR | The current state of the order (e.g., 'Processing', 'Shipped', 'Delivered'). |
| `total_amount` | DECIMAL | The final charged amount. |

**`order_items`**

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `order_item_id` | INTEGER | Primary key for the line item. |
| `order_id` | INTEGER | Foreign key to `orders`. |
| `product_id` | INTEGER | Foreign key to `products`. |
| `quantity` | INTEGER | Number of units ordered. |
| `price_per_unit` | DECIMAL | The price of the product at the time of sale. |

### `cases`

This table tracks customer service interactions, such as returns, complaints, or inquiries.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `case_id` | INTEGER | Primary key for the case. |
| `contact_id` | INTEGER | Foreign key to `contacts`. |
| `order_id` | INTEGER | Foreign key to the related `orders` (if applicable). |
| `subject` | VARCHAR | A brief summary of the issue. |
| `status` | VARCHAR | The current state of the case (e.g., 'New', 'In Progress', 'Resolved'). |
| `priority` | VARCHAR | The urgency of the case (e.g., 'Low', 'Medium', 'High'). |

---

## 2. Salesforce Platform Configuration Datasets

This data model represents the configuration state of the underlying Salesforce and AWS infrastructure. The agent modifies this data to perform administrative and maintenance tasks.

### `salesforce_orgs`

This table lists the Salesforce instances that the agent is authorized to manage.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `org_id` | VARCHAR | The unique, immutable Salesforce Organization ID. |
| `org_name` | VARCHAR | A human-readable name for the org (e.g., "Production", "UAT"). |
| `instance_url` | VARCHAR | The base URL for API and UI access. |
| `api_version` | VARCHAR | The Salesforce API version to use for interactions. |

### `custom_setting`

This table stores key-value pairs that control application behavior within Salesforce.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `setting_id` | INTEGER | Primary key for the setting. |
| `org_id` | VARCHAR | Foreign key to `SalesforceOrg`. |
| `setting_name` | VARCHAR | The programmatic name of the setting (e.g., `CacheAPI.ExternalSystemURL`). |
| `value` | VARCHAR | The configured value for the setting. |

### `connected_app`

This table represents OAuth-enabled applications used for API access to Salesforce.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `app_id` | INTEGER | Primary key for the app. |
| `org_id` | VARCHAR | Foreign key to `SalesforceOrg`. |
| `app_name` | VARCHAR | The name of the client application. |
| `client_id` | VARCHAR | The public identifier for the app. |
| `client_secret_stored` | BOOLEAN | Indicates if the secret is securely stored (the secret itself is not here). |
| `oauth_scopes` | VARCHAR | A comma-separated list of permissions (e.g., `api, refresh_token`). |

### `cache_job`

This table tracks the status of administrative jobs within the Vlocity CMT package, primarily for managing the API cache.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `job_id` | INTEGER | Primary key for the job definition. |
| `org_id` | VARCHAR | Foreign key to `SalesforceOrg`. |
| `job_name` | VARCHAR | The name of the job (e.g., `Load API Metadata`). |
| `last_run_status` | VARCHAR | The result of the last execution ('Success', 'Failed'). |
| `last_run_time` | TIMESTAMP | The timestamp of the last execution. |

### `trace_flag`

This table represents diagnostic flags in Salesforce that can be enabled for debugging or disabled for performance.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `flag_id` | INTEGER | Primary key for the flag. |
| `org_id` | VARCHAR | Foreign key to `SalesforceOrg`. |
| `flag_name` | VARCHAR | The programmatic name of the flag (e.g., `CacheAPI.EcommLogger`). |
| `is_active` | BOOLEAN | The current state of the flag. |

### `aws_elasticache_cluster`

This table represents external Redis cache clusters provisioned in AWS.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `cluster_id` | VARCHAR | The unique identifier for the ElastiCache cluster. |
| `cluster_name` | VARCHAR | A human-readable name for the cluster. |
| `endpoint_url` | VARCHAR | The connection endpoint for the Redis cluster. |
| `status` | VARCHAR | The current provisioning status (e.g., 'available', 'creating'). |
| `instance_type` | VARCHAR | The AWS instance type (e.g., `cache.m5.large`). |
| `security_group_id` | VARCHAR | The ID of the associated AWS security group. |

### `aws_security_group_rule`

This table represents firewall rules that control network access to AWS resources.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `rule_id` | VARCHAR | The unique identifier for the security group rule. |
| `security_group_id` | VARCHAR | Foreign key to the parent security group. |
| `protocol` | VARCHAR | The network protocol (e.g., 'TCP'). |
| `port` | INTEGER | The port number for the rule (e.g., `6379` for Redis). |
| `source_ip` | VARCHAR | The source IP range in CIDR notation that is allowed access. |
| `description` | VARCHAR | A human-readable description of the rule's purpose. |

### `aws_subnet_groups`

This table represents groups of subnets in AWS.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `subnet_group_id` | VARCHAR | The unique identifier for the subnet group. |
| `name` | VARCHAR | A human-readable name for the subnet group. |
| `description` | VARCHAR | A description of the subnet group. |
| `vpc_id` | VARCHAR | The ID of the associated VPC. |
| `subnet_ids` | ARRAY | A list of subnet IDs that belong to the group. |
