# 导包
from pyspark import SparkConf, SparkContext
# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("Test_Spark_App")
# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)
# 打印Pyspark的运行版本
print(sc.version)
# 停止
sc.stop()