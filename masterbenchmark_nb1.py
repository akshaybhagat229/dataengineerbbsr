# Databricks notebook source
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

dbutils.secrets.listScopes()
dbutils.secrets.list(scope='projectbbsr')
acc_key = dbutils.secrets.get(scope='projectbbsr', key='classproject')

# COMMAND ----------

spark.conf.set("fs.azure.account.key.class9001sa.dfs.core.windows.net",acc_key)

# COMMAND ----------

dbutils.fs.ls("abfss://classproject@class9001sa.dfs.core.windows.net/")

