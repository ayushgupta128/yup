from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from eds.config.ConfigStore import *
from eds.functions import *

def Deduplicate_0(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.dropDuplicates(in0.columns)
