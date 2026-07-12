-- EJERCICIO 2 POSTGRESQL

-- PL/pgSQL Extension - Allows programming to SQL
-- DO $$ Command - To execute the code giving a Start and End
-- DECLARE: Used to save variables
-- INTO: Saves values extracted with SELECT
-- RAISE NOTICE: Prints text to the user
-- EXCEPTION: Similar to try or catch

DO $$
DECLARE -- Variables
    v_user_id INT := 1;    -- User ID
    v_new_bill_id INT;     -- Dynamic New bill
    v_user_exists BOOLEAN; -- Check existing users

    v_product_stock INT; -- Check product availability
    v_product_name VARCHAR(50);
    v_item RECORD; -- Variable to go through the loop

BEGIN
    -- Verify if user exists
    SELECT EXISTS(SELECT 1 FROM Users WHERE user_id = v_user_id)
    INTO v_user_exists;

    IF v_user_exists = FALSE THEN
        RAISE EXCEPTION 'El usuario % no existe', v_user_id;
    END IF;

    -- Create New Bill
    INSERT INTO Bills (user_id, bill_date, bill_status)
    VALUES (v_user_id, CURRENT_DATE, 'Completada')
    RETURNING bill_id INTO v_new_bill_id;

    -- Loop for multiple products
    FOR v_item IN
        SELECT 4 AS product_id, 2 AS item_quantity UNION ALL
        SELECT 3 AS product_id, 1 AS item_quantity
    LOOP
        -- Verify current stock
        SELECT product_name, product_stock
        INTO v_product_name, v_product_stock
        FROM Products
        WHERE Product_id = v_item.product_id;

        -- Verify Stock
        IF v_product_stock < v_item.item_quantity THEN
            RAISE EXCEPTION 'No hay suficientes productos de "%".', v_product_name;
        END IF;

        -- Modify stock according to quantity purchased
        UPDATE Products
        SET product_stock = product_stock - v_item.item_quantity
        WHERE product_id = v_item.product_id;

        -- Insert Product info to bill details using New Bill ID
        INSERT INTO Bill_Details(bill_id, product_id, purchase_quantity)
        VALUES (v_new_bill_id, v_item.product_id, v_item.item_quantity);

        RAISE NOTICE 'Se agrego % de "%" a la factura #%.', 
            v_item.item_quantity, v_product_name, v_new_bill_id;

    END LOOP;

    -- Purchase Message
    RAISE NOTICE 'Compra exitosa completa! Se genero la factura #% para el usuario %.',
        v_new_bill_id, v_user_id;

EXCEPTION -- Similar to try or catch
    WHEN OTHERS THEN
        RAISE EXCEPTION '%', SQLERRM;
END $$;

-- Check inventory substraction
SELECT product_id, product_name, product_stock 
FROM Products 
WHERE product_id IN (3, 4);

-- Verify Bill Detail is saved using the last generated bill
SELECT * FROM Bill_Details 
WHERE bill_id = (SELECT MAX(bill_id) FROM Bills);