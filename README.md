# Banking Management System

A command-line banking management project built with Python, object-oriented programming, and PostgreSQL. It demonstrates account creation and authentication, balance enquiries, deposits, withdrawals, account maintenance, and transaction audit logging. The repository also contains a SQL script with database-level examples such as triggers, indexes, materialized views, functions, and procedures.

> **Educational project:** This code is intended for learning and demonstration. It is not production banking software and should not be used to store real customer funds or credentials.

## Features

- Create a bank account with a generated account number.
- Log in to an account using an account number and PIN.
- Check account balance.
- Deposit and withdraw funds.
- View account transaction history.
- Update account details and PIN.
- Delete an account after confirmation.
- Maintain audit records for account activity.
- Includes SQL examples for balance constraints, timestamps, reporting views, indexes, functions, and procedures.

## Tech Stack

- **Python 3** – application logic and command-line interface.
- **PostgreSQL** – persistent account and audit data.
- **psycopg2** – Python/PostgreSQL connectivity.
- **SQL / PL/pgSQL** – constraints, triggers, views, indexes, and stored routines.

## Project Structure

```text
Banking-system-main/
└── SQL3/
    ├── Database.py              # PostgreSQL connection helper
    ├── Main.py                  # Main command-line banking application
    ├── main2.py                 # Additional/alternate implementation
    ├── Query.sql                # Advanced PostgreSQL queries and objects
    └── Guide/
        ├── phase_wise_guide.txt
        └── sql_phase_guide.txt
```

## Prerequisites

- Python 3.9 or later.
- PostgreSQL installed and running.
- A PostgreSQL database named `BankData`.
- Python package `psycopg2-binary` (or `psycopg2` built for your environment).

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/IslamBilal/Banking-system-main.git
cd Banking-system-main
```

### 2. Install the Python dependency

```bash
pip install psycopg2-binary
```

### 3. Create the database

Create a PostgreSQL database named `BankData` using pgAdmin or psql.

### 4. Configure the database connection

Update the connection settings used by `SQL3/Database.py` for your local PostgreSQL host, database, username, and password. Do not commit real database passwords to the repository. The connection helper currently contains example local connection values and should be moved to environment-based configuration before deployment.

### 5. Run the application

```bash
cd SQL3
python Main.py
```

The application initializes the account and audit tables when it starts.

## Advanced SQL

After the base tables have been created by the application, review and execute `SQL3/Query.sql` in PostgreSQL to explore the additional database features. The script includes:

- A trigger that prevents negative account balances.
- An account update timestamp trigger.
- Materialized views for deposits, withdrawals, recent transactions, and active users.
- Subqueries and grouped reporting queries.
- Indexes for account and audit lookups.
- Transaction examples using `BEGIN`, `COMMIT`, and `ROLLBACK`.
- Example functions and procedures.

Run the SQL script against a test database first and review each statement before applying it. Some statements create persistent database objects or modify existing tables.

## Security Notes

- The current database connection helper contains hardcoded local connection values; replace these with environment variables before sharing or deploying.
- The current PIN hashing approach in the application uses SHA-256 without a per-user salt. This is not appropriate for production authentication; use a dedicated password-hashing algorithm such as Argon2id or bcrypt with unique salts.
- Admin/audit operations in a command-line learning project are not a substitute for real role-based access control.
- Use test data only.

## Future Improvements

- Move credentials to environment variables.
- Use a dedicated salted PIN/password hashing algorithm.
- Add automated tests for deposits, withdrawals, authentication, and audit logging.
- Use database transactions to keep balance changes and audit records atomic.
- Add explicit admin authentication and authorization.
- Add a web interface and deployment documentation.
