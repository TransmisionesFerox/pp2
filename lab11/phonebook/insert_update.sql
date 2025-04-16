CREATE OR REPLACE PROCEDURE insert_or_update_contact(
    p_first_name VARCHAR(50),
    p_last_name VARCHAR(50),
    p_phone_number VARCHAR(20)
) AS $$
BEGIN
    -- Check if the user with the given phone number already exists
    IF EXISTS (SELECT 1 FROM contacts WHERE phone_number = p_phone_number) THEN
        -- Update the existing record
        UPDATE contacts
        SET first_name = p_first_name,
            last_name = p_last_name
        WHERE phone_number = p_phone_number;
        RAISE NOTICE 'Contact with phone number % updated.', p_phone_number;
    ELSE
        -- Insert a new record
        INSERT INTO contacts (first_name, last_name, phone_number)
        VALUES (p_first_name, p_last_name, p_phone_number);
        RAISE NOTICE 'New contact % % with phone number % inserted.', p_first_name, p_last_name, p_phone_number;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Example usage:
-- CALL insert_or_update_contact('John', 'Doe', '123-456-7890');
-- CALL insert_or_update_contact('Jane', 'Smith', '987-654-3210');
-- CALL insert_or_update_contact('John', 'Newlastname', '123-456-7890'); -- This will update John's last name