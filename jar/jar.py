class Jar:
    def __init__(self, capacity=12):

        self.capacity = capacity
        self.size = 0

    @property
    def capacity(self):
        return self.insideproperty #The value for self.insideproperty comes from the setter
    @capacity.setter #This assigns 'setter' to the capacity property and runs a function
    def capacity(self, capacity):
        if capacity< 0:
            raise ValueError
        self.insideproperty = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if size < self.capacity:
            raise ValueError
        self._size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self._size += n

    def withdraw(self, n):
        self._size -= n



bank = Jar(15)
print(bank.capacity)
Jar.deposit(bank, 12)
print(bank)
Jar.deposit(bank, 4)
print(bank)
Jar.withdraw(bank, 12)
print(bank)
Jar.deposit(bank, 12)
print(bank)