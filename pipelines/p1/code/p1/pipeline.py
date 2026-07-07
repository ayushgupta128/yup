from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from p1.config.ConfigStore import *
from p1.functions import *
from prophecy.utils import *
from p1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_ds = ds(spark)
    df_cast_columns_to_int = cast_columns_to_int(spark, df_ds)
    df_Reformat_1 = Reformat_1(spark, df_cast_columns_to_int)
    df_Limit_1 = Limit_1(spark, df_Reformat_1)
    df_random_sample_seven_rows = random_sample_seven_rows(spark, df_Limit_1)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("p1").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/p1")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/p1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
