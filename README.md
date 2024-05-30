# Finance Master

## Description

Finance Master is a personal finance management application designed to help users efficiently manage their incomes, expenses, and balances. The application provides various features including user registration and login, expense and revenue tracking, and data visualization to offer insights into financial activities.

## Project Structure
- **Database:** MongoDB will manage our data efficiently.
- **Server-side:** We're using Python for server-side development.
- **Client-side:** React will power our client-side interface.

## Application Features:
- **User Routes**: Register, login, update profile, and fetch user data seamlessly.
- **User Action Routes**: Create, update, delete user actions, and fetch action data effortlessly.
- **Visual Routes**: Retrieve data in visualization-friendly formats using matplotlib.

## Quality Assurance and Installation

To ensure high-quality performance, Finance Master undergoes rigorous testing and continuous improvement

## Directory Tree

```plaintext
finance_master/
├── app/
│   ├── controllers/
│   │   ├── expense_controller.py
│   │   ├── revenue_controller.py
│   │   ├── user_controller.py
│   │   └── visualization_controller.py
│   ├── database/
│   │   ├── database_connection.py
│   │   └── repository.py
│   ├── log/
│   │   ├── app.log
│   │   └── log.py
│   ├── models/
│   │   ├── expense.py
│   │   ├── revenue.py
│   │   └── user.py
│   ├── services/
│   │   ├── balance_service.py
│   │   ├── expense_service.py
│   │   ├── revenue_service.py
│   │   ├── user_service.py
│   │   └── visualization_service.py
│   ├── validation/
│   │   └── validation_function.py
│   └── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```


### File Descriptions

#### `app` Directory

##### `database` Directory

- `database_connection.py`: Contains the database connection and collection definitions.
- `repository.py`: Contains functions for interfacing with the database, including CRUD (Create, Read, Update, Delete) operations.

##### `log` Directory

- `log.py`: Contains a decorator for logging various actions.

##### `models` Directory

- `expense.py`: Defines the Expense model.
- `revenue.py`: Defines the Revenue model.
- `user.py`: Defines the User model.

##### `routes` Directory

- `revenue_router.py`: Defines the routes for managing revenues.
- `visualization_router.py`: Defines the routes for data visualization.

##### `services` Directory

- `balance_service.py`: Contains services for managing user balances.
- `expense_service.py`: Contains services for managing expenses.
- `revenue_service.py`: Contains services for managing revenues.
- `user_service.py`: Contains services for managing users.
- `visualization_service.py`: Contains services for creating data visualizations.

##### `validation` Directory

- `validation_function.py`: Contains functions for data validation.

##### `main.py` File

- The main entry point of the application.

#### Other Files

- `.env`: Contains environment variables such as the database connection string.
- `requirements.txt`: Lists the project's dependencies.
- `README.md`: Contains information about the project, including file descriptions and the directory tree.

## Installation and Running

To install and run Finance Master, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/mali053/financemaster.git
    cd financemaster
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory and set the required environment variables:

    ```dotenv
    DB_CONNECTION_STRING=mongodb://localhost:27017
    ```

5. **Run the application:**

    ```bash
    uvicorn app.main:app --reload
    ```

## Thank you🙏🙏
  We appreciate your interest in Finance Master. Thank you for choosing our application!


## Documentation

Clear and comprehensive documentation is crucial for understanding and maintaining the Finance Master application. Here's why documentation is important to us:

1. **Clarity**: Well-documented code enhances readability and comprehension for developers, making it easier to understand the functionality and purpose of each component.

2. **Maintainability**: With thorough documentation, future updates and modifications become more manageable. Developers can quickly grasp the existing structure and make informed decisions about changes.

3. **Onboarding**: Documentation serves as a valuable resource for new team members joining the project. It provides them with insights into the project's architecture, conventions, and best practices.

4. **Troubleshooting**: In case of issues or bugs, detailed documentation helps in identifying and resolving problems efficiently. It serves as a reference guide for troubleshooting and debugging.

By prioritizing documentation, we ensure that Finance Master remains transparent, maintainable, and accessible to all stakeholders involved in its development and usage.

---



This README provides clear instructions for installing and running Finance Master on your system. If you encounter any issues, feel free to customize it further or reach out for assistance.