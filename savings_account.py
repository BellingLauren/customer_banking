"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance,interest_rate,months):
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
    create_savings_account = Account(balance, interest_rate)

    print('Account Balance:',balance)
    print("Interest Rate:", interest_rate)

    # Calculate interest earned
    savings_interest_earned= balance *(interest_rate /100) * (months/12)

    
    # Update the savings account balance by adding the interest earned
    updated_balance = create_savings_account.balance + savings_interest_earned
    create_savings_account.set_balance(updated_balance)

    print('Account Balance:', create_savings_account.balance)
    print("Interest Rate:",savings_interest_earned)

    # Return the updated balance and interest earned.
    return create_savings_account.balance, savings_interest_earned

