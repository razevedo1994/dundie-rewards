from pydantic import BaseModel, validator
from decimal import Decimal
from datetime import datetime
import json
from dundie.utils.email import check_valid_email


class InvalidEmailError(Exception):
    ...


class Person(BaseModel):
    pk: str
    name: str
    dept: str
    role: str

    @validator("pk")
    def validate_email(cls, v):
        if not check_valid_email(v):
            raise InvalidEmailError(f"Invalid email for {v!r}")
        return v

    def __str__(self) -> str:
        return f"{self.name} - {self.role}"


class Balance(BaseModel):
    person: Person
    value: Decimal

    @validator("value", pre=True)
    def value_logic(cls, v):
        return Decimal(v) * 2

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class Movement(BaseModel):
    person: Person
    date: datetime
    actor: str
    value: Decimal


from dundie.database import connect

db = connect()

for pk, data in db["people"].items():
    p = Person(pk=pk, **data)

print(p)
print(json.dumps(p.dict()))

balance = Balance(person=p, value=100)
print(balance)
print(balance.json(models_as_dict=False))
