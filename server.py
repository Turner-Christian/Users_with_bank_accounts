class BankAccount:
    pop = 0

    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate
        self.yield_int = int_rate * self.balance
        BankAccount.pop += 1

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Your interest rate is {self.int_rate}")
        print(f"Your current balance is {self.balance}")
        return self

    def yield_interest(self):
        print(f"Your interest yield is {self.yield_int}")
        return self

    @classmethod
    def user_pop(cls):
        print(f"there are {cls.pop} instances!")

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.accounts = {}

    def make_account(self, int_rate, balance, acc_name):
        new_account = BankAccount(int_rate, balance)
        self.accounts[acc_name] = new_account
        return self

    def transfer(self, person, from_acc, to_acc, amount):
        if self.accounts[from_acc].balance < amount:
            print("CANNOT TRANSFER, NOT ENOUGH $$$")
            return self
        self.make_withdrawal(amount, from_acc)
        person.make_deposit(amount, to_acc)
        return self

    def make_deposit(self, amount, acc_name):
        self.accounts[acc_name].deposit(amount)
        return self

    def make_withdrawal(self, amount, acc_name):
        if self.accounts[acc_name].balance < amount:
            print("INSUFFICIENT FUNDS!")
        else:
            self.accounts[acc_name].withdraw(amount)
        return self

    def display_user_balances(self):
        print("-"*20)
        for x in self.accounts:
            print(f"{self.first_name} - Your account: {x}: has a balance of {self.accounts[x].balance}$")
        return self

user1 = User("chris", "turner")
user1.make_account(0.02, 0, "Checking").make_account(0.02, 500, "Savings")

user2 = User("catherine", "murphey")
user2.make_account(0.02, 1000, "Checking").transfer(user1, "Checking", "Checking", 2000)

user1.display_user_balances()
user2.display_user_balances()