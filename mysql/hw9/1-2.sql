SELECT OR REPLACE VIEW vw_tmp AS
SELECT products.name, catalogs.name FROM products 
JOIN catalogs ON products.catalog_id = catalogs.id;