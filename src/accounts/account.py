#initializing balance to 4000
account_balance = 4000
# getting the balance which is 4000
def get_balance():
    global account_balance
    return account_balance
# setting  the balance after an update of deposit or withdraw
def set_balance(new_balance):
    global account_balance
    account_balance = new_balance