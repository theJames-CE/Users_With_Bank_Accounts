# Assignment: Users with Bank Account

#! Create a User class that has an association with the BankAccount class.
# You should not have to change anything in the BankAccount class.

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, chk_balance = 0, sav_balance = 0)

    def make_deposit(self, amount, account):
        self.account.deposit(amount, account)
        return self

    def make_withdrawal(self, amount, account):
        self.account.withdraw(amount, account)
        return self

    # SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount
    #  and a different User instance, and transfers money from the user's account into another user's account.

        # a transfer_money method to withdraw an ammount from user1's Checking account & deposit that amount into user2's Checking account
    def transfer_money(self, amount, user2):
        self.account.withdraw(amount, "Checking")
        user2.account.deposit(amount, "Checking")
        return self

    def display_user_balance(self):
        print("--------------------")
        print(self.name,"-->", "\n")
        self.account.display_account_info()
        print("--------------------","\n")


class BankAccount:

    accounts = []

    def __init__(self,int_rate, chk_balance, sav_balance):
        self.int_rate = int_rate
        self.chk_balance = 0
        self.sav_balance = 0
        # BankAccount.accounts.append(self)

        #  Giving the users two separate accounts to deposit/withdraw funds into
                # increases the account balance by the given amount
    def deposit(self, amount, account):
        if account == "Checking":
            self.chk_balance += amount
        elif account == "Savings":
            self.sav_balance += amount
        return self

    # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds;
        # if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount, account):
        if account == "Checking":
            if self.chk_balance >= amount:
                self.chk_balance -= amount
                return self
            else:
                print("Insufficient Funds: Charging a $5 Overdfraft Fee", "\n")
                self.chk_balance -= 5
                return self
        if account == "Savings":
            if self.sav_balance >= amount:
                self.sav_balance -= amount
                return self
            else:
                print("Insufficient Funds: Charging a $5 Overdfraft Fee", "\n")
                self.sav_balance -= 5
                return self

    # SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
        # updated to include both a Checking and Savings account for Users
    def display_account_info(self):
        print(f"Checking: ${self.chk_balance}")
        print(f"Savings: ${self.sav_balance}")
        return self

    # yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.chk_balance > 0:
                self.chk_balance = (self.chk_balance * self.int_rate) + self.chk_balance
                return self
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

#User test
user1 = User("James", "jbrandonw88@gmail.com")
user2 = User("Sara", "sara_amato89@gmail.com")

user1.make_deposit(620, "Checking").make_deposit(2000, "Savings").make_withdrawal(50, "Savings").make_deposit(1330, "Checking").transfer_money(600, user2).display_user_balance()
user2.make_deposit(1200, "Checking").make_deposit(835, "Checking").make_deposit(5000, "Savings").make_withdrawal(120, "Checking").display_user_balance()