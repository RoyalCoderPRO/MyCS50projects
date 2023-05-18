class Jar:
    def __init__(self, capacity=12):

        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self._size += n

    def withdraw(self, n):
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity< 0:
            raise ValueError
        self._capacity = capacity
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size



bank = Jar(15)
print(bank.size)
print(bank)
Jar.deposit(bank, 4)
print(bank.size)
print(bank)
Jar.withdraw(bank, 2)
print(bank.size)
print(bank)
Jar.deposit(bank, 12)
print(bank)