-- EJERCICIO 2 POSTGRESQL

-- PL/pgSQL Extension - Allows programming to SQL
-- DO $$ Command - To execute the code giving a Start and End
-- DECLARE: Used to save variables
-- INTO: Saves values extracted with SELECT
-- RAISE NOTICE: Prints text to the user
-- EXCEPTION: Similar to try or catch

DO $$
DECLARE -- Variables
    v_bill_id INT := 2; 
    v_product_id INT := 4;
    v_purchase_quantity INT := 2;

    v_product_stock INT; -- Checks availability on invetory
    v_product_name VARCHAR(50);

BEGIN
    -- Verify current stock
    SELECT product_name, product_stock
    INTO v_product_name, v_product_stock
    FROM Products
    WHERE Product_id = v_product_id;

    -- Modify stock according to quantity purchased
    UPDATE Products
    SET product_stock = product_stock - v_purchase_quantity
    WHERE product_id = v_product_id;

    -- Insert Product info to bill details
    INSERT INTO Bill_Details(bill_id, product_id, purchase_quantity)
    VALUES (v_bill_id, v_product_id, v_purchase_quantity);

    -- Purchase Message - % Symbol replaces the variable values
    RAISE NOTICE 'Compra exitosa! Se agrego % de "%" a la factura #%.',
    v_purchase_quantity, v_product_name, v_bill_id;


EXCEPTION -- Similar to try or catch
    WHEN OTHERS THEN
        RAISE EXCEPTION '%', SQLERRM;
END $$;

-- Check inventory substraction
SELECT product_id, product_name, product_stock 
FROM Products 
WHERE product_id = 4;

-- Verify Bill Datail is saved
SELECT * FROM Bill_Details 
WHERE bill_id = 2 AND product_id = 4;