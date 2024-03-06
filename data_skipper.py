try:
    import os
    import sys
    import uuid
    import pyspark
    import datetime
    from pyspark.sql import SparkSession
    from pyspark import SparkConf, SparkContext
    from faker import Faker
    import datetime
    from datetime import datetime
    import random
    import pandas as pd  # Import Pandas library for pretty printing

    print("Imports loaded ")

except Exception as e:
    print("error", e)



HUDI_VERSION = '0.14.0'
SPARK_VERSION = '3.4'

SUBMIT_ARGS = f"--packages org.apache.hudi:hudi-spark{SPARK_VERSION}-bundle_2.12:{HUDI_VERSION} pyspark-shell"
os.environ["PYSPARK_SUBMIT_ARGS"] = SUBMIT_ARGS
os.environ['PYSPARK_PYTHON'] = sys.executable

spark = SparkSession.builder \
    .config('spark.serializer', 'org.apache.spark.serializer.KryoSerializer') \
    .config('spark.sql.extensions', 'org.apache.spark.sql.hudi.HoodieSparkSessionExtension') \
    .config('className', 'org.apache.hudi') \
    .config('spark.sql.hive.convertMetastoreParquet', 'false') \
    .getOrCreate()


path = "file:///Users/soumilshah/IdeaProjects/SparkProject/tem/hudidb/customers"

spark.read.format("hudi") \
    .option("hoodie.enable.data.skipping", "true") \
    .option("hoodie.metadata.enable", "true") \
    .option("hoodie.metadata.index.column.stats.enable", "true") \
    .load(path) \
    .createOrReplaceTempView("hudi_snapshot1")

spark.sql("SELECT * FROM hudi_snapshot1 WHERE salary >= 50000000 ").show()