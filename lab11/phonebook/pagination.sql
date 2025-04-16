CREATE OR REPLACE FUNCTION get_contacts_paginated(
    p_limit INTEGER DEFAULT 10,
    p_offset INTEGER DEFAULT 0
)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_number VARCHAR(20),
    total_records BIGINT
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.first_name,
        c.last_name,
        c.phone_number,
        (SELECT COUNT(*) FROM contacts) AS total_records
    FROM contacts c
    ORDER BY c.first_name -- You can order by any column
    LIMIT p_limit
    OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

-- Example usage:
-- SELECT * FROM get_contacts_paginated(5, 0); -- First 5 records
-- SELECT * FROM get_contacts_paginated(5, 5); -- Next 5 records
-- SELECT * FROM get_contacts_paginated(limit := 3); -- First 3 records (using named arguments)