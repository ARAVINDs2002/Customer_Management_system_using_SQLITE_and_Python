---------------------------------------------------------------------------------------------------------------------------- 
# C U S T O M E R     M A N A G E M E N T     S Y S T E M  U S I N G    P Y T H O N    A N D    S Q L I T E
----------------------------------------------------------------------------------------------------------------------------

Welcome,this project "CUSTOMER MANAGEMENT SYSTEM" is done completely on Python by integrating it to SQLITE.SQLite is an open-source database engine designed for simplicity and embedded use. Unlike other database management systems (DBMS), SQLite doesn't require a separate server process, allowing applications to manage their data with minimal overhead.This app works on command line interface sorry for not making it web based.
----------------------------------------------------------------------------------------------------------------------------
# WHAT IS THIS APP ABOUT?

The code is designed to interact with a SQLite database to manage customer information, offering a simple and effective solution for storing and retrieving customer data. Using Python's built-in sqlite3 module, the code establishes a connection to a SQLite database file, allowing it to execute SQL commands for various operations such as creating tables, inserting records, updating information, and retrieving data. It includes error handling to manage potential database errors, ensuring robustness. The code also formats the output to ensure a consistent display of data, with appropriate headers and alignment for easy readability. This structure provides a flexible framework for managing customer information in a lightweight database without the need for complex server setups. Whether you need to add new customers, update existing records, or display customer lists, the code is designed to be intuitive and straightforward, supporting a range of operations commonly required in customer management systems.
--------------------------------------------------------------------------------------------------------------------------

# FUNCTIONALITY

The application connects to an SQLite database (customer_db.db) and interacts with it through a cursor object. It ensures the database structure is set up by creating a "customers" table if it doesn't exist, with fields for id, first_name, last_name, and email.
--------------------------------------------------------------------------------------------------------------------------
# CORE FEATURES

# 👉INSERT A NEW CUSTOMER:
 The system allows you to add a new customer by providing their first name, last name, and email. The application includes basic validation to ensure that the data is in the correct format.

# 👉DISPLAY ALL CUISTOMERS:
 This feature retrieves all customer records from the database and displays them in a formatted manner. If no customers are found, the system will notify you accordingly.

# 👉UPDATE CUSTOMER INFORMATION:
 You can update a specific customer's information by selecting which field to update (first_name, last_name, or email) and providing a new value. The system ensures that you choose a valid field to update.

# 👉DELETE A CUSTOMER:
 This feature allows you to delete a customer by ID. The system asks for confirmation to prevent accidental deletions.

# 👉DROP THE COMPLETE TABLE:
 For extreme cases, the system provides an option to drop (delete) the entire "customers" table. It requires confirmation before proceeding, to avoid accidental data loss.

# 👉EXIT THE APPLICATION:
 The system includes a clean exit option, ensuring proper closure of the SQLite database connection.

# 👉USER INTERACTION AND ERROR HANDILING:
The application operates through a loop-based menu, allowing users to select from various options. It handles invalid inputs and database errors gracefully, providing clear error messages and allowing users to correct their mistakes.

If you need to change or add information to this system, ensure that the SQLite connection is properly established and closed, to avoid data corruption or memory leaks.
--------------------------------------------------------------------------------------------------------------------
# CONCLUDING REMARKS

This Customer Information Management System is a simple yet effective solution for managing customer records with SQLite and Python. It is designed for small to medium-sized applications where a full-fledged database server may be unnecessary. The straightforward menu-driven approach and robust error handling make it accessible to a wide range of users.
-------------------------------------------------------------------------------------------------------------------
SORRY FOR NOT PROVIDING A BETTER UI EVEN THOUGH I KNOW THE IMPORTANCE OF A USER INTERFACE I REALLY HAD LESS TIME IN DEVELOPING THESE PROJECTS ON MY OWN IN MIDREST OF MY STUDIES ...THANKYOU FOR YOUR UNDERSTANDING.
