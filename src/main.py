from menu.menu import display_menu
from features.balance_inquiry import check_balance
from features.deposit import deposit_money
from features.withdraw import withdraw_money
from validation.validation import input_validation
from accounts.account import get_balance, set_balance

def main():
    while True:
        display_menu()
        choice = input("Choose an option between (1-4): ")
        choice = input_validation(choice)
        if choice is None:
            continue

        account_balance = get_balance()

        if choice == 1:
            check_balance(account_balance)
        elif choice == 2:
            account_balance = deposit_money(account_balance)
            set_balance(account_balance)
        elif choice == 3:
            account_balance = withdraw_money(account_balance)
            set_balance(account_balance)
        elif choice == 4:
            print("Thank you for choosing our system. Goodbye!")
            break

if __name__ == "__main__":
    main()
