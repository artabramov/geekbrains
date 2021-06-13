mysql> select * from users;
+----+-----------+----------+-------------------------+---------------+-------+
| id | firstname | lastname | email                   | password_hash | phone |
+----+-----------+----------+-------------------------+---------------+-------+
|  7 | Walter    | White    | white.walter@noname.no  | NULL          |  NULL |
|  8 | Jesse     | Pinkman  | pinkman.jesse@noname.no | NULL          |  NULL |
|  9 | Skyler    | White    | white.skyler@noname.no  | NULL          |  NULL |
| 10 | Gustavo   | Fring    | fring.gustavo@noname.no | NULL          |  NULL |
+----+-----------+----------+-------------------------+---------------+-------+
4 rows in set (0.00 sec)

mysql> SELECT distinct firstname, lastname FROM users;
+-----------+----------+
| firstname | lastname |
+-----------+----------+
| Gustavo   | Fring    |
| Jesse     | Pinkman  |
| Skyler    | White    |
| Walter    | White    |
+-----------+----------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM users LIMIT 1 offset 2;
+----+-----------+----------+------------------------+---------------+-------+
| id | firstname | lastname | email                  | password_hash | phone |
+----+-----------+----------+------------------------+---------------+-------+
|  9 | Skyler    | White    | white.skyler@noname.no | NULL          |  NULL |
+----+-----------+----------+------------------------+---------------+-------+
1 row in set (0.00 sec)

mysql> SELECT * FROM users WHERE id = 2 OR firstname = 'Walter';
+----+-----------+----------+------------------------+---------------+-------+
| id | firstname | lastname | email                  | password_hash | phone |
+----+-----------+----------+------------------------+---------------+-------+
|  7 | Walter    | White    | white.walter@noname.no | NULL          |  NULL |
+----+-----------+----------+------------------------+---------------+-------+
1 row in set (0.00 sec)

mysql> SELECT * FROM users WHERE id IN (1,2,3);
Empty set (0.00 sec)

mysql> SELECT * FROM users WHERE id IN (7,8,9);
+----+-----------+----------+-------------------------+---------------+-------+
| id | firstname | lastname | email                   | password_hash | phone |
+----+-----------+----------+-------------------------+---------------+-------+
|  7 | Walter    | White    | white.walter@noname.no  | NULL          |  NULL |
|  8 | Jesse     | Pinkman  | pinkman.jesse@noname.no | NULL          |  NULL |
|  9 | Skyler    | White    | white.skyler@noname.no  | NULL          |  NULL |
+----+-----------+----------+-------------------------+---------------+-------+
3 rows in set (0.00 sec)

mysql>