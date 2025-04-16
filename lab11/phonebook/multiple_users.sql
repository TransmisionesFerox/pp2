CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_contacts_data TEXT[] -- Array of text, where each element is 'first_name,last_name,phone_number'
) AS $$
DECLARE
    contact_info TEXT[];
    first_name VARCHAR(50);
    last_name VARCHAR(50);
    phone_number VARCHAR(20);
    incorrect_data TEXT[] := '{}';
    i INTEGER;
BEGIN
    FOR i IN array_lower(p_contacts_data, 1) .. array_upper(p_contacts_data, 1) LOOP
        contact_info := string_to_array(p_contacts_data[i], ',');
        IF array_length(contact_info, 1) = 3 THEN
            first_name := trim(contact_info[1]);
            last_name := trim(contact_info[2]);
            phone_number := trim(contact_info[3]);

            -- Basic phone number correctness check (you might need more sophisticated validation)
            IF phone_number ~ '^[0-9+\-() ]+$' THEN
                INSERT INTO contacts (first_name, last_name, phone_number)
                VALUES (first_name, last_name, phone_number);
            ELSE
                incorrect_data := array_append(incorrect_data, p_contacts_data[i]);
                RAISE NOTICE 'Incorrect phone number format: % in data: %', phone_number, p_contacts_data[i];
            END IF;
        ELSE
            incorrect_data := array_append(incorrect_data, p_contacts_data[i]);
            RAISE NOTICE 'Incorrect data format: %', p_contacts_data[i];
        END IF;
    END LOOP;

    IF array_length(incorrect_data, 1) > 0 THEN
        RAISE NOTICE 'The following data entries were incorrect: %', incorrect_data;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Example usage:
-- CALL insert_many_contacts(ARRAY[
--     'John,Doe,123-456-7890',
--     'Jane,Smith,9876543210',
--     'Peter,Pan,+1 (555) 123 4567',
--     'Invalid Data',
--     'Another,Bad,ABC'
-- ]);

-- SELECT * FROM contacts;