def withdraw_money(account_balance):
    try:
        amount = float(input("Enter the amount to withdraw: "))
        #checking if amount is greater than zero cuase amount to be withdrawan mus be a positive figure
        if amount > 0:
            #if amount passed is less than account balance if less withdraw else isufficient balance to be displayed
            if amount <= account_balance:
                account_balance -= amount
                print(f"Ksh {amount:,.2f} has been withdrawn successfully.")
            else:
                print(f"Insufficient balance! Withdrawal amount exceeds your account balance.ksh {account_balance:,.2f}" )
        else:
            print("Withdrawal amount must be positive.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
    return account_balance
