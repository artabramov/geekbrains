SELECT * 
FROM users
WHERE id IN (SELECT DISTINCT user_id FROM orders);
