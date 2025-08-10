import sys
from bank_account import BankAccount

def main():
<<<<<<< HEAD
    account = BankAccount(100)  # Example starting balance
=======
    account = BankAccount(100)  # Starting balance

>>>>>>> d18f9db70ec9eacd856cd0e94df605db7d0dbce4
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
<<<<<<< HEAD
        result = account.deposit(amount)
        print(result)
    elif command == "withdraw" and amount is not None:
        result = account.withdraw(amount)
        print(result)
    elif command == "display":
        result = account.display_balance()
        print(result)
=======
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
>>>>>>> d18f9db70ec9eacd856cd0e94df605db7d0dbce4
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
