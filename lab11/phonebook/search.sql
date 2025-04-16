CREATE OR REPLACE FUNCTION search_contacts_by_pattern(search_pattern TEXT)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_number VARCHAR(20)
) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.first_name, c.last_name, c.phone_number
    FROM contacts c
    WHERE c.first_name ILIKE '%' || search_pattern || '%'
       OR c.last_name ILIKE '%' || search_pattern || '%'
       OR c.phone_number LIKE '%' || search_pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- Example usage:
-- SELECT * FROM search_contacts_by_pattern('John');
-- SELECT * FROM search_contacts_by_pattern('123');