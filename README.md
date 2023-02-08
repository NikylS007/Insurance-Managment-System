# Insurance-Management-System
The Insurance Management System is a console-based program to handle insurance policy administration. It efficiently manages policy and policyholder information, processes claims, and provides improved customer service. It saves time and effort, improving the overall experience for insurance companies and their customers.
## Overview
This is a codebase for an insurance management system, written in Python, that provides a way to manage and track insurance policies. The system allows creating and managing policies, clients, and claims.

## Requirements
#### The following packages are required to run the code:
* python (version 3.7 or later)
* pandas
* numpy
## Running the code
* Clone the repository onto your local machine
* Navigate to the directory containing the code using the command line
* Run the command python main.py to start the program
## Code Structure
#### The codebase consists of three main files:

* main.py
* Method.py
* Policy.py
* Customer.py (Dummy Class)
### main.py
This file contains the main function that runs the insurance management system. It imports classes and functions from Method.py and Policy.py, and uses them to perform different tasks related to policy management.

### Method.py
#### This file contains functions and classes used by the main function in main.py. It contains the following classes:

* Policy
* Client
* Claim

1. The Policy class contains information about a policy, such as the policy number, the client, and the policy type.

2. The Client class contains information about a client, such as their name, address, and date of birth.

3. The Claim class contains information about a claim, such as the date of the claim, the amount claimed, and the status of the claim.

### Policy.py
This file contains the Policy class, which is used to create and manage policies. The class has methods for adding and retrieving policies, as well as for calculating the premium for a policy.


## Limitations
* The system is limited to managing only one insurance company.
* The system is limited to only three types of insurance policies: general, health, and motor.
* The system does not provide any mechanism for handling payments or billing.
* The system does not provide any mechanism for handling policy renewals or cancellations.
* The system does not provide any security features, such as authentication or authorization. 
## Contributions
If you find any bugs or have suggestions for improvements, feel free to open an issue or make a pull request.
## Conclusion
This repository provides a complete solution to the problem at hand, using the three Python files. By following the instructions in the README, you should be able to run the code and reproduce the results.