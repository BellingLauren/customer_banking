# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

balance = ()
interest_rate,months= ()
months = ()
create_savings_account= Account(balance, interest_rate,months)
savings_interest_earned = create_savings_account.calculate_interest(months)
create_cd_account= Account(balance, interest_rate)
CD_interest_earned = create_cd_account.calculate_interest(months)

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    balance = float(input("Enter the savings account balance: "))
    interest_rate,months = float(input("Enter the savings interest rate ( as a decimal): "))
    months = int(input("Enter the number of months for saving account: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(balance, interest_rate,months, months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Interest earned on savings account: ${savings_interest_earned:.2f}")
    print(f"Updated savings account balance: ${updated_savings_balance:.2f}")
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    balance = float(input("Enter the CD account balance: "))
    interest_rate = float(input("Enter the CD interest rate ( as a decimal): "))
    months = int(input("Enter the number of months for the CD: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_balance, CD_interest_earned = create_cd_account(balance, interest_rate, months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Interest earned on CD Account: ${CD_interest_earned:.2f}")
    print(f"Updated CD Account Balance: ${updated_balance:.2f}")
if __name__ == "__main__":
    # Call the main function.
    main()