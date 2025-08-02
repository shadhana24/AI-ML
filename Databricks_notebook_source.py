# Databricks notebook source
# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("StudentAssignment").getOrCreate()
data = [
    (1, "Alice", "Engineering", 65000),
    (2, "Bob", "Marketing", 58000),
    (3, "Charlie", "Sales", 52000)
]

schema = ["ID", "Name", "Department", "Salary"]
df = spark.createDataFrame(data, schema=schema)
df.show()
df.printSchema()
df.filter(df["Salary"] > 60000).show()
df.groupby("Department").count().show()
df.groupby("Department").avg("Salary").show()

# COMMAND ----------

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Spark DataFrames").getOrCreate()
df = spark.read.csv("/Volumes/workspace/default/sam_volume")
df.show()
df.printSchema()