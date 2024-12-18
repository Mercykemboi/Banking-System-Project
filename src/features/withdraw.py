def withdraw_money(account_balance):
    try:
        amount = float(input("Enter the amount to withdraw: "))
        # checking if amount is greater than zero
        if amount > 0:
            # if amount passed is less than account balance
            if amount <= account_balance:
                account_balance -= amount
                print(f"Ksh {amount:,.2f} has been withdrawn successfully.")
            else:
                print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
    return account_balance
