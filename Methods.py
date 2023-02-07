import mysql
from mysql.connector import Error
from prettytable import PrettyTable

import Policy
from Customer import Customers
import random
import re

password = "Nikyl1978@"  # database connection password
Agent_password = "Insurance@1515"  # common password for the agent login


# login page
def login_input():
    print("Home Page\n")
    info_1 = input("1. Customer Registration\n2. Customer Login\n3. Agent Login\n4. Exit\n\nOption No : ")
    while not re.match(r'^[1-4]$', info_1):
        print("Invalid Option! Select from the below option\n")
        info_1 = input("1. Customer Registration\n2. Customer Login\n3. Agent Login\n4. Exit\n\nOption No : ")
    python_switch_1(int(info_1))


# switch case for login page
def python_switch_1(argument):
    if argument == 1:
        customer_registration()
    elif argument == 2:
        customer_login()
    elif argument == 3:
        agent_login()
    else:
        print("Welcome Back!")


# Go back button
def back_but():
    input("\nPress Enter key to go back to main menu\n")
    login_input()


# Customer registration
def customer_registration():
    customer_id = ''.join(random.sample('0123456789', 7))
    print("\nRegistration Page")
    customer_name = input("Enter Full Name   : ")
    while not re.match(r'^[a-zA-Z ]{2,50}$', customer_name):
        print("Invalid Customer Name! Please enter a valid name [3-50 characters]")
        customer_name = input("Enter Full Name   : ")
    customer_age = input("Enter Age         : ")
    while not re.match(r'^(1[8-9]|[2-9][0-9]|1[0-2][0-9]|130)$', customer_age):
        print("Invalid Customer Age! Please enter a valid Customer Age [18-130]")
        customer_age = input("Enter Age         :")
    customer_gender = input("Enter Gender      : ")
    while not re.match(r'^(male|female|Others)$', customer_gender):
        print("Invalid Gender! Please enter a valid Gender(male|female|Others)")
        customer_gender = input("Enter Gender      : ")
    contact_number = input("Enter Contact Number: ")
    while not re.match(r'^\d{10}$', contact_number):
        print("Invalid Contact Number! Please enter a valid 10 digit number")
        contact_number = input("Enter Contact Number: ")
    email_id = input("Enter Email Id    : ")
    while not re.match(r'^[a-z\d]+@[a-z]{2,30}\.com$', email_id):
        print("Invalid email_id! Please enter a valid Email Id(.com)")
        email_id = input("Enter Email Id    : ")
    password_user = input("Enter Password    : ")
    while not re.match(r'^[a-zA-Z\W\d]{8,30}$', password_user):
        print("Invalid Password! Please enter a valid Password[5-30 characters][include at least one special character "
              "and number]")
        password_user = input("Enter Password    : ")
    address = input("Enter Address     : ")
    while not re.match(r'^[a-zA-Z\d\W]{5,150}$', address):
        print("Invalid Address! Please enter a valid Address[5-150 characters]")
        address = input("Enter Address     : ")
    nominee_name = input("Enter Nominee Name: ")
    while not re.match(r'^[a-zA-Z ]{2,50}$', nominee_name):
        print("Invalid Nominee_Name! Please enter a valid Nominee_Name[2-50 characters]")
        nominee_name = input("Enter Nominee Name: ")
    nominee_relationship = input("Enter Nominee Relationship: ")
    while not re.match(r'^[a-zA-Z ]{2,80}$', nominee_relationship):
        print("Invalid Nominee_relationship! Please enter a valid Nominee_relationship[2-80 characters]")
        nominee_relationship = input("Enter Nominee Relationship: ")

    if check_customer(contact_number, email_id):
        Customers(customer_id, customer_name, customer_age, customer_gender, contact_number, email_id, password_user,
                  address,
                  nominee_name, nominee_relationship)
        insert_customer(customer_id, customer_name, customer_age, customer_gender, contact_number, email_id,
                        password_user, address, nominee_name, nominee_relationship)
    else:
        print("Customer with same Phone number or emailId is already Present\n")
    back_but()


# customer login
def customer_login():
    print("\nLogin Page")
    customer_Id = input("Customer Id   : ")
    pass_word = input("Password      : ")
    login_check(customer_Id, pass_word)


# Agent login
def agent_login():
    print("\nAgent Login Page")
    input("Agent Id      : ")
    pass_word = input("Password      : ")
    if pass_word == Agent_password:
        agent_view()
    else:
        print("Incorrect Password...")
        back_but()
    back_but()


# Getting value for Agent table from Customer and policy table
def agent_view():
    connection = create_db_connection("localhost", "root", password, "mysql_python")
    sql = """select c.Customer_id, c.Customer_Name, c.Contact_Number, c.Email_Id, c.Address, p.Policy_id, p.Policy_Name, p.Sum_Assured, p.Premium, p.Term from customer_info as c inner join policy_info as p on c.Customer_id = p.Customer_id"""
    cursor = connection.cursor()

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        agent_table(result)
    except Error as err:
        print(f"Error: '{err}")
    finally:
        connection.close()


# Create Server Connection+
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        # print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


# Create Database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        # print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}")


# Create Database
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        # print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


# Execute Query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        # print("Query was successfully")
    except Error as err:
        print(f"Error: '{err}")


# Whole server
def server():
    connection = create_server_connection("localhost", "root", password)

    create_database_query = "Create database mysql_python"
    create_database(connection, create_database_query)

    connection = create_db_connection("localhost", "root", password, "mysql_python")
    create_table(connection)


# Customer and Policy table Creation
def create_table(connection):
    query = """CREATE TABLE customer_info (
      Customer_id INT PRIMARY KEY,
      Customer_Name VARCHAR(255) NOT NULL,
      Customer_Age INT NOT NULL,
      Customer_Gender ENUM('Male', 'Female', 'Other') NOT NULL,
      Contact_Number VARCHAR(20) NOT NULL,
      Email_Id VARCHAR(255) NOT NULL,
      Password VARCHAR(255) NOT NULL,
      Address TEXT NOT NULL,
      Nominee_Name VARCHAR(255) NOT NULL,
      Nominee_relationship VARCHAR(255) NOT NULL
    );"""
    execute_query(connection, query)
    connection.commit()
    query = """CREATE TABLE policy_info (
  Customer_id INT,
  Policy_id INT,
  Policy_Name VARCHAR(255) NOT NULL,
  Sum_Assured INT NOT NULL,
  Premium VARCHAR(20) NOT NULL,
  Term VARCHAR(255) NOT NULL,
  FOREIGN KEY (Customer_id)
  REFERENCES customer_info(Customer_id)
);
"""
    execute_query(connection, query)
    connection.commit()


# Query Reader
def read_query():
    connection = create_db_connection("localhost", "root", password, "mysql_python")
    query = """select * from customer_info"""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}")


# Check for duplicate contact number and email
def check_customer(contact_number, email_id):
    connection = create_db_connection("localhost", "root", password, "mysql_python")
    sql = """select * from customer_info where Contact_Number = %s or Email_Id = %s"""
    val = (contact_number, email_id)
    cursor = connection.cursor()

    try:
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if not result:
            return True
        else:
            return False
    except Error as err:
        print(f"Error: '{err}")


# Inserting values into Customer table
def insert_customer(customer_id, customer_name, customer_age, customer_gender, contact_number, email_id, password_user,
                    address, nominee_name, nominee_relationship):
    connection = create_db_connection("localhost", "root", password, "mysql_python")
    sql = ("INSERT INTO customer_info (Customer_id, Customer_Name, Customer_Age, Customer_Gender, Contact_Number, \n"
           "    Email_Id, Password, Address, Nominee_Name, Nominee_relationship) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,"
           " %s, %s)")
    val = (customer_id, customer_name, customer_age, customer_gender, contact_number, email_id, password_user,
           address, nominee_name, nominee_relationship)
    cursor = connection.cursor()

    try:
        cursor.execute(sql, val)
        connection.commit()
        print(f"{cursor.rowcount} Customer Registered Successfully\nCustomer Id : {customer_id}")
    except Error as err:
        print(f"Error: '{err}")


# Login Validation
def login_check(customer_Id, pass_word):
    # Connect to the database with the provided parameters
    connection = create_db_connection("localhost", "root", password, "mysql_python")
    # SQL query to retrieve customer information from the database using the provided customer ID
    sql = """select * from customer_info where Customer_id = %s"""
    val = (customer_Id,)
    cursor = connection.cursor()

    try:
        cursor.execute(sql, val)
        result = cursor.fetchall()
        # If no customer information is found, print the error message and call the back_but function
        if not result:
            print(f"{customer_Id} is not registered")
            back_but()
        else:
            # If the password matches the one in the database, call the policy_page function with the customer ID as a parameter
            if result[0][6] == pass_word:
                Policy.policy_page(customer_Id)
            else:
                # If the password doesn't match, print the error message and call the back_but function
                print("Incorrect Password")
                back_but()
    except Error as err:
        print(f"Error: '{err}")


# Inserting values into policy table
def insert_policy_info(Customer_id, Policy_id, Policy_Name, Sum_Assured, Premium, Term):
    # Connect to the database with the provided parameters
    connection = create_db_connection("localhost", "root", password, "mysql_python")
    # SQL query to insert policy information into the policy_info table
    sql = "INSERT INTO policy_info (Customer_id, Policy_id , Policy_Name, Sum_Assured, Premium, Term) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (Customer_id, Policy_id, Policy_Name, Sum_Assured, Premium, Term)
    cursor = connection.cursor()
    try:
        cursor.execute(sql, val)
        connection.commit()
        # If the insertion is successful, print a success message with the policy ID
        print(f"{cursor.rowcount} Policy Taken Successfully\nPolicy Id : {Policy_id}")
    except Error as err:
        print(f"Error: '{err}")


# Getting value for Customer table from Customer and policy table
def display_customer(customer_id):
    # Connect to the database
    connection = create_db_connection("localhost", "root", password, "mysql_python")

    # SQL query to retrieve data from customer_info and policy_info tables based on the customer_id
    sql = """select * from customer_info inner join policy_info on customer_info.Customer_id = policy_info.Customer_id where customer_info.Customer_id = %s"""
    val = (customer_id,)
    cursor = connection.cursor()

    try:
        # Execute the SQL query using the provided customer_id value
        cursor.execute(sql, val)
        result = cursor.fetchall()
        # Display the result in a table format
        table(result)
        # Prompt the user to press the Enter key to continue
        input("\npress Enter Key to Continue...")
    except Error as err:
        # Print an error message in case of an exception
        print(f"Error: '{err}")


# Function to display customer data in a table format
def table(value):
    x = PrettyTable()
    # Define the header fields for the table
    x.field_names = ["Customer_id", "Customer_Name", "Customer_Age", "Customer_Gender", "Contact_Number",
                     "Email_Id", "Password", "Address", "Nominee_Name", "Nominee_relationship", "Policy_id",
                     "Policy_Name", "Sum_Assured", "Premium", "Term"]
    for val in value:
        # Add a row to the table for each data entry
        x.add_row(
            [val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8], val[9], val[10], val[12], val[13],
             val[14], val[15]])
    x.align = "l"
    print(x)


# Function to display agent data in a table format
def agent_table(value):
    x = PrettyTable()
    # Define the header fields for the table
    x.field_names = ["Customer_id", "Customer_Name", "Contact_Number", "Email_Id", "Address", "Policy_id",
                     "Policy_Name", "Sum_Assured", "Premium", "Term"]
    for val in value:
        # Add a row to the table for each data entry
        x.add_row([val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8], val[9]])
    x.align = "l"
    print(x)
