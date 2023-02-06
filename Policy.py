import random
import re
import Methods

cust_Id = 0
# Nested dict list to store option for selecting policy
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


# Selecting policy page
def policy_page(customer_Id):
    global cust_Id
    cust_Id = customer_Id
    print(f"\nWelcome, Your Customer Id : {customer_Id}")
    log = input("1. View Details\n2. Select Policy\n3. Main Menu\n\nOption No : ")
    while not re.match(r'^[1-3]$', log):
        print("Invalid Option! Select from the below option\n")
        log = input("1. View Policies\n2. Select Policy\n3. Main Menu\n\nOption No : ")
    if log == '1':
        Methods.display_customer(customer_Id)
        policy_page(cust_Id)
    elif log == '2':
        print("\nInsurance Policy Selection")
        info_1 = input("1. Health Insurance\n2. Motor Insurance\n3. General Insurance\n4. Main Menu\n\nOption No : ")
        while not re.match(r'^[1-4]$', info_1):
            print("Invalid Option! Select from the below option\n")
            info_1 = input(
                "1. Health Insurance\n2. Motor Insurance\n3. General Insurance\n4. Go Back\n\nOption No : ")
        python_switch_2(int(info_1))
    else:
        print()
        Methods.login_input()


# for selecting the type of policy
def python_switch_2(argument):
    if argument == 1:
        select_policy(Health_insurances)
    elif argument == 2:
        select_policy(Motor_insurances)
    elif argument == 3:
        select_policy(General_insurances)
    else:
        policy_page(cust_Id)


# inserting the values to the policy table
def select_policy(Root_insurances):
    i = 1
    for insurance in Root_insurances:
        insurance_name = insurance["policy_name"]
        sum_assured = insurance["sum_assured"]
        premium = insurance["premium"]
        term = insurance["term"]
        print(f"{i}. {insurance_name} - Sum Assured: {sum_assured}, Premium: {premium}, Term: {term} year(s)")
        i = i + 1
    option = input("\nSelect one policy : ")
    while not re.match(r'^[1-3]$', option):
        print("Invalid Option! Select valid option\n")
        option = input("\nSelect one policy : ")
    option = int(option) - 1
    if input(
            f"\nSelected Policy\n{Root_insurances[option]}\n\nTo Confirm Press y | Press Enter key to go back : ") == 'y':
        Policy_id = ''.join(random.sample('0123456789', 7))
        Methods.insert_policy_info(cust_Id, Policy_id, Root_insurances[option]["policy_name"],
                                   Root_insurances[option]["sum_assured"], Root_insurances[option]["premium"],
                                   Root_insurances[option]["term"])
    policy_page(cust_Id)
