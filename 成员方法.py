"""
访问类的成员变量必须使用self
"""
class Student :
    name = None

    def say_hello(self):
        print(f"亻尔女子,{self.name}")

    def say_hi(self,msg):
        print(f"亻尔女子,{self.name},{msg}")

stu = Student() # 构建类对象的方法
stu.name = "zzz"
stu.say_hello()
stu.say_hi("繁秋")

