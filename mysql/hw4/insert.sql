mysql> delete from users;
Query OK, 4 rows affected (0.02 sec)

mysql> INSERT INTO `users` (`firstname`, `lastname`, `email`) VALUES ('Walter', 'White', 'white.walter@noname.no');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO users (`firstname`, `lastname`, `email`) VALUES
    -> ('Jesse', 'Pinkman', 'pinkman.jesse@noname.no'),
    -> ('Skyler', 'White', 'white.skyler@noname.no');
Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> INSERT INTO users
    -> SET
    -> firstname = 'Gustavo',
    -> lastname = 'Fring',
    -> email = 'fring.gustavo@noname.no';
Query OK, 1 row affected (0.01 sec)

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

mysql>