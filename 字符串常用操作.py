my_string = "独眼是男人的浪漫"
my_new_string = my_string.replace ("男人","夏侯惇")
print(my_new_string)

my_string2 = "why so serious"
list = my_string2.split(" ")
print(list)

my_string3  = "  losers lose    their   hearts"
print(my_string3.strip())
# 不传输参数，默认去除首尾的空格以及换行符

my_string3  = "12losers lose    their   hearts21"
print(my_string3.strip("12"))
# 识别子传入参数，相当于去除首尾的1与2

