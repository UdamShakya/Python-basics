# oop_dataclass_encapsulation.py
from dataclasses import dataclass, field
from typing import List

@dataclass
class Person:
    name: str
    age: int
    hobbies: List[str] = field(default_factory=list)

    def greet(self) -> str:
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = float(balance)  # "private" attribute by convention

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def __repr__(self) -> str:
        return f"<BankAccount owner={self.owner!r} balance={self._balance:.2f}>"

if __name__ == "__main__":
    # dataclass usage
    alice = Person("Alice", 25, hobbies=["boxing", "coding"])
    print(alice.greet())

    # bank account usage
    acct = BankAccount("Udam", 100.0)
    print(acct)
    acct.deposit(50)
    print("After deposit:", acct.balance)
    try:
        acct.withdraw(200)
    except ValueError as e:
        print("Withdraw error:", e)
