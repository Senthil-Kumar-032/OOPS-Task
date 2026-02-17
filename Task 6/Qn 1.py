#   Problem:- 1 Bank Account


class BankAccount:

    # Base class for a bank account

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # encapsulation

    def deposit(self, amount):

        #   Add money to the account

        if amount > 0:
            self.__balance += amount
            print(" Amount deposited successfully ")
        else:
            print(" Invalid deposit amount ")

    def withdraw(self, amount):

        #   Withdraw money from the account

        if amount <= 0:
            print(" Invalid withdrawal amount ")
        elif amount > self.__balance:
            print(" Insufficient balance ")
        else:
            self.__balance -= amount
            print(" Amount withdrawn successfully ")

    def get_balance(self):

        #   Return current balance

        return self.__balance


class SavingsAccount(BankAccount):

    #   Savings account with interest rate

    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):

        #   Calculate interest on current balance

        interest = self.get_balance() * self.interest_rate / 100
        return interest


class CurrentAccount(BankAccount):

    #   Current account with minimum balance requirement

    def __init__(self, account_number, balance, minimum_balance):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):

        #   Withdraw money makes sure minimum balance is maintained

        if amount <= 0:
            print(" Invalid withdrawal amount ")
        elif self.get_balance() - amount < self.minimum_balance:
            print(" Minimum balance requirement not maintained ")
        else:
            super().withdraw(amount)


if __name__ == "__main__":

    # Create Savings Account

    savings = SavingsAccount("87787", 10000, 5)
    savings.deposit(2000)
    savings.withdraw(3000)
    print("Savings Balance:- ", savings.get_balance())
    print("Interest:- ", savings.calculate_interest())

    print("---------------------------------------------------------------------")

    # Create Current Account

    current = CurrentAccount("22677", 15000, 5000)
    current.deposit(1000)
    current.withdraw(12000)
    print("Current Balance:- ", current.get_balance())
