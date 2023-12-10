# Expense Tracker

Expense Tracker is a desktop application that aligns with SDG#1, SDG#8 and SDG#12 designed to help you manage your expenses effectively. This README provides detailed instructions and insights into the project.

## Overview

The Expense Tracker allows users to record and track their spending by category. The application provides a user-friendly interface for adding, viewing, searching, and managing expense records. Additionally, it offers graphical representation of expenses by category through interactive graphs.

## Features

Record Management:


• Add new records to the expense table.

• Delete records in the expense table.

• View all recorded expenses.

• Search for specific records by title, price, or category.


Graphical Representation:

• Visualize expenses through interactive graphs.

• Categories are represented for a clear overview of spending patterns.


Error Handling:

• The application provides error messages for blank fields, incorrect text lengths, and invalid inputs.

## Technologies Used

Python: The primary programming language.

Pandas: Used for data manipulation and analysis.

Plotly: Enables the creation of interactive and visually appealing graphs.

SQLite3: The database management system for storing expense records.

Tkinter and ttkbootstrap: Provide the graphical user interface for the desktop application.

## Screenshots of the Program
Starting Page:
![image](https://github.com/thizizzen/duling-sa-coding/assets/118614992/b9760e39-fdb3-499a-af1c-e12a51bf3819)

Main Page:
![image](https://github.com/thizizzen/duling-sa-coding/assets/118614992/7e42c6e7-c25c-4bbe-89c9-b94c8230030c)


Graphing Page:
![image](https://github.com/thizizzen/duling-sa-coding/assets/118614992/a019a408-f0c0-4aa5-b42a-3ada1eb5b42a)


## Implementation
DRY Method (Don't Repeat Yourself):

In our code, We embrace the DRY principle to avoid code duplication. Take, for example, the create_treeview function in main.py. It's designed to instantiate and configure a Treeview widget, consolidating the widget creation logic in one place for efficient reuse. This not only streamlines the code but also enhances maintainability.


OOP Principles (Object-Oriented Programming):

We incorporated object-oriented programming (OOP) principles by introducing the Budget class to manage interactions with the database. Creating an instance, such as budget = Budget(), enables the use of dot notation to access methods and properties seamlessly across the codebase.

Simplicity and Robustness:

We prioritize simplicity for clarity and maintainability, ensuring each code block serves a specific purpose. While basic error handling is in place using messagebox.showwarning, there's room for further enhancements to fortify the code's robustness. The aim is a balanced approach, making the application both easy to understand and resilient.

## Self Assessment
|       Metric       | 4 | 3 | 2 | 1 |
|:------------------:|:-:|:-:|:-:|:-:|
| Code Reusability   |   |   | ✔ |   |
| Maintainability    |   | ✔ |   |   |
| Scalability        | ✔ |   |   |   |
| Execution          | ✔ |   |   |   |
| Originality        |   |   | ✔ |   |
| Overall Impression |   | ✔ |   |   |

## Group Assessment
|  SR-CODE |       MEMBER      | GRADE |   CONTRIBUTION  |
|:--------:|:-----------------:|:-----:|:---------------:|
| 21-02313 | OCAMPO, ZHENREL   | 34%   | Lead Programmer |
| 20-58433 | BON, PETER AMADOR | 22%   | Troubleshooter  |
| 21-58727 | HERILLA, LAURENCE | 22%   | Debugger        |
| 21-02154 | CASTILLO, KHASTIN | 22%   | Beta Tester     |
|          | TOTAL             | 100%  |                 |

## License

This project is licensed under the MIT License.
