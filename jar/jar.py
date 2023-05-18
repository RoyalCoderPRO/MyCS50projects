class Jar:
    def __init__(self, capa=12):

        self.capacity = capa
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self.insideproperty #The value for self.insideproperty comes from the setter

    @capacity.setter #This assigns 'setter' to the capacity property and runs a function

    def capacity(self, capa):
        if capa< 0:
            raise ValueError
        self.insideproperty = capa

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size



def main():
    bank = Jar(12)
    print(bank.capacity)
    Jar.deposit(bank, 5)
    print(bank)
    Jar.deposit(bank, 2)
    print(bank)
    Jar.withdraw(bank, 1)
    print(bank)
    Jar.deposit(bank, 1)
    print(bank)

if __name__ == "__main__":
    main()