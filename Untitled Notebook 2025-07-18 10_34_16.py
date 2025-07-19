# Databricks notebook source
from pyspark.sql import SparkSession 
spark = SparkSession.builder.appName("StudentAssignment").getOrCreate() 
# Sample employee data 
data = [ 
(1, "praveen", "Engineering", 65000), 
(2, "shadhana", "Marketing", 58000), 
(3, "ramya", "Sales", 52000), 
(4, "sameer", "Engineering", 72000), 
(5, "rani", "Sales", 54000) 
] 

# COMMAND ----------

schema = ["ID", "Name", "Department", "Salary"] 
df = spark.createDataFrame(data, schema=schema) 
df.show()

# COMMAND ----------

#Show schema 
df.printSchema()

# COMMAND ----------

# Filter: Salary > 60000 
df.filter(df["Salary"] > 60000).show()

# COMMAND ----------

# Group by Department 
df.groupBy("Department").count().show()

# COMMAND ----------

# Average Salary by Department 
df.groupBy("Department").avg("Salary").show()

# COMMAND ----------

from pyspark.sql import SparkSession

# COMMAND ----------

spark = SparkSession.builder.appName("Spark DataFrames").getOrCreate()

# COMMAND ----------

df = spark.read.csv("/Volumes/workspace/default/sample_vol/employees1.csv")

# COMMAND ----------

df.show()

# COMMAND ----------

df.printSchema()