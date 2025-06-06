SELECT
	CUSTOMERS.CUSTOMER_NAME,
	COUNT(CUSTOMERS.CUSTOMER_ID) AS COUNT_ID
FROM
	ORDERS
	LEFT JOIN CUSTOMERS ON ORDERS.CUSTOMER_ID = CUSTOMERS.CUSTOMER_ID
GROUP BY
	CUSTOMERS.CUSTOMER_NAME
HAVING
	COUNT(CUSTOMERS.CUSTOMER_ID) > 5;