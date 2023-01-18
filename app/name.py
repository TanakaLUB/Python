from dataclasses import dataclass


@dataclass()
class User:
    firstname: str
    lastname: str
    age: int = 0

    def show(self):
        return self.firstname + self.lastname

    def error(self):
        raise TypeError
