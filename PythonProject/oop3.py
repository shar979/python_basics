#

class Client:
    def __init__(self, names, kra_pin, dob, gender):
        self.names = names
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender

        def print_details(self):
            print(self.names)
            print(self.kra_pin)

            class BankAccount:
                def __init__(self, owner, acc_no, balance):
                    self.owner = owner
                    self.acc_no = acc_no
                    self.balance = balance

                    def deposit(self, amount):

                        self.balance += abs(amount)

                        def withdraw(self, amount):

                        if amount > self.balance:
                            print("Not enough money")
                        else:
                            self.balance -= abs(amount)

    def print_details(self):
        print(self.owner)
        print(self.acc_no)
        print(self.balance)
        print("----------------------")

jane = Client(names: 'Jane Doue', kra_pin: 'A001', dob:'1999-01-16', gender: 'F')
yusuf =Client(names: 'Yusuf Owambo', kra_pin:'A002', dob: '')