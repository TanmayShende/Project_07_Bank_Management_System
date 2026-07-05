# 🏦 Bank Management System

A console-based **Bank Management System** developed using **Python** and **SQLite**. This project allows users to manage bank accounts by creating accounts, viewing details, searching, deleting, depositing and withdrawing money, checking balances, and generating account reports.

---

## 🚀 Features

* Create a new bank account
* View all accounts
* Search account by account holder name
* Delete an account
* Deposit money
* Withdraw money
* Check account balance
* View bank summary
* Generate account report (sorted by balance)
* Input validation for text and numeric fields
* Interactive menu-driven interface

---

## 🛠️ Technologies Used

* Python 3
* SQLite3
* Git
* GitHub

---

## 📂 Project Structure

```text
Project_07_Bank_Management_System/
│
├── main.py
├── bank.db
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🗄️ Database Schema

### accounts

| Column  | Type                              |
| ------- | --------------------------------- |
| id      | INTEGER PRIMARY KEY AUTOINCREMENT |
| name    | TEXT                              |
| balance | INTEGER                           |

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project folder

```bash
cd Project_07_Bank_Management_System
```

3. Run the application

```bash
python main.py
```

---

## 📋 Sample Menu

```text
BANK MANAGEMENT SYSTEM

1 - Create Account
2 - View Accounts
3 - Search Account
4 - Delete Account
5 - Deposit Money
6 - Withdraw Money
7 - Check Balance
8 - Bank Summary
9 - Account Report
10 - Exit
```

---

## 📈 Future Improvements

* Account number generation
* PIN-based authentication
* Transaction history
* Money transfer between accounts
* Interest calculation
* Account type (Savings/Current)
* Export reports to CSV or PDF
* Graphical User Interface (Tkinter)

---

## 👨‍💻 Author

**Tanmay Shende**

Python Developer | Learning Backend Development | Building Real-World Python Projects
