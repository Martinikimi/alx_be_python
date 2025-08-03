class BankAccount:
    def __init__(self, initial_balance=0):
<<<<<<< HEAD
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: ${amount}"

    def withdraw(self, amount):
        if amount > self.account_balance:
            return "Insufficient funds."
        else:
            self.account_balance -= amount
            return f"Withdrew: ${amount}"

    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"
=======
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")
>>>>>>> d18f9db70ec9eacd856cd0e94df605db7d0dbce4
