# Beginner Friendly Project - 01

def show_balance(balance):
    print(f"Current balance is {balance:.2f}")
    return 0


def deposit():
    amount = float(input("Enter your amount: "))

    if amount < 0:
        print("Invalid amount")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter your amount: "))

    if amount > balance:
        print("Insufficient Balance")
        return 0
    else:
        return amount


def main():
    balance = 0
    running = True

    while running:
        print("*******************************")
        print("Welcome to Our Bank!!")
        print("*******************************")

        print("Choose an option: ")
        print("1. Balance Check")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        option = input("Enter your an option (from 1-4): ")

        if option == '1':
            show_balance(balance)
        elif option == '2':
            balance += deposit()
        elif option == '3':
            balance -= withdraw(balance)
        elif option == '4':
            running = False
        else:
            print("Invalid option, Dear Sir/Mam")


if __name__ == '__main__':
    main()
