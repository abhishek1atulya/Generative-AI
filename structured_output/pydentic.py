from pydantic import BaseModel, Field
from typing import List, Literal, Annotated, Optional

class Person(BaseModel):
    salary: int = Field(..., description="Salary in USD")
    name: str
    age: int = Field(default =25 , gt=18, lt=60, description="Age in years")
    # we can also pass the integer value as string it will not throw any error
    city: Optional[str] = Field('New Delhi', description="City of residence")
d = Person(salary='1000', name='john', age=30) # it will not throw any error
print(d)
# we can also pass dictionary to the class
d = {"salary":1000, "name":'john',}
p = Person(**d)
print(p)
# but if we write it as:
# d = Person(salary='1000', name=13, age=40) # it will give error
