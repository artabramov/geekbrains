CREATE TRIGGER tmp BEFORE INSERT ON products
FOR EACH ROW BEGIN
    IF NEW.name IS null AND NEW.description IS null THEN
        SIGNAL SQLSTATE '45000';
    END IF;
END;