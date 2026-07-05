import sqlite3

connection = sqlite3.connect(
    "bank.db"
)

cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS accounts(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        balance INTEGER
    )
    """
)

connection.commit()


def get_text(message):

    while True:

        value = input(message).strip()

        if value == "":

            print("\nInput cannot be empty")

            continue

        return value


def get_number(message):

    while True:

        try:

            number = int(
                input(message)
            )

            if number < 0:

                print(
                    "\nValue cannot be negative"
                )

                continue

            return number

        except ValueError:

            print(
                "\nEnter numbers only"
            )


def add_account():

    name = get_text(
        "\nEnter account holder name: "
    )

    balance = get_number(
        "Enter opening balance: "
    )

    cursor.execute(
        """
        INSERT INTO accounts(
        name,
        balance
        )
        VALUES (?,?)
        """,
        (
            name,
            balance
        )
    )

    connection.commit()

    print(
        "\nAccount created successfully"
    )


def view_accounts():

    print("\nALL ACCOUNTS\n")

    cursor.execute(
        "SELECT * FROM accounts"
    )

    accounts = cursor.fetchall()

    if len(accounts) == 0:

        print(
            "No accounts found"
        )

        return

    print(
        "ID | Account Holder | Balance"
    )

    for account in accounts:

        print(
            f"{account[0]} | {account[1]} | ₹{account[2]}"
        )


def search_account():

    account = get_text(
        "\nEnter account holder name: "
    )

    cursor.execute(
        """
        SELECT *
        FROM accounts
        WHERE TRIM(LOWER(name)) = TRIM(LOWER(?))
        """,
        (
            account,
        )
    )

    result = cursor.fetchone()

    if result:

        print(
            f"\nID : {result[0]}"
        )

        print(
            f"Account Holder : {result[1]}"
        )

        print(
            f"Balance : ₹{result[2]}"
        )

    else:

        print(
            "\nAccount not found"
        )

def delete_account():

    account = get_text(
        "\nEnter account holder name: "
    )

    cursor.execute(
        """
        DELETE FROM accounts
        WHERE TRIM(LOWER(name)) = TRIM(LOWER(?))
        """,
        (
            account,
        )
    )

    connection.commit()

    if cursor.rowcount > 0:

        print(
            "\nAccount deleted"
        )

    else:

        print(
            "\nAccount not found"
        )


def deposit_money():

    account = get_text(
        "\nEnter account holder name: "
    )

    cursor.execute(
        """
        SELECT *
        FROM accounts
        WHERE TRIM(LOWER(name)) = TRIM(LOWER(?))
        """,
        (
            account,
        )
    )

    result = cursor.fetchone()

    if result is None:

        print(
            "\nAccount not found"
        )

        return

    amount = get_number(
        "Enter deposit amount: "
    )

    new_balance = result[2] + amount

    cursor.execute(
        """
        UPDATE accounts
        SET balance = ?
        WHERE id = ?
        """,
        (
            new_balance,
            result[0]
        )
    )

    connection.commit()

    print(
        "\nDeposit successful"
    )


def withdraw_money():

    account = get_text(
        "\nEnter account holder name: "
    )

    cursor.execute(
        """
        SELECT *
        FROM accounts
        WHERE TRIM(LOWER(name)) = TRIM(LOWER(?))
        """,
        (
            account,
        )
    )

    result = cursor.fetchone()

    if result is None:

        print(
            "\nAccount not found"
        )

        return

    amount = get_number(
        "Enter withdrawal amount: "
    )

    if amount > result[2]:

        print(
            "\nInsufficient balance"
        )

        return

    new_balance = result[2] - amount

    cursor.execute(
        """
        UPDATE accounts
        SET balance = ?
        WHERE id = ?
        """,
        (
            new_balance,
            result[0]
        )
    )

    connection.commit()

    print(
        "\nWithdrawal successful"
    )


def check_balance():

    account = get_text(
        "\nEnter account holder name: "
    )

    cursor.execute(
        """
        SELECT *
        FROM accounts
        WHERE TRIM(LOWER(name)) = TRIM(LOWER(?))
        """,
        (
            account,
        )
    )

    result = cursor.fetchone()

    if result is None:

        print(
            "\nAccount not found"
        )

        return

    print(
        f"\nCurrent Balance : ₹{result[2]}"
    )


def bank_summary():

    print(
        "\nBANK SUMMARY\n"
    )

    cursor.execute(
        """
        SELECT balance
        FROM accounts
        """
    )

    accounts = cursor.fetchall()

    if len(accounts) == 0:

        print(
            "No accounts found"
        )

        return

    total_balance = 0

    for account in accounts:

        total_balance += account[0]

    print(
        f"Total Accounts : {len(accounts)}"
    )

    print(
        f"Total Bank Balance : ₹{total_balance}"
    )

def account_report():

    print(
        "\nACCOUNT REPORT\n"
    )

    cursor.execute(
        """
        SELECT *
        FROM accounts
        ORDER BY balance DESC
        """
    )

    accounts = cursor.fetchall()

    if len(accounts) == 0:

        print(
            "No accounts found"
        )

        return

    print(
        "ID | Account Holder | Balance"
    )

    for account in accounts:

        print(
            f"{account[0]} | {account[1]} | ₹{account[2]}"
        )

def main():

    while True:

        print("\nBANK MANAGEMENT SYSTEM")

        print("1 - Create Account")
        print("2 - View Accounts")
        print("3 - Search Account")
        print("4 - Delete Account")
        print("5 - Deposit Money")
        print("6 - Withdraw Money")
        print("7 - Check Balance")
        print("8 - Bank Summary")
        print("9 - Account Report")
        print("10 - Exit")

        choice = input(
            "\nEnter choice: "
        ).strip()

        if choice == "1":

            add_account()

        elif choice == "2":

            view_accounts()

        elif choice == "3":

            search_account()

        elif choice == "4":

            delete_account()

        elif choice == "5":

            deposit_money()

        elif choice == "6":

            withdraw_money()

        elif choice == "7":

            check_balance()

        elif choice == "8":

            bank_summary()

        elif choice == "9":

            account_report()

        elif choice == "10":

            print(
        "\nGoodbye"
    )

            break

        else:

            print(
                "\nInvalid choice"
            )


main()

connection.close()