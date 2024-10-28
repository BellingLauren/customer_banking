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

    create_savings_account= Account(balance, interest_rate)

    print('Account Balance:',balance)
    print("Interest Rate:", interest_rate)

    # Calculate interest earned
     # ADD YOUR CODE HERE

    savings_interest_earned = create_savings_account.calculate_interest(months)

    print(f"Interest earned: ${savings_interest_earned:.2f}")

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    create_savings_account.update_balance(savings_interest_earned)

    print('Updated Account balance:',create_savings_account.balance)
    
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    create_savings_account.set_balance(create_savings_account.balance)
   
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    create_savings_account.set_interest(savings_interest_earned)
    
    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    return create_savings_account.balance,savings_interest_earned