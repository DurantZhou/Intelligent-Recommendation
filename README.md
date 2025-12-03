# Project Overview

# Tools and Technology
  MySQL Community Server, MySQL Workbench, PowerBI, ODBC, Python

## SQL Syntax
### SQL： Create database
```sql
CREATE DATABASE recommendation;
USE recommendation;
```

---

### SQL:  Create fact_order_line

```sql
CREATE TABLE fact_order_line_summary AS

    order_number       VARCHAR(50),
    customer_name      VARCHAR(255),
    order_date         DATE,
    amount_paid        DECIMAL(18,2),
    product_id         VARCHAR(50),
    quantity           INTEGER,
    unit_price         DECIMAL(18,2),
    subtotal           DECIMAL(18,2)
);
```

---

### SQL:  Create dim_customer

```sql
CREATE TABLE dim_customer (
    customer_name   VARCHAR(255) PRIMARY KEY,
    industry        VARCHAR(100),
    contact_name    VARCHAR(255),
    phone           VARCHAR(50),
    email           VARCHAR(255)
);
```

---

### SQL:  Create dim_product

```sql
CREATE TABLE dim_product (
    product_id      VARCHAR(50) PRIMARY KEY,
    category        VARCHAR(255),
    description     VARCHAR(255),
    default_unit_price    DECIMAL(18,2),
    retail_price    DECIMAL(18,2)
);
```

---

### SQL:  Create customer_top_products (Materialized Table, Not View)

```sql
CREATE TABLE customer_top_products AS
SELECT
    customer_name,
    product_name,
    COUNT(*) AS times_ordered,
    SUM(product_quantity) AS total_qty,
    SUM(product_subtotal) AS total_amount
FROM fact_order_line
GROUP BY customer_name, product_name;

```

---

### SQL:  Create Frequently Bought Together：product_cooccurrence (Materialized Table, Not View)

```sql
CREATE TABLE product_cooccurrence AS
SELECT 
    a.product_name AS base_product,
    b.product_name AS co_product,
    COUNT(*) AS times_together
FROM fact_order_line a
JOIN fact_order_line b
    ON a.order_number = b.order_number    
    AND a.product_name <> b.product_name   
GROUP BY a.product_name, b.product_name;

```

---

### SQL: Add Index for customer_top_products & Frequently Bought Together

```sql
ALTER TABLE customer_top_products
ADD INDEX idx_ctp_customer (customer_name),
ADD INDEX idx_ctp_product (product_name);


ALTER TABLE product_cooccurrence
ADD INDEX idx_pco_base (base_product),
ADD INDEX idx_pco_co (co_product),
ADD INDEX idx_pco_times (times_together);

```

---


