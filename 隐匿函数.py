def test(inner):
    result = inner(1,2)
    print(f"运算的结果是{result}")
test(lambda x,y : x+y )
