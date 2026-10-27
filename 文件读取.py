f = open("C:\Users\Lenovo\Desktop\友利奈绪.jpg","rb")
# f定义文件打开对象
# jpg文件由于字节不符合文本编码规则，不能用encoding="utf-8",读取图片更复杂只做样例说明
print(type(f))
print(f.read(10))
print(f.readlines())
f.close()
with open("C:\Users\Lenovo\Desktop\友利奈绪.jpg","rb")as f:
    for line in f:
        print(f"每行的数据为{line}")
# 打开后自动close