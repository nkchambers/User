class User:
    
    def __init__(self, first_name, last_name, age, account_balance):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.account_balance = account_balance

    def make_deposit(self, amount):
        
        self.account_balance += amount


    def make_withdrawal(self, amount):
        
        self.account_balance -= amount


    def display_user_balance(self):
        
        print(f"User: {self.first_name} {self.last_name}, Balance: {self.account_balance}")


    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()




# Insantiate Users
Nick = User ('Nick', 'Chambers', 30, account_balance = 0)
Russell = User ('John', 'Doe', 22, account_balance = 0)
Bruce = User ('Bruce', 'Wayne', 45, account_balance = 500000)



# 1st User - Nick
Nick.make_deposit(100)
Nick.make_deposit(700)
Nick.make_deposit(200)
Nick.make_withdrawal(500)


# 2nd User - Russell
Russell.make_deposit(500000)
Russell.make_deposit(100000)
Russell.make_withdrawal(150000)
Russell.make_withdrawal(50000)


# 3rd User - Bruce
Bruce.make_deposit(700000)
Bruce.make_withdrawal(200000)
Bruce.make_withdrawal(50000)
Bruce.make_withdrawal(100000)


# Display User Balances
Nick.display_user_balance()
Russell.display_user_balance()
Bruce.display_user_balance()


Bruce.transfer_money(150000, Nick)



