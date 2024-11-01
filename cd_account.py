"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

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
    create_cd_account = Account(balance,interest_rate)
   
    print('CD Account Balance:', balance)
    print("CD Interest Rate:", interest_rate)
   

    # Calculate interest earned
    cd_interest_earned = balance *(interest_rate /100) * (months/12)


    # Update the CD account balance by adding the interest earned
    updated_balance = create_cd_account.balance + cd_interest_earned
    create_cd_account.set_balance(updated_balance)

    print('CD Account Balance:', create_cd_account.balance)
    print("Interest Rate:",cd_interest_earned)
    

    # Return the updated balance and interest earned.
    return create_cd_account.balance, cd_interest_earned     
   

    
    