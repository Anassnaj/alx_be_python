class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self._account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the amount from account balance if sufficient funds exist."""
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")
