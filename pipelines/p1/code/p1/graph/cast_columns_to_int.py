from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from p1.config.ConfigStore import *
from p1.functions import *

def cast_columns_to_int(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        expr("TRY_CAST(a AS INT)").alias("a"), 
        expr("TRY_CAST(b AS INT)").alias("b"), 
        expr("TRY_CAST(c AS INT)").alias("c")
    )
