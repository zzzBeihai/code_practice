num = 114514
def funa () :
    print(f"num的值为{num}")
def funb () :
    global num
    num =1919810
    print(f"num的值为{num}")
funa()
funb()
