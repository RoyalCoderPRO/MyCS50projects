class Jar:
    def __init__(self, capacity=12):

        if int(capacity) < 0:
            raise ValueError
        self.capacity = capacity
        self.size = size


    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    #@property
    #def capacity(self):
        ...

    @property
    def size(self):
        
bank = Jar(3)
print(bank.size)
print(bank)
Jar.deposit(bank, 3)
print(bank.size)
print(bank)