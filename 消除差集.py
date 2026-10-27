set1 = {1,2,3}
set2 = {1,2,4,5,6}
set2.difference_update(set1)
print(set2)
# 删除相同的元素，集合2被修改，集合1不变

print(set1.difference(set2))
# 注意我这里的集合2已经被修改了，为{4,5,6}

set3 = set1.union(set2)
# 将集合1与集合2合并，形成一个新的集合
# 定义空集合用set()，因为单独的{}用于定义空字典

