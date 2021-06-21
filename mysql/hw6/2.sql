SELECT COUNT(id) AS cnt 
FROM messages 
WHERE from_user_id IN (SELECT initiator_user_id AS id FROM friend_requests WHERE initiator_user_id=1900 AND status='approved') 
OR from_user_id IN (SELECT initiator_user_id AS id FROM friend_requests WHERE target_user_id=1900 AND status='approved') 
ORDER BY cnt DESC LIMIT 1;
