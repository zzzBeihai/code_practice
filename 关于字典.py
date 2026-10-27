dianfeng = {"温华":16.0 , "南瓜":9.1 , "桑杰":14.4 }
print(f"这位up的经典评分为{dianfeng["温华"]}")

dianfeng["南瓜"] = 7.8
dianfeng["fly"] = 6.4
print(dianfeng)

all = dianfeng.keys()
print(all)

for key in dianfeng :
    print(key)
    print(dianfeng[key])

juehuo = dianfeng.pop("fly")
print(f"删除的评分是{juehuo}")

print(f"字典转列表的结果是{list(dianfeng)}")

print(f"字典的排序结果是{sorted(dianfeng,reverse=True)}")
# 反向排序或正向都会相应丢失字典的键值