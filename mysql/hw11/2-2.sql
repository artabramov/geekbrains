HMSET user:1000 name Doe email noreply@noreply.no

SET Doe 1000
SET noreply@noreply.no 1000

GET Doe
GET noreply@noreply.no

HGETALL user:1000
