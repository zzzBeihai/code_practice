class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
       return f"student,name: {self.name}, age: {self.age}"

    def __lt__(self, other):
        return self.age < other.age
# __le__添加了等于的大小判断 __eq__添加了等于

student1 = Student("zzzz", 18)
student2 = Student("zzz", 15)
print(student1)
print(str(student2))
print(student1<student2)
# 当类对象需要被转换为字符串才输出时，直接输出为其内存地址