import random
import re
import Methods

# A global variable to store customer id
cust_Id = 0

# Nested dictionary list to store options for selecting insurance policy
Health_insurances = [{"policy_name": "HDFC Ergo Health Insurance", "sum_assured": 5000000, "premium": 9000, "term": 1},
                     {"policy_name": "Max Bupa Health Insurance", "sum_assured": 10000000, "premium": 12000, "term": 1},
                     {"policy_name": "Star Health Insurance", "sum_assured": 8000000, "premium": 10500, "term": 1}]
Motor_insurances = [
    {"policy_name": "Third-Party Liability Insurance", "sum_assured": 10000, "premium": 500, "term": 1},
    {"policy_name": "Comprehensive Insurance", "sum_assured": 20000, "premium": 1000, "term": 2},
    {"policy_name": "Motorcycle Insurance", "sum_assured": 5000, "premium": 250, "term": 1}]
General_insurances = [
    {"policy_name": "Bajaj Allianz General Insurance", "sum_assured": 500000, "premium": 7000, "term": 1},
    {"policy_name": "TATA AIG General Insurance", "sum_assured": 800000, "premium": 8000, "term": 1},
    {"policy_name": "ICICI Lombard General Insurance", "sum_assured": 700000, "premium": 7500, "term": 1}]


# Define a function to display policy selection page
def policy_page(customer_Id):
    # Set the global variable cust_Id to customer_Id
    global cust_Id
    cust_Id = customer_Id
    # Display the welcome message with customer_Id
    print(f"\nWelcome, Your Customer Id : {customer_Id}")

    # Ask user for an option - view details or select policy
    log = input("1. View Details\n2. Select Policy\n3. Main Menu\n\nOption No : ")

    # Validate user input, repeat the prompt if invalid
    while not re.match(r'^[1-3]$', log):
        print("Invalid Option! Select from the below option\n")
        log = input("1. View Policies\n2. Select Policy\n3. Main Menu\n\nOption No : ")

    # If user chose to view details, call display_customer method from Methods module
    if log == '1':
        Methods.display_customer(customer_Id)
        policy_page(cust_Id)
    # If user chose to select policy, display options for policy types
    elif log == '2':
        print("\nInsurance Policy Selection")
        info_1 = input("1. Health Insurance\n2. Motor Insurance\n3. General Insurance\n4. Main Menu\n\nOption No : ")
        # Validate user input, repeat the prompt if invalid
        while not re.match(r'^[1-4]$', info_1):
            print("Invalid Option! Select from the below option\n")
            info_1 = input("1. Health Insurance\n2. Motor Insurance\n3. General Insurance\n4. Go Back\n\nOption No : ")
        # Call python_switch_2 function with user selected option
        python_switch_2(int(info_1))
    # If user chose main menu, call the login_input method from Methods module
    else:
        print()
        Methods.login_input()


# This function allows the user to select the type of policy they want to buy
def python_switch_2(argument):
    # If the user selects option 1, display the available health insurance policies
    if argument == 1:
        select_policy(Health_insurances)
    # If the user selects option 2, display the available motor insurance policies
    elif argument == 2:
        select_policy(Motor_insurances)
    # If the user selects option 3, display the available general insurance policies
    elif argument == 3:
        select_policy(General_insurances)
    # If the user selects an invalid option, go back to the policy page
    else:
        policy_page(cust_Id)


# function to allow the user to select a policy from the available options
def select_policy(Root_insurances):
    i = 1
    # loop through the available insurances to display the insurance name, sum assured, premium, term
    for insurance in Root_insurances:
        insurance_name = insurance["policy_name"]
        sum_assured = insurance["sum_assured"]
        premium = insurance["premium"]
        term = insurance["term"]
        # print the insurance details for the user
        print(f"{i}. {insurance_name} - Sum Assured: {sum_assured}, Premium: {premium}, Term: {term} year(s)")
        i = i + 1
    # ask the user to select a policy
    option = input("\nSelect one policy : ")
    # validate the user input
    while not re.match(r'^[1-3]$', option):
        print("Invalid Option! Select valid option\n")
        option = input("\nSelect one policy : ")
    option = int(option) - 1
    # check if the user wants to confirm their policy choice
    if input(
            f"\nSelected Policy\n{Root_insurances[option]}\n\nTo Confirm Press y | Press Enter key to go back : ") == 'y':
        # generate a random policy id
        Policy_id = ''.join(random.sample('0123456789', 7))
        # insert the policy info into the database
        Methods.insert_policy_info(cust_Id, Policy_id, Root_insurances[option]["policy_name"],
                                   Root_insurances[option]["sum_assured"], Root_insurances[option]["premium"],
                                   Root_insurances[option]["term"])
        # go back to the policy page
        policy_page(cust_Id)
