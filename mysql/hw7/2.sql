SELECT * 
FROM products
LEFT JOIN catalogs 
ON products.id = catalogs.product_id;
