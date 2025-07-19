# Databricks notebook source
from pyspark.sql  import SparkSession
spark = SparkSession.builder.appName("Spark DataFrames").getOrCreate()
data = [("ritham",1),("praveen",19),("shadhu",21)]
df = spark.createDataFrame(data,["name","age"])
df.show()
spark.stop()