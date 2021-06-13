mysql> select * from users;
+----+-----------+----------+-------------------------+----------------------------------+-----------+
| id | firstname | lastname | email                   | password_hash                    | phone     |
+----+-----------+----------+-------------------------+----------------------------------+-----------+
|  7 | Walter    | White    | white.walter@noname.no  | 0123456789abcdef0123456789abcdef | 987654321 |
|  8 | Jesse     | Pinkman  | pinkman.jesse@noname.no | NULL                             |      NULL |
|  9 | Skyler    | White    | white.skyler@noname.no  | NULL                             |      NULL |
| 10 | Gustavo   | Fring    | fring.gustavo@noname.no | NULL                             |      NULL |
+----+-----------+----------+-------------------------+----------------------------------+-----------+
4 rows in set (0.00 sec)

mysql> delete from users where id=9;
Query OK, 1 row affected (0.01 sec)

mysql> select * from users;
+----+-----------+----------+-------------------------+----------------------------------+-----------+
| id | firstname | lastname | email                   | password_hash                    | phone     |
+----+-----------+----------+-------------------------+----------------------------------+-----------+
|  7 | Walter    | White    | white.walter@noname.no  | 0123456789abcdef0123456789abcdef | 987654321 |
|  8 | Jesse     | Pinkman  | pinkman.jesse@noname.no | NULL                             |      NULL |
| 10 | Gustavo   | Fring    | fring.gustavo@noname.no | NULL                             |      NULL |
+----+-----------+----------+-------------------------+----------------------------------+-----------+
3 rows in set (0.00 sec)

mysql>