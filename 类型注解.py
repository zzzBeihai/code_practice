import json
import random
from typing import Union

var_1: int = 10
var_2: str ="zhangbeihai"
var_3: bool = True

class Student:
    pass
stu: Student = Student()

my_list: list = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "zhangbeihai", True)
my_dict: dict = {"zhangbeihai":666}

var_4 = random.randint(1,10) # type: int
var_5 = json.loads('{"zhangbeihai": "666"}') # type: dict[str, str]
def func():
    return 91
var_6 = func() # type: int



def add(x: int, y: int) -> int:
    return x + y


listpro: list[Union[int, str]] = [1, 2, "beihai"]
def funcpro(data: Union[int, str]) -> Union[int, str]:
    pass
funcpro()