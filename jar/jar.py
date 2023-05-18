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

    @property
    def capacity(self):
        ...
    @capacity.setter
    def capacity(self, n):

    @property
    def size(self):
        return self.size
    @size.setter
    def size(self, n):
        

bank = Jar(3)
print(bank.size)
print(bank)
Jar.deposit(bank, 3)
print(bank.size)
print(bank)