f = open("C:/Users/Lenovo/Desktop/pythontest.docx","w",encoding="utf-8")
f.write("Hello World")
f.flush()
# 先存储在缓冲区，再通过刷新一次性写入到文件中
f.close()
# close的语法自带了flush的功能
# w的模式，若文件存在将清空原有内容
# a的模式，代表文本追加