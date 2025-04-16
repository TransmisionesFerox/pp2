CREATE OR REPLACE PROCEDURE delete_contact_by_identifier(
    p_identifier TEXT,
    p_search_by VARCHAR(10) DEFAULT 'username' -- Can be 'username' or 'phone'
) AS $$
BEGIN
    IF p_search_by = 'username' THEN
        DELETE FROM contacts
        WHERE first_name ILIKE '%' || p_identifier || '%'
           OR last_name ILIKE '%' || p_identifier || '%';
        RAISE NOTICE 'Deleted contacts with username or lastname matching %', p_identifier;
    ELSIF p_search_by = 'phone' THEN
        DELETE FROM contacts
        WHERE phone_number = p_identifier;
        RAISE NOTICE 'Deleted contact with phone number %', p_identifier;
    ELSE
        RAISE NOTICE 'Invalid search_by option. Use "username" or "phone".';
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Example usage:
-- CALL delete_contact_by_identifier('John', 'username');
-- CALL delete_contact_by_identifier('987-654-3210', 'phone');
-- CALL delete_contact_by_identifier('Jane'); -- Defaults to searching by username