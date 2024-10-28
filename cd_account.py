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

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    create_cd_account= Account(balance, interest_rate,months)

    print('CD Balance:', create_cd_account.balance)
    print('Interest Rate', create_cd_account.interest)

    # Calculate interest earned
    # ADD YOUR CODE HERE

    CD_interest_earned = create_cd_account.calculate_interest(months)

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    create_cd_account.update_balance(CD_interest_earned)

    print('Updated CD balance:',create_cd_account.balance)

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    create_cd_account.set_balance(create_cd_account.balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    create_cd_account.set_interest(CD_interest_earned)
    
    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    return create_cd_account.balance, CD_interest_earned
    