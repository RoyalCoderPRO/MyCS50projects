class Jar:
    def __init__(self, capacity=12):


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

    @capacity.setter
    def capacity(self, capacity):
        if self.capacity< 0:
            raise ValueError

    @property
    def size(self):
        return self.size
    @size.setter
    def size(self, size):
        self.size = 


bank = Jar(3)
print(bank.size)
print(bank)
Jar.deposit(bank, 3)
print(bank.size)
print(bank)