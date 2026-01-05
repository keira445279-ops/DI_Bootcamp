
import pandas as pd
from sqlalchemy import create_engine

# create in-memory SQLite database
engine = create_engine("sqlite://")

# -----------------------------
# Question 1
# -----------------------------
q1 = """
SELECT
    ROUND(
        COUNT(CASE WHEN r.review_score = 5 THEN 1 END) * 100.0 / COUNT(*),
        2
    ) AS percentage
FROM olist_orders AS o
JOIN olist_order_reviews AS r
    ON o.order_id = r.order_id
WHERE o.order_purchase_timestamp LIKE '2018-01%';
"""

# df_q1 = pd.read_sql_query(q1, engine)

# -----------------------------
# Question 2
# -----------------------------
q2 = """
WITH yearly_stats AS (
    SELECT
        STRFTIME('%Y', o.order_purchase_timestamp) AS year,
        COUNT(DISTINCT o.order_id) AS total_orders,
        COUNT(DISTINCT c.customer_unique_id) AS unique_customers
    FROM olist_orders o
    JOIN olist_customers c
        ON c.customer_id = o.customer_id
    GROUP BY 1
)
SELECT
    year,
    total_orders,
    unique_customers,
    ROUND(
        100.0 * (total_orders - LAG(total_orders) OVER (ORDER BY year)) /
        LAG(total_orders) OVER (ORDER BY year),
        2
    ) AS orders_growth_pct,
    ROUND(
        100.0 * (unique_customers - LAG(unique_customers) OVER (ORDER BY year)) /
        LAG(unique_customers) OVER (ORDER BY year),
        2
    ) AS customers_growth_pct
FROM yearly_stats;
"""

# df_q2 = pd.read_sql_query(q2, engine)

# -----------------------------
# Question 3
# -----------------------------
q3 = """
SELECT
    c.customer_unique_id,
    STRFTIME('%Y-%m', o.order_purchase_timestamp) AS year_month,
    ROUND(
        SUM(p.payment_value) / COUNT(DISTINCT o.order_id),
        2
    ) AS average_order_value
FROM olist_customers c
JOIN olist_orders o
    ON o.customer_id = c.customer_id
JOIN olist_order_payments p
    ON p.order_id = o.order_id
GROUP BY 1, 2
ORDER BY year_month DESC, average_order_value DESC;
"""

# df_q3 = pd.read_sql_query(q3, engine)


# -----------------------------
# Question 4
# -----------------------------

q4 = """
SELECT
    c.customer_city,
    ROUND(SUM(p.payment_value), 2) AS revenue
FROM olist_order_payments p
JOIN olist_orders o
    ON o.order_id = p.order_id
JOIN olist_customers c
    ON c.customer_id = o.customer_id
WHERE o.order_purchase_timestamp BETWEEN '2016-01-01' AND '2018-12-31'
GROUP BY 1
ORDER BY revenue DESC
LIMIT 5;
"""

# df_q4 = pd.read_sql_query(q4, engine)


# -----------------------------
# Question 5
# -----------------------------

q5 = """
SELECT
    c.customer_state,
    ROUND(SUM(p.payment_value), 2) AS revenue
FROM olist_order_payments p
JOIN olist_orders o
    ON o.order_id = p.order_id
JOIN olist_customers c
    ON c.customer_id = o.customer_id
WHERE o.order_purchase_timestamp BETWEEN '2016-01-01' AND '2018-12-31'
GROUP BY 1
ORDER BY revenue DESC;
"""

# df_q5 = pd.read_sql_query(q5, engine)

# -----------------------------
# Question 6
# -----------------------------

q6 = """
SELECT
    oi.seller_id,
    COUNT(oi.order_id) AS total_goods_sold,
    ROUND(SUM(oi.price), 2) AS total_revenue,
    COUNT(DISTINCT o.customer_id) AS total_customers,
    SUM(CASE WHEN r.review_score = 5 THEN 1 ELSE 0 END) AS count_5_star_ratings,
    ROUND(AVG(r.review_score), 2) AS avg_rating
FROM olist_order_items oi
JOIN olist_orders o
    ON oi.order_id = o.order_id
JOIN olist_order_reviews r
    ON oi.order_id = r.order_id
GROUP BY oi.seller_id
HAVING count_5_star_ratings > 50
ORDER BY total_revenue DESC
LIMIT 10;
"""

# df_q6 = pd.read_sql_query(q6, engine)

# -----------------------------
# Question 7
# -----------------------------

q7 = """
SELECT
    c.customer_state,
    COUNT(o.order_id) AS total_orders_in_state,
    SUM(CASE WHEN o.order_status = 'delivered' THEN 1 ELSE 0 END) AS delivered_in_state,
    ROUND(
        SUM(CASE WHEN o.order_status = 'delivered' THEN 1.0 ELSE 0.0 END) * 100.0
        / COUNT(o.order_id),
        2
    ) AS delivery_success_rate
FROM olist_customers c
JOIN olist_orders o
    ON o.customer_id = c.customer_id
GROUP BY 1
ORDER BY delivery_success_rate DESC;
"""

# df_q7 = pd.read_sql_query(q7, engine)

# -----------------------------
# Question 8
# -----------------------------

q8 = """
SELECT
    t.product_category_name_english AS product_category_name,
    p.payment_type,
    COUNT(*) AS payments_for_products
FROM olist_order_payments p
JOIN olist_order_items i
    ON p.order_id = i.order_id
JOIN olist_products_dataset prod
    ON i.product_id = prod.product_id
JOIN product_category_name_translation t
    ON prod.product_category_name = t.product_category_name
GROUP BY 1, 2
ORDER BY payments_for_products DESC;
"""

# df_q8 = pd.read_sql_query(q8, engine)

# -----------------------------
# Question 9
# -----------------------------

q9 = """
WITH city_coords AS (
    SELECT
        geolocation_city,
        AVG(geolocation_lat) AS lat,
        AVG(geolocation_lng) AS lng
    FROM olist_geolocation
    GROUP BY 1
)
SELECT
    o.order_id,
    c.customer_city,
    s.seller_city,
    ROUND(
        SQRT(
            (c_coord.lat - s_coord.lat) * (c_coord.lat - s_coord.lat) +
            (c_coord.lng - s_coord.lng) * (c_coord.lng - s_coord.lng)
        ) * 111,
        2
    ) AS distance_km
FROM olist_orders o
JOIN olist_customers c
    ON o.customer_id = c.customer_id
JOIN olist_order_items i
    ON o.order_id = i.order_id
JOIN olist_sellers s
    ON i.seller_id = s.seller_id
JOIN city_coords c_coord
    ON c.customer_city = c_coord.geolocation_city
JOIN city_coords s_coord
    ON s.seller_city = s_coord.geolocation_city
LIMIT 10;
"""

# df_q9 = pd.read_sql_query(q9, engine)