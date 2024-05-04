import sqlite3

# Connecting to SQLite database
con = sqlite3.connect('customer_db.db')  # Connect to the SQLite database
c = con.cursor()  # Create a cursor to interact with the database

# Ensure the "customers" table exists or create it
c.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY, 
    first_name TEXT, 
    last_name TEXT,  
    email TEXT 
)
""")
con.commit()  # Commit is like saving or pushing the app

# Function to insert a new customer
def insert_customer(first_name, last_name, email):
    try:
        c.execute("INSERT INTO customers (first_name, last_name, email) VALUES (?, ?, ?)", 
                  (first_name, last_name, email))  # Insert customer data
        con.commit()  # Commit the transaction
        print("Customer inserted successfully.")  # Success message
    except sqlite3.Error as e:  # Catch SQLite errors
        print(f"Error inserting customer: {e}")  # Display error message

# Function to fetch and display all customers
def display_customers():
    try:
        c.execute("SELECT * FROM customers")  # Fetch all customer records
        all_customers = c.fetchall()  # Get all results from the query
        if not all_customers:  # Check if there are no customers
            print("No customers found.")  # No records message
        else:
            # Display customer data in a formatted way
            print("ID   firstname    lastname    email")
            for customer in all_customers:
                print(f"{customer[0]}     {customer[1]}       {customer[2]}     {customer[3]}")
    except sqlite3.Error as e:  # Handle potential database errors
        print(f"Error fetching customers: {e}")

# Ensure this function is defined
def update_customer(customer_id, field, new_value):
    try:
        c.execute(f"UPDATE customers SET {field} = ? WHERE id = ?", 
                  (new_value, customer_id))  # Update a specific field for a given customer ID
        con.commit()  # Commit the transaction
        print("Customer updated successfully.")  # Success message
    except sqlite3.Error as e:
        print(f"Error updating customer: {e}")  # Handle SQLite errors

# Function to delete a customer by ID
def delete_customer(customer_id):
    try:
        c.execute("DELETE FROM customers WHERE id = ?", (customer_id,))  # Delete customer by ID
        con.commit()  # Commit the deletion
        print("Customer deleted successfully.")  # Success message
    except sqlite3.Error as e:
        print(f"Error deleting customer: {e}")  # Handle SQLite errors

# Function to drop the entire "customers" table
def drop_table():
    try:
        c.execute("DROP TABLE IF EXISTS customers")  # Drop the entire table
        con.commit()  # Commit the drop
        print("The 'customers' table has been dropped.")  # Confirmation message
    except sqlite3.Error as e:  # Handle SQLite errors
        print(f"Error dropping table: {e}")

# Main menu loop
while True:
    print("\nCustomer Information Management System")
    print("1. Insert a new customer")
    print("2. Display all customers")
    print("3. Update a customer's information")
    print("4. Delete a customer")
    print("5. Drop the entire 'customers' table")
    print("6. Exit")  # Options for user input
    
    try:
        choice = int(input("Enter your choice: "))  # Get user choice
        
        if choice == 1:
            # Insert a new customer
            first_name = input("Enter first name: ").strip()  # Strip white spaces
            last_name = input("Enter last name: ").strip()
            email = input("Enter email: ").strip()
            
            # Basic validation
            if not first_name or not last_name or "@" not in email:
                print("Invalid input. Please enter valid details.")
            else:
                insert_customer(first_name, last_name, email)  # Call insert function

        elif choice == 2:
            # Display all customers
            display_customers()

        elif choice == 3:
            # Update a customer's information
            customer_id = int(input("Enter customer ID to update: "))  # Get the customer ID
            field = input("Which field do you want to update? (first_name, last_name, email): ").strip()  # Get the field to update
            new_value = input("Enter the new value: ").strip()  # Get the new value
            
            # Check if the field is valid
            if field not in ["first_name", "last_name", "email"]:
                print("Invalid field. Please choose 'first_name', 'last_name', or 'email'.")
            else:
                update_customer(customer_id, field, new_value)  # Update the customer

        elif choice == 4:
            # Delete a customer
            customer_id = int(input("Enter customer ID to delete: "))  # Get the customer ID
            confirmation = input(f"Are you sure you want to delete customer with ID {customer_id}? (yes/no): ").strip().lower()  # Confirmation
            if confirmation == 'yes':
                delete_customer(customer_id)  # Call delete function
            else:
                print("Deletion cancelled.")  # Cancellation message

        elif choice == 5:
            # Drop the entire 'customers' table
            confirmation = input("Are you sure you want to drop the entire 'customers' table? (yes/no): ").strip().lower()  # Confirmation
            if confirmation == 'yes':
                drop_table()  # Call drop function
            else:
                print("Operation cancelled.")  # Cancellation message

        elif choice == 6:
            # Exit the program
            print("Thank you for using the Customer Information Management System.")
            print("""


                       _   _                 _                        
| |_| |__   __ _ _ __ | | __  _   _  ___  _   _ 
| __| '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | |
| |_| | | | (_| | | | |   <  | |_| | (_) | |_| |
 \__|_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_|

                    """)
            break  # Exit the loop

        else:
            print("Invalid choice. Please try again.")  # Handle invalid options

    except ValueError:  # Handle invalid input types
        print("Invalid input. Please enter a valid choice.")

# Close the connection to the database when done
con.close()  # Ensures data is saved and resources are released
