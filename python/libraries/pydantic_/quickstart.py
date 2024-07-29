"""
Pydantic --- библиотека для валидации данных. Ядро пайдентика написано на Rust,
что обеспечивает скорость его работы. В отличие от других валидаторов,
позволяет использовать родные тайпхинтинги и проделывать всю работу без танцев
с бубном.
"""
from pydantic import BaseModel, ValidationError, Field, field_validator, root_validator
from typing import Optional

class City(BaseModel):
    city_id: int
    name: str
    population: int

input_json = '{"name": "Moscow", "population": 10000, "city_id":123, "foo":"bar"}' # Лишние данные отбрасываются

try:
    city = City.parse_raw(input_json) # Пайдентик распарсит и получит необхоимые данные
    print(city)
except ValidationError as e:
    print(e.json()) # Pydatinc выведет в виде json ошибку о местонахождении ошибки и причине её возникновения


# Мы можем создавать вложенные структуры и так же валидировать их при помощи pydantic

class FullName(BaseModel):
    first_name: str
    last_name: str
    number_phone: Optional[int]


class Villager(BaseModel):
    city_id: int
    full_name: list[FullName]


input_json = '''{
"city_id":123, 
"full_name": [{"first_name": "Vlad", "last_name": "Popov", "number_phone": "88005553535"}]
}''' # Провалидирует и превратит строку number_phone в int и наоборот при возможности!


try:
    villager = Villager.parse_raw(input_json)
    print(villager)
except ValidationError as e:
    print(e.json())

print(villager.json()) # Легко превращает в json


# Pydantic поддреживает аллиасинг! Это позволяет отправлять на frontend данные в нужном для него формате,
# а на бекенде работать с данными в нужном мне формате.


class FullName_(BaseModel):
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')


input_json = '''{
"firstName": "Vlad", "lastName": "Popov"
}''' # Должен сработать аллиасинг


try:
    fullname_ = FullName_.parse_raw(input_json)
    print(fullname_) # first_name='Vlad' last_name='Popov'
except ValidationError as e:
    print(e.json())
else:
    print(fullname_.json(by_alias=True)) # {"firstName":"Vlad","lastName":"Popov"}

# Так же можно исключать поля, которые нам не нужны при помощи параметра exclude
print(fullname_.json(by_alias=True, exclude=["last_name"] )) # в качестве параметра указывается любая коллекция


# Так же Pydantic позволяет гораздо глубже валидировать данные при помощи декоратора validator


class ToyotaMark2(BaseModel):
    mark: str

    @field_validator('mark') # декоратор validator устарел
    def mark2_check(cls, string):
        if 'mark2' not in string.lower():
            raise ValueError("Мы продаем только Mark 2!")
        return string

input_json = '''{
"mark": "Toyota mark2"
}'''
try:
    toyotamark2 = ToyotaMark2.parse_raw(input_json)
    print(toyotamark2)
except ValidationError as e:
    print(e.json())


# Так же можно валидировать все поля при помощи root_validator
