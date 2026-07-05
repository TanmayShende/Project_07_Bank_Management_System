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


def main():

    while True:

        print("\nBANK MANAGEMENT SYSTEM")

        print("1 - Create Account")
        print("2 - View Accounts")
        print("3 - Exit")

        choice = input(
            "\nEnter choice: "
        )

        if choice == "1":

            add_account()

        elif choice == "2":

            view_accounts()

        elif choice == "3":

            print("\nGoodbye")

            break

        else:

            print(
                "\nInvalid choice"
            )


main()