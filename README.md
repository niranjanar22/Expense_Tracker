**EXPENSE TRACKER**



I think it is really important to keep track of the money we spend everyday. This helps us to be careful with our money and not waste it. A lot of people have trouble keeping track of where their money's going and this can lead to spending too much and not having a good budget.

To help with this problem I made a Command-Line Expense Tracker using Python.This application lets users record, view and analyze their expenses in a simple way.It is easy to use.Can be run directly from the terminal without needing any special interface.

This project also helps me learn about programming concepts that I studied in my course.





***PROBLEM STATEMENT***

Keepingtrack of expenses by hand can be really hard and can lead to mistakes. We need a digital solution that:

* Record expense details in a systematic way
* Gives a clear overview  of spending
* Caliculates expenditure quickly

The Expense Tracker solves this problem by giving a structured and interactive system for managing expenses.





***OBJECTIVES***

The main goals of this project are:

To make a command-line based expense tracking system

To use programming concepts like loops, conditionals, lists and dictionaries

To give users an easy-to-use interface for recording expenses

To help users monitor and calculate their spending efficiently





***FEATURES***

The application has following features:

Users can add expenses by entering details like date, category, description and amount

All recorded expense can be viewed in a format

The total expenditure can be calculated instantly 

The system uses a menu-drivem interface making it easy to navigate

The program runs continuously until the user choses to exit





***TECHNOLOGY STACK***

The project uses:

&#x20;     Programming language:Python 3

&#x20;     Execution environment: Command Line Interface(CFI)

&#x20;     Development Tool: Spyder IDE(Anaconda distribution)

No external libraries or frameworks are used. The project is lightweight and easy to run.





***PROJECT STRUCTURE***

The repository is organized like this:

expense\_tracker.py    # Main python script containing the application logic

README.md             # Project documentatiom

PROJECT\_REPORT.pdf    # Formal document that explains project in a clear and structured way





***INSTALLATION AND SETUP***

To run this project on your system follow these steps:

Step 1:Install python:-make sure python 3 is installed on yopur system.

Step 2:Clone the repository

Step 3:Run the application

How the Application works:-When the program is run it displays a menu with four options:

&#x20;                          i)Add Expense

&#x20;                         ii)View all expenses

&#x20;                        iii)View total Expense

&#x20;                         iv)Exit

The Expense Tracker application runs inside a loop allowing the user to perform multiple operations until they choose to exit.

Adding an Expense:When the user selects the "Add Expense" option the program asks for the following inputs:

* Date of expense
* category
* Description of the Expense
* Amount spent

&#x20;  This information is stored as a dictionary.Added to a list that keeps all expense records.

Viewing Expense:When the user selects the"View all Expense"option the program shows each expense entry in a format along with its index number

Calculating Total Expense:The total expenditure is calculated by adding up the amount values of all stored expenses.The result is then displayed to the uset.

Exiting the application:Selecting the exit option ends the loop.Stops the program.





***IMPLEMENTATION DETAILS***

The core logic of the program is based on the following concepts:

* A list is used to store expense records
* Each expense is represented as a dictionary, which allows storage of related data
* A while loop is used to keep the program running
* Conditional statements are used to control the flow based on user input
* Loops are used to iterate through the list for displaying and calculating data





***VALIDATION***

The application has been tested with:

* Multiple expense entries
* categories and descriptions
* Edge cases such as viewing expenses when no data is present
* Invalid menu choices

The program handles these scenarios by displaying messages.





***LIMITATIONS***

The Expense Tracker project has some limitations:

* The data is stored in memory. Is lost once the program is terminated
* There is validation for incorrect user inputs
* The interface is text-based. Lacks graphical representation





***FUTURE OUTCOMES***

The project can be improved with the following features:

* Saving data to a file (JSON/CSV) to keep it permanently
* Analyzing expenses by category
* Adding date filtering and search functionality
* Creating a graphical user interface (GUI)
* Visualizing expenses using charts and graphs





NIRANJANA\_R  25BOE10012



