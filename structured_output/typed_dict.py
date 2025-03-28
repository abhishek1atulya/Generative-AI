from typing import TypedDict, Annotated, Literal

class person(TypedDict):
    name:str
    age:int
    city:str
    country:Annotated[str, "Country of residence"] # Annotated is used to add metadata to the type hint or we can 
    # say it is used to add extra information to the type hint
    occupation:Literal["Engineer", "Doctor", "Teacher"] 
    # Literal is used to specify the exact value that the key can have
d = person(name="John", age=30, city="Delhi", country="India", occupation="Engineer")
# or we can write it as:
# d : person = {"name":"John", "age":30, "city":"Delhi", "country":"India", "occupation":"Engineer"}
# print(d)
# here person class will only help during typing to have suggestion it does not validate the data
# so if we write it as:
d : person = {"name":"John", "age":'fifty', "city":"Delhi", "country":"India", "occupation":"Engineer"}
print(d) # it will not give any error
# but if we write it as:
# d : person = {"name":"John", "age":'fifty', "city":"Delhi", "country":"India", "occupation":"Engineer", "extra":"extra"}
print(d) # it will also not give error but it will also not create extra key in the dictionary
# so it is only for type hinting , suggestion, and to have fixed keys in the dictionary
# to validate the data we can use pydantic library