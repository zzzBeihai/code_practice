from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/code/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("Test_Spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(["flower dance", "fruit 666", "beihai"])
rdd2 = rdd.flatMap(lambda x: x.split(" "))
print(rdd2.collect())
