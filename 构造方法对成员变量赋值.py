class Student:
    name = None
    age = None
    tel = None
    # 可以删去不写

    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        #声明self的内置变量等于外界传入变量
        print("Student创建了一个类对象")

stu = Student("zzz", 18 ,"13615801481")
