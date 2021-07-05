DELIMITER $$
CREATE FUNCTION hello() RETURNS VARCHAR
BEGIN
    DECLARE tmp = HOUR(NOW());
    IF tmp >= 6 AND tmp < 12 THEN RETURN 'Good morning!';
    ELSE IF IF tmp >= 12 AND tmp < 18 THEN RETURN 'Good day!';
    ELSE IF IF tmp >= 18 AND tmp < 0 THEN RETURN 'Good evening!';
    ELSE RETURN 'Good night!';
    END IF;
END$$
DELIMITER ;