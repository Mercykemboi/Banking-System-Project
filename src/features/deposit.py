#functionality for depositing money
def deposit_money(account_balance):
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            account_balance += amount
            print(f"Ksh {amount:,.2f} has been deposited successfully.")
            print(f"Your updated account balance is: Ksh {account_balance:,.2f}")
        else:
            print("Deposit amount must a be positive value.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
    return account_balance
