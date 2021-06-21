SELECT COUNT(id) AS cnt, user_id 
FROM likes 
WHERE user_id IN (SELECT user_id FROM profiles ORDER BY YEAR(birthday) DESC) 
GROUP BY user_id LIMIT 10;



SELECT COUNT(*) AS cnt, user_id FROM users_communities GROUP BY user_id ORDER BY cnt ASC LIMIT 10;