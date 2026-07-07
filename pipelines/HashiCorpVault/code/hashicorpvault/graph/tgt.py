from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from hashicorpvault.config.ConfigStore import *
from hashicorpvault.functions import *

def tgt(spark: SparkSession) -> DataFrame:
    from pyspark.dbutils import DBUtils
    df = spark.read\
             .format("jdbc")\
             .option("url", "jdbc://btdghbf")\
             .option(
               "user",
               "{}".format(DBUtils(spark).secrets.get(scope = "hblair_dbx_scope", key = "prophecy-synapse-passsword"))
             )\
             .option(
               "password",
               "{}".format(DBUtils(spark).secrets.get(scope = "databricks_default", key = "DATABRICKS_TOKEN_2"))
             )\
             .option("dbtable", "berd")\
             .option("pushDownPredicate", True)\
             .option("driver", "")\
             .load()

    return df
