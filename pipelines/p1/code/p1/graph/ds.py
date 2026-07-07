from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from p1.config.ConfigStore import *
from p1.functions import *

def ds(spark: SparkSession) -> DataFrame:
    schemaFields = StructType([
        StructField("a", FloatType(), True), StructField("b", IntegerType(), True), StructField("c", IntegerType(), True)
    ])\
        .fields
    readSchema = StructType([StructField(f.name, StringType(), True) for f in schemaFields])

    return spark.createDataFrame([Row("1", "2", "4"), Row("4", "5", "0"), Row("7", "8", "9")], readSchema)
