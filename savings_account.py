"""Import the Account class from the Account.py file."""
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


# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.
    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    account_balance = 2000.00
    interest_rate= 0.07

    account= Account(account_balance, interest_rate)

    print('Account Balance:', account_balance)
    print("Interest Rate:", interest_rate)

    # Calculate interest earned
     # ADD YOUR CODE HERE
    time_period = 6

    interest_earned = account.calculate_interest(time_period)

    print(f"Interest earned: ${interest_earned:.2f}")

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    account.update_balance(interest_earned)

    print('Updated Account balance:',account_balance)
    
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    account.set_balance(account_balance)
   
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    account.set_interest(interest_earned)
    
    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    return account_balance,interest_earned