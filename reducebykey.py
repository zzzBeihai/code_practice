from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/code/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("Test_Pyspark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([('男', 99), ('男', 88), ('女', 100), ('女', 60)])
rdd2 = rdd.reduceByKey(lambda x, y: x + y)
print(rdd2.collect())

# 运行发现python解释器的位置出现了问题