mysql> select * from users where id=7;
+----+-----------+----------+------------------------+---------------+-------+
| id | firstname | lastname | email                  | password_hash | phone |
+----+-----------+----------+------------------------+---------------+-------+
|  7 | Walter    | White    | white.walter@noname.no | NULL          |  NULL |
+----+-----------+----------+------------------------+---------------+-------+
1 row in set (0.00 sec)

mysql> UPDATE users
    -> SET
    -> phone = '987654321',
    -> password_hash = '0123456789abcdef0123456789abcdef'
    -> WHERE
    -> firstname = 'Walter' and lastname = 'White';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from users where id=7;
+----+-----------+----------+------------------------+----------------------------------+-----------+
| id | firstname | lastname | email                  | password_hash                    | phone     |
+----+-----------+----------+------------------------+----------------------------------+-----------+
|  7 | Walter    | White    | white.walter@noname.no | 0123456789abcdef0123456789abcdef | 987654321 |
+----+-----------+----------+------------------------+----------------------------------+-----------+
1 row in set (0.00 sec)

mysql>