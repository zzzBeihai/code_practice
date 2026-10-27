def user_identity (name,age,gender):
    print(f"你的姓名是{name},年龄是{age},性别是{gender}")
# 位置参数,默认的传参形式
user_identity("小明",20,"女")
# 关键字参数
user_identity(age=20,name="小明",gender="女")
# 缺省参数，注意设置默认值必须放在最后
def user_identity (name,age,gender="男"):
    print(f"你的姓名是{name},年龄是{age},性别是{gender}")
user_identity("小天",12)
# 不定长参数，两类分别作为元组和字典形式存在，默认规范取名为args
def user_identity (*args):
    print(f"存储的数据类型为{type(args)},数据内容为{args}")
user_identity(1,2,3)

def user_identity (**kwargs):
    print(f"存储的数据类型为{type(kwargs)},数据内容为{kwargs}")
user_identity(name="温华",gender="男",character="夏侯惇")

