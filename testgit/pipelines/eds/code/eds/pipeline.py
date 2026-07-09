from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from eds.config.ConfigStore import *
from eds.functions import *
from prophecy.utils import *
from eds.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Deduplicate_0 = Deduplicate_0(spark)
    df_Repartition_1 = Repartition_1(spark)
    df_Reformat_1 = Reformat_1(spark)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("eds").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/eds")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/eds", config = Config)(pipeline)

if __name__ == "__main__":
    main()
