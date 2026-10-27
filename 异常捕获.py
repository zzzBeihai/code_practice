'''
try:
    f = open("none", "r", encoding="utf-8")
except:
    f = open("none", "w", encoding="utf-8")
'''
# 尝试...否则...
try:
    print(name)
except NameError as e :
    print("出现了未定义自变量的错误")
    print(e)
# 捕获指定的异常
try:
    1/0
except (NameError, ZeroDivisionError) as e:
    print("出现了未定义自变量错误 或者 除以零的错误")
    print(e)
# 以元组的形式捕获多个异常
try:
    1/0
except Exception as e:
    print("出现异常了")
else:
    print("呦西，没毛病")
finally:
    print("无论如何我都会被执行")
# 捕获所有的异常（补充了else和finally的语法）
