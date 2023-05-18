class Jar:
    def __init__(self, capacity=12):


        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if self.capacity< 0:
            raise ValueError
        return capacity

    @property
    def size(self):
        return self.size

bank = Jar(3)
print(bank.size)
print(bank)
Jar.deposit(bank, 3)
print(bank.size)
print(bank)