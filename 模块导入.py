import time
print("S")
time.sleep(5)
print("B")
# 基本import语法
from time import sleep
print("2")
sleep(5)
print("B")
# 针对某个功能进行使用
# from time import *代表调用全部
# 补充笔记 if __name__ == '__main__':
# 可在自定义模块中执行时，将内置变量转化成main，仅在此执行
# __all__[]定义了调用模块时所选取的元素



