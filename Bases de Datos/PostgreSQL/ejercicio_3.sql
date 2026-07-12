-- EJERCICIO 3 POSTGRESQL

-- SELECT EXISTS() INTO - Function to verify if the value exists in the database
-- LOOP - To run in the table and verify each values

DO $$
DECLARE
    v_bill_id INT := 2; -- Bill ID to be returned
    v_bill_exists BOOLEAN; -- Saves if TRUE
    v_record RECORD; 
BEGIN
    -- Verify if Bill exists in the database
    SELECT EXISTS(SELECT 1 FROM Bills WHERE bill_id = v_bill_id)
    INTO v_bill_exists;
    
    -- Check if Bill is valid
    IF v_bill_exists = TRUE THEN
        -- LOOP to Increase Stock for the products in the Bill
        FOR v_record IN
            SELECT product_id, purchase_quantity
            FROM Bill_Details
            WHERE bill_id = v_bill_id
        LOOP
            UPDATE Products
            SET product_stock = product_stock + v_record.purchase_quantity
            WHERE product_id = v_record.product_id;
        END LOOP;
        
        -- Modifies bill
        UPDATE Bills
        SET bill_status = 'Retornada'
        WHERE bill_id = v_bill_id;

        RAISE NOTICE 'Se devolvio la factura #%.', v_bill_id;
    ELSE
        RAISE NOTICE 'Error! La factura #% no existe.', v_bill_id;
    END IF;

EXCEPTION -- EXCEPTION to check errors
    WHEN OTHERS THEN
        RAISE EXCEPTION '%', SQLERRM;
END $$;


-- Query to verify stock after product returned
SELECT product_id, product_name, product_stock 
FROM Products 
WHERE product_id IN (4);

-- Query to verify Bill
SELECT bill_id, bill_status FROM Bills WHERE bill_id = 2;