# Define class MyFirstClass
class MyFirstClass():
    print('Who wrote this?"')
    # Define string variable called index
    index = "Author-Book"
    # Define function hand_list()
    def hand_list(self, philosopher, book):
        # variable + “ wrote the book: ” + variable
        print(MyFirstClass.index)
        print(philosopher + " " + "wrote the book:" + book)
# Call function handlist()
whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "Art of War")


#Example of abstract classes methods and functions.
from abc import ABC, abstractmethod

class Bank(ABC):
    def basicinfo(self):
        print("This is a generic bank")
        return str("Generic bank: 0")

    @abstractmethod
    def withdraw(self):
        pass
    
class Swiss(Bank):
    def __init__(self):
        self.bal = 1000

    def basicinfo(self):
        print("This is the Swiss Bank")
        return "Swiss Bank: " + str(self.bal)

    def withdraw(self, amount):
        if self.bal >= amount:
            self.bal -= amount
            print("Withdrawn amount: " + str(amount))
            print("New balance: " + str(self.bal))
            return self.bal
        else:
            print("Insufficient funds")
            return self.bal
        
# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()