from prettytable import PrettyTable


# Customer.py is not crucial to this program and may be reconstructed in future developments.
class Customers:
    # parameterized constructor to assign values
    def __init__(self, customer_id, customer_name, customer_age, customer_gender, contact_number, email_id, password,
                 address, nominee_name, nominee_relationship):
        self.Customer_id = customer_id
        self.Customer_Name = customer_name
        self.Customer_Age = customer_age
        self.Customer_Gender = customer_gender
        self.Contact_Number = contact_number
        self.Email_Id = email_id
        self.Password = password
        self.Address = address
        self.Nominee_Name = nominee_name
        self.Nominee_relationship = nominee_relationship

    # The "display_customer" method creates a table and displays the customer information
    def display_customer(self):
        # Creating a "PrettyTable" object to format the table
        x = PrettyTable()
        # Defining the column headers for the table
        x.field_names = ["Customer_id", "Customer_Name", "Customer_Age", "Customer_Gender", "Contact_Number",
                         "Email_Id", "Password", "Address", "Nominee_Name", "Nominee_relationship"]
        # Adding a row with the customer object's attributes to the table
        x.add_row([self.Customer_id, self.Customer_Name, self.Customer_Age, self.Customer_Gender, self.Contact_Number,
                   self.Email_Id, self.Password, self.Address, self.Nominee_Name, self.Nominee_relationship])
        # Setting the table alignment to "l" for left
        x.align = "l"
        # Printing the table
        print(x)
