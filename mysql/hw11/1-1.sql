create table logs (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `table_name` ENUM('users', 'catalogs', 'products'),
    `table_id` INT(20),
    `name` VARCHAR(255)
) ENGINE=ARCHIVE CHARACTER SET utf8;

DELIMITER $$
CREATE TRIGGER t_users AFTER INSERT ON users
FOR EACH ROW BEGIN
    INSERT INTO logs (table_name, table_id, name) VALUES ('users', NEW.id, NEW.name);
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER t_catalogs AFTER INSERT ON catalogs
FOR EACH ROW BEGIN
    INSERT INTO logs (table_name, table_id, name) VALUES ('catalogs', NEW.id, NEW.name);
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER t_products AFTER INSERT ON products
FOR EACH ROW BEGIN
    INSERT INTO logs (table_name, table_id, name) VALUES ('products', NEW.id, NEW.name);
END$$
DELIMITER ;

