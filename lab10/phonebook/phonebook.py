import psycopg2
import csv

def insert_from_csv(conn, csv_filepath):
    cursor = conn.cursor()
    try:
        with open(csv_filepath, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row if it exists
            for row in reader:
                first_name, last_name, phone_number = row
                sql = "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)"
                cursor.execute(sql, (first_name, last_name, phone_number))
        conn.commit()
        print("Data imported successfully from CSV.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error while importing from CSV: {error}")
        conn.rollback()
    finally:
        if cursor:
            cursor.close()

def insert_from_console(conn):
    cursor = conn.cursor()
    first_name = input("Enter first name: ")
    last_name = input("Enter last name (optional): ")
    phone_number = input("Enter phone number: ")
    sql = "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)"
    try:
        cursor.execute(sql, (first_name, last_name, phone_number))
        conn.commit()
        print("Contact added successfully.")
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        print("Error: Phone number already exists.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error adding contact: {error}")
        conn.rollback()
    finally:
        if cursor:
            cursor.close()

def update_contact(conn):
    cursor = conn.cursor()
    phone_number_to_update = input("Enter the phone number of the contact you want to update: ")
    print("What would you like to update?")
    print("1. First Name")
    print("2. Phone Number")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        new_first_name = input("Enter the new first name: ")
        sql = "UPDATE contacts SET first_name = %s WHERE phone_number = %s"
        data = (new_first_name, phone_number_to_update)
    elif choice == '2':
        new_phone_number = input("Enter the new phone number: ")
        sql = "UPDATE contacts SET phone_number = %s WHERE phone_number = %s"
        data = (new_phone_number, phone_number_to_update)
    else:
        print("Invalid choice.")
        return

    try:
        cursor.execute(sql, data)
        if cursor.rowcount > 0:
            conn.commit()
            print("Contact updated successfully.")
        else:
            conn.rollback()
            print("Contact with that phone number not found.")
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        print("Error: That phone number already exists.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error updating contact: {error}")
        conn.rollback()
    finally:
        if cursor:
            cursor.close()

def query_contacts(conn, search_term=None, search_field=None):
    cursor = conn.cursor()
    sql = "SELECT id, first_name, last_name, phone_number FROM contacts"
    params = ()

    if search_term and search_field in ["first_name", "last_name", "phone_number"]:
        sql += f" WHERE {search_field} ILIKE %s" # ILIKE for case-insensitive search
        params = (f"%{search_term}%",)
    elif search_term:
        print("Invalid search field. Please choose from: first_name, last_name, phone_number.")
        cursor.close()
        return

    try:
        cursor.execute(sql, params)
        results = cursor.fetchall()
        if results:
            print("\n--- Contacts ---")
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]} {row[2] or ''}, Phone: {row[3]}")
            print("------------------")
        else:
            print("No contacts found matching your criteria.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error querying contacts: {error}")
    finally:
        if cursor:
            cursor.close()

def query_by_name(conn, name):
    query_contacts(conn, name, "first_name")
    query_contacts(conn, name, "last_name")

def query_by_phone(conn, phone):
    query_contacts(conn, phone, "phone_number")

def delete_by_username(conn, username):
    cursor = conn.cursor()
    sql = "DELETE FROM contacts WHERE first_name ILIKE %s"
    try:
        cursor.execute(sql, (f"%{username}%",))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"Deleted {cursor.rowcount} contact(s) with username containing '{username}'.")
        else:
            conn.rollback()
            print(f"No contacts found with username containing '{username}'.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error deleting by username: {error}")
        conn.rollback()
    finally:
        if cursor:
            cursor.close()

def delete_by_phone(conn, phone_number):
    cursor = conn.cursor()
    sql = "DELETE FROM contacts WHERE phone_number = %s"
    try:
        cursor.execute(sql, (phone_number,))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"Deleted contact with phone number '{phone_number}'.")
        else:
            conn.rollback()
            print(f"No contact found with phone number '{phone_number}'.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error deleting by phone number: {error}")
        conn.rollback()
    finally:
        if cursor:
            cursor.close()