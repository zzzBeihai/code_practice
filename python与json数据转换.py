import json
# 列表的每一个元素都是字典，将其转化为json
data = [{"name":"夏侯惇", "gender":"M"}, {"name":"甄姬", "gender":"F"}, {"name":"曹操", "gender":"M"}]
json.dumps(data, ensure_ascii=False)
# 不进行转化
s = '[{"name":"夏侯惇", "gender":"M"}, {"name":"甄姬", "gender":"F"}, {"name":"曹操", "gender":"M"}]'
json.loads(s)
# 补充：字典格式的字符串也能进行转化

