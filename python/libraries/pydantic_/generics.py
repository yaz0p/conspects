from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')

class DataClass(BaseModel, Generic[T]):
    data: T


print(DataClass[str](data='foo'))
# >>> data = 'foo'

print(DataClass[list[int]](data=[1, 2, 3]))
# >>> data = [1, 2, 3]

print(DataClass[tuple[int, str]](data=(1, 'foo', 'bar'))) # Выдаст ошибку: слишком много элементов для кортежа
# >>> Tuple should have at most 2 items after validation, not 3 [type=too_long, input_value=(1, 'foo', 'bar'), input_type=tuple]
