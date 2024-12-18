def deposit_money(account_balance):
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            account_balance += amount
            print(f"${amount:.2f} has been deposited successfully.")
        else:
            print("Deposit amount must be positive.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
    return account_balance
