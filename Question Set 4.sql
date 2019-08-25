/* Question 4: Total amount And average amount spent by the top 10 paying customers.*/
WITH Total_Amount AS(
WITH CTE AS (SELECT (first_name || ' ' || last_name) AS name, 
                   c.customer_id, 
                   p.amount, 
                   p.payment_date
              FROM customer AS c
                   JOIN payment AS p
                    ON c.customer_id = p.customer_id),

     sub1 AS (SELECT CTE.customer_id
              FROM CTE
             GROUP BY 1
             ORDER BY SUM(CTE.amount) DESC
             LIMIT 10),

     sub2 AS (SELECT CTE.name,
                   DATE_TRUNC('month', CTE.payment_date) AS pay_mon, 
                   COUNT(*) AS pay_countpermon,
                   SUM(CTE.amount) AS pay_amount
              FROM CTE
                   JOIN sub1
                    ON CTE.customer_id = sub1.customer_id
              WHERE CTE.payment_date BETWEEN '20070101' AND '20080101'
              GROUP BY 1, 2
              ORDER BY 1, 3, 2)

SELECT sub2.name,
       sub2.pay_mon,
       sub2.pay_amount,
	    ROUND(AVG(sub2.pay_amount) OVER (PARTITION BY sub2.name), 2) AS avg_amount					
  FROM sub2
 ORDER BY 1, 2
)
SELECT Total_Amount.name, sum(Total_Amount.pay_amount)as Total_Sum, (sum(Total_Amount.avg_amount)/count(avg_amount)) as Average
FROM Total_Amount
GROUP BY 1
ORDER BY 3